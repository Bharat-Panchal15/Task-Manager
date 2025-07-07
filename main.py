import json
import os

class TaskManager:
    def __init__(self,filename='01_projects/01_Task_Manager_Project/tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename,'r') as file:
                    self.tasks = json.load(file)
            
            except json.JSONDecodeError:
                print("\n Corrupted task file. Starting fresh.")
        
        else:
            self.tasks = []
    
    def save_tasks(self):
        try:
            with open(self.filename,'w') as file:
                json.dump(self.tasks,file,indent=4)
        
        except Exception as e:
            print(e)

    def finding_task(self,title):
        for task in self.tasks:
            if task['title'] == title:
                return task
        return None
    
    def add_task(self):
        title = input("Enter the task: ").strip().capitalize()
        if not title:
            print("\n Task cannot be empty.")
            return

        if self.finding_task(title):
            print(f"\nTask already exists.")
        
        else:  
            self.tasks.append({"title":title,"status":"Pending"})
            self.save_tasks()
            print(f"\nTask '{title}' was added successfully")

    def remove_task(self,task_title):
        task = self.finding_task(task_title)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print(f"\nTask '{task_title}' has been successfully removed.")
        
        else:
            print(f"\nTask {task_title} not found in tasks.")

    def mark_task(self,task_title,status):
        task = self.finding_task(task_title)
        if task:
            task['status'] = status
            self.save_tasks()
            print(f'\nStatus of task "{task_title}" is changed to "{status}"')

    def view_all_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.")
        
        else:
            for idx, task in enumerate(self.tasks,start=1):
                print(f"\nTask {idx}: {task['title']} - Status: {task['status']}")

    def view_completed_tasks(self):
        found = False
        for ele in self.tasks:
            if ele['status'] == 'Done':
                print(f"\nThe task {ele['title']} is done.")
                found = True
            
        if not found:
            print(f'\nNo task completed yet.')

    def view_pending_tasks(self):
        found = False
        for ele in self.tasks:
            if ele['status'] == 'Pending':
                print(f"\nThe task {ele['title']} is pending.")
                found = True

        if not found:
            print("\nNo pending task left.")

if __name__ == "__main__":
    manager = TaskManager()

    while True:
        # To show all the options to user.
        print("\nEnter 1 to ADD task")
        print("Enter 2 to REMOVE task")
        print("Enter 3 to MARK THE TASK is completed or pending.")
        print("Enter 4 to VIEW ALL TASKS.")
        print("Enter 5 to VIEW COMPLETED TASKS.")
        print("Enter 6 to VIEW PENDING TASKS.")
        print("Enter 7 to QUIT.")

        # To let the user the it's choice.
        try:
            user_choice = int(input("\nEnter your choice: "))
        
        except ValueError:
            print("Invalid Input Please a number between 1 and 7.")
            continue

        match user_choice:
            case 1:
                manager.add_task()

            case 2:
                task_title = input("Enter the task you want to remove: ").capitalize()
                manager.remove_task(task_title)

            case 3:
                user_task = input("\nEnter the task to mark: ").strip().capitalize()
                if not user_task:
                    print("\nTask cannot be empty.")
                    continue

                task = manager.finding_task(user_task)

                if task:
                    user_mark = input("\nEnter the status (pending/done): ").strip().capitalize()

                    if user_mark not in ['Pending','Done']:
                        print("\nInvalid status. Only 'pending' or 'done' allowed.")
                        continue
                    
                    manager.mark_task(user_task,user_mark)
                
                else:
                    print(f"\nTask not found, please enter valid task.")

            case 4:
                manager.view_all_tasks()

            case 5:
                manager.view_completed_tasks()

            case 6:
                manager.view_pending_tasks()

            case 7:
                print("\nHere are all your tasks before exiting:")
                manager.view_all_tasks()
                manager.save_tasks()
                print("\nExiting... Goodbye!")
                break

            case _:
                print("\nInvalid Input!")
                print("Please enter number between 1 to 7!")