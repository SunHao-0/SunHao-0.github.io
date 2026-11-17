#!/usr/bin/env python3
"""Regenerate the commit list in linux.html from a Linux git tree.

Usage: tools/linux_commits.py <linux-repo> [<ref>]

Lists the non-merge commits reachable from <ref> (default HEAD) whose author
or message carries one of ADDRESSES, newest first, and rewrites the rows
between the commits:begin and commits:end markers. Use a mainline ref: the
links point to Linus's tree, where a commit still in bpf-next does not exist.
"""
import datetime
import html
import pathlib
import re
import subprocess
import sys

ADDRESSES = ["sunhao.th@gmail.com", "hao.sun@inf.ethz.ch", "sunhaoyl@outlook.com"]
URL = "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id="
PAGE = pathlib.Path(__file__).resolve().parent.parent / "linux.html"

ROW = """    <li>
      <span class="when">{date}</span>
      <span>{subject}
        <span class="where"><code>{short}</code> &middot; <a href="{url}">git.kernel.org</a></span></span>
    </li>"""


def commits(repo, ref):
    """(hash, commit date, subject) for each matching commit, newest first."""
    pattern = "|".join(re.escape(a) for a in ADDRESSES)
    found = {}
    # git log ANDs --author with --grep, so run one query for each and merge.
    for flag in ("--author", "--grep"):
        out = subprocess.run(
            ["git", "-C", repo, "log", ref, "--no-merges", "-E", "-i",
             f"{flag}={pattern}", "--format=%H%x00%cs%x00%s"],
            check=True, capture_output=True, text=True).stdout
        for line in out.splitlines():
            sha, date, subject = line.split("\0")
            found[sha] = (date, subject)
    return sorted(((sha, d, s) for sha, (d, s) in found.items()),
                  key=lambda c: (c[1], c[0]), reverse=True)


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__.split("\n\n")[1])
    repo = sys.argv[1]
    ref = sys.argv[2] if len(sys.argv) == 3 else "HEAD"

    rows = "\n".join(
        ROW.format(date=d, subject=html.escape(s), short=sha[:12], url=URL + sha)
        for sha, d, s in commits(repo, ref))
    today = datetime.date.today()

    text = PAGE.read_text()
    text = re.sub(r"(<!-- commits:begin -->).*?(\n\s*<!-- commits:end -->)",
                  lambda m: m.group(1) + "\n" + rows + m.group(2), text, flags=re.S)
    text = re.sub(r'<time id="generated"[^>]*>.*?</time>',
                  f'<time id="generated" datetime="{today}">{today.day} {today:%B %Y}</time>', text)
    PAGE.write_text(text)
    print(f"{rows.count('<li>')} commits written to {PAGE.name}")


if __name__ == "__main__":
    main()
