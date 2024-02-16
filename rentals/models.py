from django.db import models
from cars.models import Mobil
from users.models import User

# Create your models here.
class Penyewaan(models.Model):
    penyewaan_id = models.AutoField(primary_key=True)
    mobil = models.ForeignKey(Mobil, models.DO_NOTHING, db_column='MobilID', related_name='penyewaan')
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID', related_name='penyewaan')
    tanggal_sewa = models.DateField(db_column='TanggalSewa')
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'penyewaan'
