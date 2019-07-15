class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print('Total Employee %d' % Employee.empCount)

    def displayEmployee(self):
        print('Name: ', self.name, ', Salary: ', self.salary)


emp1 = Employee('Mahima', 55000)
print('Total Employee :', Employee.empCount)
emp2 = Employee('Abhinn', 54000)
emp1.displayEmployee()
emp2.displayEmployee()
print('Total Employee %d' % Employee.empCount)
emp3 = Employee('Manu Gupta', 55500)
emp3.displayCount()
emp2.displayCount()
emp1.displayCount()
