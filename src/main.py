def lambda_handler(event, context):
    pass


if __name__ == "__main__":
    with open(".github/ISSUE_TEMPLATE/retrospective_weekly.md", "r") as f:
        text = f.read()
