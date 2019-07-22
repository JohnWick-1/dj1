from django.db import models

# Create your models here.
class Country(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    landmark = models.CharField(max_length=30)
    pincode = models.IntegerField()

    class Meta:
        db_table = "country_Info"
