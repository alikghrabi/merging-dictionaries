def input_employees():
    employees() = {}
    while True:
        department = input("enter department name or type exit to stop: ")
        if department.lower() == 'exit':
            break
        department_employees = {}
        while True:
            employee_name = input(f"enter employee name in {department} or type exit to stop")
            if employee_name.lower() == 'exit':
                break
            age = input(f"enter age for {employee_name}: ")
            role = input(f"enter role for {employee_name}: ")

            department_employees[employee_name] = {"age": int(age), "role": role}
        
        employees[department] = department_employees

def print_employees(cmpnyemply):
    print(cmpnyemply)

def add_employee(cmpnyemply, department, age, role):
    if department in cmpnyemply:
        cmpnyemply[department][name] = {"age": age, "role": role}
    else:
        print(f"Department  {department} doesn't exit!")
    
def count_total_employees(cmpnyemply):
    total = 0
    for department in cmpnyemply.values():
        total += len(department)
    
    return total

company_employees = input_company_employees()

print_company_employees(company_employees)

add_employee(company_employees, "Engineering", "David", 27, "Data Scientist")
print("\nAfter adding David:")
print_company_employees(company_employees)

total_employees = count_total_employees(company_employees)
print(f"\nTotal number of employees: {total_employees}")