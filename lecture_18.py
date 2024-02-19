# ..........................................................              Python Project - Youtube manager app



# >>> x = ("masala", "coffee", "comment")                                                              # enumerate : all values using enumerate can be converted into list in key-value pair
# >>> y = inumerate(x)
# <enumerate object at 0x000002494E23C220>
# >>> list(y)
# [(0, 'masala'), (1, 'coffee'), (2, 'comment')]                                                       # key:value - pair




# ..............................................................            Exception Handling




# file = open('youtube.txt', 'w')                                                                         # 'w' - write mode : file not there then it will create a new file
#                                                                                                         # # File Handling:  Code, Cautious interaction with database of files
# try:
#     file.write('chai aur code')                                                                         # The `try` block is used to enclose a section of code that may raise an exception, if exception occurs the program will jump to the 'finally'.
# finally:
#     file.close()                                                                                        # The 'finally' block is used to specify a section of code that will always be executed, regardless of whether an exception occurred or not (In this case, closing the file to release any resources)                                                                                       



# with open('youtube.txt', 'w') as file:                                                                  # Better way of handling file operations in python as automatic file closing
#     file.write('chai aur python')                                                                       # 'with' statement : ensures that the file is properly closed after its use even if an exception occurs



# ...............................................................                YouTube Manager App



import json                                                                                             # JSON is a popular data format used for storing and exchanging data between a server and a client.
                                                                                                        # The json module is used to load and save data from/to a file in JSON format
# file = 'youtube.txt'              
def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = (json.load(file))                                                                        # Example: edge (google website loading) and In this case, data loading in backend of compiler
            # print(test)                                                                                   # json.load() function to load the data from the file and convert it into a JSON object.
            # print(type(test)) # behind : test is a list of json                                           # json.load(file) : list of json objects
            
            return test                                                                                     # Here, the load_data() function is called, which returns the value of test. According to the code, test is assigned the value of json.load(file), which is a list of JSON objects. 
                                                                                                            # Therefore, videos is assigned the value of test, making it a list
    except (FileNotFoundError):
        return ["Create File"]
    
def save_data_helper(videos):                                                                               # this code saves the videos data into a file named 'file' in JSON format.
    with  open('youtube.txt', 'w') as file:
        json.dump(videos, file)                                                                             # The json.dump() function is used to serialize the videos object and write it as a JSON string to the file. [store the videos data(json format) in the 'youtube.ext' file]
                                                                                                            # The dump() function takes two parameters: the data to be written and the file object to write the data.
def list_all_videos(videos):
    print("\n")
    print("*" * 79)
    for index, video in enumerate(videos, start = 1):                                                       # enumerate(): It add indexing to iterable objects (user ko pata nahi hai what indexing to use) 
        print(f"{index}. {video['name']}, Duration: {video['time']} ")                                      # jaise hi videos list ko enumerate kiya vo enumerate type me convert ho gya in key:value pair and usko access karke ke liye looping use ki 
    print("*" * 79)
    
        
def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})                                                             # list should be like: [{}, {}, {}]
    save_data_helper(videos)
    
def update_video(videos):
    list_all_videos(videos)
    
    index = int(input("Enter the number to update: ")) 
    if 1<= index <= len(videos):
        new_name = input("Enter the new video name: ")
        new_time = input("Enter the new video time: ")
        videos[index-1] = {'name': new_name, 'time': new_time}                                              # user index = 1 but actual index = 0 (index -1 )
        save_data_helper(videos)
    else:
        print("Invalid, number list is out of bound ")    
        
        
def delete_video(videos):
    list_all_videos(videos)
    
    index = int(input("Enter the number to be deleted: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]                                                                               # del(a keyword) : removes an item at a specified index
        save_data_helper(videos)
        
    else:
        print("Invalid number")
        
def main():                                                                                                 # Industry standard : which method to run first 
    
    videos = load_data()                                                                                    # Taking videos as a list is easy to be done

    while True:                                                                                             # Continuous questioning (user instructions)
        print("\n Youtube Manager | choose an option")
        print("1. List all youtube Video")
        print("2. Add a Youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        # print(videos)
        
        # Choices option : multiple cases
        match choice:
            case "1":
                list_all_videos(videos)                                                                     # method: 
            case "2":
                add_video(videos)                   
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break                                                                                       # exiting 
            case _:                                                                                         # Default case
                print("Invalid choice")
                
    
if __name__ == "__main__":                                                                                  # using if __name__ == "__main__": allows a script to be both run as a standalone program and imported as a module into other scripts. 
    main()                                                                                                  # If this line is not used, the code inside the if statement will always be executed, even when the script is imported as a module, which may lead to unintended behavior.
    





# ..................................................                Working of enumerate():



# >>> list = [{'name':'dunky', 'time':'2hr 24min'}, {'name':'tiger', '[{'name': 'dunky', 'time': '2hr 24min'}, {'name': 'tiger', 'time': '3 hrs'}]
# >>> enumerate(list)
# <enumerate object at 0x000002349DDD3A10>

# >>> for i, video in enumerate(list, start=1):
# ...     print(f"{i}. {video['name']}")                                                                    # video ke andar bhi two values hai, so specifying the value needed
# ...
# 1. dunky
# 2. tiger










