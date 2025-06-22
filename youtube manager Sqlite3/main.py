import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cur = conn.cursor()

cur.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
    )
''')

def list_videos():
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)

def add_video(name, time):
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cur.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List a all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        Choice = input("Enter your choice: ")
        
        if Choice == '1':
            list_videos()
        elif Choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif Choice == '3':
            video_ID = input("Enter Video ID to update: ")
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            update_video(video_ID, name, time)
        elif Choice == "4":
            video_ID = input("Enter Video ID to delete: ")
            delete_video(video_ID)
        elif Choice == "5":
            break
        else:
            print("Invalid choice")
    
    conn.close()


if __name__ == "__main__":
    main()