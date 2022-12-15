# Name: Jerico James F. Viteño
# Laboratory Exercise 4: Stacks, Queues, and Priority Queues in Practice
# 4. Using Asynchronous Queues
# December 17, 2022

# First, install "python -m pip install rich"

# Imports

# 1
import argparse
import asyncio
from collections import Counter
import aiohttp

# 2
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# 3
import sys
from typing import NamedTuple

# 3: Data type
class Job(NamedTuple):
    url: str
    depth: int = 1

# 1: Building Blocks
async def main(args):
    session = aiohttp.ClientSession()
    try:
        links = Counter()
        display(links)
    finally:
        await session.close()

# 3: Defined a new data type, as well as an asynchronous worker performing the job
async def worker(worker_id, session, queue, links, max_depth):
    print(f"[{worker_id} starting]", file=sys.stderr)
    while True:
        url, depth = await queue.get()
        links[url] += 1
        try:
            if depth <= max_depth:
                print(f"[{worker_id} {depth=} {url=}]", file=sys.stderr)
                if html := await fetch_html(session, url):
                    for link_url in parse_links(url, html):
                        await queue.put(Job(link_url, depth + 1))
        except aiohttp.ClientError:
            print(f"[{worker_id} failed at {url=}]", file=sys.stderr)
        finally:
            queue.task_done()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("-d", "--max-depth", type=int, default=2)
    parser.add_argument("-w", "--num-workers", type=int, default=3)
    return parser.parse_args()

async def fetch_html(session, url):
    async with session.get(url) as response:
        if response.ok and response.content_type == "text/html":
            return await response.text()

# 2: Added fetching content and parsing HTML links
def parse_links(url, html):
    soup = BeautifulSoup(html, features="html.parser")
    for anchor in soup.select("a[href]"):
        href = anchor.get("href").lower()
        if not href.startswith("javascript:"):
            yield urljoin(url, href)

def display(links):
    for url, count in links.most_common():
        print(f"{count:>3} {url}")

if __name__ == "__main__":
    asyncio.run(main(parse_args()))