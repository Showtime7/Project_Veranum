from django.db import models

class Promocion(models.Model):
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    discount = models.PositiveIntegerField()

    def __str__(self):
        return self.code
