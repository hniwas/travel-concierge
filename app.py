"""Travel Concierge - AI-powered travel planning assistant."""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

DESTINATIONS = [
    {
        "id": 1,
        "name": "Paris, France",
        "emoji": "🗼",
        "description": "The City of Light, famous for the Eiffel Tower, world-class cuisine, and art.",
        "best_time": "April–June, September–November",
        "currency": "Euro (EUR)",
        "language": "French",
        "highlights": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral", "Montmartre", "Seine River"],
        "budget_per_day": "$150–$300",
        "tags": ["romantic", "culture", "art", "food"],
    },
    {
        "id": 2,
        "name": "Tokyo, Japan",
        "emoji": "🗾",
        "description": "A vibrant metropolis blending futuristic technology with ancient traditions.",
        "best_time": "March–May, September–November",
        "currency": "Japanese Yen (JPY)",
        "language": "Japanese",
        "highlights": ["Shibuya Crossing", "Mount Fuji", "Senso-ji Temple", "Akihabara", "Shinjuku"],
        "budget_per_day": "$100–$250",
        "tags": ["culture", "food", "technology", "adventure"],
    },
    {
        "id": 3,
        "name": "New York, USA",
        "emoji": "🗽",
        "description": "The Big Apple – a global hub of culture, finance, and entertainment.",
        "best_time": "April–June, September–November",
        "currency": "US Dollar (USD)",
        "language": "English",
        "highlights": ["Central Park", "Times Square", "Statue of Liberty", "Brooklyn Bridge", "Broadway"],
        "budget_per_day": "$200–$400",
        "tags": ["urban", "culture", "food", "shopping"],
    },
    {
        "id": 4,
        "name": "Bali, Indonesia",
        "emoji": "🏝️",
        "description": "A tropical paradise with lush landscapes, temples, and stunning beaches.",
        "best_time": "April–October",
        "currency": "Indonesian Rupiah (IDR)",
        "language": "Balinese / Indonesian",
        "highlights": ["Ubud Rice Terraces", "Tanah Lot Temple", "Seminyak Beach", "Mount Batur", "Uluwatu"],
        "budget_per_day": "$50–$150",
        "tags": ["beach", "relaxation", "culture", "adventure"],
    },
    {
        "id": 5,
        "name": "Rome, Italy",
        "emoji": "🏛️",
        "description": "The Eternal City, home to ancient ruins, Renaissance art, and incredible food.",
        "best_time": "April–June, September–October",
        "currency": "Euro (EUR)",
        "language": "Italian",
        "highlights": ["Colosseum", "Vatican City", "Trevi Fountain", "Roman Forum", "Pantheon"],
        "budget_per_day": "$120–$250",
        "tags": ["history", "culture", "food", "art"],
    },
    {
        "id": 6,
        "name": "Cape Town, South Africa",
        "emoji": "🌍",
        "description": "A breathtaking coastal city with Table Mountain, wildlife, and diverse culture.",
        "best_time": "November–March",
        "currency": "South African Rand (ZAR)",
        "language": "English / Afrikaans / Xhosa",
        "highlights": ["Table Mountain", "Cape of Good Hope", "Robben Island", "Boulders Beach", "V&A Waterfront"],
        "budget_per_day": "$80–$180",
        "tags": ["nature", "adventure", "wildlife", "beach"],
    },
]

PACKING_LISTS = {
    "beach": ["Sunscreen SPF 50+", "Swimsuit", "Beach towel", "Flip-flops", "Sunglasses", "Hat", "Insect repellent", "Snorkeling gear"],
    "city": ["Comfortable walking shoes", "City map / offline maps", "Day bag / backpack", "Portable charger", "Umbrella", "Smart casual clothes"],
    "adventure": ["Hiking boots", "Quick-dry clothing", "First aid kit", "Water bottle", "Trail snacks", "Headlamp", "Trekking poles"],
    "culture": ["Modest clothing for temples", "Phrasebook / translation app", "Camera", "Travel journal", "Comfortable shoes", "Scarf/shawl"],
}

TRAVEL_TIPS = [
    "Always carry a photocopy of your passport and keep the original in a secure place.",
    "Notify your bank before traveling internationally to avoid card blocks.",
    "Download offline maps and translation apps before your trip.",
    "Purchase travel insurance to cover medical emergencies and trip cancellations.",
    "Research local customs and etiquette to respect the culture you're visiting.",
    "Keep emergency contacts and your embassy's phone number handy.",
    "Exchange some local currency at the airport for immediate expenses.",
    "Book popular attractions in advance to avoid long queues.",
    "Check visa requirements for your destination well in advance.",
    "Stay hydrated and eat local food from busy restaurants for a safer experience.",
]


@app.route("/")
def index():
    return render_template("index.html", destinations=DESTINATIONS)


@app.route("/destination/<int:dest_id>")
def destination(dest_id):
    dest = next((d for d in DESTINATIONS if d["id"] == dest_id), None)
    if dest is None:
        return render_template("404.html"), 404
    packing = []
    for tag in dest["tags"]:
        if tag in PACKING_LISTS:
            packing.extend(PACKING_LISTS[tag])
    packing = list(dict.fromkeys(packing))
    return render_template("destination.html", destination=dest, packing_list=packing)


@app.route("/api/destinations")
def api_destinations():
    query = request.args.get("q", "").lower()
    tag = request.args.get("tag", "").lower()
    results = DESTINATIONS
    if query:
        results = [d for d in results if query in d["name"].lower() or query in d["description"].lower()]
    if tag:
        results = [d for d in results if tag in d["tags"]]
    return jsonify(results)


@app.route("/api/tips")
def api_tips():
    return jsonify(TRAVEL_TIPS)


@app.route("/planner")
def planner():
    return render_template("planner.html", destinations=DESTINATIONS)


if __name__ == "__main__":
    import os
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug)
