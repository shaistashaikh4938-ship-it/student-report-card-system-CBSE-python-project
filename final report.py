import csv

total = 0
count = 0
highest_marks = 0
topper = ""

with open("Studentss.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    with open("Final_Report.csv", "w", newline="") as report:
        writer = csv.writer(report)

        writer.writerow(["name", "marks", "grade"])

        for row in reader:
            name = row[0]
            marks = int(row[1])

            # Average calculation
            total += marks
            count += 1

            # Topper
            if marks > highest_marks:
                highest_marks = marks
                topper = name

            # Grade assignment
            if marks >= 90:
                grade = "A"
            elif marks >= 80:
                grade = "B"
            elif marks >= 70:
                grade = "C"
            else:
                grade = "Fail"

            writer.writerow([name, marks, grade])

average = total / count

print("Average Marks =", average)
print("Topper =", topper)
print("Highest Marks =", highest_marks)
print("Final_Report.csv created successfully")
