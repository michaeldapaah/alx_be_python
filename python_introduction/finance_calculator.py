monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")

monthly_savings = float(monthly_income) - float(monthly_expenses)

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)  # Assuming a 5% annual interest rate

print("Your monthly savings are: $", monthly_savings)
print("Projected savings after one year, with interest, is: $", projected_savings)