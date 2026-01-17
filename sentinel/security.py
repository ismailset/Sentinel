import requests
from rich import print

SEC_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "Referrer-Policy"
]

def check_security(url):
    r = requests.get(url, timeout=8)
    print(f"\n[bold]Security Report for {url}[/bold]\n")

    print("HTTPS:", "✅" if url.startswith("https") else "❌")

    for h in SEC_HEADERS:
        print(f"{h}:", "✅" if h in r.headers else "❌")
