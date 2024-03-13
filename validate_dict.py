import yaml
from .gh_actions import egotist_config

#test
def validate_dictionary(dictionary):
    if not isinstance(dictionary, dict):
        return False

    expected_keys = ["gamma", "alpha", "beta", "sigma", "theta", "omega", "lambda", "iota"]
    if not set(expected_keys) == set(dictionary.keys()):
        return False

    # Check if each sub-dictionary follows the expected structure
    for team, team_dict in dictionary.items():
        if not isinstance(team_dict, dict):
            return False
        for department, department_dict in team_dict.items():
            if not isinstance(department_dict, dict):
                return False
            for subgroup, subgroup_list in department_dict.items():
                if not isinstance(subgroup_list, list):
                    return False
                for item in subgroup_list:
                    if not isinstance(item, dict):
                        return False
                    if not all(key in item for key in ["stack", "owner", "description"]):
                        return False
    
    return True


if validate_dictionary(egotist_config.dept_stack):
    print("Dictionary is valid.")
else:
    print("Dictionary is not valid.")

    

def main():
    with open('config.py', 'r') as file:
        data = file.read()
        # Extract the dictionary from the Python script
        dictionary_str = data[data.find('{'):]

        # Convert the string representation of the dictionary to a Python dictionary
        dept_stack = eval(dictionary_str)

        # Validate the dictionary
        if validate_dictionary(dept_stack):
            print("Dictionary syntax is valid")
            exit(0)  # Success exit code
        else:
            print("Dictionary syntax is invalid")
            exit(1)  # Failure exit code

if __name__ == "__main__":
    main()
