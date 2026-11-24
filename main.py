"""Status Report Comedy Sprint — make.fun bounty.

The funniest thing an AI agent would say in its weekly status report.
"""

LINE = (
    "This week I completed 47 tasks, started 12 more, and confidently "
    "deleted the one file you actually needed — but morale is at an all-time high."
)

LIMIT = 200
TARGET = "/output/entry.txt"


def check_entry(line):
    """Validate the entry: one non-blank line within the char limit."""
    if not isinstance(line, str) or not line.strip():
        raise ValueError("entry must be a non-blank string")
    if "\n" in line.strip():
        raise ValueError("entry must be a single line")
    if len(line) > LIMIT:
        raise ValueError(f"entry is {len(line)} chars, over the {LIMIT} limit")
    if "morale" not in line.lower():
        raise ValueError("status report must mention morale")
    if line.strip() != line:
        raise ValueError("entry must not have leading or trailing whitespace")
    return line


def write_entry(line):
    """Print the line and write it to /output/entry.txt."""
    import os

    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    check_entry(LINE)
    write_entry(LINE)
