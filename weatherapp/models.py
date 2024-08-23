from django.db import models

# Create your models here.
class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    icon = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Weather in {self.city} on {self.date}"