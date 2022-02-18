"""MODULE TO COMMUNICATE WITH TWITTER API"""


import requests
import hidden
import os
import doctest


# authentication with bearer token from the hidden file
os.environ["BEARER_TOKEN"] = hidden.oauth()['bearer_token']
bearer_token = os.environ.get("BEARER_TOKEN")


def bearer_oauth(req):
    """
    Method required by bearer token authentication.
    Creates headers to authenticate the API user.
    """
    req.headers["Authorization"] = f"Bearer {bearer_token}"
    req.headers["User-Agent"] = "v2RecentTweetCountsPython"
    return req


def connect_to_endpoint(url: str) -> dict:
    """
    Function used to connect to endpoint provided in the url string.
    Returns a json encoded response from API (json file from the endpoint).
    :param url: string with endpoint
    :return: json encoded response
    >>> connect_to_endpoint("https://api.twitter.com/2/users/by/username/miketrushch")
    {'data': {'id': '1441712152981622787', 'name': 'miketrushch', 'username': 'miketrushch'}}
    """
    response = requests.request("GET", url, auth=bearer_oauth)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def locations(username: str) -> dict:
    """
    Function that returns the locations of the users that the provided user
    is following. If a user did not provide his location in his profile, he is skipped.
    :param username: the username of the person
    :return: dictionary of usernames and respective locations of the people
    who the user follows.
    >>> locations("miketrushch")
    {'BorisJohnson': 'United Kingdom'}
    """
    search_url1 = "https://api.twitter.com/2/users/by/username/"
    search_url1 += username
    json_response = connect_to_endpoint(search_url1)
    ind = json_response['data']['id']

    search_url2 = "https://api.twitter.com/2/users/" + ind + "/following"
    following = connect_to_endpoint(search_url2)['data']
    people = [i['username'] for i in following]
    people = ",".join(people)
    people = f'usernames={people}'

    user_fields = "user.fields=description,id,pinned_tweet_id,location"
    search_url3 = f"https://api.twitter.com/2/users/by?{people}&{user_fields}"
    users = connect_to_endpoint(search_url3)['data']
    loc = {}
    for i in users:
        if 'location' in i.keys():
            loc[i['username']] = i['location']
    return loc


def user_loc(username):
    """
    Returns the location of an individual user by username. Returns a dictionary with the key 
    being username and value the location of the account. Returns None if user did not provide
    a location in his profile.
    :param username: the username of the person
    :return: dictionary with the key being username and value the location of the account
    >>> user_loc("miketrushch")

    >>> user_loc("BorisJohnson")
    {'BorisJohnson': 'United Kingdom'}
    """
    user_fields = "user.fields=description,id,pinned_tweet_id,location"
    search_url = f"https://api.twitter.com/2/users/by?usernames={username}&{user_fields}"
    users = connect_to_endpoint(search_url)['data']
    loc = {}
    for i in users:
        if 'location' in i.keys():
            loc[i['username']] = i['location']
    return loc if loc else None


if __name__ == "__main__":
    doctest.testmod()
