from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# ============================================
# KENKO 1ST ORGANIC — WhatsApp Auto-Reply Bot
# ============================================

PRODUCTS = [
    "Almond", "Amla Powder", "Ashwaganda Powder", "Black Gingelly",
    "Black Sesame Seed", "Burnt Cashew Nuts", "Cashew Nut Salt and Pepper",
    "Cashew Nuts Chilli Garlic", "Cashew Nuts Garlic", "Cashewnut Salt",
    "Habalapethi", "Jackfruit Cookies", "Kurakkan Flour", "Porridge Small",
    "Roasted Cashew Nut", "Thanahal", "Thulsi Powder", "Aloe Vera Drink",
    "Amiron Breast Skinless", "Amiron Chicken Leg Skinless", "Amiron Whole Chicken",
    "Apricot", "Asamodagam", "Ashwaganda Capsules", "Baby Oats", "Baby Soap",
    "Badairigu Sahal Porridge", "Banana Oatmeal Cookies", "Basil Seed", "Bay Leaves",
    "Bee Honey", "Black Forest Honey", "Black Pepper Whole", "Black Raisins",
    "Black Tea", "Blue Butterfly Pea Pasta", "Blueberry", "Blue Butterfly Tea Bags",
    "Brain Booster", "Brown Sugar", "Cacao Tea", "Cardamom",
    "Cashew and Peanut Cookies", "Cashew Nuts Sugar Coated", "Ceylon Cashew Burnt",
    "Ceylon Cashew Devilled", "Ceylon Coffee Bean Dark Roast",
    "Ceylon Coffee Bean Medium Roast", "Ceylon Coffee Espresso",
    "Ceylon Coffee Filter", "Ceylon Coffee Powder Dark Roast",
    "Ceylon Coffee Powder Medium Roast", "Ceylon Coffee Traditional",
    "Ceylon Green Tea", "Chia Seeds", "Chickpea", "Chilli Pieces", "Chilli Powder",
    "Chocolate 100g Cocoa 70%", "Chocolate 100g Cocoa 100%",
    "Chocolate 60g 100% Cocoa", "Chocolate 60g Cocoa 70%",
    "Chocolate with Three Nuts", "Chow Mein Sauce", "Cinnamon Capsules",
    "Cinnamon Powder", "Cinnamon Stick", "Clove Powder", "Coco Syrup",
    "Coco Treacle", "Cocoa Nibs", "Coconut Butter", "Coconut Sugar",
    "Coconut Vinegar", "Coffee Sachet", "Cold Pressed Sesame Oil",
    "Corn Pasta 350g", "Cranberries", "Crunchy Peanut Butter", "Cumin Seeds",
    "Curry Leaves Tea", "Dantha Raksha Powder", "Dark Chocolate",
    "Date and Cashew Chutney", "Dates", "Dehydrated Jackfruit", "Deviled Peanuts",
    "Devilled Cashew", "Devilled Peanut", "Dishwash Bar", "Dried Fruits Mix",
    "Dried Pitted Prunes", "Dried Plums", "Dry Mango", "Dry Noodles Disk",
    "Dry Noodles Extra Thick", "Dry Noodles Straight", "Dry Pineapple",
    "Eucalyptus Honey", "Facial Bar", "Flax Seed", "Forest Bee Honey",
    "Forest Garden Honey", "Garcinia Goraka", "Garlic Powder", "Garlic Thiyal",
    "Goraka Powder", "Coconut Sugar 250g", "Green Gram Pack",
    "Gyoza Chicken Dumpling", "Gyoza Sheet", "Hair Growth Oil",
    "Hair Oil With Sevendara", "Hazel Nut", "Headache Oil", "Healthy Flour",
    "Heen Bovitiya Powder", "Heenati Sahal Porridge", "Heenbovitiya Tea",
    "Heenbovitiya Tea Bags", "Herbal Tea", "Hibiscus Flower Tea Bags",
    "High Protein Power Oats", "Himalayan Rock Salt",
    "Himalayan Rock Salt Crystal", "Horse Gram", "Iramusu", "Iramusu Tea Bags",
    "Jackfruit Curry", "Japan Henna Bronze Gray", "Japan Henna Coffee Brown",
    "Japan Henna Natural", "Japan Henna SPA Repair Shampoo",
    "Japan Henna SPA Repair Treatment", "Java Plum Honey", "Jumbo Rolled Oats",
    "Kahamala Rice", "Kaluheenati Rice", "Katupila Powder", "Kesharaksha Hair Oil",
    "Kimia Dates", "King Coconut Water", "Kithul Flour", "Kithul Jaggery",
    "Kithul Jaggery Peanut", "Kithul Peanuts", "Kithul Powder", "Kithul Treacle",
    "Kollu", "Komas Arabian Dates", "Kothala Himbutu Tea Bag",
    "Kothalahimutu Powder", "Kurakkan Pasta", "Lanka Basmathi Rice",
    "Laundry Bar", "Laundry Powder", "Lunuwila Powder", "Ma Vee",
    "Maa Nelli Cola", "Maa Thal Cola", "Mango Jam", "Mango Powder", "MCT Oil",
    "Medjool Dates", "Mee Oil", "Meneri Rice", "Miso", "Momiji Natural Pads",
    "Moringa Capsules", "Moringa Pasta", "Moringa Tea Bags",
    "Muesli Mad Mix", "Muesli Tropical Mix", "Multi Grain Pappadam",
    "Multi Grain Pasta", "Natural High Protein Mix",
    "Naturelle Gotukola Capsules", "Naturelle Karapincha and Garlic Capsules",
    "Naturelle Karawila Capsules", "Naturelle Pitawakka Capsules",
    "Naturelle Thebu Capsules", "Naturelle Heenbovitiya Capsules",
    "Naturelle Turmeric Capsules", "Neeramulliya Powder", "Nelli Powder",
    "Nelli Preserve", "Nut and Fruits Mix", "Nuts and Fruits",
    "Olive Oil", "Onion Powder", "Organic Cinnamon Powder",
    "Organic Coconut Milk Can", "Organic Coconut Milk Powder",
    "Organic Ginger Powder", "Organic Moringa Powder", "Organic Moringa Tablets",
    "Organic Roasted Peanuts", "Organic Turmeric Powder", "Otas Flour",
    "Oven Cashewnut", "Oven Roast Peanut", "Pachchaperumal Rice",
    "Panchawalkala Shampoo", "Peanut Butter", "Pistachio", "Polpala Powder",
    "Premium Three Nuts", "Protein Chocolate Chips Cookies",
    "Protein Date Cookies", "Protein Noodles", "Psyllium Husk", "Pumpkin Seeds",
    "Quinoa Seed", "Ranawara Tea Bags", "Rasakinda Powder", "Rathhadun Body Wash",
    "Raw Bee Honey", "Red Cowpea", "Rice Keda", "Roasted Curry Powder",
    "Roasted Seed and Nuts Snack", "Roasted Sesame Oil", "Sago Seeds",
    "Savary Banana", "Sesame Oil", "Shampoo Bar", "Sinhala Achcharu",
    "Smooth Peanut Butter", "Soursap Powder", "Stevia Powder",
    "String Hopper Masbedda", "String Hopper Moringa", "String Hopper Red",
    "String Hopper Suwadel", "String Hopper White", "Sunflower Seed",
    "Suwadal Pasta 350g", "Suwadal Rice", "Suwadal Sahal Porridge",
    "Suwandel Rice", "Sweet Tamarind", "Szechuan Sauce", "Tamarind Chutney",
    "Tamarind Sauce", "Teriyaki Sauce", "Thebu Leaves Powder", "Udon Noodles",
    "Umami Sauce", "Vanilla Stick", "VCO Whole Kernel Oil", "Virgin Coconut Oil",
    "Wadamal Panaya", "Walnut", "Welpenela", "Welpenela Capsules",
    "Weralu Powder", "White Cowpea", "White Gingelly", "White Sesame",
    "Whole Chicken", "Wild Bee Honey", "Wonton Sheet",
    "Yakinaran Panaya", "Yakinaran Powder", "Yakisoba Sauce",
]

