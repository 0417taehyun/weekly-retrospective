from slack_sdk import WebClient


class SlackWorker:
    def __init__(self, token) -> None:
        self.client = WebClient(token=token)

    def create_issue_template(self, channel, option):
        blocks = {}

        if option == "weekly":
            blocks = {}

        self.client.chat_postMessage(channel=channel, blocks=blocks)
