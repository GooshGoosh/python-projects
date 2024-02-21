'''
anime_info_getter.py - Uses the Jikan Unofficial MyAnimeList API to parse the
MyAnimeList.net site for information on any animethat the user desires.

Gives information on any anime related to the search for the name given by
the user. Information given inclues:
    - Name (English)
    - Name (Japanese)
    - Release Date
    - Number of seasons
    - Number of episodes
    - Animation studios
    - Score
'''


import json
import time
import sys
try:
    import requests
except ImportError:
    print("\nPlease install the required module: requests\n")
try:
    import pyinputplus as pyip
except ImportError:
    print("\nPlease install the required module: pyinputplus\n")
    sys.exit(1)


def get_site_data(url):
    """Gets the site data for the requested URL and returns it as a json object.

    Args:
        url (str): Jikan API URL for the anime that the user wants information on.

    Returns:
        list: List of dictionary results received from the HTTP request.
    """
    try:
        # Send the HTTP request to the specified URL and ensure that it returns an
        # HTTP Status response of 200 - OK before returning any data.
        res = requests.get(url=url, timeout=10)
        if res.status_code == 200:
            text = res.text
            data = json.loads(text)
            return data['data']

        return None
    except requests.exceptions.ReadTimeout:
        print("\nError: Request timed out.\n")
        return None
    except requests.exceptions.HTTPError:
        print("\nHTTP Error!")
        print(f'Status code: {res.status_code}')
        return None


def main():
    """Main function to run the program.
    """
    anime = 'naruto'
    my_url = 'https://api.jikan.moe/v4/anime?q=' + anime + '/characters'

    my_data = get_site_data(my_url)
    print(my_data)


if __name__ == "__main__":
    main()