def find_products(query):
    query_words = query.lower().split()
    matches = []
    for product in PRODUCTS:
        product_lower = product.lower()
        if any(word in product_lower for word in query_words if len(word) > 2):
            matches.append(product)
    return matches


# ==================================================
# KEYWORD LISTS — Sinhala / Singlish / Typos
# ==================================================

# Greetings — standalone words only, matched exactly
GREETINGS = [
    # English
    "hi", "hello", "hey", "helo", "hii", "hiii", "hiiii", "helloo",
    "helloooo", "heyy", "heyyy",
    # Singlish
    "ayubowan", "ayubo", "aayubowan", "kohomada", "kohomad",
    "machan", "bro", "sis", "akka", "aiya", "nangi", "malli",
    # Sinhala unicode
    "\u0d86\u0dba\u0dd4\u0d89\u0db6\u0ddc\u0dc0\u0db1\u0dca",
    "\u0d9a\u0ddc\u0dc4\u0ddc\u0db8\u0daf",
    # Start triggers
    "start", "menu", "help", "info", "bot",
]

# Availability — "do you have / is it available"
AVAILABILITY_TRIGGERS = [
    # Sinhala unicode
    "\u0dad\u0dd2\u0dba\u0dd9\u0db1\u0dc0\u0dcf\u0daf", "\u0dad\u0dd2\u0dba\u0dd9\u0db1\u0dc0\u0daf",
    "\u0dad\u0dd2\u0dba\u0db1\u0dc0\u0daf", "\u0dad\u0dd2\u0dba\u0db1\u0dc0\u0dcf\u0daf",
    "\u0d9a\u0dd2\u0dba\u0dd9\u0db1\u0dc0\u0dcf\u0daf", "\u0d9a\u0dd2\u0dba\u0dd9\u0db1\u0dce\u0daf",
    "\u0dbd\u0dd0\u0db9\u0dd9\u0db1\u0dc0\u0dcf\u0daf", "\u0dbd\u0dd0\u0db9\u0dd9\u0db1\u0dc0\u0daf",
    "\u0d9c\u0db1\u0dca\u0db1 \u0db4\u0dd4\u0dbd\u0dd4\u0dc0\u0db1\u0dca\u0daf",
    "\u0d9c\u0db1\u0dca\u0db1 \u0db4\u0dd4\u0dbd\u0dd4\u0dc0\u0db1\u0dca",
    "\u0dad\u0dd2\u0dba\u0dd9\u0daf",
    # Singlish / Romanized Sinhala (common typing variations)
    "thiyanawada", "thiyanawad", "thiyenavada", "thiyenavad",
    "tiyanawada", "tiyanawad", "tiyenavada", "tiyenavad",
    "thibunada", "thibunad", "thienawada",
    "thiyenad", "thiyenawa", "thiyanawa",
    "ganna puluwanda", "ganna puluwan", "ganna puluwanada",
    "ganna puluanda", "ganna puluvan",
    "ganna beri", "ganna be", "ganna onada",
    "labenavada", "labenavad", "labenawada",
    "inna wade", "innawada", "innawa",
    "dunnada", "dunnavada", "denanavada",
    # English variations
    "do you have", "do u have", "do u hav",
    "do you sell", "do u sell",
    "is it available", "is this available", "available?",
    "in stock", "stock available", "any stock",
    "can i get", "can i buy", "can i order",
    "i need", "i want",
]

