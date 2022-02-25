from slack_sdk import WebClient


class SlackWorker:
    def __init__(self, token) -> None:
        self.client = WebClient(token=token)

    def get_(self):
        pass
