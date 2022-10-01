from django.db import models
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Region(models.Model):
    iebc_region = models.CharField(max_length=200, null=False)

    def __repr__(self):
        return f"Region( '{self.id}', '{self.region_id}'"


class Pdfpath(models.Model):
    form_34_path = models.CharField(max_length=200, null=False)
    polling_station_code = models.CharField(max_length=900, null=False, editable=False)
    date_posted = models.DateTimeField(null=True, blank=False)
    iebc_region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __repr__(self):
        return f"Pdfpath( '{self.id}', '{self.form_34_path}', '{self.polling_station_code}')"
