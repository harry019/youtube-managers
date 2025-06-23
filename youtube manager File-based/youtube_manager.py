import json

file = 'youtube.txt'

def load_data():
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(file, 'w') as f:
        json.dump(videos, f)

def list_all_videos(videos):
    print("\n")
    print("*"*70)
    print("\n")

    for index , video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*"*70)

def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name" : name, "time" : time})
    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1<= index <= len(videos):
        name = input("Enter the new video Name: ")
        time = input("Enter the new video Time: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video index")
        
def main():

    videos = load_data()

    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. List a all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        Choice = input("Enter your choice: ")
        print(videos)

        match Choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_videos(videos)
            case "4":
                delete_videos(videos)
            case "5":
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()

# [{} , {}]