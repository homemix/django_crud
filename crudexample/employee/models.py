from django.db import models


class Employee(models.Model):
    e_id = models.CharField(max_length=20)
    e_name = models.CharField(max_length=100)
    e_email = models.EmailField(max_length=20)
    e_contact = models.CharField(max_length=15)

    class Meta:
        db_table = "employee"
