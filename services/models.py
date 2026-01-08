from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)  # Nome da trança (ex: Box Braids)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço
    duration_minutes = models.IntegerField()  # Tempo em minutos (ex: 180)

    def __str__(self):
        return self.name