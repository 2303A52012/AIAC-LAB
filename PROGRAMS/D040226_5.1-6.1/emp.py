class Employee:
    def __init__(self, emp_id,emp_name,emp_designation, emp_salary,emp_experience):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_designation = emp_designation
        self.emp_salary = emp_salary
        self.emp_experience = emp_experience
    def display_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Designation: {self.emp_designation}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Experience: {self.emp_experience} years")
    def cal_allowance(self):
        if self.emp_experience >10:
            allowance = 0.20 * self.emp_salary
        elif 5<=self.emp_experience <=10:
            allowance = 0.10 * self.emp_salary
        else:
            allowance = 0.05 * self.emp_salary
        return allowance, self.emp_salary+ allowance
    
# Example usage
if __name__ == "__main__":
    emp1 = Employee(101, "Alice", "Manager", 80000, 12)
    emp2 = Employee(102, "Bob", "Developer", 60000, 7)
    emp3 = Employee(103, "Charlie", "Intern", 30000, 2)

    employees = [emp1, emp2, emp3]

    for emp in employees:
        emp.display_employee_details()
        allowance, salary = emp.cal_allowance()
        print(f"Allowance: {allowance}")
        print(f"Total Salary including Allowance: {salary + allowance}\n")
        
"""
Employee ID: 101
Employee Name: Alice
Employee Designation: Manager
Employee Salary: 80000
Employee Experience: 12 years
Allowance: 16000.0
Total Salary including Allowance: 112000.0

Employee ID: 102
Employee Name: Bob
Employee Designation: Developer
Employee Salary: 60000
Employee Experience: 7 years
Allowance: 6000.0
Total Salary including Allowance: 72000.0

Employee ID: 103
Employee Name: Charlie
Employee Designation: Intern
Employee Salary: 30000
Employee Experience: 2 years
Allowance: 1500.0
Total Salary including Allowance: 33000.0

"""