import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Lấy token từ biến môi trường
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN")  # bắt đầu với xapp-
print(f"SLACK_BOT_TOKEN: {SLACK_BOT_TOKEN}")
print(f"SLACK_APP_TOKEN: {SLACK_APP_TOKEN}")

# Khởi tạo app
app = App(token=SLACK_BOT_TOKEN)

# Gửi phản hồi khi bot bị mention
@app.event("app_mention")
def handle_mention(event, say, client):
    user = event["user"]
    channel = event["channel"]
    ts = event["ts"]

    # Phản hồi
    say(f"Yo <@{user}>, tôi thấy ông gọi rồi nè 😎")

@app.message("help")
def help_command(message, say):
    say(
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Hi! SlackBot_0 🤖*\n\nTôi có thể làm những thứ sau:"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*`roll`*: Roll một con xúc xắc 🎲"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*`help`*: Xem các lệnh hiện có"
                    }
                ]
            }
        ],
        text="SlackBot_0 Command List"
    )
# Chạy bot
if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
