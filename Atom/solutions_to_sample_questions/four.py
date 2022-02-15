import sys, os.path

def get_grades():
    grades = []
    with open(os.path.join(sys.path[0], "grades.txt"), "r") as file:
        for line in file:
            grades.append(int(line.replace("\n", "")))
    return grades

def get_stats(grades):
    print(f"Number of items: {len(grades)}")
    print(f"Average: {round(sum(grades) / len(grades), 2)}")
    print(f"Lowest: {min(grades)}")
    print(f"Highest:{max(grades)}")

grades = get_grades()
print(grades)
get_stats(grades)