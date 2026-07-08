import requests

def create_user(name, job):
    url = "https://reqres.in/api/users"
    payload = {
        "name": name,
        "job": job
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        return response
    except Exception as e:
        print(e)


def display_response(response):
    data = response.json()
    print(response.status_code)
    print(response.elapsed.total_seconds())
    print(response.headers["Content-Type"])
    print(data["name"])
    print(data["job"])
    print(data["id"])
    print(data["createdAt"])


if __name__ == "__main__":
    response = create_user(
    "Ravi",
    "QA Engineer")

display_response(response)