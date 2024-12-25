import json

def getVideos():
    try:
        with open("video.txt" , "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def saveVideo(videos):
    with open("video.txt","w") as file:
        json.dump(videos , file)

def showAllVideos(videos):
    for idx,vid in enumerate(videos,start=1):
        print(f"{idx} {vid['name']} ,Duration-{vid['time']}")

def addVideo(videos):
    print("\n")
    name = input("enter video name : ")
    time = input("enter youtube time : ")
    
    videos.append({
        'name' : name,
        'time' : time
    })
    
    saveVideo(videos)

def updateVideo(videos):
    showAllVideos(videos)
    print("\n")
    idx = int(input("enter no which you want update : "))
    
    if 1 <= idx <= len(videos):
        name = input("enter new video name : ")
        time = input("enter new youtube time : ")
        
        videos[idx-1] = {
            'name'  : name,
            'time' : time
        }
        
        saveVideo(videos)
    else:
        print("invalid no : ")
   
def deleteVideo(videos):
    showAllVideos(videos)
    print("\n")
    idx = int(input("enter no which you want delete : "))
    
    if 1 <= idx <= len(videos):
        del videos[idx-1]
        saveVideo(videos)
    else:
        print("invalid no : ") 
    