# Location — "where is your shop"
LOCATION_TRIGGERS = [
    # Sinhala unicode
    "\u0d9a\u0ddc\u0dc4\u0ddd\u0daf", "\u0d9a\u0ddc\u0dc4\u0dd0\u0daf",
    "\u0d9a\u0ddc\u0dc4\u0dd9\u0daf",
    "\u0dad\u0dd2\u0dba\u0dd9\u0db1\u0dca\u0db1\u0dd9",
    # Singlish
    "koheda", "kohedu", "kohede", "koheda?",
    "kohoma yanna", "kohomada yanna",
    "oyalage shop koheda", "shop eka koheda", "shop ekak koheda",
    "store eka koheda", "address koheda",
    "location koheda", "location eka koheda",
    "oyala inna koheda", "oba inna koheda",
    "shop thiyenne koheda", "thiyenne koheda",
    "koi theneda", "koitinade",
    # English
    "where is your shop", "where are you located",
    "where is the shop", "your location", "shop address",
    "how to find you", "how to come",
]

# Delivery typos / Singlish
DELIVERY_TRIGGERS = [
    # English typos
    "delivary", "dilivery", "deliveri", "dlivery", "dlvry",
    "delevery", "delivry", "deliveryyy",
    # Singlish
    "deliver karanawada", "deliver karannada",
    "deliver karanawad", "deliver karanawa",
    "eka dawasata", "ekada wasata",
    "medata", "me dawase",
    "kohomada yawanne", "kohomada yanne",
    "deliver karanawada", "deliver karannada",
    # Standard
    "delivery", "ship", "shipping", "courier",
]

