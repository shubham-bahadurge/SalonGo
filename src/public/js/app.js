// SalonGo homepage: live search + filters + real-location distance
const searchInput = document.getElementById("search");
const distanceSelect = document.getElementById("distance");
const onlyAvailable = document.getElementById("onlyAvailable");
const grid = document.getElementById("grid");
const cards = Array.from(document.querySelectorAll(".card"));
const chips = document.querySelectorAll(".chip");
const emptyMsg = document.getElementById("empty");
const locBtn = document.getElementById("useLocation");
const locStatus = document.getElementById("locStatus");

let activeCategory = "";

function applyFilters() {
    const text = searchInput.value.trim().toLowerCase();
    const maxKm = parseFloat(distanceSelect.value);
    let visible = 0;

    cards.forEach(function (card) {
        const name = card.dataset.name;
        const services = card.dataset.services;
        const distance = parseFloat(card.dataset.distance);
        const status = card.dataset.status;

        const matchText = !text || name.includes(text) || services.includes(text);
        const matchCat = !activeCategory || services.includes(activeCategory);
        const matchDist = distance <= maxKm;
        const matchAvail = !onlyAvailable.checked || status === "available";

        const show = matchText && matchCat && matchDist && matchAvail;
        card.hidden = !show;
        if (show) { visible += 1; }
    });

    emptyMsg.hidden = visible > 0;
}

function haversineKm(lat1, lon1, lat2, lon2) {
    c¶»§q«^