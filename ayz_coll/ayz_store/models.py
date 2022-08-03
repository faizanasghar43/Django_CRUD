from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=64, unique=False)
    cust_id = models.CharField(max_length=10, unique=True)


class Employee(models.Model):
    name = models.CharField(max_length=64, unique=False)
    salary = models.BigIntegerField()
    emp_id = models.CharField(max_length=10, unique=True)


class Order(models.Model):
    order_id = models.CharField(max_length=64, unique=True)
    assigned_to = models.ForeignKey(to=Employee, on_delete=models.CASCADE)
    given_by = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    bill = models.IntegerField(null=False)