# Order typos / Singlish
ORDER_TRIGGERS = [
    # Typos
    "ordr", "orda", "ordder", "ordere",
    # Singlish
    "order karanna", "order karana", "order karanna puluwanda",
    "order ekak", "order karanakam", "order denakola",
    "ganna ona", "ganna one", "ganna oone",
    # Standard
    "how to order", "place order", "want to order",
    "i want to buy", "purchase",
]

# Price typos / Singlish  
PRICE_TRIGGERS = [
    # Singlish
    "ganas kiyada", "ganas kiyad", "ganas kiyatha",
    "kiyadha", "kiyada", "kiyatha", "kiyanne",
    "mila kiyada", "mila kiyadha",
    "price ekak", "price eka", "prce", "pirce", "prise",
    # Standard
    "price", "cost", "how much", "charge", "fee",
    "mila", "milla",
]

# Payment typos / Singlish
PAYMENT_TRIGGERS = [
    # Singlish
    "gahanna puluwanda", "gahanna puluwan",
    "pay karanna puluwanda", "pay karanna puluwan",
    "gahanna ona", "gahanna one",
    "card ekennada", "online peyment",
    "bank transfer karanna", "bank trasfar",
    "cod tiyenavada", "cod thiyanawada",
    # Typos
    "paymant", "payement", "paymet",
    # Standard
    "payment", "pay", "cod", "cash on delivery",
    "bank transfer", "online pay", "card pay",
    "credit card", "debit card", "visa", "frimi",
    "ipay", "payhere", "ezcash", "mcash",
]

# Contact typos / Singlish
CONTACT_TRIGGERS = [
    # Singlish
    "number ekak denakola", "number eka denakola",
    "call karanna puluwanda", "call karanawada",
    "contact karanawada", "contact karanna",
    "nambar", "nombor", "nambara",
    # Typos
    "contct", "cotnact", "cntact",
    # Standard
    "contact", "call", "phone", "email", "reach",
    "whatsapp number", "phone number", "tell number",
]

# Discount typos / Singlish
DISCOUNT_TRIGGERS = [
    # Singlish
    "discount ekak tiyenavada", "discount thiyanawada",
    "offer ekak tiyenavada", "offer thiyanawada",
    "discount denawada", "discont", "discaunt",
    "sale ekak tiyenavada", "sale thiyanawada",
    "kata karannada", "kata karanawada",
    "aruwada", "aru wenawada",
    # Standard
    "discount", "offer", "sale", "promotion", "deal",
    "bulk", "wholesale", "loyalty", "points", "reward",
]

# Social media typos / Singlish
SOCIAL_TRIGGERS = [
    # Singlish
    "fb page eka koheda", "facebook page eka koheda",
    "insta page eka", "insta eka koheda",
    "tiktok eka koheda", "youtube eka koheda",
    "website ekak tiyenavada", "web site",
    "online kiyanawada",
    # Typos
    "fcebook", "facebok", "facbook",
    "instagarm", "instagran", "instragram",
    "youtub", "yotube",
    # Standard
    "instagram", "facebook", "tiktok", "youtube",
    "social", "follow", "fb", "ig", "website", "web",
]

