def task():
    tasks = []        
    completed = []     

    print("----WELCOME TO THE TASK MANAGEMENT APP---")

    total = int(input("How many tasks you want to add: "))   
    for i in range(1, total + 1):
        t = input("Enter task {i}: ".format(i=i))
        tasks.append(t)

    print("Today's tasks are:", tasks)

    while True:
        print("\n1-Add\n2-Update\n3-View\n4-Mark Complete\n5-Delete\n6-Exit/Stop")
        op = int(input("Enter your choice: "))

        if op == 1:
            new = input("Enter new task: ")
            tasks.append(new)
            print("Task", new, "added.")

        elif op == 2:
            old = input("Enter task you want to update: ")
            if old in tasks:
                new = input("Enter updated task: ")
                ind = tasks.index(old)
                tasks[ind] = new
                print("Task updated to:", new)
            else:
                print("Task not found.")

        elif op == 3:
            print("\nPending tasks:", tasks)
            print("Completed tasks:", completed)
       
        elif op == 4:
            t = input("Enter task name to mark complete: ")
            if t in tasks:
                tasks.remove(t)
                completed.append(t)
                print("Task", t, "marked as complete.")
            else:
                print("Task not found in pending list.")

        elif op == 5:
            d = input("Enter task to delete: ")
            if d in tasks:
                tasks.remove(d)
                print("Task", d, "deleted.")
            elif d in completed:
                completed.remove(d)
                print("Completed task", d, "deleted.")
            else:
                print("Task not found.")

        elif op == 6:
            print("Closing program...")
            break
       
        else:
            print("Invalid Input")

task()
