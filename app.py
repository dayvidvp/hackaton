import os, json, uuid, logging, traceback
from pathlib import Path
from flask import Flask, request, jsonify, session, redirect, url_for, render_template, Response
from dotenv import load_dotenv
from auth import check_credentials, get_user
from claude_client import ClaudeClient

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

load_dotenv(Path(__file__).parent / ".env", override=True)

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-change-me")

claude = ClaudeClient()
log.debug("API key loaded: %s", bool(os.getenv("ANTHROPIC_API_KEY")))


@app.route("/")
def index():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("chat.html", user=get_user(session["username"]))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if check_credentials(username, password):
            session["username"] = username
            session["messages"] = []
            return redirect(url_for("index"))
        error = "Ongeldige gebruikersnaam of wachtwoord"
    return render_template("chat.html", login_mode=True, error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/chat", methods=["POST"])
def chat():
    if "username" not in session:
        return jsonify({"error": "Niet ingelogd"}), 401

    data = request.get_json()
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Leeg bericht"}), 400

    if "messages" not in session:
        session["messages"] = []

    session["messages"].append({"role": "user", "content": user_message})
    session.modified = True

    try:
        result = claude.chat(messages=session["messages"])
    except Exception as e:
        log.error("Claude chat error: %s\n%s", e, traceback.format_exc())
        return jsonify({"error": str(e)}), 500

    if result["type"] == "confirmation_required":
        action_id = str(uuid.uuid4())
        session["pending_action"] = {
            "id": action_id,
            "tool_name": result["tool_name"],
            "tool_id": result["tool_id"],
            "tool_input": result["tool_input"],
            "assistant_content": result["assistant_content"],
            "messages_at_confirmation": result["messages_at_confirmation"],
        }
        session.modified = True
        return jsonify({
            "type": "confirmation_required",
            "action_id": action_id,
            "message": result["message"]
        })

    session["messages"].append({"role": "assistant", "content": result["text"]})
    session.modified = True
    return jsonify({"type": "text", "message": result["text"]})


@app.route("/confirm", methods=["POST"])
def confirm():
    if "username" not in session:
        return jsonify({"error": "Niet ingelogd"}), 401

    data = request.get_json()
    action_id = data.get("action_id")
    confirmed = data.get("confirmed", False)

    pending = session.get("pending_action")
    if not pending or pending["id"] != action_id:
        return jsonify({"error": "Geen geldige actie"}), 400

    session.pop("pending_action", None)
    session.modified = True

    if not confirmed:
        return jsonify({"type": "text", "message": "Actie geannuleerd."})

    result = claude.execute_confirmed_tool(
        tool_name=pending["tool_name"],
        tool_id=pending["tool_id"],
        tool_input=pending["tool_input"],
        messages_at_confirmation=pending["messages_at_confirmation"],
        assistant_content=pending["assistant_content"]
    )
    session["messages"].append({"role": "assistant", "content": result.get("text", "Actie uitgevoerd.")})
    session.modified = True
    return jsonify({"type": "text", "message": result.get("text", "Actie uitgevoerd.")})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
