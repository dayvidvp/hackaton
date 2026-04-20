const chatContainer = document.getElementById('chat-container');
const input = document.getElementById('message-input');
const sendBtn = document.getElementById('send-btn');

function addMessage(text, role) {
  const div = document.createElement('div');
  div.className = `message ${role}`;
  div.innerHTML = text.replace(/\n/g, '<br>').replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
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
    addMessage(data.message, 'assistant');
  } catch (e) {
    hideTyping();
    addMessage('Er is een fout opgetreden.', 'assistant');
  } finally {
    sendBtn.disabled = false;
    input.focus();
  }
}

async function sendMessage() {
  const text = input.value.trim();
  if (!text) return;

  addMessage(text, 'user');
  input.value = '';
  sendBtn.disabled = true;
  showTyping();

  try {
    const resp = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text })
    });
    const data = await resp.json();
    hideTyping();

    if (data.type === 'confirmation_required') {
      showConfirmation(data.action_id, data.message);
    } else {
      addMessage(data.message, 'assistant');
    }
  } catch (e) {
    hideTyping();
    addMessage('Er is een fout opgetreden. Probeer opnieuw.', 'assistant');
  } finally {
    sendBtn.disabled = false;
    input.focus();
  }
}

sendBtn.addEventListener('click', sendMessage);
input.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

addMessage('Hallo! Ik ben de Sterima AI assistent. Hoe kan ik je helpen?\n\nVoorbeelden:\n- "Toon open tickets"\n- "Maak een ticket voor login probleem"\n- "Zoek oplossing voor API timeout"', 'assistant');
