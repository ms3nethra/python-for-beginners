"""
Grading system

* A: marks equal and above 90
* B: marks equal to 80 and less than 90
* C: marks equal to 70 and less than 80
* D: marks equal to 60 and less than 70
* E: less than or 60
"""

marks = int(90)

if marks >= 90 and marks <= 100:
    print("A Grade")

elif marks >= 80 and marks < 90:
    print("B grade")

elif marks >= 70 and marks < 80:
    print("C grade")

elif marks >= 60 and marks < 70:
    print("D grade")

elif marks < 60:
    print("E")

else:
    print("Invalied")