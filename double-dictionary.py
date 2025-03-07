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

