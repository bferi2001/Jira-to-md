import json

def print_return(func):
        def inner(*args, **kwargs):
            print(func(*args, **kwargs))
            return func(*args, **kwargs)
        return inner
    
def return_json_to_file(func):
    def inner(*args, **kwargs):
        returnvalue=func(*args, **kwargs)
        with open("test.json", "w", encoding="utf-8") as file:
            json.dump(returnvalue, file)
        return returnvalue
    return inner