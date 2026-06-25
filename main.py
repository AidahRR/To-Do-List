Tasks = []

while True:
    print("This is your To Do List!")
    print("---MAIN MENU---")
    print("1. Add task:")
    print("2. View tasks:")
    print("3. Delete task:")
    print("4. Exit")
    Choice = int(input("Choose an option from the above: "))
    if Choice == 1:
        Name = input("Enter the task: ")
        priority = input("Enter priority (High/Medium/Low): ")
        Due_Date = input ("Enter your due date (DD/MM/YYYY): ")
        Task = {
            "Name": Name,
            "priority": priority,
            "Due Date": Due_Date
        }
        Tasks.append(Task)
    if Choice == 2:
        for i, task in enumerate(Tasks, start=1):
            print(
                f"{i}. {task["Name"]} | "
                f"{task["priority"]} | "
                f"{task["Due Date"]} | "
            )
    if Choice == 3:
        print (Tasks)
        Choice_Delete = int(input("Enter the number of the position of the task you want to delete: "))
        Tasks_Delete = Choice_Delete - 1
        Tasks.pop(Tasks_Delete)
    if Choice == 4:
        print("Exiting now!")
        break
