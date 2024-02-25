import json

def loader():
    try:
        with open("youtube.txt", "r") as file:
            load = json.load(file)
            return load
    except FileNotFoundError:
        return("File not created or cannot be accessed")

def saver(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)                                                                 # 1st mistake : remember to use dump(what, where) to store
        
def add_videos(videos):
    name = input("Name of the video to add: ")
    time = input("Duration of video: ")
    videos.append({"name": name, "time": time})                                                 
    saver(videos)

def show_list(videos):
    for index, video in enumerate(videos, start=1): 
        print(f"{index} - name: {video['name']} , Duration: {video['time']}")                   # 2nd mistake : Use of f-string

def update_videos(videos):
    id = int(input("Enter the list no. to update: "))
    new_name = input("Enter new name: ")
    new_time = input("Enter updated time: ")
    videos[id-1] = {"name": new_name, "time": new_time}                                         # 3rd mistake: id is taken in enumerate from 1 but actual indexing of videos from 0 --> so adjust that
    saver(videos)

def delete_video(videos):
    id = int(input("Enter the list no. to delete: "))
    del videos[id-1]
    saver(videos)
    
def main():
    while True: 
    
        videos = loader()
        
        print("/ YouTube video Manager /")
        
        print("1 - Add videos to manager")
        print("2 - Show videos's list")
        print("3 - Update videos to manager")
        print("4 - Delete videos from manager")
        print("5 - Exit from Manager")
        
        command = input("Enter your command: ")
        
        match command:
            
            case "1":
                add_videos(videos)
            case '2':
                show_list(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_video(videos)
            case '5':
                exit()
            case _:
                print("Invalid command")
    

if __name__ == "__main__":                                              # Creating/Treating main() as a module
    main()                                          
