# Challenge info is located at https://hackattic.com/challenges/help_me_unpack
from src.utils import retrieve_problem, submit_solution

from base64 import b64decode

import struct

PROBLEM = "help_me_unpack"


def solve_help_me_unpack():
    """
    Solve help_me_unpack
    """
    problem_data = retrieve_problem(PROBLEM)

    # Decode and Unpack the data.
    decode = b64decode(problem_data["bytes"])
    unpacked_data = struct.unpack("iIhfdd", decode)

    solution = {
        "int": unpacked_data[0],
        "uint": unpacked_data[1],
        "short": unpacked_data[2],
        "float": unpacked_data[3],
        "double": unpacked_data[4],
        "big_endian_double": unpacked_data[4]
    }

    # Submit the solution
    solution_result = submit_solution(PROBLEM, solution)

    print(solution_result)


if __name__ == "__main__":
    solve_help_me_unpack()
