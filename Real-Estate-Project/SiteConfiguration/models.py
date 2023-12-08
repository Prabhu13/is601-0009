from django.db import models
from solo.models import SingletonModel
# Create your models here.


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=50, default='RealEstateSite')
    phone = models.CharField(max_length=20,default='201-920-9928')
    email = models.EmailField(max_length=50,default='py98@njit.edu')

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"