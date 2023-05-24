from django.db import models
class Task(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField( auto_now_add=True)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.name
# Create your models here.
