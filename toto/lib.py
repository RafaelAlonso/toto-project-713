from termcolor import colored

def say_my_name():
    return 'Hello my name is Rafa'

def who_am_i():
    print(colored(f"{say_my_name}. Nice to meet you. Pretty neat huh", 'green'))