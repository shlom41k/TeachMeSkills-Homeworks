from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class NatureImage(models.Model):

    link = models.CharField(max_length=500,
                            verbose_name="Link",
                            help_text="Input image link",
                            null=False)

    height = models.IntegerField(verbose_name="Height",
                                 help_text="Input picture height",
                                 null=False,
                                 default=480,
                                 validators=[MinValueValidator(0)])

    weight = models.IntegerField(verbose_name="Weight",
                                 help_text="Input picture weight",
                                 null=False,
                                 default=640,
                                 validators=[MinValueValidator(0)])

    comment = models.CharField(max_length=200,
                               verbose_name="Comment",
                               help_text="Input comment to picture",
                               null=True,
                               default="Nature image")
