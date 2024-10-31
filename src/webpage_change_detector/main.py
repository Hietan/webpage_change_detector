import argparse
import requests
import time


def exist_webpage(url: str) -> bool:
    try:
        response = requests.head(url, allow_redirects=True)
        return response.status_code == 200
    except requests.RequestException:
        return False
    

def wait(url: str, webhook: str):
    while True:
        if exist_webpage(url):
            requests.post(webhook, json={"text": f"Webpage {url} exists."})
            break
        else:
            print("Waiting")
        time.sleep(10)
    
def main():
    parser = argparse.ArgumentParser(description="Check the existence of a webpage.")
    parser.add_argument("--url", type=str, required=True, help="URL of the webpage to check.")
    parser.add_argument("--webhook", type=str, required=True, help="Webhook URL of Slack to notify.")
    args = parser.parse_args()

    wait(args.url, args.webhook)

if __name__ == "__main__":
    main()
