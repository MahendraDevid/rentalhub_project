from django.db import models

# Create your models here.
class Mobil(models.Model):
    mobil_id = models.AutoField(primary_key=True)
    merek = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    tahun = models.IntegerField()
    STATUS_CHOICES = [
        ('Tersedia', 'Tersedia'),
        ('Sedang Disewa', 'Sedang Disewa'),
    ]
    status = models.CharField(max_length=13, choices=STATUS_CHOICES)

    class Meta:
        managed = False
        db_table = 'mobil'
