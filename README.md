# ✈️ Travel Concierge

An AI-assisted travel planning web application built during the **S&T AI Session** — UWCC, June 2026.

## Features

- 🌍 **Destination Explorer** — Browse curated travel destinations with quick facts, highlights, and budget estimates.
- 🔍 **Search & Filter** — Find destinations by name or travel style (beach, culture, adventure, food, romantic).
- 🎒 **Smart Packing Lists** — Auto-generated packing checklists tailored to each destination's tags.
- 🗓️ **Trip Planner** — Generate a day-by-day itinerary based on destination, duration, and travel style.
- 💡 **Travel Tips** — Rotating expert travel tips to keep you safe and prepared.

## Getting Started

### Prerequisites

- Python 3.9+

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Run the development server
python app.py
```

Open your browser at **http://127.0.0.1:5000**.

## Running Tests

```bash
pip install pytest
pytest tests/
```

## Project Structure

```
travel-concierge/
├── app.py               # Flask application & data
├── requirements.txt     # Python dependencies
├── templates/
│   ├── index.html       # Home page – destination grid
│   ├── destination.html # Destination detail page
│   ├── planner.html     # Trip planner page
│   └── 404.html         # Error page
├── static/
│   ├── css/style.css    # Stylesheet
│   └── js/main.js       # Frontend JavaScript
└── tests/
    └── test_app.py      # Unit tests
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Home page |
| GET | `/destination/<id>` | Destination detail |
| GET | `/planner` | Trip planner |
| GET | `/api/destinations?q=&tag=` | JSON list of destinations |
| GET | `/api/tips` | JSON list of travel tips |

---

Built with ❤️ using Python, Flask, and GitHub Copilot.