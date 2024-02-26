# ................................................            Youtuber Manager using MongoDB          ........................................................


# In MongoDB, Network Access is used to control which IP addresses or IP ranges have access to your MongoDB databases. 
# This is a crucial aspect of database security, as it allows you to limit access to your databases to only trusted sources. 
# You can set up IP whitelisting rules to specify the IP addresses or CIDR ranges that are allowed to connect to your MongoDB databases. 
# This can help prevent unauthorized access and protect your data.

# As we are just testing: 
    
# To allow all IP addresses to access your MongoDB database, you would need to add a rule to your IP whitelist that includes all IP addresses. 
# This is typically done by adding the IP address "0.0.0.0/0" to your whitelist, which represents all possible IP addresses


from pymongo import MongoClient                                                                                                             # Standard practice: we don't have to write pymongo.MongoClient often

from bson import ObjectId                                                                                                                   # The line `from bson import ObjectId` is importing the `ObjectId` class from the `bson` module.
                                                                                                                                            # In MongoDB, each document in a collection has a unique identifier called `_id`, which is of type `ObjectId`. 
                                                                                                                                            # By importing `ObjectId`, you can create instances of this class to work with `_id`
                                                                                                                                            # values when querying, updating, or deleting documents in MongoDB collections using Python.


client = MongoClient('mongodb+srv://youtubedata:TZEtL_VdiAg$!i5@cluster0.3ir6vsm.mongodb.net/YoutubeManager')                               # This line of code is creating a MongoDB client object that connects to a MongoDB server hosted on
                                                                                                                                            # the specified URI. The URI contains the necessary information for establishing a connection to the
                                                                                                                                            # MongoDB server, including the username, password, host, and database name.
# In local Machine: client = pymongo.MongoClient("localhost", 27017)
                                                                                                                                            # Not a good idea to include id and password in code files
                                                                                                                                        
db = client["YoutubeManager"]                                                                                                               # The line `db = client["YoutubeManager"]` is creating a reference to the database named
                                                                                                                                            # "YoutubeManager" within the MongoDB server that the client is connected to. 
                                                                                                                                            # This allows you to interact with the "YoutubeManager" database using the `db` reference in your Python code.
try:
    video_collection = db["videos"]                                                                                                         # In MongoDB, we have use the database to actually see some changes/progress in atlas
except Exception as e: print(str(e))
    
# print(video_collection)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})                                                                               # All values must be passed as a Object

def show_table():
    table = video_collection.find()                                                                                                         # find() : Returns an iterable object
    for video in table:
        print(f"ID: {video['_id']}, Name: {video['name']}, time: {video['time']}")                                                                                                        

def update_video(video_id, new_name, new_time):                                                                                             # In mongoDB, id = _id
    video_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}})                                # ObjectID() : Converting video_id (string) to objectID to access the _id in mongoDB
                                                                                                                                            # PROBLEM : When we try to update with input _id, then _id is taken as a string(not handled by pymongo)

def delete_video(video_id): 
    video_collection.delete_one({"_id": ObjectId(video_id)})                                                                                # MongoDB : Standard format --> '{}'       
                                                                                                                                            # '_id' : It is automatically created and assigned by MongoDB when a new document is inserted.
def main():
    
    while True:
        
        print("\n YouTube Manager app using DataBase")
        print("1-Add videos to the table")
        print("2-Show the table")
        print("3-Update videos in the table")
        print("4-Delete videos from table")
        print("5-Exit the process")

        choice = int(input("Enter you choice: "))
        
        if choice == 1:
            name = input("Enter the name of the video: ")
            time = input("Enter the duration of the video: ")
            add_video(name, time)
            
        elif choice == 2:
            show_table()
            
        elif choice == 3:
            show_table()
            video_id = input("Id of the video to be deleted: ")
            name = input("Name of the video: ")
            time = input("Duration of the video: ")
            update_video(video_id, name, time)
            
        elif choice == 4:
            show_table()
            id = input("Id of the video to be deleted: ")
            delete_video(id)
            
        elif choice == 5:
            break
        
        else:
            print("Invalid syntax")    
                                                                                                                                            # In mongoDB, not necessary to close the

if __name__ == "__main__":  
    main()


























