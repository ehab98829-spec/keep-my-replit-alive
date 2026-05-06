import requests

# هاد هو الرابط تبعك اللي بالصورة
url = "http://cf20a42e-e4e2-405a-bd55-8867535e761c-00-30sp6a2w6ce6m.pike.replit.dev/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers, timeout=15)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Done! Replit is awake.")
except Exception as e:
    print(f"Error: {e}")
