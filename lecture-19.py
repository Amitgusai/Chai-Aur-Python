# Project: -

# Video manager app
# add = videos name and time
# save
# list show
# update 
# delete
# exit the app


"""     ..............................................              PRACTICE        ....................................................     """


# import json                    # To save and load the data in json format in a file

# def load_file():
#     try:
#         with open("video.txt", "r") as file:
#             return json.load(file)                      # returns a list of json object
#     except (FileNotFoundError):
#         return []               # As we have to create a list

# def save_file(videos):
#     with open("video.txt", "w") as file:
#         json.dump(videos, file)

# def add_video(videos):
#     name = input("Name of video to be added: ")
#     time = input("Duration of Video: ")
#     videos.append({"name": name, "time": time})
#     save_file(videos)

# def show_list(videos):
#     print("\n")
#     for index, video in enumerate(videos, start = 1):                                                       # enumerate(): It add indexing to iterable objects (user ko pata nahi hai what indexing to use) 
#         print(f"{index}. {video['name']}, Duration: {video['time']} ")
#     print("\n")
    
# def update_video(videos):
#     show_list(videos)
#     index = int(input("Enter the number list you want to update: "))                 # index should not be out of bound
    
#     if 1 <= index <= len(videos):
#         name = input("Enter the new video name: ")
#         time = input("Enter the duration of new video: ")
#         videos[index-1] = [{"name": name, "time": time}]
#         save_file(videos)
#     else:
#         print("Invalid Syntax")
        
# def delete_video(videos):
#     show_list(videos)
#     index = int(input("Enter the list_num to be deleted: "))
    
#     if 1 <= index <= len(videos):
#         del videos[index-1]
#         save_file(videos)
#     else:
#         print("Invalid")

# def main():
#     while True: 
    
#         # Takind a list
#         videos = load_file()        # Taking list of json.load(file)
        
#         print("\n")
        
#         print("1 - Add the video to the list")
#         print("2 - Show the list of videos")
#         print("3 - Update the exiting list")
#         print("4 - Deleting a video")
#         print("5 - Exit the app")
        
#         choice = input("Enter your intended Execution number: ")
        
#         match choice:
            
#             case '1': 
#                 add_video(videos)
#             case '2':
#                 show_list(videos)
#             case '3':
#                 update_video(videos)
#             case '4':
#                 delete_video(videos)
#             case '5':
#                 break
#             # default
#             case _:
#                 print("Out of bound")
            
    

# # Creating as a Module 
# if __name__ == "__main__":
#     main()



"""     ............................................................        END         ................................................        """





















