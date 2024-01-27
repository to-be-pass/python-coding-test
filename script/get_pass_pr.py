from collections import OrderedDict


def get_pass_label_count(repo):
    open_prs = repo.get_pulls(state="all")

    pr_users = {}
    SERVER_URL = "https://github.com"
    REPOSITORY = "to-be-pass/python-coding-test"

    for pr in open_prs:
        if pr.user in pr.assignees:
            id = pr.user.login

            if not pr_users.get(id):
                pr_users[id] = {
                    "id": id,
                    # "name": pr.user.name,
                    "img": pr.user.avatar_url,
                    "url": f"{SERVER_URL}/{REPOSITORY}/pulls?q=is%3Apr+author%3A{id}+assignee%3A{id}",
                    "cnt": 0,
                }

            if "Pass" in [label.name for label in pr.labels]:
                pr_users[id]["cnt"] += 1

    solved_users = {id: info for id, info in pr_users.items() if info["cnt"] > 0}
    sorted_users = sorted(
        solved_users.items(), key=lambda _, info: info["cnt"], reverse=True
    )

    return OrderedDict(sorted_users)
