# .......................................................         Practice -1         ......................................................


import requests

def fetch_random_jokes():
    # url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    
    response = requests.get(url="https://api.freeapi.app/api/v1/public/randomjokes/joke/random")
    data = response.json()                                                                                  # Json typically convert the data in a dictionary (key:value pair)

    if data["success"] and "data" in data:
        user_data = data["data"]
        jokes = user_data["content"]
        return jokes
    else:
        raise Exception("Api failed to fetch")

def main():
    try:
        content = fetch_random_jokes()
        print("Joke (Smile): ", content)
    except Exception:
        print(str(Exception))

if __name__ == "__main__":
    main()










