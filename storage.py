import json
import os

FILE_PATH = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)
    

def save_tasks(tasks):
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)
        
