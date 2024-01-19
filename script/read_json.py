import json
import sys


if __name__ == "__main__":
    path = sys.argv[1]
    key = sys.argv[2]

    with open(f"{path}", encoding="utf-8") as fp:
        solutions = json.load(
            fp,
        )
        result = solutions.get(key)

    print(result)
