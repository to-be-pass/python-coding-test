def get_pass_label_count(repo):
    open_prs = repo.get_pulls(state="all")

    users = {}
    SERVER_URL = "https://github.com"
    REPOSITORY = "to-be-pass/python-coding-test"

    for pr in open_prs:
        if pr.user in pr.assignees:
            id = pr.user.login

            if not users.get(id):
                users[id] = {
                    "id": id,
                    # "name": pr.user.name,
                    "img": pr.user.avatar_url,
                    "url": f"{SERVER_URL}/{REPOSITORY}/pulls?q=is%3Apr+author%3A{id}+assignee%3A{id}",
                    "cnt": 0,
                }

            if "Pass" in [label.name for label in pr.labels]:
                users[id]["cnt"] += 1

    return sorted(
        [user for user in users if user["cnt"] > 0],
        key=lambda user: user["cnt"],
        reverse=True,
    )
