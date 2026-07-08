import requests

def get_user(user_id):
    response = (f"https://jsonplaceholder.typicode.com/users/{user_id}")
    try:
        response = requests.get(response, timeout=10)
        return response
    except Exception as e:
        print(e)
    

def display_user(response):
    if response.status_code == 200:
        data = response.json()

        print(response.status_code)
        print(response.elapsed.total_seconds())
        print(response.headers["Content-Type"])
        print(data["username"])
        print(data["email"])
    else:
        print("Request Failed")

if __name__ == "__main__":
    response = get_user(1)
    display_user(response)