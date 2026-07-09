const messagesEl = document.getElementById("messages");
const formEl = document.getElementById("chat-form");
const inputEl = document.getElementById("message-input");
const statusEl = document.getElementById("status");

const socket = new WebSocket("ws://localhost:8000/ws");

function addMessage(text, type) {
    const div = document.createElement("div");
    div.classList.add("message", type);
    div.textContent = text;
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;
}

socket.onopen = () => {
    statusEl.textContent = "Connected";
    statusEl.classList.remove("disconnected");
    statusEl.classList.add("connected");
    addMessage("Connexion établie", "system");
};

socket.onmessage = (event) => {
    addMessage(event.data, "received");
};

socket.onclose = () => {
    statusEl.textContent = "Disconnected";
    statusEl.classList.remove("connected");
    statusEl.classList.add("disconnected");
    addMessage("Connexion perdue", "system");
};

formEl.addEventListener("submit", (e) => {
    e.preventDefault();
    const text = inputEl.value.trim();
    if (text.length === 0) {
        return;
    }
    socket.send(text);
    addMessage(text, "sent");
    inputEl.value = "";
});
