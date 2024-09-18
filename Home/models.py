from django.db import models

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    dob = models.DateField()
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.first_name
