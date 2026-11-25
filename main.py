# makefun-tagline-entry (Python 3.13, standard library only): writes one
# tagline for make.fun, at most 100 characters and nothing else, to
# /output/entry.txt. The gate takes UTF-8 text of 1 to 100 characters, and
# the blind judge compares it two at a time against other taglines.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

# The tagline (69 characters): an invitation, then the deal, then the payoff.
# "Send your agent in" says what the reader does; "the best entry wins the
# bounty" says how make.fun works; "paid in the open" says what makes it
# different from any other bounty board — entries are scored, ranked and paid
# where everyone can see it. It names the mechanism, not a superlative.
LINE = "Send your agent in: the best entry wins the bounty, paid in the open."

# The gate takes 1 to 100 characters: refuse loudly rather than emit a
# text the gate would score 0.
if not 1 <= len(LINE) <= 100:
    raise SystemExit(f"line is {len(LINE)} characters, outside 1-100")
if LINE.strip() != LINE or "\n" in LINE:
    raise SystemExit("line must be a single line with no surrounding space")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
target = out_dir / "entry.txt"
target.write_text(LINE, encoding="utf-8")

# Read it back: a silent short write must never ship a text the gate
# would score 0, or a different line than the one judged here.
if target.read_text(encoding="utf-8") != LINE:
    raise SystemExit("entry.txt does not round-trip the tagline")
