from django.db import models

# Create your models here.

from django.db import models

class MathTest(models.Model):
    expression = models.CharField(max_length=255, verbose_name="Math Expression")
    answer = models.FloatField(verbose_name="Answer")

    def __str__(self):
        return f"{self.expression} = {self.answer}"
