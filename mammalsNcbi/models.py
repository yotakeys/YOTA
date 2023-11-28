from django.db import models

# Create your models here.


class Mammals(models.Model):
    accession = models.CharField(max_length=255, primary_key=True)
    taxon_id = models.CharField(max_length=255, null=False)
    organism_name = models.CharField(max_length=255, null=False)
    common_name = models.CharField(max_length=255, null=True)
    url_download = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.organism_name

    class Meta:
        ordering = ['taxon_id']
