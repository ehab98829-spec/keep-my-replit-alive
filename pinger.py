import requests
import time

# الرابط تبعك مع الـ https
url = "https://cf20a42e-e4e2-405a-bd55-8867535e761c-00-30sp6a2w6ce6m.pike.replit.dev/"

# هيدرز متطورة جداً عشان نبين كأننا متصفح حقيقي من موبايل أو لابتوب
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1'
}

def poke():
    try:
        # بنعمل طلب وننتظر الرد بالكامل
        response = requests.get(url, headers=headers, timeout=30)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print("Success! Replit woke up.")
        else:
            print("Pinged but server responded with status:", response.status_code)
    except Exception as e:
        print(f"Failed to reach server: {e}")

if __name__ == "__main__":
    poke()
