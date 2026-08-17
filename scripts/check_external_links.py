"""Check external Markdown links in a scheduled, retry-tolerant job."""

from __future__ import annotations

import argparse
import concurrent.futures
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
LINK_PATTERN = re.compile(r"\[[^\]]+\]\((https?://[^) >]+)")
SOFT_STATUSES = {401, 403, 405, 429}


def discover_links() -> list[str]:
    links: set[str] = set()
    for path in ROOT.rglob("*.md"):
        if any(part in {".git", ".venv", "artifacts"} for part in path.parts):
            continue
        for target in LINK_PATTERN.findall(path.read_text(encoding="utf-8")):
            parsed = urlparse(target)
            if parsed.scheme in {"http", "https"} and parsed.netloc:
                links.add(target)
    return sorted(links)


def check_link(url: str, timeout: float, retries: int) -> tuple[str, bool, str]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "ttai-internship-link-check/1.0", "Range": "bytes=0-1023"},
        method="GET",
    )
    last_error = "unknown error"
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                status = int(response.status)
                return url, status < 400 or status in SOFT_STATUSES, f"HTTP {status}"
        except urllib.error.HTTPError as error:
            status = int(error.code)
            if status < 400 or status in SOFT_STATUSES:
                return url, True, f"HTTP {status}"
            last_error = f"HTTP {status}"
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            last_error = str(error.reason if isinstance(error, urllib.error.URLError) else error)
        if attempt < retries:
            time.sleep(1.5 * (attempt + 1))
    return url, False, last_error


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--list-only", action="store_true")
    args = parser.parse_args()

    links = discover_links()
    if args.list_only:
        print("\n".join(links))
        return 0
    failures: list[tuple[str, str]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = [executor.submit(check_link, url, args.timeout, args.retries) for url in links]
        for future in concurrent.futures.as_completed(futures):
            url, ok, detail = future.result()
            print(f"{'PASS' if ok else 'FAIL'} {detail} {url}")
            if not ok:
                failures.append((url, detail))
    if failures:
        print(f"External link check failed for {len(failures)} of {len(links)} links.", file=sys.stderr)
        return 1
    print(f"Validated {len(links)} external links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
