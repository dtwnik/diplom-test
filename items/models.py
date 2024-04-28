from django.db import models

# Create your models here.


class CPU(models.Model):
    CPU_TYPE = [
        ('APU', 'APU'),
        ('CPU', 'CPU'),
    ]
    model = models.CharField(max_length=255)
    series = models.CharField(max_length=255)
    socket = models.CharField(max_length=20)
    type = models.CharField(max_length=5, choices=CPU_TYPE, default='CPU')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'


class MB(models.Model):
    FORM_FACTOR = [
        ('Mini-ITX ', 'Mini-ITX '),
        ('Micro-ATX ', 'Micro-ATX '),
        ('ATX', 'ATX'),
        ('E-ATX', 'E-ATX')
    ]

    model = models.CharField(max_length=255)
    chipset = models.CharField(max_length=255)
    socket = models.CharField(max_length=255)
    DDR_Type = models.CharField(max_length=5, null=True)
    M2_sum = models.SmallIntegerField(null=True)
    form_factor = models.CharField(max_length=30,choices=FORM_FACTOR, default='ATX')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Материнская плата'
        verbose_name_plural = 'Материнские платы'


class Ram(models.Model):
    Mem_type = [
        ('DDR4','DDR4'),
        ('DDR5','DDR5')
    ]

    Mem_size = [
        ('8gb','8Гб (1x8Гб)'),
        ('16gbx1','16Гб (1x16Гб)'),
        ('16gbx2','16Гб (2x8Гб)'),
        ('32gbx1','32Гб (1x32Гб)'),
        ('32gbx2','32Гб (2x16Гб)'),
    ]

    model = models.CharField(max_length=255, null=True)
    Vendor = models.CharField(max_length=255, null=True)
    Type = models.CharField(max_length=25, choices=Mem_type, null=True)
    Freq = models.IntegerField()
    Capacity = models.CharField(max_length=20,choices=Mem_size, null=True)
    Timing = models.SmallIntegerField(null=True)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Оперативная память'
        verbose_name_plural = 'Оперативная память'


class Storage(models.Model):
    STORAGE_TYPE = [
        ('HDD','HDD'),
        ('SSD','SSD'),
        ('M2','M2'),
    ]
    model = models.CharField(max_length=255)
    Type = models.CharField(max_length=10, choices=STORAGE_TYPE)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Жесткий диск'
        verbose_name_plural = 'Жесткие диски'


class GPU(models.Model):
    model = models.CharField(max_length=255)
    recommend_psu = models.SmallIntegerField()

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Вмдеокарта'
        verbose_name_plural = 'Вмдеокарты'


class PSU(models.Model):
    model = models.CharField(max_length=255)
    power = models.SmallIntegerField()

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Блок питания'
        verbose_name_plural = 'Блоки питания'


