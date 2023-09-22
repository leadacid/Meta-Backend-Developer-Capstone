from django.db import models

# Create your models here.


class MenuItem(models.Model):
    title = models.CharField(max_length=230)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
    

class TableBooking(models.Model):
    name =models.CharField(max_length=30)
    num_people=models.IntegerField()
    date = models.DateField()
    hour = models.TimeField()
