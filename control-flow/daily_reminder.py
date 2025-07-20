task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: {task} is a high priority task, but it can be scheduled for later this week.")
        else:
            print("Invalid input for time-bound status.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that should be completed today")
        elif time_bound == "no":
            print(f"Note: {task} is a medium priority task, you can complete it later this week.")
        else:
            print("Invalid input for time-bound status.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")
        elif time_bound == "no":
            print(f"Note: {task} is a low priority task. You can complete it whenever you have time.")
        else:
            print("Invalid input for time-bound status.")
    case _:
        print("Invalid input. Please enter a valid task priority (high, medium, or low).")