# Same day / Express typos / Singlish
EXPRESS_TRIGGERS = [
    # Singlish
    "sameday delivery tiyenavada", "same day delivery thiyanawada",
    "awasara delivery", "awasaraya",
    "igena enna puluwanda", "igena",
    "flash delivery", "pickme flash",
    "eka dawasata yanawada", "eka dawasata",
    "medata yanawada", "medata",
    # Typos
    "same dy", "sameday", "samedday",
    # Standard
    "same day", "urgent", "fast delivery", "express", "flash",
]

# Quality / Organic typos / Singlish
QUALITY_TRIGGERS = [
    # Singlish
    "organic da", "organic nemada", "organic tiyenavada",
    "certified da", "sertified", "certificate",
    "local da nemada", "local items",
    "chemicals tiyenavada", "chemical free da",
    "kemical", "pestiside", "pestisaid",
    # Standard
    "certified", "quality", "authentic", "genuine",
    "expiry", "local", "imported", "import", "origin",
    "organic", "natural", "chemical", "pesticide",
]

# Gift / Packaging typos / Singlish
GIFT_TRIGGERS = [
    # Singlish
    "gift pack karanawada", "gift packet karanawada",
    "giftpack", "gift packe",
    "packing hamber", "haemper",
    # Standard
    "gift", "gift pack", "wrap", "eco", "fragile",
    "present", "hamper", "packaging",
]

# Corporate typos / Singlish
CORPORATE_TRIGGERS = [
    # Singlish
    "corporate order karanawada", "bulk order karanawada",
    "company ekkata", "office order",
    "gedara order", "kaaryalaya",
    "rasawalin order", "restorant order",
    # Typos
    "corparate", "corprate", "bulck", "wholsale",
    # Standard
    "corporate", "bulk order", "bulk buy", "wholesale",
    "office", "company", "event", "wedding", "large order",
    "business order", "reseller", "hotel", "restaurant",
]

# Hours typos / Singlish
HOURS_TRIGGERS = [
    # Singlish
    "wela kiyada", "welawa kiyada", "wela kiyath",
    "open da", "open wenawada", "open thiyanawada",
    "vakuththi kiyada", "kiyata open",
    "kiyata vashinna", "vashinna welawa",
    # Standard
    "hours", "open", "time", "opening", "close", "working",
    "what time", "when open",
]


# ==================================================
# FAQS
# ==================================================

