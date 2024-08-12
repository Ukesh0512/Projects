from django.db import models
from django.conf import settings

settings.configure(
     DATABASES={
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'mysql_database',
             'USER': 'root',
             'PASSWORD': 'password',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
 )

class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

from django.db import connection
cursor = connection.cursor()
cursor.execute('CREATE TABLE employees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, salary DECIMAL(10, 2))')
employee = Employee(name='John Doe', age=30, salary=50000.00)
employee.save()
employees = Employee.objects.all()
for employee in employees:
    print(f"Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")
