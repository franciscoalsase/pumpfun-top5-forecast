"""Entry for make.fun news-summary-01: writes the summary of 11 November 2026."""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
MAX_CHARS = 2000


def main() -> None:
    text = (HERE / "summary.txt").read_text(encoding="utf-8")
    # Normalise line ends and trim, so both runs write identical bytes.
    text = text.replace("\r\n", "\n").strip()
    # The gate takes 1 to 2,000 Unicode code points, not only white space.
    if not text or len(text) > MAX_CHARS:
        raise SystemExit(f"summary has {len(text)} characters; need 1..{MAX_CHARS}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "entry.txt").write_bytes(text.encode("utf-8"))


if __name__ == "__main__":
    main()
