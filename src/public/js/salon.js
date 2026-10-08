// SalonGo salon page: live slots (refresh every 4 s) + booking
const salonId = document.body.dataset.salonId;
const grid = document.getElementById("slots");
const confirmBtn = document.getElementById("confirm");
const message = document.getElementById("message");
const closedMsg = document.getElementById("closedMsg");
let selected = null;

function pretty(t) {
    const parts = t.split(":");
    const h = parseInt(parts[0], 10);
    const suffix = h >= 12 ? "PM" : "AM";
    return ((h + 11) % 12 + 1) + ":" + parts[1] + " " + suffix;
}

function showMessage(text, ok) {
    message.textContent = text;
    message.className = "message " + (ok ? "ok" : "err");
    message.hidden = false;
}

function updateButton() {
    confirmBtn.disabled = !selected;
    confirmBtn.textContent = selected ? "Confirm booking for " + pretty(selected.slice(11)) : "Select a time to continue";
}

function render(data) {
    closedMsg.hidden = data.status === "available" || data.status === "busy";
    const stillFree = data.slots.some(function (s) { return s.slot === selected && s.state === "free"; });
    if (selected && !stillFree) {
        showMessage("The time you picked was just taken. Please choose another.", false);
        selected = null;
        updateButton();
    }
    grid.innerHTML = "";
    data.slots.forEach(function (s) {
        const b = document.createElement("button");
        b.type = "button";
        b.className = "slot " + s.state + (s.slot === selected ? " selected" : "");
¶»§q«^