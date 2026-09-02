from bs4 import BeautifulSoup
import re
import requests


def imsdb_query(movie_title):
    response = requests.post(
        "https://imsdb.com/search.php",
        data={"search_query": movie_title}
    )
    # isolate only the text between the results heading and the next <script> tag
    section_match = re.search(r"Search results for.*?</h1>(.*?)<script", response.text, re.DOTALL)
    if not section_match:
        return False
    results_section = section_match.group(1)
    return bool(re.search(r'/Movie Scripts/[^"]+\.html', results_section))

def script_fetch(url):
    response = requests.get(url)
    match = re.search(r'<pre>(.*)</pre>', response.text, re.DOTALL)
    if not match:
        return None
    raw_script_html = match.group(1)
    soup = BeautifulSoup(raw_script_html, "html.parser")
    plain_text = soup.get_text()
    return plain_text