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
    
# Add -----------------------------------------------------------------
    
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

# List ----------------------------------------------------------------

    elif command == "list":
        tasks = list_tasks()

        if not tasks:
            print("No tasks yet. Add one with the 'add' command!")
            return
        
        print("\n📋 Your tasks:\n")
        for task in tasks:
            print_task(task)
        print()
          
# Complete -------------------------------------------------------------

    elif command == "complete":
        if len(sys.argv) < 3:
            print("Error: You must enter the task ID")
            print("Eg.: python main.py complete 1")
            return
        
        try:
            task_id = int(sys.argv[2])
            task = complete_task(task_id)
            
            print(f"✅ Task [{task['id']}] marked as completed: {task['title']}")
        
        except ValueError as e:
            print(f"Error: {e}")

# Delete ---------------------------------------------------------------

    elif command == "delete":
        if len(sys.argv) < 3:
            print("❌ Error: You must enter the task ID.")
            print("Eg. python main.py delete 1")
            return
        
        try:
            task_id = int(sys.argv[2])
            delete_task(task_id)
            print(f"🗑️  Task [{task_id}] successfully deleted.")
            
        except ValueError as e:
            print(f"Error: {e}")

# Help -----------------------------------------------------------------

    elif command == "help":
        show_help()  
        