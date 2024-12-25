from pymongo import MongoClient
from bson import ObjectId

try:
    client = MongoClient("mongodb://localhost:27017")

    db = client['ytmanager']
    videoCollection = db['videos']
except Exception as e:
    print(f"{e}")

def show_all_videos():
    for video in videoCollection.find():
        print(f"{video['_id']} => {video['name']} : {video['time']}")
    

def add_video():
    name = input("enter video name : ")
    time = input("enter video time : ")
    
    videoCollection.insert_one({
        'name' : name,
        'time' : time
    })
    

def delete_video():
    id = input('enter video id for delete : ')
    try:
        videoCollection.delete_one({"_id" : ObjectId(id)})
    except Exception as e: 
        print(f"{e}")

def update_video():
    id = input('enter video id for update : ')
    
    name = input("enter video name : ")
    time = input("enter video time : ")
    
    try:
        videoCollection.update_one({"_id" : ObjectId(id)} , {
            "$set":{
                "name" : name,
                "time" : time
            }
        })
    except Exception as e:
        print(f"{e}")
        
def search_video():
    id = input('enter video id for search : ')
    
    try:
        print(videoCollection.find_one({"_id" : ObjectId(id)}))
    except Exception as e:
        print(f"{e}")


def main():
    while True:
        print("\n")
        print("Welcome to the Youtube Video Manager | Version 1.0")
        print("--------------------------------------------------")
        print("\n")
        print("1. show all videos")
        print("2. add video")
        print("3. delete video")
        print("4. update video")
        print("5. search video")
        print("6. exit")
        print("\n")
        print("--------------------------------------------------")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                show_all_videos()
            case "2":
                add_video()
            case "3":
                delete_video()
            case "4":
                update_video()
            case "5":
                search_video()
            case "6":
                print("Goodbye!")
                exit()
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main() 
    