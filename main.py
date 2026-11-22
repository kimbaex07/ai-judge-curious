"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt.
"""

import os

TEXT = (
    "This morning the lighthouse keeper found a bottle, and inside it a letter, "
    "addressed to someone who hasn't been born yet. It begins: 'By the time "
    "you read this, the sea will have given back what it took.' He has read "
    "it four times now. The handwriting is his own."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()
