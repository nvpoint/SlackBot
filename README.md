## 📎 Project Here
Click [here](/Slackbot/readme.md) to view the README for this project.

## 📦 Setup

### Step 1: Create a Slack App

1. Go to [Slack API](https://api.slack.com/apps) and click **Create New App**.
2. Select **From Scratch** and choose a name for your app (e.g., `SlackBot_0`) and select the workspace where you'd like to install the app.
3. Click **Create App**.

### Step 2: Configure Bot Permissions

1. In your app's settings, go to **OAuth & Permissions**.
2. Under **Bot Token Scopes**, add the following permissions:
   - `chat:write`
   - `app_mentions:read`
   - `channels:read`
   - `channels:history`
   - `groups:history`
   - `im:history`
   - `mpim:history`

3. Enable **Socket Mode** by going to the **Settings** → **Interactivity & Shortcuts** and toggle the **Enable Interactivity** button.
4. Then, go to **Settings** → **Socket Mode** and toggle the **Enable Socket Mode** button.
5. Save your changes.

### Step 3: Install the App to Your Workspace

1. Go to the **OAuth & Permissions** page of your app.
2. Click the **Install App to Workspace** button.
3. Review the permissions and click **Allow** to install the bot in your workspace.

### Step 4: Create a `.env` File

Create a `.env` file in the project directory and add your **Slack bot token** and **app token**:

```env
SLACK_BOT_TOKEN=xoxb-your-token
SLACK_APP_TOKEN=xapp-your-app-token
```
## final result
![Bot replying in Slack](https://github.com/nvpoint/SlackBot/blob/main/image/image.png)
