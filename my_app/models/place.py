from django.db import models


class Place(models.Model):

    title = models.CharField("Название", max_length=120)
    description = models.TextField("Описание", null=True)
    city = models.ForeignKey("my_app.city", on_delete=models.CASCADE, related_name="city", verbose_name="Город")
    address = models.CharField("Адрес", max_length=300)
    categories = models.ForeignKey("my_app.category", verbose_name="Категории", on_delete=models.CASCADE, related_name="category")
    create_time = models.DateTimeField("Дата создания", auto_now_add=True)
    update_time = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Заведения"
        verbose_name_plural = "Заведении"

    def __str__(self) -> str:
        return self.title
