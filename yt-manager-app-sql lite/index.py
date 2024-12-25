import sqlite3


conn = sqlite3.connect('youtube_manager.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS youtube_manager (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        video TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def print_videos():
    print("\n--- List of Videos ---")
    cursor.execute("SELECT * FROM youtube_manager")
    videos = cursor.fetchall()
    if videos:
        for video in videos:
            print(f"ID: {video[0]} | Video Name: {video[1]} | Time: {video[2]}")
    else:
        print("No videos found.")
    print("----------------------")

def add_video():
    print("\n--- Add New Video ---")
    video = input("Enter video name: ").strip()
    time = input("Enter video time (e.g., 00:05:30): ").strip()
    
    if video and time:
        cursor.execute("INSERT INTO youtube_manager (video, time) VALUES (?, ?)", (video, time))
        conn.commit()
        print("Video successfully added!")
    else:
        print("Invalid input. Video name and time are required.")
    print("----------------------")

def update_video():
    print_videos()
    print("\n--- Update Video ---")
    try:
        video_id = int(input("Enter the ID of the video to update: "))
        cursor.execute("SELECT * FROM youtube_manager WHERE id=?", (video_id,))
        if not cursor.fetchone():
            print("Invalid ID. Video not found.")
            return
        
        new_video = input("Enter new video name: ").strip()
        new_time = input("Enter new video time (e.g., 00:05:30): ").strip()
        
        if new_video and new_time:
            cursor.execute("UPDATE youtube_manager SET video = ?, time = ? WHERE id = ?", 
                           (new_video, new_time, video_id))
            conn.commit()
            print("Video successfully updated!")
        else:
            print("Invalid input. Both fields are required.")
    except ValueError:
        print("Invalid input. Please enter a valid numeric ID.")
    print("----------------------")


def delete_video():
    print_videos()
    print("\n--- Delete Video ---")
    try:
        video_id = int(input("Enter the ID of the video to delete: "))
        cursor.execute("SELECT * FROM youtube_manager WHERE id=?", (video_id,))
        if not cursor.fetchone():
            print("Invalid ID. Video not found.")
            return

        cursor.execute("DELETE FROM youtube_manager WHERE id=?", (video_id,))
        conn.commit()
        print("Video successfully deleted!")
    except ValueError:
        print("Invalid input. Please enter a valid numeric ID.")
    print("----------------------")


def main():
    while True:
        print("\nWelcome to YouTube Manager | Version 1.0")
        print("1. Print Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            print_videos()
        elif choice == '2':
            add_video()
        elif choice == '3':
            update_video()
        elif choice == '4':
            delete_video()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()


if __name__ == "__main__":
    main()
