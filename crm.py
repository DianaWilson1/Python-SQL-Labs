# terminal_crm.py

class Company:
    id_counter = 1
    def __init__(self, name):
        self.id = Company.id_counter
        Company.id_counter += 1
        self.name = name
        self.employees = []

    def __str__(self):
        return f"[{self.id}] {self.name} (Employees: {len(self.employees)})"

class Employee:
    id_counter = 1
    def __init__(self, name, company):
        self.id = Employee.id_counter
        Employee.id_counter += 1
        self.name = name
        self.company = company

    def __str__(self):
        return f"[{self.id}] {self.name} (Company: {self.company.name})"

class CRM:
    def __init__(self):
        self.companies = []
        self.employees = []

    def create_company(self):
        name = input("Enter company name: ")
        company = Company(name)
        self.companies.append(company)
        print(f"Company '{name}' created!\n")

    def list_companies(self):
        if not self.companies:
            print("No companies found.\n")
        else:
            for company in self.companies:
                print(company)
            print()

    def update_company(self):
        self.list_companies()
        company_id = int(input("Enter company ID to update: "))
        company = self.find_company(company_id)
        if company:
            new_name = input(f"Enter new name for '{company.name}': ")
            company.name = new_name
            print("Company updated!\n")
        else:
            print("Company not found.\n")

    def delete_company(self):
        self.list_companies()
        company_id = int(input("Enter company ID to delete: "))
        company = self.find_company(company_id)
        if company:
            self.companies.remove(company)
            # Remove employees of this company too
            self.employees = [e for e in self.employees if e.company != company]
            print("Company deleted!\n")
        else:
            print("Company not found.\n")

    def create_employee(self):
        self.list_companies()
        if not self.companies:
            print("No companies available. Create a company first.\n")
            return
        company_id = int(input("Enter employer company ID: "))
        company = self.find_company(company_id)
        if company:
            name = input("Enter employee name: ")
            employee = Employee(name, company)
            self.employees.append(employee)
            company.employees.append(employee)
            print(f"Employee '{name}' created!\n")
        else:
            print("Company not found.\n")

    def list_employees(self):
        if not self.employees:
            print("No employees found.\n")
        else:
            for employee in self.employees:
                print(employee)
            print()

    def update_employee(self):
        self.list_employees()
        employee_id = int(input("Enter employee ID to update: "))
        employee = self.find_employee(employee_id)
        if employee:
            new_name = input(f"Enter new name for '{employee.name}': ")
            employee.name = new_name
            print("Employee updated!\n")
        else:
            print("Employee not found.\n")

    def delete_employee(self):
        self.list_employees()
        employee_id = int(input("Enter employee ID to delete: "))
        employee = self.find_employee(employee_id)
        if employee:
            employee.company.employees.remove(employee)
            self.employees.remove(employee)
            print("Employee deleted!\n")
        else:
            print("Employee not found.\n")

    def find_company(self, company_id):
        for company in self.companies:
            if company.id == company_id:
                return company
        return None

    def find_employee(self, employee_id):
        for employee in self.employees:
            if employee.id == employee_id:
                return employee
        return None

    def main_menu(self):
        while True:
            print("=== CRM Menu ===")
            print("1. Create Company")
            print("2. List Companies")
            print("3. Update Company")
            print("4. Delete Company")
            print("5. Create Employee")
            print("6. List Employees")
            print("7. Update Employee")
            print("8. Delete Employee")
            print("9. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                self.create_company()
            elif choice == '2':
                self.list_companies()
            elif choice == '3':
                self.update_company()
            elif choice == '4':
                self.delete_company()
            elif choice == '5':
                self.create_employee()
            elif choice == '6':
                self.list_employees()
            elif choice == '7':
                self.update_employee()
            elif choice == '8':
                self.delete_employee()
            elif choice == '9':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    crm = CRM()
    crm.main_menu()
