from random import choice
import string


def PasswordGeneration():
    password = ""
    valores = string.ascii_letters + string.digits + string.punctuation
    for i in range(0, 21):
        random = choice(valores)
        password += random
    return password
