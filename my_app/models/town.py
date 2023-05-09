from django.db import models


class Town(models.Model):

    name = models.CharField("Название", max_length=50)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self) -> str:
        return self.name