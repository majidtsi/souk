from django.db import models
from django.utils.translation import gettext_lazy as _

class Brand(models.Model):
    BRDName = models.CharField(max_length=40)
    BRDDesc = models.TextField(blank=True,null=True)

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")
    def __str__(self):
        return self.BRDName

class Variant(models.Model):
    VARName = models.CharField(max_length=40)
    VARDesc = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")

    def __str__(self):
        return self.VARName

