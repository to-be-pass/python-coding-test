import sys


if __name__ == "__main__":
    head_ref: str = sys.argv[1]

    print(head_ref.split("/")[-1])
