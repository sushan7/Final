from django.db import models

# Create your models here.
class restoinfo(models.Model):
    resto_name = models.CharField(max_length=200)
    resto_review = models.CharField(max_length=3)
    resto_type = models.CharField(max_length=50)
    resto_detail = models.TextField(max_length=500)


    def __str__(self):
        return self.resto_name

class restoinfo_test(models.Model):
    resto_test = models.CharField(max_length=200)

    def __str__(self):
        return self.resto_test
