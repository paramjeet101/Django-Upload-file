from django.db import models

# Create your models here.
class Upload(models.Model):
    file = models.FileField(upload_to='csv_files/',blank=False,max_length=500)
    added_on=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.file.name
    
class Data(models.Model):
    name=models.CharField(max_length=100)
    domain=models.CharField(max_length=100)
    year_foundation=models.CharField(max_length=4)
    industry=models.CharField(max_length=80)
    sizerange=models.CharField(max_length=10)
    locality=models.CharField(max_length=60)
    country=models.CharField(max_length=60)
    linked_url=models.CharField(max_length=40)
    current_emp=models.CharField(max_length=10)
    total_emp=models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="All data"