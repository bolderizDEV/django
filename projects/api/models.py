from django.db import models


class Employee(models.Model):
    employee_id = models.IntegerField(null=False)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=25, null=False)
    email = models.CharField(max_length=25, null=False)
    phone_number = models.CharField(max_length=20)
    hire_date = models.DateField(null=False)
    job_id = models.CharField(max_length=10, null=False)
    salary = models.FloatField(max_length=8.2)
    commission_pct = models.FloatField(max_length=2.2)
    manager_id = models.IntegerField()
    department_id = models.IntegerField()

    def __str__(self):
        return str(self.employee_id) + '  ' + self.first_name + '  ' + self.last_name + '  ' + self.email

