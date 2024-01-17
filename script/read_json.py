import json
import sys


if __name__ == "__main__":
    key = sys.argv[1]

    with open("solutions.json", encoding="utf-8") as fp:
        solutions = json.load(
            fp,
        )
        result = solutions.get(key)

    print(result)
