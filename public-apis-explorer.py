#!/usr/bin/env python3
"""
public-apis-explorer.py
A simple CLI tool to explore the public-apis list locally.

Self-delivered by the persistent-self-coder skill after analyzing trending repositories.
"""

import json
import sys
import urllib.request
from pathlib import Path
from typing import List, Dict

API_LIST_URL = "https://raw.githubusercontent.com/public-apis/public-apis/master/README.md"
CACHE_FILE = Path.home() / ".cache" / "public-apis.json"


def fetch_apis() -> List[Dict]:
    """Fetch and parse the public APIs list (simple parser for the README table)."""
    print("Fetching latest public APIs list...")
    try:
        with urllib.request.urlopen(API_LIST_URL, timeout=15) as response:
            content = response.read().decode("utf-8")
    except Exception as e:
        print(f"Error fetching APIs: {e}")
        return []

    apis = []
    in_table = False
    for line in content.splitlines():
        if "| API | Description | Auth | HTTPS | CORS |" in line:
            in_table = True
            continue
        if in_table and line.startswith("|") and not line.startswith("|---"):
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 5:
                apis.append({
                    "name": parts[0].replace("**", "").strip(),
                    "description": parts[1].strip(),
                    "auth": parts[2].strip(),
                    "https": parts[3].strip(),
                    "cors": parts[4].strip()
                })
    return apis


def search_apis(apis: List[Dict], query: str) -> List[Dict]:
    """Simple search across name and description."""
    query = query.lower()
    return [api for api in apis if query in api["name"].lower() or query in api["description"].lower()]


def main():
    if len(sys.argv) < 2:
        print("Usage: python public-apis-explorer.py <search-term>")
        print("Example: python public-apis-explorer.py weather")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    apis = fetch_apis()

    if not apis:
        print("Could not load API list.")
        sys.exit(1)

    results = search_apis(apis, query)

    print(f"\nFound {len(results)} APIs matching '{query}':\n")
    for api in results[:15]:  # Limit output
        print(f"• {api['name']}")
        print(f"  {api['description']}")
        print(f"  Auth: {api['auth']} | HTTPS: {api['https']} | CORS: {api['cors']}\n")


if __name__ == "__main__":
    main()
