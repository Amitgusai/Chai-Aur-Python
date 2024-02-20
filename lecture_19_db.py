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
#         with open("PRACTICE.txt", "r") as file:
#             return json.load(file)                      # returns a list of json object
#     except (FileNotFoundError):
#         return []               # As we have to create a list

# def save_file(videos):
#     with open("PRACTICE.txt", "w") as file:
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
        
# # def delete_video(videos):
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



"""     ............................................................        USING DATABASE : SQlite3         ................................................        """



import sqlite3                                                                  # sqlite3 is a lightweight : can be used without a standalone server

conn = sqlite3.connect('lecture_19_db')                                         # `conn = sqlite3.connect('lecture_19')` is establishing a connection to a SQLite database named 'lecture_19'. 
                                                                                # This line of code creates a connection object `conn` that allows you to interact with the SQLite database. 
                                                                                # This connection object is used to execute SQL queries and perform other database operations.

cursor = conn.cursor()                                                          # This cursor object allows you to execute SQL queries, fetch results, and perform various operations on the database.

# PRIMARY KEY : Ensures that there are no duplicate rows and that the data can be efficiently retrieved and manipulated.
cursor.execute("""
                CREATE TABLE IF NOT EXISTS videos(
                    Id INTEGER PRIMARY KEY,                                     
                    name TEXT NOT NULL,     
                    time TEXT NOT NULL
                )   
""")


def show_table():
    cursor.execute("SELECT * FROM videos")                                                                      # Obtained a tuple 
    print("*" * 80 )
    for row in cursor.fetchall():                                                                               # cursor is holding the result (fetchall: all values in it)
        print(row)
    print("*" * 80)
    
def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES(?, ?)", (name, time))                                # To insert in Table
    conn.commit()                                                                                             # To commit or save in DataBase (using connection)
    
def update_video(new_name, new_time, id):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, id))               # To update in Table
    conn.commit()
    
def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id = ? ", (id,))                                                   # To delete from Table
    conn.commit()                                                                                               # Python requires tuples to have at least one element.
                                                                                                                # If the comma were omitted, the Python interpreter would raise a syntax error.

def main():
    
    while True:
        
        print("\n YouTube Manager app using DataBase")
        print("1-Show the table")
        print("2-Add videos to the table")
        print("3-Update videos in the table")
        print("4-Delete videos from table")
        print("5-Exit the process")

        choice = int(input("Enter you choice: "))
        
        if choice == 1:
            show_table()
            
        elif choice == 2:
            name = input("Enter the name of the video: ")
            time = input("Enter the duration of the video: ")
            add_videos(name, time)
            
        elif choice == 3:
            show_table()
            id = int(input("Id of the video to be deleted: "))
            name = input("Name of the video: ")
            time = input("Duration of the video: ")
            update_video(name, time, id)
            
        elif choice == 4:
            show_table()
            id = int(input("Id of the video to be deleted: "))
            delete_video(id)
            
        elif choice == 5:
            break
        
        else:
            print("Invalid sysntex")

    conn.close()                                                                # closing the database to prevent from corruption

if __name__ == "__main__":  
    main()


