# 🎂 BdayNotifier – Birthday Reminder via Telegram using n8n

**BdayNotifier** is a smart, automated workflow built using [n8n](https://n8n.io/) that reminds you of birthdays **1 day in advance**, sending messages directly to your **Telegram bot**.

No more forgetting birthdays – let your bot keep you updated and ready to send your wishes 🎉

---

## 📌 Features

- ⏰ **Daily Scheduled Checks**  
- 📄 **Google Sheets Integration**  
- 🧠 **AI-Powered Personalized Messages**  
- 🤖 **Telegram Message Delivery**  
- ⚙️ **Fully Customizable & Extendable**

---

## 📁 Google Sheets Format (Example)

Make sure your Google Sheet (named `Birthday_List`) follows this format:

| Name          | Date to reminder | Date of Birth |
|---------------|------------------|----------------|
| Arushan       | 09-04            | 10-04          |
| Kugaparan     | 29-05            | 30-05          |
| Thiruvarankan | 07-07            | 08-07          |
| Abisan        | 08-08            | 09-08          |
| Changeethan   | 08-08            | 09-08          |
| Kopithan      | 09-08            | 10-08          |

📝 **Notes**:
- Dates should be in `dd-MM` format (without year).
- “Date to reminder” must be **one day before** the actual birthday.

---

## 🔄 How It Works (Workflow Logic)

1. **Schedule Trigger** – Runs automatically every day at 2:00 AM & 3:15 AM.
2. **Date Formatting** – Fetches and formats today’s date as `dd-MM`.
3. **Google Sheets Lookup** – Matches today's date with the "Date to reminder" column.
4. **Python Filtering** – Confirms if the birthday falls tomorrow (based on "Date of Birth").
5. **Condition Check** – If matches are found, proceed; otherwise, stop.
6. **AI Message Generation** – Uses an OpenRouter-powered AI agent to create a custom message.
7. **Telegram Notification** – Sends the generated message directly to your Telegram account.

---

## 🚀 Setup Instructions

### 1. Clone or Download the Repo

```bash
git clone https://github.com/yourusername/BdayNotifier.git
````

### 2. Import the Workflow into n8n

* Open your n8n instance.
* Click **Import** → Upload the included `BdayNotifier.json` file.
* You’ll see the entire birthday reminder workflow appear.

### 3. Configure Credentials

Ensure the following credentials are added in n8n:

* **Google Sheets OAuth2** – Access the sheet containing birthday data.
* **Telegram Bot API** – For message delivery.
* **OpenRouter (AI)** – Used for generating birthday messages using models like DeepSeek.

### 4. Set Your Google Sheet

Ensure your sheet is:

* Public or shared with your Google Sheets integration account.
* The correct **document ID** and **sheet name/gid** are configured in the `Get row(s) in sheet` node.

---

## 🧠 Tech Stack

* 🔄 **n8n** – Workflow automation
* 🐍 **Python** – For logic and date parsing
* 📄 **Google Sheets** – Data source
* 🧠 **OpenRouter AI** – Custom message generation
* 🤖 **Telegram Bot API** – For reminders

---

## 🛠️ Customize This Project

You can easily adapt this workflow to:

* Send reminders to groups
* Trigger SMS or email instead of Telegram
* Add birthday age, personalized notes, etc.

---

## 📸 Screenshots (Optional)

*Add screenshots of your n8n workflow here to visually show how it works.*

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
Free to use, share, and modify!

---

## 💡 Tip

> Set your workflow to **active** to run it automatically.
> You’ll never miss a birthday again – and your wishes will always be on time! 🥳

---

## ✨ Built With

Created by \[M.Thiruvarankan]
🔗 Powered by [n8n.io](https://n8n.io), [OpenRouter.ai](https://openrouter.ai), and [Telegram Bot API](https://core.telegram.org/bots/api)

```

