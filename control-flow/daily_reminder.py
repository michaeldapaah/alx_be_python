task = input("Input your task for today: ")
task_priority = input("Is this task high, medium, or low priority? ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

match task_priority:
    case "high" if time_bound == "yes":
        print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
    case "high" if time_bound == "no":
        print(f"Note: {task} is a high priority task, but it can be scheduled for later this week.")
    case "medium" if time_bound == "yes":
        print(f"Reminder: {task} is a medium priority task that should be completed today")
    case "medium" if time_bound == "no":
        print(f"Note: {task} is a medium priority task, you can complete it later this week.")
    case "low" if time_bound == "yes":
        print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")
    case "low" if time_bound == "no":
        print(f"Note: {task} is a low priority task. You can complete it whenever you have time.")
    case _:
        print("Invalid input. Please enter a valid task priority (high, medium, low) and time-bound status (yes, no).")

