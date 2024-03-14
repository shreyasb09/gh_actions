import yaml
import egotist_config

def validate_config(dept_stack):
    for account, departments in dept_stack.items():
        if not isinstance(account, str):
            print("Error: Account name should be a string")
            return False
        if not isinstance(departments, dict):
            print(f"Error: Departments for account '{account}' should be a dictionary")
            return False
        for department, categories in departments.items():
            if not isinstance(department, str):
                print("Error: Department name should be a string")
                return False
            if not isinstance(categories, dict):
                print(f"Error: Categories for department '{department}' in account '{account}' should be a dictionary")
                return False
            for category, stacks in categories.items():
                if not isinstance(category, str):
                    print("Error: Category name should be a string")
                    return False
                if not isinstance(stacks, list):
                    print(f"Error: Stacks for category '{category}' in department '{department}' under account '{account}' should be a list")
                    return False
                if not stacks:
                    print(f"Error: Stacks list for category '{category}' in department '{department}' under account '{account}' is empty")
                    return False
                for stack in stacks:
                    if not isinstance(stack, dict):
                        print(f"Error: Stack entry '{stack}' in category '{category}' under department '{department}' in account '{account}' should be a dictionary")
                        return False
                    if not all(key in stack for key in ["stack", "owner", "description"]):
                        print(f"Error: Stack entry '{stack}' in category '{category}' under department '{department}' in account '{account}' is missing required keys")
                        return False
                    for key, value in stack.items():
                        if not isinstance(value, str):
                            print(f"Error: Value '{value}' for key '{key}' in stack entry '{stack}' is not a string")
                            return False
    return True




# Validate the dictionary
if validate_config(egotist_config.dept_stack):
    print("Dictionary is valid.")
else:
    print("Dictionary is not valid.")


    

def main():
    with open('egotist_config.py', 'r') as file:
        data = file.read()
        # Extract the dictionary from the Python script
        dictionary_str = data[data.find('{'):]

        # Convert the string representation of the dictionary to a Python dictionary
        dept_stack = eval(dictionary_str)

        # Validate the dictionary
        if validate_config(dept_stack):
            print("Dictionary syntax is valid")
            exit(0) 
        else:
            print("Dictionary syntax is invalid")
            exit(1)  # Failure exit code

if __name__ == "__main__":
    main()
