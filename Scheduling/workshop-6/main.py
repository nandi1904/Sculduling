import schedule
import time
import requests

def fetch_posts():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        if response.status_code == 200:
            posts = response.json()
            print("Posts:")
            for post in posts:
                print(f"Post ID: {post['id']}")
                print(f"Title: {post['title']}")
                print(f"Body: {post['body']}")
                print("-" * 30)
        else:
            print(f"Failed to fetch posts. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while fetching posts: {str(e)}")

def fetch_users():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        if response.status_code == 200:
            users = response.json()
            print("Users:")
            for user in users:
                print(f"User ID: {user['id']}")
                print(f"Name: {user['name']}")
                print(f"Email: {user['email']}")
                print("-" * 30)
        else:
            print(f"Failed to fetch users. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while fetching users: {str(e)}")

def fetch_comments():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/comments")
        if response.status_code == 200:
            comments = response.json()
            print("Comments:")
            for comment in comments[:5]:  # Display the first 5 comments
                print(f"Comment ID: {comment['id']}")
                print(f"Name: {comment['name']}")
                print(f"Email: {comment['email']}")
                print(f"Body: {comment['body']}")
                print("-" * 30)
        else:
            print(f"Failed to fetch comments. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while fetching comments: {str(e)}")

# Schedule tasks to fetch data at different intervals
schedule.every(10).seconds.do(fetch_posts)  # Fetch posts every 10 seconds
schedule.every(30).seconds.do(fetch_users)  # Fetch users every 30 seconds
schedule.every(15).seconds.do(fetch_comments)  # Fetch comments every 15 seconds

while True:
    schedule.run_pending()
    time.sleep(1)
