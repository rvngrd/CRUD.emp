from django.db import models

# Create your models here.


class Employee(models.Model):
    eid = models.IntegerField('آیدی')
    ename = models.CharField('نام', max_length=100)
    elname = models.CharField('نام خانوادگی', max_length=20)
    eemail = models.EmailField('ایمیل')
    econtact = models.CharField('شماره تماس', max_length=11)

    class Meta:
        verbose_name = 'کارمند'
        verbose_name_plural = 'کارمندان'
