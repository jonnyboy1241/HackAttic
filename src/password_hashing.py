# Challenge info is located at https://hackattic.com/challenges/password_hashing
from src.utils import retrieve_problem, submit_solution

from base64 import b64decode

import hashlib
import hmac

PROBLEM = "password_hashing"


def solve_password_hashing():
    """
    Solve password_hashing
    """
    problem_data = retrieve_problem(PROBLEM)

    # Get the data from the problem
    password = problem_data["password"].encode()
    salt = b64decode(problem_data["salt"])
    pbkdf2 = problem_data["pbkdf2"]
    scrypt = problem_data["scrypt"]

    # Calculate the SHA256 hash
    sha256_hash = hashlib.sha256(password)

    # Calculate the HMAC-SHA256
    hmac_sha256 = hmac.new(salt, password, digestmod=hashlib.sha256)

    # Calculate the PBKDF2-SHA256 digest
    pbkdf2_hash = pbkdf2["hash"]
    pbkdf2_rounds = pbkdf2["rounds"]
    pbkdf2 = hashlib.pbkdf2_hmac(pbkdf2_hash, password, salt, pbkdf2_rounds)

    # Construct the solution for HackAttic
    solution = {
        "sha256": sha256_hash.hexdigest(),
        "hmac": hmac_sha256.hexdigest(),
        "pbkdf2": pbkdf2.hex(),
        "scrypt": ""
    }

    solution_result = submit_solution(PROBLEM, solution)
    print(solution_result)


if __name__ == "__main__":
    solve_password_hashing()
