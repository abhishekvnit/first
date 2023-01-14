from django.db import models

# Create your models here.

from django.db import models


class TalcherDirect(models.Model):
    id = models.AutoField(db_column='ID', primary_key='True')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    activity = models.TextField(db_column='Activity', blank=True, null=True)  # Field name made lowercase.
    start = models.DateTimeField(db_column='Start', blank=True, null=True)  # Field name made lowercase.
    finish = models.DateTimeField(db_column='Finish', blank=True, null=True)  # Field name made lowercase.
    pgma = models.TextField(db_column='PGMA', blank=True, null=True)  # Field name made lowercase.
    system = models.TextField(db_column='System', blank=True, null=True)  # Field name made lowercase.
    mu = models.TextField(db_column='MU', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'talcher direct'