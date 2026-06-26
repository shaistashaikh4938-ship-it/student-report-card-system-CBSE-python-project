# Student Report System

## 📌 Overview
Student Report System is a simple Python project that uses CSV file handling to manage student records. It reads student data from a CSV file, calculates the average marks, finds the topper, assigns grades, and saves the final report into a new CSV file.

## ✨ Features
- Read student data from `students.csv`
- Calculate average marks
- Find the topper
- Assign grades based on marks
- Save the final report into `final_report.csv`

## 📊 Grade Criteria
| Marks | Grade |
|-------|-------|
| 90 and above | A |
| 80 – 89 | B |
| 70 – 79 | C |
| Below 70 | Fail |

## 📂 Project Structure
```
Student_Report_System/
│── students.csv
│── final_report.csv
│── report.py
│── README.md
```

## 🛠 Requirements
- Python 3.x
- csv module (built-in)

## ▶️ How to Run
1. Clone the repository.
2. Open the project folder.
3. Place the `students.csv` file in the project directory.
4. Run the program:
   ```bash
   python report.py
   ```
5. The generated report will be saved as `final_report.csv`.

## 📁 Sample Input (students.csv)

| Name | Marks |
|------|------:|
| Ali | 95 |
| Sara | 82 |
| Ahmed | 76 |
| Zoya | 68 |

## 📄 Output
The program:
- Calculates the average marks.
- Finds the topper.
- Assigns grades.
- Saves the results to `final_report.csv`.

## 🚀 Technologies Used
- Python
- CSV