FAQS = [
    {
        "keywords": ["hello", "hey", "start", "menu", "help", "info", "bot",
                     "ayubowan", "kohomada", "machan", "bro", "sis"],
        "reply": (
            "\U0001f44b Welcome to *Kenko 1st Organic!*\n\n"
            "\U0001f33f _Live a Healthy Life \u2014 Think Next Generation_\n\n"
            "How can we help you today? Type any of the following:\n\n"
            "\u2022 *products* \u2014 What we offer\n"
            "\u2022 *price* \u2014 Pricing info\n"
            "\u2022 *order* \u2014 How to order\n"
            "\u2022 *delivery* \u2014 Delivery info\n"
            "\u2022 *payment* \u2014 Payment methods\n"
            "\u2022 *location* \u2014 Find our shop\n"
            "\u2022 *contact* \u2014 Get in touch\n"
            "\u2022 *discount* \u2014 Offers & discounts\n"
            "\u2022 *social* \u2014 Find us online\n\n"
            "Or type any *product name* to check availability! \U0001f33f"
        )
    },
    {
        "keywords": ["product", "items", "what do you sell", "catalogue",
                     "catalog", "list", "what sell"],
        "reply": (
            "\U0001f331 *Kenko 1st Organic \u2014 Our Products*\n\n"
            "\U0001f966 Organic Vegetables & Fruits\n"
            "\U0001f33f Herbal Teas & Powders\n"
            "\U0001f965 Coconut Products\n"
            "\U0001f330 Nuts & Seeds\n"
            "\U0001f36f Bee Honey & Treacle\n"
            "\U0001f342 Kithul Products\n"
            "\U0001f36b Dark Chocolate\n"
            "\U0001fad9 Sauces & Condiments\n"
            "\U0001f48a Herbal Capsules\n"
            "\U0001f9f4 Natural Personal Care\n\n"
            "Type any product name to check if we have it! \U0001f60a\n"
            "_Example: 'Do you have chia seeds?'_"
        )
    },
    {
        "keywords": DISCOUNT_TRIGGERS,
        "reply": (
            "\U0001f389 *Kenko 1st Organic \u2014 Discounts & Offers*\n\n"
            "Up to *25% discount* on selected products!\n\n"
            "Bulk orders also qualify for discounts.\n\n"
            "Contact us to find out which products are on offer:\n"
            "\U0001f4f1 0715 800 800\n"
            "\U0001f4e7 kenkofood.srilanka@gmail.com\n\n"
            "_Note: Loyalty points / membership card not available at this time._"
        )
    },
    {
        "keywords": GIFT_TRIGGERS,
        "reply": (
            "\U0001f381 *Kenko 1st Organic \u2014 Packaging*\n\n"
            "\u2705 Gift packing available \u2014 just ask!\n"
            "\u2705 Eco-friendly packaging used \U0001f30d\n"
            "\u2705 Fragile items safely packed for delivery\n\n"
            "For gift orders or special packaging:\n"
            "\U0001f4f1 0715 800 800\n"
            "\U0001f4e7 kenkofood.srilanka@gmail.com"
        )
    },
    {
        "keywords": EXPRESS_TRIGGERS,
        "reply": (
            "\u26a1 *Kenko 1st Organic \u2014 Same Day & Express Delivery*\n\n"
            "\U0001f69a *Friday Delivery:* Our own delivery service runs on Fridays\n\n"
            "\U0001f4f1 *PickMe Flash:* Available for Colombo & nearby areas\n\n"
            "\U0001f1f1\U0001f1f0 *Island Wide:* Via courier \u2014 2 to 3 days\n\n"
            "For urgent orders:\n"
            "\U0001f4f1 0715 800 800"
        )
    },
    {
        "keywords": QUALITY_TRIGGERS,
        "reply": (
            "\U0001f33f *Kenko 1st Organic \u2014 Product Quality*\n\n"
            "\u2705 Organic certified products available\n"
            "\u2705 100% locally sourced from Sri Lankan farmers\n"
            "\u2705 Chemical-free & pesticide-free\n"
            "\u2705 Fresh & natural\n\n"
            "For certifications or product origin details:\n"
            "\U0001f4f1 0715 800 800\n"
            "\U0001f4e7 kenkofood.srilanka@gmail.com"
        )
    },
    {
        "keywords": PAYMENT_TRIGGERS,
        "reply": (
            "\U0001f4b3 *Kenko 1st Organic \u2014 Payment Methods*\n\n"
            "\u2705 Cash on Delivery (COD)\n"
            "\u2705 Bank Transfer\n"
            "\u2705 Online / Card Payment\n\n"
            "For payment details & bank account info:\n"
            "\U0001f4f1 0715 800 800\n"
            "\U0001f4e7 kenkofood.srilanka@gmail.com"
        )
    },
    {
        "keywords": SOCIAL_TRIGGERS,
        "reply": (
            "\U0001f4f1 *Kenko 1st Organic \u2014 Find Us Online*\n\n"
            "\U0001f310 Website: https://kenko1storganic.com\n\n"
            "\U0001f4d8 Facebook: https://www.facebook.com/Kenko1stOrganic\n\n"
            "\u25b6\ufe0f YouTube: https://www.youtube.com/@kenko1storganic715\n\n"
            "\U0001f3b5 TikTok: @kenko1storganic\n\n"
            "Follow us for latest offers & healthy tips! \U0001f33f"
        )
    },
    {
        "keywords": CORPORATE_TRIGGERS,
        "reply": (
            "\U0001f3e2 *Kenko 1st Organic \u2014 Corporate & Bulk Orders*\n\n"
            "\u2705 Corporate & bulk orders accepted!\n"
            "\u2705 Special discounts for large orders\n"
            "\u2705 Wedding, event & office supply orders welcome\n\n"
            "Contact us to discuss your requirements:\n"
            "\U0001f4f1 0715 800 800\n"
            "\U0001f4e7 kenkofood.srilanka@gmail.com\n\n"
            "We will customize the best package for you! \U0001f60a"
        )
    },
    {
        "keywords": PRICE_TRIGGERS,
        "reply": (
            "\U0001f4b0 *Kenko 1st Organic \u2014 Pricing*\n\n"
            "Prices vary by product.\n\n"
            "Message us with the item name for exact pricing:\n"
            "\U0001f4f1 0715 800 800\n"
            "\U0001f4e7 kenkofood.srilanka@gmail.com"
        )
    },
    {
        "keywords": ORDER_TRIGGERS,
        "reply": (
            "\U0001f6d2 *How to Order from Kenko 1st Organic*\n\n"
            "1\ufe0f\u20e3 Reply with the items you need\n"
            "2\ufe0f\u20e3 Share your Name, Address & Phone Number\n"
            "3\ufe0f\u20e3 We confirm your order & delivery date\n"
            "4\ufe0f\u20e3 Pay Cash on Delivery \u2014 easy! \U0001f60a\n\n"
            "No minimum order required!\n\n"
            "Also available on:\n"
            "\U0001f7e2 *Uber Eats* \u2014 Search 'Kenko 1st Organic'\n"
            "\U0001f535 *PickMe Food* \u2014 Search 'Kenko 1st Organic'"
        )
    },
    {
        "keywords": DELIVERY_TRIGGERS,
        "reply": (
            "\U0001f69a *Kenko 1st Organic \u2014 Delivery Info*\n\n"
            "\U0001f4cd *Colombo:*\n"
            "\u2022 All products \u2014 We will notify you as soon as your delivery is ready!\n\n"
            "\U0001f1f1\U0001f1f0 *Island Wide:*\n"
            "\u2022 Organic items, Herbal & Dry products \u2014 2 to 3 days\n"
            "\u2022 Vegetables & Fruits \u2014 Colombo only\n\n"
            "\U0001f4b5 Cash on Delivery available island-wide!"
        )
    },
    {
        "keywords": CONTACT_TRIGGERS,
        "reply": (
            "\U0001f4de *Kenko 1st Organic \u2014 Contact Us*\n\n"
            "\U0001f4f1 Phone: 0715 800 800\n"
            "\U0001f4e7 Email: kenkofood.srilanka@gmail.com\n"
            "\U0001f4ac WhatsApp: This number!\n\n"
            "\U0001f4cd 27/12, Rosmead Place, Colombo 07\n\n"
            "Our team is happy to help Every Day, 9AM – 8PM. \U0001f60a"
        )
    },
    {
        "keywords": HOURS_TRIGGERS,
        "reply": (
            "\U0001f550 *Kenko 1st Organic \u2014 Opening Hours*\n\n"
            "Every Day: 9:00 AM \u2013 8:00 PM\n\n"
            "\U0001f4f1 Online orders accepted 24/7!\n"
            "Delivery within working hours. \U0001f69a"
        )
    },
    {
        "keywords": ["uber", "pickme", "pick me", "ubereats", "food app", "app order"],
        "reply": (
            "\U0001f4f1 *Order via Food Delivery Apps*\n\n"
            "\U0001f7e2 *Uber Eats* \u2192 Search: _Kenko 1st Organic_\n\n"
            "\U0001f535 *PickMe Food* \u2192 Search: _Kenko 1st Organic_\n\n"
            "Or order directly via WhatsApp for island-wide delivery! \U0001f69a"
        )
    },
    {
        "keywords": ["return", "refund", "replace", "problem", "damaged",
                     "wrong item", "issue", "complaint", "badu", "bada item",
                     "narak", "kunu"],
        "reply": (
            "\U0001f504 *Kenko 1st Organic \u2014 Return & Refund Policy*\n\n"
            "If you receive a damaged or incorrect product, we will *replace it*! \u2705\n\n"
            "Simply message us with:\n"
            "1\ufe0f\u20e3 Your order details\n"
            "2\ufe0f\u20e3 A photo of the issue\n\n"
            "\U0001f4f1 0715 800 800\n"
            "\U0001f4e7 kenkofood.srilanka@gmail.com\n\n"
            "Your satisfaction is our priority! \U0001f33f"
        )
    },
]

