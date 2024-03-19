from django.db import models


class StudentAttendance(models.Model):
    name = models.CharField(max_length=100)
    standard = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=50)
    date = models.DateField()
    
    class Meta:
        managed = True
        db_table = 'sn_details'

    def __str__(self):
        return self.name
