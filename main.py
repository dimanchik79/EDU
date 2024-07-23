import hashlib
from DB.models import Users


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def main():

    password = hash_password("password")
    print(password)


if __name__ == "__main__":
    main()
