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


import json                                                                                               # File Conversion : string to json and json to string

file = 'youtube.txt'
def load_data():
    try:
        with open('file', 'r') as file:
            return json.load(file)                                                                         # json.load() function to load the data from the file and convert it into a JSON object.
    except (FileNotFoundError):
        return []
    
def save_data_helper(videos):                                                                              # this code saves the videos data into a file named 'file' in JSON format.
    with  open('file', 'w') as file:
        json.dump(videos, file)                                                                            # The json.dump() function is used to serialize the videos object and write it as a JSON string to the file. [store the videos data(json format) in the 'youtube.ext' file]
                                                                                                           # The dump() function takes two parameters: the data to be written and the file object to write the data.
def list_all_videos(videos):
    pass
    
def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():                                                                                                 # Industry standard : which method to run first 
    
    videos = load_data()                                                                                    # Taking videos as a list is easy to be done but some complex method [Assignment]

    while True:                                                                                             # Continuous questioning (user instructions)
        print("\n Youtube Manager | choose an option")
        print("1. List all youtube Video")
        print("2. Add a Youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice")
        
        # Choices option : multiple cases
        match choice:
            case '1':
                list_all_videos(videos)                                                                     # method: 
            case '2':
                add_video(videos)                   
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break                                                                                       # exiting 
            case _:                                                                                         # Default case
                print("Invalid choice")
                
    
if __name__ == "__main__":                                                                                  # '__' : are called as 'dundar'
    main()

















