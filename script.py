import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_active_urls(domain):
    active_urls = set()
    base_url = f"http://{domain}"  # Adapt to "https://" if necessary

    try:
        response = requests.get(base_url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error when accessing {base_url}: {e}")
        return active_urls

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a", href=True)
    for link in links:
        href = link["href"]
        full_url = urljoin(base_url, href)

        if full_url.startswith(base_url):

            try:
                link_response = requests.head(full_url, allow_redirects=True)
                if link_response.status_code < 400:
                    active_urls.add(full_url)
            except requests.RequestException:
                pass

    return active_urls


if __name__ == "__main__":
    domain = input("Enter the domain (ex: example.com): ")
    active_urls = get_active_urls(domain)
    print("Active URLs found:")
    for url in active_urls:
        print(url)
