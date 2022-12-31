from django.db import models

# Create your models here.


class Employee(models.Model):
    eid = models.CharField('آیدی', max_length=20)
    ename = models.CharField('نام', max_length=100)
    elname = models.CharField('نام خانوادگی', max_length=20)
    eemail = models.EmailField('ایمیل')
    econtact = models.CharField('شماره تماس', max_length=11)

    class Meta:
        db_table = 'employee'
        verbose_name = 'کارمند'
        verbose_name_plural = 'کارمندان'
