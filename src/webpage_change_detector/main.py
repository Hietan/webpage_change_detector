import argparse
import requests


# URLの存在を確認する関数
def exist_webpage(url: str) -> bool:
    try:
        response = requests.head(url, allow_redirects=True)
        return response.status_code == 200
    except requests.RequestException:
        return False
    
def main():
    parser = argparse.ArgumentParser(description="Check the existence of a webpage.")
    parser.add_argument("url", type=str, help="URL of the webpage to check.")
    args = parser.parse_args()

    if exist_webpage(args.url):
        print(f"Webpage exists: {args.url}")
    else:
        print(f"Webpage does not exist: {args.url}")

if __name__ == "__main__":
    main()
