'''
anime_info_getter.py - Uses the Jikan Unofficial MyAnimeList API to parse the
MyAnimeList.net site for information on any animethat the user desires.

Gives information on any anime related to the search for the name given by
the user. Information given inclues:
    - Name (English)
    - Name (Japanese)
    - First aired
    - Number of episodes
    - Animation studios
    - Score
    - Media type
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


def print_info(list_of_data):
    """Prints the information of the anime requested by the user.

    Args:
        list_of_data (list): List of dictionary data to parse.
    """
    try:
        # Ensure the list is not empty.
        if len(list_of_data):
            for dic in list_of_data:

                # Check if the title_english value is None and, if not, get the title.
                if not dic.get("title_english"):
                    english_title = "N/A"
                else:
                    english_title = dic.get("title_english")

                # Check if the title_japanese value is None and, if not, get the title.
                if not dic.get("title_japanese"):
                    japanese_title = "N/A"
                else:
                    japanese_title = dic.get("title_japanese")

                # Check if the "from" value in the "aired" dict is None and, if not,
                # get the value.
                aired_dict = dic["aired"]
                if not aired_dict.get("from"):
                    first_air = "N/A"
                else:
                    first_air = aired_dict.get("from")

                # Check if the type value is None and, if not, get the media type.
                if not dic.get("type"):
                    media_type = "N/A"
                else:
                    media_type = dic.get("type")

                # Check if the episodes value is None and, if not, get the number
                # of episodes.
                if not dic.get("episodes"):
                    episodes = 0
                else:
                    episodes = dic.get("episodes")

                # Parse the list of studios dictionary data and add the names of the
                # studios to a new list.
                studio_list = dic.get("studios")
                studios = []
                if len(studio_list):
                    for studio in studio_list:
                        studios.append(studio["name"])
                # If the list of studio names is not empty, then join the names together.
                if studios:
                    studios = ", ".join(studios)
                else:
                    studios = "N/A"

                # Check if the score value is None and, if not, get the score.
                if not dic.get("score"):
                    score = 0
                else:
                    score = dic.get("score")

                print('\n' + '-' * 30 + '\n')
                print(f'Title (English): {english_title}')
                print(f'Title (Japanese): {japanese_title}')
                print(f'First Aired: {first_air}')
                print(f'Media Type: {media_type}')
                print(f'Episodes: {episodes}')
                print(f'Studios: {studios}')
                print(f'Score: {score}')
                time.sleep(0.50)
        else:
            print("\nNo data in list! Exiting...")
        sys.exit(1)
    except TypeError:
        print("\nError: Data given not of type 'list'! Exiting...")
        sys.exit(1)


def main():
    """Main function to run the program.
    """
    anime = pyip.inputStr(prompt="Please type the name of an anime you would like info on: ",
                          blank=False)
    my_url = 'https://api.jikan.moe/v4/anime?q=' + anime
    print("\nSending request...")
    time.sleep(0.25)

    my_data = get_site_data(my_url)
    print_info(my_data)


if __name__ == "__main__":
    main()
