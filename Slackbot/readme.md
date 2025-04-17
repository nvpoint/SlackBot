
## 📦 Setup

## 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/nvpoint/SlackBot.git
cd SlackBot
```
## 2. Set Up the Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # on Windows, use venv\Scripts\activate
```
## 3. Install the Required Packages
```bash
pip install -r requirements.txt
```
## 4. Create the .env File
```bash
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token-here
SLACK_APP_TOKEN=xapp-your-slack-app-token-here
```
## 5. Run the Bot
```bash
python bot/startbot.py
```
