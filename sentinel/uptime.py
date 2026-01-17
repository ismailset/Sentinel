import requests, time
from rich import print

def check_uptime(url):
    start = time.time()
    try:
        r = requests.get(url, timeout=8)
        latency = int((time.time() - start) * 1000)
        print(f"Status: {r.status_code}")
        print(f"Latency: {latency} ms")
        if latency > 3000:
            print("[yellow]Warning: High latency[/yellow]")
    except Exception:
        print("[red]Site unreachable[/red]")
