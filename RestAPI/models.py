from django.db import models

class makanan(models.Model):
    nama = models.CharField(max_length = 50 )
    Daerah_asal = models.CharField(max_length = 50 )
    def __str__ (self):
        return self.nama

