from django.db import models

# Create your models here.
class UserInfo(models.Model):
    SINGLE_OR_MARRIED = (
        ('S', 'single'),
        ('M', 'married'),
    )
    zip_code = models.IntegerField(default=00000)
    salary = models.IntegerField(default=0)
    marital_status = models.CharField(max_length=1, choices=SINGLE_OR_MARRIED)

# abstract class inherited by state & federal brackets
class Brackets(models.Model):
    greater_than = models.IntegerField(default=0)
    last_bkt = models.IntegerField(default=0)
    init_tax = models.IntegerField(default=0)
    new_rate = models.IntegerField(default=0)

    class Meta:
        abstract = True

class State(Brackets):
    state_id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=30)

class Federal(Brackets):
    federal_id = models.CharField(primary_key=True, max_length=10)

# # join table for user & their tax bracket objects
class TaxInfo(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    federal = models.ForeignKey(Federal, on_delete=models.CASCADE)
    user_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
