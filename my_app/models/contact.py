from django.db import models


class Contact(models.Model):

    phone = models.CharField("Номер телефона", max_length=12)
    additionalPhone = models.CharField("Дополнительный номер телефона", max_length=12)
    email = models.EmailField("Почта", max_length=50)
    working_mode = models.TextField("Режим работы")
    school = models.OneToOneField("my_app.school", on_delete=models.CASCADE, related_name="contact")
    image = models.ImageField(upload_to="images/")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self) -> str:
        return f"Контакты {self.school}"