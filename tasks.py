from storage import load_tasks, save_tasks

def _generate_id(tasks):
    if not tasks:
        return 1
    
    max_id = max(task["id"] for task in tasks)
    
    return max_id + 1


def add_task(title):
    if not title or not title.strip():
        raise ValueError("Task title cannot be empty.")
    
    tasks = load_tasks()
    
    new_task = {
        "id": _generate_id(tasks),
        "title": title.strip(),
        "completed": False
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    
    return new_task


def list_tasks():
    return load_tasks()


def complete_task(task_id):
    tasks = load_tasks()
    
    for task in tasks:
        
        if task["id"] == task_id:
            task["complete"] = True
            save_tasks(tasks)
            
            return task
    
    raise ValueError(f"Task ID {task_id} not found.")


def delete_task(task_id):
    tasks = load_tasks()
    filtered = [task for task in tasks if task["id"] != task_id]
    
    if len(filtered) == len(tasks):
        raise ValueError(f"Task ID {task_id} not found.")
    
    save_tasks(filtered)
    

    