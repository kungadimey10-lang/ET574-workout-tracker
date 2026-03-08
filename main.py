from tracker import add_workout, view_all_workouts, summary_report

while True:

    print("\nWelcome to Workout Log!")
    print("1 Add Workout")
    print("2 View All Workouts")
    print("3 View Summary")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_workout()

    elif choice == "2":
        view_all_workouts()

    elif choice == "3":
        summary_report()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option")