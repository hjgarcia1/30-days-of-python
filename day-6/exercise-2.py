employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00),
]

average = 0
total_wage = 0

for employee in employees:
    total_wage += employee[2]


average = round(total_wage / len(employees), 2)

print(f"Average Hourly Wage: ${average}")

for employee in employees:
    if employee[2] > average:
        print(f"Name: {employee[0]} has higher than average wage.")
        
