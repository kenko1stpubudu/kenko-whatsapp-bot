from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# ============================================
# KENKO 1ST ORGANIC — FAQ Auto-Reply Bot
# මෙතන ඔබේ replies edit කරන්න
# ============================================

FAQS = [
    {
        "keywords": ["delivery", "ඩිලිවරි", "deliver", "ship", "courier", "යවනවා"],
        "reply": (
            "🚚 *Kenko 1st Organic — Delivery Info*\n\n"
            "📦 Organic & Herbal items: දිවයින පුරා Cash on Delivery!\n"
            "📦 එළවළු & පළතුරු: Colombo & nearby areas\n\n"
            "Order කරන්න reply කරන්න 👇"
        )
    },
    {
        "keywords": ["price", "මිල", "ගාස්", "කීයද", "cost", "rate", "ගාස්තු"],
        "reply": (
            "💰 *Kenko 1st Organic — මිල ගණන්*\n\n"
            "🥦 Organic vegetables — රු.150 සිට\n"
            "🌿 Herbal items — රු.200 සිට\n"
            "🍎 Organic fruits — රු.180 සිට\n"
            "🧴 Organic products — රු.350 සිට\n\n"
            "Specific item එකක් ගැන අහන්න!"
        )
    },
    {
        "keywords": ["order", "ඕඩර්", "buy", "ගන්න", "purchase", "book", "order කරන්න"],
        "reply": (
            "🛒 *Order කරන ක්‍රමය:*\n\n"
            "1️⃣ ඕනෑ items list කරන්න\n"
            "2️⃣ ඔබේ නම, address, phone number දෙන්න\n"
            "3️⃣ Cash on Delivery — deliver වෙලා pay!\n\n"
            "Minimum order නෑ 😊\n"
            "_Live a Healthy Life — Think Next Generation_ 🌿"
        )
    },
    {
        "keywords": ["organic", "ඕගනික්", "natural", "chemical", "herbal", "හර්බල්", "pesticide"],
        "reply": (
            "🌱 *Kenko 1st Organic — 100% Natural*\n\n"
            "✅ Chemical-free & pesticide-free\n"
            "✅ Locally sourced Sri Lankan farmers\n"
            "✅ Daily fresh delivery\n"
            "✅ Certified organic & herbal items\n\n"
            "Switch to healthy living today! 🌿"
        )
    },
    {
        "keywords": ["time", "open", "hours", "වේලාව", "කවදා", "කීයට", "opening"],
        "reply": (
            "⏰ *Kenko 1st Organic — Opening Hours*\n\n"
            "සඳුදා – සෙනසුරාදා: 8am – 7pm\n"
            "ඉරිදා: 9am – 5pm\n\n"
            "📱 Online orders 24/7 accept!\n"
            "Delivery working hours ඇතුළත."
        )
    },
    {
        "keywords": ["hi", "hello", "හෙලෝ", "ආයුබෝ", "හලෝ", "hey", "start"],
        "reply": (
            "👋 *Kenko 1st Organic වෙත සාදරයෙන් පිළිගනිමු!*\n\n"
            "🌿 _Live a Healthy Life — Think Next Generation_\n\n"
            "මෙතන type කරන්න:\n"
            "• *delivery* — ඩිලිවරි info\n"
            "• *price* — මිල ගණන්\n"
            "• *order* — order කරන ක්‍රමය\n"
            "• *organic* — products ගැන\n"
            "• *hours* — opening hours"
        )
    },
]

DEFAULT_REPLY = (
    "🙏 ඔබේ message received!\n\n"
    "අපේ team member ළඟදීම reply කරයි.\n\n"
    "Quick help:\n"
    "• *delivery* — ඩිලිවරි info\n"
    "• *price* — මිල ගණන්\n"
    "• *order* — order කරන්න\n"
    "• *hours* — opening hours\n\n"
    "_Kenko 1st Organic_ 🌿"
)


def get_reply(message: str) -> str:
    msg_lower = message.lower().strip()
    for faq in FAQS:
        if any(kw.lower() in msg_lower for kw in faq["keywords"]):
            return faq["reply"]
    return DEFAULT_REPLY


@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get("Body", "")
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(get_reply(incoming_msg))
    return str(resp)


@app.route("/")
def home():
    return "✅ Kenko 1st Organic WhatsApp Bot is running!"


if __name__ == "__main__":
    app.run(debug=False)
