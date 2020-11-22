from password import User, Credential
import random
import getpass
import string
import uuid


def creat_user(name, username, password):
    '''
    Function to create a new user
    '''
    new_user = User(name, username, password)
    return new_user