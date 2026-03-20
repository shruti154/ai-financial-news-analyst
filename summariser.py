from news_fetcher import fetch_financial_news
from groq import Groq

import os
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")


def summarise_article(title, content):
    prompt = f"""You are a financial analyst assistant.

SOURCE MATERIAL:
{content}

HEADLINE: {title}

Task: Write a 3-sentence summary of this news for a retail investor. 
Focus on: what happened, why it matters, and market impact.
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response.choices[0].message.content

import csv
from datetime import datetime

if __name__ == "__main__":
    articles = fetch_financial_news()
    results = []
    
    for article in articles[:5]:
        print(f"\n📰 {article['title']}")
        try:
            summary = summarise_article(article['title'], article['content'])
            print(f"💡 {summary}")
            results.append({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "source": article['source'],
                "title": article['title'],
                "summary": summary
            })
        except Exception as e:
            print(f"❌ Error: {e}")
    
    with open("summaries.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "source", "title", "summary"])
        writer.writeheader()
        writer.writerows(results)
    
    print("\n✅ Saved to summaries.csv")


