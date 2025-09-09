# classroom_performance.py

def calculate_average(marks):
    return sum(marks) / len(marks)

def get_all_averages(students):
    averages = {}
    for name in students:
        avg = calculate_average(students[name])
        averages[name] = round(avg, 2)
    return averages

def get_top_student(averages):
    top_name = max(averages, key=averages.get)
    return top_name

if __name__ == "__main__":
    students = {
        "John": [85, 78, 92],
        "Alice": [88, 79, 95],
        "Bob": [70, 75, 80]
    }

    averages = get_all_averages(students)
    top_performer = get_top_student(averages)

    print("Average Marks:", averages)
    print("Top Performer:", top_performer)
