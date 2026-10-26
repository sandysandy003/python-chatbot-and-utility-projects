
# Task 17: URL Status Checker

import requests
from urllib.parse import urlparse

def check_url(url):
    if not url.startswith(("https://", "http://")):
        url = "https://" + url

    parsed = urlparse(url)

    if not parsed.hostname or "." not in parsed.hostname:
        print("Please enter a valid website address.")
        return

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
            headers={"User-Agent": "PythonURLChecker/1.0"},
        )

        print("\nWebsite:", url)
        print("Final URL:", response.url)
        print("HTTP status:", response.status_code)
        print("Result:", "Reachable" if response.ok else "Server returned an error")

    except requests.exceptions.Timeout:
        print("The website took too long to respond.")
    except requests.exceptions.SSLError:
        print("Secure connection failed. Check the website address or certificate.")
    except requests.exceptions.ConnectionError:
        print("Could not connect. Check your internet connection and URL.")
    except requests.exceptions.RequestException as error:
        print("Request failed:", error)


print("=" * 40)
print("URL STATUS CHECKER")
print("Type EXIT to quit.")
print("=" * 40)

while True:
    url = input("\nEnter a website (e.g., https://example.com): ").strip()

    if url.lower() == "exit":
        print("Goodbye!")
        break

    if url:
        check_url(url)
    else:
        print("Please enter a website address.")
