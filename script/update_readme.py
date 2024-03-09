from github import Github
import sys
import re

from get_pass_pr import get_pass_label_count
from readme_html import start_html, avatar_html, end_html


def update_readme(token, repo_full_name):
    github = Github(token)
    repo = github.get_repo(repo_full_name)

    # README.md 파일을 가져옵니다.
    readme_file = repo.get_contents("README.md")
    readme_content = readme_file.decoded_content.decode("utf-8")

    # 새로운 데이터를 받아옵니다.
    pass_label_counts = get_pass_label_count(repo)

    # <!-- PR Status Start -->와 <!-- PR Status End --> 사이의 부분을 새로운 데이터로 교체합니다.
    pattern = r"<!-- PR Status Start -->(.*?)<!-- PR Status End -->"
    new_content = re.sub(
        pattern,
        f"<!-- PR Status Start -->\n\n{start_html}{get_updated_data(pass_label_counts)}\n{end_html}\n\n<!-- PR Status End -->",
        readme_content,
        flags=re.DOTALL,
    )

    # README.md 파일을 업데이트합니다.
    repo.update_file(
        path=readme_file.path,
        message="Update README.md",
        content=new_content,
        sha=readme_file.sha,
    )


def get_updated_data(pass_label_counts):
    updated_data = ""
    total = 85

    col = 0
    for id, info in pass_label_counts.items():
        # TODO 전부 패스인 사람 = 명예전당
        col += 1
        if col == 1:
            updated_data += "<tr>" + avatar_html.format(**info, total=total)
        elif col == 5:
            col = 0
            updated_data += avatar_html.format(**info, total=total) + "</tr>"
        else:
            updated_data += avatar_html.format(**info, total=total)
    if col != 0:
        updated_data += "</tr>"

    return updated_data


if __name__ == "__main__":
    token: str = sys.argv[1]
    repo_full_name = sys.argv[2]

    update_readme(token, repo_full_name)
