# BdayNotifier

Automated birthday reminder system using n8n workflow automation. Sends Telegram notifications 1 day before birthdays using Google Sheets data and AI-generated messages.

## Demo

[![Demo Video](https://img.youtube.com/vi/vLQZUSjxpXA/0.jpg)](https://youtu.be/vLQZUSjxpXA)

**[Watch Live Demo](https://youtu.be/vLQZUSjxpXA)**

## Features

- Daily automated checks at scheduled times
- Google Sheets integration for birthday data
- AI-powered personalized message generation
- Telegram bot delivery
- One-day advance notifications

## Google Sheets Format

Your Google Sheet named `Birthday_List` should follow this format:

| Name          | Date to reminder | Date of Birth |
|---------------|------------------|---------------|
| Arushan       | 09-04            | 10-04         |
| Kugaparan     | 29-05            | 30-05         |
| Thiruvarankan | 07-07            | 08-07         |

**Note:** Use `dd-MM` format. "Date to reminder" should be one day before the actual birthday.

## Workflow Logic

1. **Schedule Trigger** - Runs daily at 2:00 AM & 3:15 AM
2. **Date Formatting** - Formats today's date as `dd-MM`
3. **Google Sheets Lookup** - Matches today's date with reminder column
4. **Python Filtering** - Confirms birthday falls tomorrow
5. **AI Message Generation** - Creates personalized message via OpenRouter
6. **Telegram Notification** - Sends message to your account

## Setup

### Import Workflow
1. Open your n8n instance
2. Click **Import** and upload `BdayNotifier.json`
3. Configure the following credentials in n8n:
   - Google Sheets OAuth2
   - Telegram Bot API
   - OpenRouter AI

### Configure Data Source
- Ensure Google Sheet is accessible
- Set correct document ID and sheet name in the workflow
- Activate the workflow to run automatically

## Tech Stack

- **n8n** - Workflow automation
- **Python** - Logic and date parsing
- **Google Sheets** - Data storage
- **OpenRouter AI** - Message generation
- **Telegram Bot API** - Notifications

## Workflow Screenshot

![BdayNotifier Workflow](https://github.com/ThiruvarankanM/Bday-Notifier-n8n/blob/38b14059729e06448a3eb149734d07a29bc9e158/N8N_Workflow.png)

## License

MIT License
