import requests
import json


def githubAPI(username):
    """:returns boolean"""
    try:
        result = requests.get("https://api.github.com/users/" + username + "/repos")
    except (TypeError):
        return "Github user not correct"

    result = result.json()
    if len(result) == 0:
        print("No Repos")
        return False
    for i in result:
        resultRepo = requests.get(i['commits_url'].split("{")[0])
        resultRepo = resultRepo.json()
        print("Repo Name: " + i['name'] + "\t Number of commits: " + str(len(resultRepo)))
    return True


if __name__ == "__main__":
    response = input("Please input the Github Username: ")
    response = "konglingwengit"
    githubAPI(response)
