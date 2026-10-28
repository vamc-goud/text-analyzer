
import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    print("Task ID:", data["id"])
    print("Task:", data["title"])
    print("Completed:", data["completed"])

except requests.RequestException as error:
    print("Request failed:", error)
