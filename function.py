import os
import streamlit as st
FILEPATH = ''

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        tasks_local = file_local.readlines()
        return tasks_local


def store_todos(tasklist, filepath=FILEPATH):
    with open(filepath, "w") as file_local:
        file_local.writelines(tasklist)



categories = ""
completed_dir = ""

def opendir(categories, completed_dir):
    for dirr in categories:
        if not os.path.exists(f'{dirr}.txt'):
            with open(f'{dirr}.txt', "w") as file:
                pass
    if not os.path.exists(completed_dir ):
        with open(completed_dir , "w") as file:
            pass

