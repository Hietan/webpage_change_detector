import argparse
import requests
import time
from datetime import datetime


def exist_webpage(url: str) -> bool:
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.RequestException:
        return False
    
def exist_words(url: str, words: list[str]) -> bool:
    try:
        response = requests.get(url)
        return any(word in response.text for word in words)
    except requests.RequestException:
        return False
    

def wait(url: str, webhook: str, wait_time: int, words: list[str]):
    while True:
        if exist_webpage(url):
            if exist_words(url, words):
                requests.post(webhook, json={"text": f"Webpage exists with words {words}.\n{url}"})
            else:
                requests.post(webhook, json={"text": f"Webpage exists but words {words} not found.\n{url}"})
            break
        else:
            print(datetime.now(), "Waiting")
        time.sleep(wait_time)
    
def main():
    parser = argparse.ArgumentParser(description="Check the existence of a webpage.")
    parser.add_argument("--url", type=str, required=True, help="URL of the webpage to check.")
    parser.add_argument("--webhook", type=str, required=True, help="Webhook URL of Slack to notify.")
    parser.add_argument("--time", type=int, default=60, help="Time to wait between checks.")
    parser.add_argument("--words", nargs="+", help="Words to check in the webpage.")
    args = parser.parse_args()

    wait(args.url, args.webhook, args.time, args.words)

if __name__ == "__main__":
    main()
