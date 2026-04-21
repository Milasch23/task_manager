import sys

from tasks import add_task, list_tasks, complete_task, delete_task

def print_task(task):
    status = "✅" if task["Completed"] else "⬜"
    print(f"[{task['id']}] {status} {task['title']}")
    

def show_help():
    print("""
╔══════════════════════════════════════════╗
║          📋 CLI TASK MANAGER             ║
╠══════════════════════════════════════════╣
║  COMMAND                  DESCRIPTION    ║
╠══════════════════════════════════════════╣
║  add "title"           → Add a task      ║
║  show                  → Show tasks      ║
║  complete <id>         → Mark ✅         ║
║  delete <id>           → Delete a task   ║
║  help                  → This menu       ║
╚══════════════════════════════════════════╝
""")
    

def main():
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == "add":
        if len(sys.argv) < 3:
            print("Error: must write the task title.")
            print(" Eg. python main.py add 'Buy milk' ")
            return
    
    title = sys.argv[2]
        
    try:
        task = add_task(title)
        print(f"Task added: [{task['id']}] {task['title']}")
    except ValueError as e:
        print(f"Error: {e}")



    
