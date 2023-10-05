import schedule
import time
import requests

def fetch_and_display_posts():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(f"Post ID: {post['id']}")
                print(f"Title: {post['title']}")
                print(f"Body: {post['body']}")
                print("-" * 30)
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Schedule the task to fetch and display posts every 10 seconds
schedule.every(10).seconds.do(fetch_and_display_posts)

while True:
    schedule.run_pending()
    time.sleep(1)
