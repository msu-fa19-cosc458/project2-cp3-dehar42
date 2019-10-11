import requests, os, json, chatbot

my_header = {
    'Authorization': "Bearer " + os.getenv("YELP_BEARER")
    # use os.getenv("YELP_BEARER")
    }
    
def YelpBusinessSearch(message):
    
    url = "https://api.yelp.com/v3/businesses/search?location=Baltimore&sort_by=rating&term=" + message
    response = requests.get(url, headers=my_header)
    return (response.json())
    
def YelpBusinessId(chatbot_response):
    url = "https://api.yelp.com/v3/businesses/" + chatbot_response
    response = requests.get(url, headers=my_header)
    return (response.json())
    