const chatContainer = document.getElementById('chat-container');
const input = document.getElementById('message-input');
const sendBtn = document.getElementById('send-btn');

function formatMessage(text) {
  const jiraBase = (window.JIRA_BASE_URL || '').replace(/\/$/, '');

  if (jiraBase) {
    text = text.replace(/\b([A-Z][A-Z0-9]+-\d+)\b/g, (_, id) =>
      `[${id}](${jiraBase}/browse/${id})`
    );
  }

  const html = marked.parse(text, { breaks: true, gfm: true });
  return html.replace(/<a href=/g, '<a target="_blank" rel="noopener" href=');
}

function addMessage(text, role) {
  const div = document.createElement('div');
  div.className = `message ${role}`;
  div.innerHTML = formatMessage(text);
  chatContainer.appendChild(div);
  chatContainer.scrollTop = chatContainer.scrollHeight;
  return div;
}

function showTyping() {
  const div = document.createElement('div');
  div.className = 'typing';
  div.id = 'typing-indicator';
  div.innerHTML = '<span></span><span></span><span></span>';
  chatContainer.appendChild(div);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

function hideTyping() {
  const t = document.getElementById('typing-indicator');
  if (t) t.remove();
}

function showConfirmation(actionId, message) {
  const card = document.createElement('div');
  card.className = 'confirmation-card';
  card.id = `confirm-${actionId}`;
  card.innerHTML = `
    <p>${message}</p>
    <div class="buttons">
      <button class="btn btn-confirm" onclick="handleConfirm('${actionId}', true)">Ja, uitvoeren</button>
      <button class="btn btn-cancel" onclick="handleConfirm('${actionId}', false)">Annuleren</button>
    </div>
  `;
  chatContainer.appendChild(card);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

async function handleConfirm(actionId, confirmed) {
  const card = document.getElementById(`confirm-${actionId}`);
  if (card) card.remove();

  showTyping();
  sendBtn.disabled = true;

  try {
    const resp = await fetch('/confirm', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ action_id: actionId, confirmed })
    });
    const data = await resp.json();
    hideTyping();
    if (data.error) {
      addMessage('Fout: ' + data.error, 'assistant');
    } else if (data.type === 'confirmation_required') {
      showConfirmation(data.action_id, data.message);
    } else {
      addMessage(data.message || '(leeg antwoord)', 'assistant');
    }
  } catch (e) {
    hideTyping();
    addMessage('Er is een fout opgetreden.', 'assistant');
  } finally {
    sendBtn.disabled = false;
    input.focus();
  }
}

function startWizard() {
  input.value = 'Ik wil een nieuw IT-supportticket aanmaken.';
  autoResize();
  sendMessage();
}

async function newChat() {
  await fetch('/new-chat', { method: 'POST' });
  chatContainer.innerHTML = '';
  showWelcome();
}

async function sendMessage() {
  const text = input.value.trim();
  if (!text) return;

  addMessage(text, 'user');
  input.value = '';
  autoResize();
  sendBtn.disabled = true;
  showTyping();

  try {
    const resp = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text })
    });

    if (resp.status === 401) {
      window.location.href = '/login';
      return;
    }

    const data = await resp.json();
    hideTyping();

    if (data.error) {
      addMessage('Fout: ' + data.error, 'assistant');
    } else if (data.type === 'confirmation_required') {
      showConfirmation(data.action_id, data.message);
    } else {
      addMessage(data.message || '(leeg antwoord)', 'assistant');
    }
  } catch (e) {
    hideTyping();
    addMessage('Netwerkfout: ' + e.message, 'assistant');
    console.error(e);
  } finally {
    sendBtn.disabled = false;
    input.focus();
  }
}

function autoResize() {
  input.style.height = 'auto';
  input.style.height = Math.min(input.scrollHeight, 140) + 'px';
}

function showWelcome() {
  addMessage('Hallo! Ik ben de Helpdesk AI assistent. Hoe kan ik je helpen?\n\nVoorbeelden:\n- "Toon open tickets"\n- "Maak een ticket voor login probleem"\n- "Zoek oplossing voor API timeout"', 'assistant');
}

async function loadHistory() {
  try {
    const resp = await fetch('/api/history');
    if (!resp.ok) { showWelcome(); return; }
    const msgs = await resp.json();
    if (!msgs.length) { showWelcome(); return; }
    msgs.forEach(m => addMessage(m.content, m.role));
  } catch (e) {
    showWelcome();
  }
}

sendBtn.addEventListener('click', sendMessage);
input.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});
input.addEventListener('input', autoResize);

function switchUser(email) {
  fetch('/switch-user', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ email }) })
    .then(r => r.json()).then(d => { if (d.ok) location.reload(); });
}

loadHistory();
