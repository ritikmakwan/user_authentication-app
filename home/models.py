from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=20)
    number=models.IntegerField()
    img=models.ImageField(upload_to='pics')
    def __str__(self) -> str:
        return self.name