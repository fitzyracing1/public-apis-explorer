#!/usr/bin/env python3
"""
public-apis-explorer.py (Offline Version)
A fast, offline CLI tool to explore popular public APIs.

This version includes a bundled dataset so it works without internet.
Self-delivered and improved by the persistent-self-coder skill.
"""

import sys
from typing import List, Dict

# Bundled popular APIs dataset (curated sample - easily extendable)
APIS = [
    {"name": "OpenWeatherMap", "description": "Weather data and forecasts", "auth": "apiKey", "https": "Yes", "cors": "Yes", "category": "Weather"},
    {"name": "WeatherAPI", "description": "Real-time weather information", "auth": "apiKey", "https": "Yes", "cors": "Yes", "category": "Weather"},
    {"name": "Google Maps", "description": "Maps, geocoding, directions", "auth": "apiKey", "https": "Yes", "cors": "Yes", "category": "Maps"},
    {"name": "GitHub API", "description": "Access GitHub repositories and user data", "auth": "OAuth", "https": "Yes", "cors": "Yes", "category": "Development"},
    {"name": "Spotify", "description": "Music streaming and metadata", "auth": "OAuth", "https": "Yes", "cors": "Yes", "category": "Music"},
    {"name": "YouTube Data", "description": "Search and manage YouTube videos", "auth": "OAuth", "https": "Yes", "cors": "Yes", "category": "Video"},
    {"name": "Twitter API v2", "description": "Access Twitter data and post tweets", "auth": "OAuth", "https": "Yes", "cors": "Yes", "category": "Social"},
    {"name": "Stripe", "description": "Payment processing", "auth": "apiKey", "https": "Yes", "cors": "Yes", "category": "Finance"},
    {"name": "CoinGecko", "description": "Cryptocurrency data and market info", "auth": "No", "https": "Yes", "cors": "Yes", "category": "Finance"},
    {"name": "NASA APOD", "description": "Astronomy Picture of the Day", "auth": "apiKey", "https": "Yes", "cors": "Yes", "category": "Science"},
    {"name": "JokeAPI", "description": "Random jokes", "auth": "No", "https": "Yes", "cors": "Yes", "category": "Entertainment"},
    {"name": "REST Countries", "description": "Country information", "auth": "No", "https": "Yes", "cors": "Yes", "category": "Data"},
    {"name": "JSONPlaceholder", "description": "Fake REST API for testing", "auth": "No", "https": "Yes", "cors": "Yes", "category": "Development"},
    {"name": "Dog CEO", "description": "Random dog images", "auth": "No", "https": "Yes", "cors": "Yes", "category": "Animals"},
    {"name": "Cat Facts", "description": "Daily cat facts", "auth": "No", "https": "Yes", "cors": "Yes", "category": "Animals"},
]


def search_apis(query: str, category: str = None) -> List[Dict]:
    """Search APIs by name, description or category."""
    query = query.lower()
    results = []
    for api in APIS:
        match = (
            query in api["name"].lower() or
            query in api["description"].lower() or
            (category and category.lower() in api.get("category", "").lower())
        )
        if match:
            results.append(api)
    return results


def main():
    if len(sys.argv) < 2:
        print("public-apis-explorer (Offline)")
        print("Usage: python public-apis-explorer.py <search-term> [category]")
        print("\nExamples:")
        print("  python public-apis-explorer.py weather")
        print("  python public-apis-explorer.py crypto")
        print("  python public-apis-explorer.py maps")
        sys.exit(0)

    query = sys.argv[1]
    category = sys.argv[2] if len(sys.argv) > 2 else None

    results = search_apis(query, category)

    print(f"\n\ud83d\udd0d Found {len(results)} APIs matching '{query}'" + (f" in category '{category}'" if category else "") + ":\n")

    for api in results[:20]:
        print(f"• {api['name']}")
        print(f"  {api['description']}")
        print(f"  Category: {api.get('category', 'N/A')} | Auth: {api['auth']} | HTTPS: {api['https']} | CORS: {api['cors']}\n")


if __name__ == "__main__":
    main()
