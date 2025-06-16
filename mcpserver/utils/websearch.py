import requests
import os 
from dotenv import load_dotenv
load_dotenv()

def web_search(query):

    your_google_api_key = os.environ.get('GOOGLE_API_KEY')
    your_search_engine_id = os.environ.get('GOOGLE_SEARCH_ENGINE')
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={your_google_api_key}&cx={your_search_engine_id}"
    response = requests.get(url)
    data = response.json()
    
    # 検索結果を取得
    results = []
    if "items" in data:
        for item in data["items"][:3]:  # 上位3件を取得
            results.append(f"{item['title']}: {item['link']}")
    
    return "\n".join(results) if results else "検索結果が見つかりませんでした。"