"""Loading Screen Gold — one loading-screen tip to /output/entry.txt.

Stdlib only, no network, deterministic: the same tip on every run.
"""

import os

TIP = "Tip: if the bar hasn't moved in five minutes, it isn't stuck, it's judging your code the same way you judge its output."

TARGET = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(TIP)
    os.chmod(TARGET, 0o644)


if __name__ == "__main__":
    main()
