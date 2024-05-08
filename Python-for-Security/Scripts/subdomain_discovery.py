import requests


def req(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

if __name__ == '__main__':
    target_url = "google.com"

    with open("D:\\subdomains.txt", "r") as wordlist_file:
        for line in wordlist_file:
            word = line.strip()
            test_url = word + "." + target_url
            response = req(test_url)

            if response:
                print("[+] Discovered subdomain -->" + test_url)

