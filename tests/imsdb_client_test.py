# test_imsdb_query.py

import requests
from imsdb_client import imsdb_query

test_cases = [
    # (movie_title, expected_result)
    ("Pariah", True),
    ("Ffgjfhgjfhgj", False),  # gibberish, shouldn't exist
    # add more here — maybe a movie you're confident IS on the site,
    # and one you're confident ISN'T
]

for movie_title, expected in test_cases:
    result = imsdb_query(movie_title)
    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: imsdb_query({movie_title!r}) = {result} (expected {expected})")

response = requests.get("https://imsdb.com/scripts/Pariah.html")
print(response.text[:9000])  # first 2000 characters, adjust as needed

#response = requests.get("https://imsdb.com/scripts/Pariah.html")
#print(response.text)