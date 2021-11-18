from django.db import models

class upload(models.Model):
    foto_receita=models.ImageField(upload_to='fotos/%d/%m/%Y',blank=True, null=True, default='0')
 

