from src.configs import api_token, playground_mode

import requests


def retrieve_problem(problem) -> dict:
    """
    Make an API call to HackAttic to get the problem set.
    :param: The problem to retrieve (This will be part of the URL). Convention is snake case
    :return: The problem set as a dict. This will be the json of the Response
    """
    url = f"https://hackattic.com/challenges/{problem}/problem?access_token={api_token()}"

    response = requests.get(url)
    return response.json()


def submit_solution(problem, json) -> dict:
    """
    Make an API call to HackAttic to submit our solution.
    :param problem: The problem to submit a solution for (This will be part of the URL). Convention is snake case.
    :param json: The solution to submit as a json
    :return: The response from HackAttic as a dict. This will include details of whether we were right or not.
    """
    url = f"https://hackattic.com/challenges/{problem}/solve?access_token={api_token()}"

    if playground_mode():
        url = f"{url}&playground=1"

    response = requests.post(url, json=json)

    return response.json()

