# ...................................................               API handling            ................................................



# Selective data extraction

# The locations of these pieces of information in the JSON object are known beforehand --> json.formatter


import requests                                                                             # This module allows the Python script to send GET, POST, PUT, DELETE, etc. requests to web servers and handle the responses received.

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)                                                            # get() : This method is used to send a HTTP GET request to the specified URL and fetch the data from the API.
    
    data = response.json()                                                                  # The response from the API is received in a string format. The response.json() method is used to convert this string data into a JSON (JavaScript Object Notation) format, which is easier to work with in Python.

    # data extracting
    if data["success"] and "data" in data:                                                  # The function then checks if the response was successful and if it contains the "data" key. 
        user_data = data["data"]                                                            # it extracts the user data from the response using user_data = data["data"].
        username = user_data["login"]["username"] 
        country = user_data["location"]["country"]                                          # The locations of these pieces of information in the JSON object are known beforehand, so they can be accessed directly.
        return username, country
    else:
        raise  Exception("Failed to fetch user_data")                                       # raise(a keyword) : any error occurs during the process, an exception is raised

# fetch_random_user_freeapi()   
def main():
    try:                                                                                    # Whenever gives web request or external request : use of try-except block to protecting the method
        username_demo, country_demo = fetch_random_user_freeapi()                           # method call
        print(f" Username: {username_demo} \n Country: {country_demo}")               
    except Exception as e:
        print(str(e))
       
if __name__ == "__main__":
    main()
    
    
    
    