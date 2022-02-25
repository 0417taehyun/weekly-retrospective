import requests  # type: ignore[import]


class GitHubWorker:
    def __init__(self, token, owner) -> None:
        self.token = token
        self.owner = owner
        self.base_url = "https://api.github.com"

    def create_issue(self, repo):
        response = requests.post(
            url=self.base_url + f"/repos/{self.owner}/{repo}/issues",
            headers={"Authorization": f"token {self.token}"},
            data={"title": "", "body": "", "labels": ""},
        )
        print(response)
