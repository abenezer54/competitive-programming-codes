import requests

def check_urls(base_url, start, end):
    working_urls = []
    for number in range(start, end + 1):
        url = f"{base_url}{number}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Working URL: {url}")
                working_urls.append(url)
            else:
                print(f"URL not working: {url} (Status Code: {response.status_code})")
        except requests.RequestException as e:
            print(f"Error for URL {url}: {e}")
    
    return working_urls

if __name__ == "__main__":
    base_url = "https://bloomberg.avature.net/careers/JobDetail/"
    start_number = 6000
    end_number = 9999

    working_urls = check_urls(base_url, start_number, end_number)
    
    print("\nWorking URLs:")
    for url in working_urls:
        print(url)
