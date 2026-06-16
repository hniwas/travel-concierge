/* ===== Travel Tips ===== */
let tips = [];
let tipIndex = 0;

async function loadTips() {
  try {
    const res = await fetch('/api/tips');
    tips = await res.json();
    showTip();
  } catch {
    document.getElementById('tipText').textContent =
      'Always carry a photocopy of your passport and keep the original in a secure place.';
  }
}

function showTip() {
  const el = document.getElementById('tipText');
  if (el && tips.length > 0) {
    el.textContent = tips[tipIndex % tips.length];
  }
}

function nextTip() {
  tipIndex++;
  showTip();
}

/* ===== Destination Search / Filter ===== */
function filterDestinations() {
  const query = document.getElementById('searchInput').value.toLowerCase().trim();
  applyFilter({ query });
}

function filterByTag(tag) {
  document.querySelectorAll('.tag-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('onclick') === `filterByTag('${tag}')`);
  });
  const query = document.getElementById('searchInput')
    ? document.getElementById('searchInput').value.toLowerCase().trim()
    : '';
  applyFilter({ query, tag });
}

function applyFilter({ query = '', tag = '' }) {
  const cards = document.querySelectorAll('#destinationsGrid .card-link');
  cards.forEach(link => {
    const card = link.querySelector('.card');
    const name = card.getAttribute('data-name') || '';
    const desc = card.getAttribute('data-desc') || '';
    const tags = card.getAttribute('data-tags') || '';

    const matchQuery = !query || name.includes(query) || desc.includes(query);
    const matchTag   = !tag   || tags.split(' ').includes(tag);

    link.classList.toggle('hidden', !(matchQuery && matchTag));
  });
}

/* ===== Packing List Checkbox ===== */
function togglePacked(checkbox) {
  const span = checkbox.nextElementSibling;
  if (span) span.classList.toggle('packed', checkbox.checked);
}

/* ===== Search on Enter key ===== */
document.addEventListener('DOMContentLoaded', () => {
  const input = document.getElementById('searchInput');
  if (input) {
    input.addEventListener('keyup', e => {
      if (e.key === 'Enter') filterDestinations();
    });
  }

  if (document.getElementById('tipText')) loadTips();
});
