import hashlib
import json


db_path = 'database/'


def read_db(file_name: str) -> dict:
    file_path = f"{db_path}{file_name}"
    f = open(file_path)

    data_json = f.read()
    f.close()

    data_dict = json.loads(data_json)
    return data_dict


def update_db(file_name: str, data: dict) -> None:
    file_path = f"{db_path}{file_name}"
    f = open(file_path, "w")

    data_json = json.dumps(data, indent=4)

    f.write(data_json)
    f.close()


def add_user(
        first_name: str, 
        last_name: str, 
        birth_year: int, 
        email: str, 
        password: str
    ) -> bool:
    users = read_db("users.json")
    
    if not users['users']:
        id = 0
    else:
        id = users['users'][-1]['id'] + 1
        for user in users['users']:
            if user['email'] == email:
                return False

    user = {
        "id": id,
        "first_name": first_name,
        "last_name": last_name,
        "birth_year": birth_year,
        "email": email,
        "password": hashlib.sha256(password.encode()).hexdigest()
    }
    users['users'].append(user)

    update_db("users.json", users)
    return True


def get_user(email: str, password: str) -> dict:
    users = read_db("users.json")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    for user in users['users']:
        if user['email'] == email and user['password'] == hashed_password:
            users['session'] = user['id']
            update_db('users.json', users)
            return user

    return {}

