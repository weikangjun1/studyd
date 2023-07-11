from django.db import models


# Create your models here.
class students(models.Model):
    name = models.CharField('姓名', max_length=12)
    sex = models.CharField('性别', max_length=2)
    address = models.CharField('地址', max_length=40)
    no = models.CharField('学号', max_length=10)

    class Meta:
        unique_together = ('name', 'sex', 'address')


class access(models.Model):
    create_timme = models.DateTimeField('创建时间',
                                        db_column='create_time',
                                        auto_now_add=True)
    no = models.CharField('学号', max_length=16)
    results = models.CharField('结果', max_length=8)