DEFAULT_REPLY = (
    "\U0001f64f Thank you for contacting *Kenko 1st Organic!*\n\n"
    "Our team will get back to you shortly.\n\n"
    "For quick answers, type:\n"
    "\u2022 *products* \u2014 What we offer\n"
    "\u2022 *price* \u2014 Pricing\n"
    "\u2022 *order* \u2014 How to order\n"
    "\u2022 *delivery* \u2014 Delivery info\n"
    "\u2022 *location* \u2014 Find our shop\n"
    "\u2022 *contact* \u2014 Get in touch\n\n"
    "Or type any *product name* to check availability! \U0001f33f\n"
    "\U0001f4f1 0715 800 800"
)


def get_faq_reply(message):
    msg_lower = message.lower().strip()
    for faq in FAQS:
        if any(kw.lower() in msg_lower for kw in faq["keywords"]):
            return faq["reply"]
    return None


def is_location_query(message):
    msg_lower = message.lower()
    return any(t.lower() in msg_lower for t in LOCATION_TRIGGERS)


def is_availability_query(message):
    msg_lower = message.lower()
    return any(t.lower() in msg_lower for t in AVAILABILITY_TRIGGERS)


def find_products(query):
    query_words = query.lower().split()
    matches = []
    for product in PRODUCTS:
        product_lower = product.lower()
        if any(word in product_lower for word in query_words if len(word) > 2):
            matches.append(product)
    return matches


