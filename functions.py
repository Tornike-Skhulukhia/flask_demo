'''
    define helper functions for our simple flask app
'''
import json


def check_login_status(username, password):
    '''
    function returns
        1. "success"  - if user is registered and password is correct
        2. "incorrect password" - if password is incorrect
        3. "user not registered" - if user is not registered 
    False otherwise
    '''
    with open("users_list.txt") as f:
        for line in f:
            line_data = json.loads(line)

            if line_data['username'] == username:
                if line_data['password'] == password:
                    return "success"
                else:
                    return "incorrect password"
        return "user not registered"


def register_user(username, password):
    '''
    registers user with given username and password.
    
    Returns "username is taken" if this username is taken,
    or "success" if registration is successfull. 
    '''
    with open("users_list.txt", "r+") as f:
        for line in f:
            line_data = json.loads(line)

            if line_data['username'] == username:
                return "username is taken"
        # breakpoint()
        f.write(json.dumps({"username": username,
                            "password": password},
                            ensure_ascii=False) + "\n")
    return "success"


def get_ideas():
    '''
    returns list of all users ideas
    '''
    data = []

    with open("users_ideas.txt") as f:
        for line in f:
            line_data = json.loads(line)
            data.append(line_data)
    return data


def save_idea(idea):
    '''
    save idea.
    idea argument(dict) should contain title, tag and text keys. 
    '''
    with open("users_ideas.txt", "a") as f:
        f.write(json.dumps(idea, ensure_ascii=False) + "\n")


