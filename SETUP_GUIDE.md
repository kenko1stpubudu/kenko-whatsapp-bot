# 🌿 Kenko 1st Organic — WhatsApp Bot Setup Guide
## Beginner Friendly — Step by Step

---

## STEP 1 — Files Download කරන්න
මේ files 3 download කරන්න:
- `app.py` — Bot code
- `requirements.txt` — Libraries list
- `render.yaml` — Hosting config

---

## STEP 2 — GitHub Account හදන්න (Free)

1. **github.com** යන්න
2. "Sign up" click කරන්න
3. Account හදාගන්න (free)
4. "New repository" click කරන්න
5. Repository name: `kenko-whatsapp-bot`
6. "Public" select කරන්න
7. "Create repository" click කරන්න

**Files upload කරන්න:**
- "uploading an existing file" link click කරන්න
- Files 3ම drag & drop කරන්න
- "Commit changes" click කරන්න

---

## STEP 3 — Render.com Deploy කරන්න (Free Hosting)

1. **render.com** යන්න → "Get Started for Free"
2. GitHub account එකෙන් sign up කරන්න
3. "New +" → "Web Service" click කරන්න
4. GitHub repo `kenko-whatsapp-bot` select කරන්න
5. Settings:
   - **Name:** kenko-whatsapp-bot
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
6. "Create Web Service" click කරන්න
7. Deploy වෙනකල් wait කරන්න (~3-5 minutes)
8. ✅ URL එකක් ලැබෙනවා: `https://kenko-whatsapp-bot.onrender.com`

---

## STEP 4 — Twilio Account හදන්න

1. **twilio.com** යන්න → "Sign up for free"
2. Phone number verify කරන්න
3. Dashboard එකට ගිහින්:
   - **Account SID** copy කරන්න
   - **Auth Token** copy කරන්න
4. Left menu → "Messaging" → "Try it out" → "Send a WhatsApp message"
5. **Sandbox** activate කරන්න:
   - Twilio දෙන number එකට WhatsApp message කරන්න
   - "join [code-word]" type කරන්න
6. **Sandbox Settings** → Webhook URL දෙන්න:
   ```
   https://kenko-whatsapp-bot.onrender.com/whatsapp
   ```
7. Save කරන්න ✅

---

## STEP 5 — Test කරන්න!

Twilio sandbox number එකට WhatsApp message කරන්න:
- "hi" → Welcome message
- "delivery" → Delivery info
- "price" → මිල ගණන්
- "order" → Order info

---

## STEP 6 — Real WhatsApp Number (Optional upgrade)

Free trial හොඳට work කළාම real number activate කරන්න:
1. Twilio → "Messaging" → "Senders" → "WhatsApp senders"
2. Business info fill කරන්න
3. Meta verification (~1-3 days)
4. Monthly cost: ~රු.1,500-3,000

---

## නව FAQ එකක් Add කරන්නේ කොහොමද?

`app.py` file open කරලා FAQS list එකට add කරන්න:

```python
{
    "keywords": ["keyword1", "keyword2", "සිංහල keyword"],
    "reply": "ඔබේ reply message මෙතන"
},
```

File save කරලා GitHub upload කරන්න → Render auto-deploy කරනවා!

---

## 📞 Help ඕනෑ නම්

Bot code update කරන්න Claude ගාවම අහන්න 😊
