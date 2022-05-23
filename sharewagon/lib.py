import requests

def try_me():
    """
    Explore a piece of wisdome right
    here in your terminal
    """
    # gets wisdome from the interweb
    url = 'https://api.quotable.io/random'
    # saving wisdome to variable response
    response = requests.get(url).json()
    # sharing the wisdome with you
    return response['content']
