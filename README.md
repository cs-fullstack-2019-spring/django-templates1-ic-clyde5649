# Dajngo templates IC

Using the Computer model, build multiple template pages that handle 404

```
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Computer(models.Model):
    name = models.CharField(max_length=200, default="")
    cores = models.IntegerField(default=0)
    speed = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)


```
