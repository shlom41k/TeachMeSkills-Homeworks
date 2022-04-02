from django.db import models


# Create your models here.
class AnimalImage(models.Model):
    url = models.CharField(max_length=500,
                           help_text="Input image url here",
                           verbose_name="Image url",
                           null=False)

    type = models.CharField(max_length=3,
                            help_text="Input type of pet here",
                            verbose_name="Pet",
                            null=False)

    date_of_creating = models.DateTimeField(help_text="Input date of creating",
                                            verbose_name="Date",
                                            auto_now_add=True,
                                            null=True)

    pic_type = models.CharField(max_length=20,
                                help_text="Input picture format",
                                verbose_name="Format",
                                null=False,
                                default="")
