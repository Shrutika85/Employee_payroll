import pymysql
import csv
from datetime import datetime

# Database connection
def connect_db():
    return pymysql.connect(host='localhost', user='root', password='yourpassword', database='payroll_db')

# Insert employee
def insert_employee():
    conn = connect_db()
    cursor = conn.cursor()
    name = input("Enter name: ")
    dept = input("Enter department: ")
    desig = input("Enter designation: ")
    salary = float(input("Enter salary: "))
    doj = input("Enter date of joining (YYYY-MM-DD): ")
    query = "INSERT INTO employee_payroll (name, department, designation, salary, doj) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (name, dept, desig, salary, doj))
    conn.commit()
    conn.close()
    print("✅ Employee added successfully.")

# Update employee
def update_employee():
    conn = connect_db()
    cursor = conn.cursor()
    emp_id = int(input("Enter employee ID to update: "))
    field = input("Which field to update (name, department, designation, salary, doj)? ")
    new_value = input(f"Enter new value for {field}: ")
    if field == 'salary':
        new_value = float(new_value)
    query = f"UPDATE employee_payroll SET {field} = %s WHERE emp_id = %s"
    cursor.execute(query, (new_value, emp_id))
    conn.commit()
    conn.close()
    print("🔄 Employee updated successfully.")

# Delete employee
def delete_employee():
    conn = connect_db()
    cursor = conn.cursor()
    emp_id = int(input("Enter employee ID to delete: "))
    query = "DELETE FROM employee_payroll WHERE emp_id = %s"
    cursor.execute(query, (emp_id,))
    conn.commit()
    conn.close()
    print("🗑️ Employee deleted successfully.")

# View all employees
def view_employees():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee_payroll")
    rows = cursor.fetchall()
    print("\n📋 Employee Records:")
    for row in rows:
        print(row)
    conn.close()

# Export to CSV
def export_to_csv():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee_payroll")
    rows = cursor.fetchall()
    with open('employee_payroll.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Emp ID', 'Name', 'Department', 'Designation', 'Salary', 'Date of Joining'])
        writer.writerows(rows)
    conn.close()
    print("📤 Data exported to employee_payroll.csv")

# Search by name
def search_by_name():
    conn = connect_db()
    cursor = conn.cursor()
    name = input("Enter name to search: ")
    query = "SELECT * FROM employee_payroll WHERE name LIKE %s"
    cursor.execute(query, ('%' + name + '%',))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Filter by salary range
def filter_by_salary():
    conn = connect_db()
    cursor = conn.cursor()
    min_salary = float(input("Enter minimum salary: "))
    max_salary = float(input("Enter maximum salary: "))
    query = "SELECT * FROM employee_payroll WHERE salary BETWEEN %s AND %s"
    cursor.execute(query, (min_salary, max_salary))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Menu
def menu():
    while True:
        print("\n📊 Employee Payroll Management System")
        print("1. Insert Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. View All Employees")
        print("5. Export to CSV")
        print("6. Search by Name")
        print("7. Filter by Salary Range")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            insert_employee()
        elif choice == '2':
            update_employee()
        elif choice == '3':
            delete_employee()
        elif choice == '4':
            view_employees()
        elif choice == '5':
            export_to_csv()
        elif choice == '6':
            search_by_name()
        elif choice == '7':
            filter_by_salary()
        elif choice == '8':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the app
if __name__ == "__main__":
    menu()
