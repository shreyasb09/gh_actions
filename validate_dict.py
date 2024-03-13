import yaml
import egotist_config


def validate_dept_stack(dept_stack):
    valid_keys = set(["gamma", "alpha", "beta", "sigma", "theta", "omega", "lambda", "iota"])

    for dept, teams in dept_stack.items():
        if dept not in valid_keys:
            print(f"Error: '{dept}' department is not a valid key in the dictionary.")
            return False
        
        if not isinstance(teams, dict):
            print(f"Invalid data type for '{dept}' department: expected dictionary.")
            return False
        
        for team, categories in teams.items():
            if not isinstance(categories, dict):
                print(f"Invalid data type for '{team}' team in '{dept}' department: expected dictionary.")
                return False
            
            for category, stacks in categories.items():
                if not isinstance(stacks, list):
                    print(f"Invalid data type for '{category}' category in '{team}' team of '{dept}' department: expected list.")
                    return False
                
                for stack in stacks:
                    if not isinstance(stack, dict):
                        print(f"Invalid data type for stack entry in '{category}' category of '{team}' team in '{dept}' department: expected dictionary.")
                        return False
                    
                    if not all(key in stack for key in ("stack", "owner", "description")):
                        print(f"Missing keys in stack entry in '{category}' category of '{team}' team in '{dept}' department.")
                        return False
                    
                    if not all(isinstance(value, str) for value in stack.values()):
                        print(f"Invalid data type for values in stack entry in '{category}' category of '{team}' team in '{dept}' department: expected strings.")
                        return False
                    
    print("Dictionary validation successful: All entries are valid.")
    return True

# Validate the dictionary
if validate_dept_stack(egotist_config.dept_stack):
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
        if validate_dept_stack(dept_stack):
            print("Dictionary syntax is valid")
            exit(0) 
        else:
            print("Dictionary syntax is invalid")
            exit(1)  # Failure exit code

if __name__ == "__main__":
    main()
