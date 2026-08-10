expenses = [250, 1200, 450, 800, 150, 2000, 350]

total = sum(expenses)
average = total / len(expenses)
highest = max(expenses)
lowest = min(expenses)

above_500 = 0
below_equal_500 = 0

for expense in expenses:
    if expense > 500:
        above_500 += 1
    else:
        below_equal_500 += 1

print("Total Expense:", total)
print("Average Expense:", average)
print("Highest Expense:", highest)
print("Lowest Expense:", lowest)
print("Number of Expenses Above ₹500:", above_500)
print("Number of Expenses Below or Equal to ₹500:", below_equal_500)

print("Expenses Above Average:")

for expense in expenses:
    if expense > average:
        print(expense)