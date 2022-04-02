from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Comment(models.Model):
    firstname = models.CharField(max_length=70, default=None,
                                 verbose_name="Имя",
                                 help_text="Введите имя",
                                 null=False)

    lastname = models.CharField(max_length=70, default=None,
                                verbose_name="Фамилия",
                                help_text="Введите фамилию",
                                null=False)

    age = models.IntegerField(default=None,
                              verbose_name="Возраст",
                              help_text="Введите возраст",
                              validators=[MinValueValidator(16), MaxValueValidator(120)])

    test = models.CharField(max_length=1000, default="Some text",
                            verbose_name="Комментарий",
                            help_text="",
                            null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}, {self.age}: {self.test}"

    def __repr__(self):
        return self.__str__()
