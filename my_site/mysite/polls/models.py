from django.db import models

class Barrack(models.Model):
    """
    Represents a barrack which houses soldiers.
    """
    DESIGNATION_CHOICES = [
        ('O', 'Офицеры'),  # Officers
        ('S', 'Рядовые'),  # Soldiers
    ]
    number = models.CharField(max_length=10, verbose_name='Номер казармы')
    capacity = models.IntegerField(verbose_name='Вместительность')
    designation = models.CharField(
        max_length=1,
        choices=DESIGNATION_CHOICES,
        verbose_name='Назначение'
    )

    def __str__(self):
        return f'Казарма {self.number}'

class Weapon(models.Model):
    """
    Represents an issued weapon.
    """
    name = models.CharField(max_length=100, verbose_name='Название оружия')
    brand = models.CharField(max_length=100, verbose_name='Марка')
    serial_number = models.CharField(max_length=50, unique=True, verbose_name='Табельный номер')

    def __str__(self):
        return f'{self.name} ({self.serial_number})'

class Soldier(models.Model):
    """
    Represents a soldier with personal details and assignments.
    """
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    service_start_date = models.DateField(verbose_name='Дата начала службы')
    service_end_date = models.DateField(verbose_name='Дата окончания службы')
    barrack = models.ForeignKey(
        Barrack,
        on_delete=models.SET_NULL,  # Если казарма удалена, поле устанавливается в NULL
        null=True,
        verbose_name='Казарма'
    )
    weapon = models.ForeignKey(
        Weapon,
        on_delete=models.SET_NULL,  # Если оружие удалено, поле устанавливается в NULL
        null=True,
        verbose_name='Табельное оружие'
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'
