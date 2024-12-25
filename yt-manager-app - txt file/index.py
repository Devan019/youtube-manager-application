from function import getVideos , updateVideo , deleteVideo  , showAllVideos ,addVideo


def main():
    while True:
        videos = getVideos()
        print("\n")
        print("#"*80)
    
        print("Welcome to my Youtube manager | total videos : " , len(videos))
        print("1. show all youtube videos")
        print("2. add new video")
        print("3. update video")
        print("4. delete video")
        print("5. exit")
        print("\n")
        choice = int(input("enter your choice : "))
    
        match choice:
            case 1:
                showAllVideos(videos)
            case 2:
                addVideo(videos)
            case 3:
                updateVideo(videos)
            case 4:
                deleteVideo(videos)
            case 5:
                exit()
            case _:
                print("invalid choice")
    
if __name__ == "__main__":
    main()