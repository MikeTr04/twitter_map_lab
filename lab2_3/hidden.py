"""HIDDEN FILE WITH BEARER TOKEN"""


# Keep this file separate

# https://apps.twitter.com/
# Create new App and get the four strings

def oauth():
    """
    Returns a dictionary with a bearer token of twitter api.
    >>> oauth()
    {'bearer_token': 'AAAAAAAAAAAAAAAAAAAAAAsyZQEAAAAAqvzT%2FpQVsm0d484gvxOmWU8dAbw%3DnXwRun3mdC1KgOVtPNVdJuTRuomk4n7yk4Z1jQYKypYC6XfEc3'}
    """
    return {"bearer_token": "AAAAAAAAAAAAAAAAAAAAAAsyZQEAAAAAqvzT%2FpQVsm0d484gvxOmWU8dAbw%3DnXwRun3mdC1KgOVtPNVdJuTRuomk4n7yk4Z1jQYKypYC6XfEc3"} # pylint: disable=C0116


if __name__ == "__main__":
    doctest.testmod()
