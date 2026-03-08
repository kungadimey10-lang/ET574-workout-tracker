from data import workout_types, durations

def add_workout():
    workout = input("Enter workout type: ")
    duration = int(input("Enter duration (minutes): "))

    workout_types.append(workout)
    durations.append(duration)

    print("Workout recorded!")

def view_all_workouts():
    if len(workout_types) == 0:
        print("No workouts recorded")
        return

    for i in range(len(workout_types)):
        print(f"{i+1}. {workout_types[i]} - {durations[i]} minutes")

def summary_report():
    if len(durations) == 0:
        print("No workouts recorded")
        return

    total = sum(durations)
    count = len(durations)
    average = total / count
    longest = max(durations)
    shortest = min(durations)

    print("Total workouts:", count)
    print("Total minutes:", total)
    print("Average duration:", average)
    print("Longest workout:", longest)
    print("Shortest workout:", shortest)