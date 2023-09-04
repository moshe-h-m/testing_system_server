import subprocess
from quastion import Solution


def run_solution_to_check(name, description, solution):
    try:
        list_of_io = Solution.__dict__[description]
        print(list_of_io)
    except:
        return "No such solution"

    error_message = ""

    for io in list_of_io:
        input = io["input"]
        output = io["output"]
        result = run_solution(input, description, solution)
        print(result)
        if str(output) != str(result):
            error_message += f"Failed on input {input} expected {output} but got {result}"
    if error_message:
        return error_message
    return f"All tests passed: Good job! {name}"
def run_solution(arguments, description, solution):
    function_name = description
    print(f'solution1: {solution}')
    result = None

    try:
        # Define the function
        arg_list =", ".join([str(x) for x in arguments[0]])
        print(f'arg_list: {arg_list}')
        code_to_execute = f'{solution}\nresult = {function_name}(*{arguments})'
        print(f'code_to_execute: {code_to_execute}')

        exec(code_to_execute, globals())

        result = globals().get("result")
    except Exception as e:
        result = str(e)

    return result
