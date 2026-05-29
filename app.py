from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# ============================================
# KENKO 1ST ORGANIC — WhatsApp Auto-Reply Bot
# ============================================

FAQS = [
    {
        "keywords": ["hi", "hello", "hey", "start", "help", "menu", "info"],
        "reply": (
            "👋 Welcome to *Kenko 1st Organic!*\n\n"
            "🌿 _Live a Healthy Life — Think Next Generation_\n\n"
            "How can we help you today? Type any of the following:\n\n"
            "• *products* — What we offer\n"
            "• *price* — Pricing info\n"
            "• *order* — How to order\n"
            "• *delivery* — Delivery info\n"
            "• *payment* — Payment methods\n"
            "• *location* — Find our shop\n"
            "• *contact* — Get in touch\n"
            "• *return* — Return & refund policy\n"
            "• *uber* — Order via Uber Eats / PickMe"
        )
    },
    {
        "keywords": ["product", "items", "what", "available", "sell", "offer", "vegetables", "fruits", "herbal", "honey", "oil", "treacle", "nuts", "seeds"],
        "reply": (
            "🌱 *Kenko 1st Organic — Our Products*\n\n"
            "🥦 Organic Vegetables & Fruits\n"
            "🌿 Herbal Tea\n"
            "🥥 Coconut Oil\n"
            "🌰 Nuts & Seeds\n"
            "🍯 Bee Honey\n"
            "🍂 Kithul Treacle\n\n"
            "All products are 100% natural, chemical-free & pesticide-free! ✅\n\n"
            "For specific items or availability, feel free to ask! 😊"
        )
    },
    {
        "keywords": ["price", "cost", "rate", "how much", "charge", "fee"],
        "reply": (
            "💰 *Kenko 1st Organic — Pricing*\n\n"
            "🥦 Organic Vegetables & Fruits — From LKR 150\n"
            "🌿 Herbal Tea — From LKR 200\n"
            "🥥 Coconut Oil — From LKR 350\n"
            "🌰 Nuts & Seeds — From LKR 300\n"
            "🍯 Bee Honey — From LKR 500\n"
            "🍂 Kithul Treacle — From LKR 400\n\n"
            "📩 For exact pricing, message us with the item name!"
        )
    },
    {
        "keywords": ["order", "buy", "purchase", "book", "how to order", "place order"],
        "reply": (
            "🛒 *How to Order from Kenko 1st Organic*\n\n"
            "1️⃣ Reply with the items you need\n"
            "2️⃣ Share your Name, Address & Phone Number\n"
            "3️⃣ We'll confirm your order & delivery date\n"
            "4️⃣ Pay Cash on Delivery — easy! 😊\n\n"
            "No minimum order required!\n\n"
            "You can also order via:\n"
            "🟢 *Uber Eats* — Search 'Kenko 1st Organic'\n"
            "🔵 *PickMe Food* — Search 'Kenko 1st Organic'"
        )
    },
    {
        "keywords": ["delivery", "ship", "courier", "deliver", "shipping", "how long", "when"],
        "reply": (
            "🚚 *Kenko 1st Organic — Delivery Info*\n\n"
            "📍 *Colombo:*\n"
            "• All products — Next day delivery\n\n"
            "🇱🇰 *Island Wide:*\n"
            "• Organic items, Herbal & Dry products — 2 to 3 days\n"
            "• Organic Vegetables & Fruits — Colombo only\n\n"
            "💵 Cash on Delivery available island-wide!\n\n"
            "📦 We'll confirm your delivery date when you place the order."
        )
    },
    {
        "keywords": ["payment", "pay", "cash", "card", "bank", "transfer", "cod"],
        "reply": (
            "💳 *Kenko 1st Organic — Payment Methods*\n\n"
            "✅ Cash on Delivery (COD)\n\n"
            "Simple & safe — you pay only when your order arrives! 😊\n\n"
            "No advance payment required."
        )
    },
    {
        "keywords": ["location", "address", "where", "shop", "store", "find", "visit", "come"],
        "reply": (
            "📍 *Kenko 1st Organic — Our Location*\n\n"
            "🏪 Kenko 1st Organic\n"
            "27/12, Rosmead Place,\n"
            "Colombo 07\n\n"
            "🕐 *Opening Hours:*\n"
            "Monday – Saturday: 8:00 AM – 7:00 PM\n"
            "Sunday: 9:00 AM – 5:00 PM\n\n"
            "You're welcome to visit us in store anytime! 🌿"
        )
    },
    {
        "keywords": ["contact", "call", "phone", "email", "reach", "talk", "number"],
        "reply": (
            "📞 *Kenko 1st Organic — Contact Us*\n\n"
            "📱 Phone: 0715 800 800\n"
            "📧 Email: kenkofood.srilanka@gmail.com\n"
            "💬 WhatsApp: This number!\n\n"
            "📍 27/12, Rosmead Place, Colombo 07\n\n"
            "Our team is happy to help you Monday – Saturday, 8AM – 7PM. 😊"
        )
    },
    {
        "keywords": ["return", "refund", "replace", "problem", "damaged", "wrong", "issue", "complaint"],
        "reply": (
            "🔄 *Kenko 1st Organic — Return & Refund Policy*\n\n"
            "If you receive a damaged or incorrect product, we will *replace it* for you! ✅\n\n"
            "📩 Simply message us with:\n"
            "1️⃣ Your order details\n"
            "2️⃣ A photo of the issue\n\n"
            "📱 Contact: 0715 800 800\n"
            "📧 Email: kenkofood.srilanka@gmail.com\n\n"
            "Your satisfaction is our priority! 🌿"
        )
    },
    {
        "keywords": ["uber", "pickme", "pick me", "ubereats", "app", "food app", "online app"],
        "reply": (
            "📱 *Order via Food Delivery Apps*\n\n"
            "You can order Kenko 1st Organic products through:\n\n"
            "🟢 *Uber Eats*\n"
            "→ Search: _Kenko 1st Organic_\n\n"
            "🔵 *PickMe Food*\n"
            "→ Search: _Kenko 1st Organic_\n\n"
            "Or simply order directly through this WhatsApp for island-wide delivery! 🚚"
        )
    },
    {
        "keywords": ["hours", "open", "time", "opening", "close", "working"],
        "reply": (
            "🕐 *Kenko 1st Organic — Opening Hours*\n\n"
            "Monday – Saturday: 8:00 AM – 7:00 PM\n"
            "Sunday: 9:00 AM – 5:00 PM\n\n"
            "📱 Online orders accepted 24/7!\n"
            "Delivery within working hours. 🚚"
        )
    },
    {
        "keywords": ["organic", "natural", "chemical", "pesticide", "fresh", "healthy", "certified"],
        "reply": (
            "🌱 *Why Choose Kenko 1st Organic?*\n\n"
            "✅ 100% Chemical-free & Pesticide-free\n"
            "✅ Locally sourced from Sri Lankan farmers\n"
            "✅ Fresh daily\n"
            "✅ Natural & certified organic products\n\n"
            "_Live a Healthy Life — Think Next Generation_ 🌿\n\n"
            "Type *products* to see what we offer!"
        )
    },
]

DEFAULT_REPLY = (
    "🙏 Thank you for contacting *Kenko 1st Organic!*\n\n"
    "Our team will get back to you shortly.\n\n"
    "For quick answers, type:\n"
    "• *products* — What we offer\n"
    "• *price* — Pricing\n"
    "• *order* — How to order\n"
    "• *delivery* — Delivery info\n"
    "• *location* — Find our shop\n"
    "• *contact* — Get in touch\n\n"
    "📱 0715 800 800 | 🌿 Kenko 1st Organic"
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
