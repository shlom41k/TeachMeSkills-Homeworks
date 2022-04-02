from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date


class MusicBand(models.Model):
    name = models.CharField(max_length=50, null=False,
                            verbose_name="Введите название группы",
                            help_text="Группа")

    year_of_release = models.IntegerField(verbose_name="Введите год основания",
                                          help_text="Год основания",
                                          validators=[MinValueValidator(1500), MaxValueValidator(date.today().year)])

    style = models.CharField(max_length=50, null=True,
                             verbose_name="Введите музыкальный стиль",
                             help_text="Стиль")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Album(models.Model):
    name = models.CharField(max_length=50, null=False,
                            verbose_name="Введите название альбома",
                            help_text="Альбом")

    year_of_release = models.IntegerField(verbose_name="Введите год выпуска",
                                          help_text="Год выпуска",
                                          validators=[MinValueValidator(1500), MaxValueValidator(date.today().year)])

    author = models.ForeignKey("MusicBand", null=True, on_delete=models.CASCADE, related_name="albums")

    def __str__(self):
        return f"{self.name} ({self.year_of_release})"

    def __repr__(self):
        return self.__str__()


class Track(models.Model):
    name = models.CharField(max_length=50, null=False,
                            verbose_name="Введите название композиции",
                            help_text="Трек")

    duration = models.IntegerField(verbose_name="Введите длительность композиции (сек.)",
                                   help_text="Длительность (сек.)",
                                   validators=[MinValueValidator(0)])

    album = models.ForeignKey("Album", null=True, on_delete=models.CASCADE, related_name="tracks")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
