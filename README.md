# Active URL Checker

This Python script checks and identifies active URLs within a specific domain. It utilizes the `requests` library to make HTTP GET requests to all URLs found on an initial page and determines which ones return successfully (status code 200). Additionally, the script makes use of the `BeautifulSoup` library to parse the HTML content of the page and extract available links. As a result, the script provides a list of active URLs found, aiding in the identification of active pages or resources on a website.

## Requirements

- Python 3.x
- BeautifulSoup (`pip install beautifulsoup4`)
- Requests (`pip install requests`)

## Usage

1. Run the script using Python: `python script.py`.
2. Enter the domain (example.com) when prompted.
