from django.db import models

# Create your models here.
from items.models import *


class build(models.Model):
    CPU = models.ForeignKey(CPU, on_delete=models.CASCADE, null=True)
    MB = models.ForeignKey(MB, on_delete=models.CASCADE, null=True)
    Ram = models.ForeignKey(Ram, on_delete=models.CASCADE, null=True)
    Storage = models.ForeignKey(Storage, on_delete=models.CASCADE, null=True)
    GPU = models.ForeignKey(GPU, on_delete=models.CASCADE, null=True)
    PSU = models.ForeignKey(PSU, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f" {self.CPU.model} {self.MB.model} {self.Ram.Capacity} {self.Storage.model} {self.GPU.model} {self.PSU.model}"

    class Meta:
        verbose_name = 'Сборка'
        verbose_name_plural = 'Сборки'