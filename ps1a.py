
anual_salary = float(input("Enter your anual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
current_saving = 0
portion_down_payment = total_cost * 0.25
month_salary = anual_salary/12
r=0.04
month = 0
while True:
    current_saving += current_saving*r/12 + month_salary*portion_saved
    month += 1
    if current_saving >= portion_down_payment:
        break
    
print("Number of months:",month)