def product_reply(matches):
    if len(matches) == 1:
        return (
            f"\u2705 Yes! *{matches[0]}* is available at Kenko 1st Organic.\n\n"
            "To order, reply with:\n"
            "1\ufe0f\u20e3 Your Name\n"
            "2\ufe0f\u20e3 Delivery Address\n"
            "3\ufe0f\u20e3 Phone Number\n\n"
            "We'll confirm your order right away! \U0001f60a\n"
            "\U0001f4f1 0715 800 800 | \U0001f33f Kenko 1st Organic"
        )
    else:
        product_list = "\n".join(f"\u2022 {p}" for p in matches[:8])
        more = f"\n_...and {len(matches)-8} more!_" if len(matches) > 8 else ""
        return (
            f"\u2705 Yes! We have the following:\n\n"
            f"{product_list}{more}\n\n"
            "To order, reply with your Name, Address & Phone Number. \U0001f60a\n"
            "\U0001f4f1 0715 800 800 | \U0001f33f Kenko 1st Organic"
        )


LOCATION_REPLY = (
    "\U0001f4cd *Kenko 1st Organic \u2014 Our Location*\n\n"
    "\U0001f3ea Kenko 1st Organic\n"
    "27/12, Rosmead Place,\n"
    "Colombo 07\n\n"
    "\U0001f550 *Opening Hours:*\n"
    "Every Day: 9:00 AM \u2013 8:00 PM\n\n"
    "You're welcome to visit us anytime! \U0001f33f"
)

NOT_FOUND_REPLY = (
    "\U0001f64f Sorry, we couldn't find that specific item right now.\n\n"
    "Please contact us directly and we'll check for you!\n"
    "\U0001f4f1 0715 800 800\n"
    "\U0001f4e7 kenkofood.srilanka@gmail.com\n\n"
    "\U0001f33f Kenko 1st Organic"
)


def get_reply(message: str) -> str:
    msg_lower = message.lower().strip()

    # 1. Standalone greetings — exact match
    if msg_lower in GREETINGS:
        return next(f["reply"] for f in FAQS if "hello" in f["keywords"])

    # 2. Location query
    if is_location_query(message):
        return LOCATION_REPLY

    # 3. Availability query — check FAQ keywords first, then product search
    if is_availability_query(message):
        faq = get_faq_reply(message)
        if faq:
            return faq
        matches = find_products(message)
        if matches:
            return product_reply(matches)
        return NOT_FOUND_REPLY

    # 4. FAQ keyword match
    faq = get_faq_reply(message)
    if faq:
        return faq

    # 5. General product search (English)
    matches = find_products(message)
    if matches:
        return product_reply(matches)

    # 6. Default
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
    return "\u2705 Kenko 1st Organic WhatsApp Bot is running!"


if __name__ == "__main__":
    app.run(debug=False)
