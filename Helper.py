# Extracts the command line arguments from a list and assigns them to key-value pairs
def extract_arguments(arguments):
    # arguments = ['--type=diff', '--principal=1000000', '--periods=10', '--interest=10']
    parameters = {}
    for argument in arguments[1:]:
        key_value = argument.split("=")
        key = key_value[0][2:]
        value = key_value[1]
        parameters.update({key: value})

    # parameters = {'type': 'diff', 'principal': '1000000', 'periods': '10', 'interest': '10'}
    return parameters


# Checks the arguments provided for negative values
def check_values(arguments):
    flag = False
    for key, value in arguments.items():
        if key == "type":
            continue
        if float(value) < 0:
            flag = True

    # False: arguments = {'type': 'diff', 'principal': '1000000', 'periods': '10', 'interest': '10'}
    # True: arguments = {'type': 'diff', 'principal': '-1000000', 'periods': '10', 'interest': '10'}
    return flag
