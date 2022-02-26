from datetime import datetime

import requests  # type: ignore[import]


class GitHubWorker:
    def __init__(self, token, owner) -> None:
        self.token = token
        self.owner = owner
        self.base_url = "https://api.github.com"
        self.today = datetime.now().strftime("%Y-%m-$d")

    def create_issue(self, repo):
        response = requests.post(
            url=self.base_url + f"/repos/{self.owner}/{repo}/issues",
            headers={"Authorization": f"token {self.token}"},
            data={
                "title": f"{self.today} weekly retrospective",
                "body": "",
                "labels": "Weekly\U0001F389",
            },
        )
        print(response)
