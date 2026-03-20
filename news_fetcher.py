import requests

NEWSAPI_KEY = "65c86ef2b1a2490ebc75e83b43efe1d7"

def fetch_financial_news(query="Federal Reserve OR central bank OR interest rates", language="en", page_size=5):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": language,
        "sortBy": "publishedAt",
        "pageSize": page_size,
        "apiKey": NEWSAPI_KEY
    }
    response = requests.get(url, params=params)
    articles = response.json().get("articles", [])
    
    results = []
    for article in articles:
        results.append({
            "title": article["title"],
            "source": article["source"]["name"],
            "published": article["publishedAt"],
            "url": article["url"],
            "content": article.get("content", "No content available")
        })
    return results

if __name__ == "__main__":
    news = fetch_financial_news()
    for item in news:
        print(f"\n📰 {item['title']}")
        print(f"   Source: {item['source']} | {item['published']}")
        print(f"   Content preview: {item['content'][:200]}")
