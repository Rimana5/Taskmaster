from django.db import models
from django.utils import timezone

# Таблица roles
class Role(models.Model):
    role_id = models.AutoField(primary_key=True, verbose_name='ID роли')
    descr = models.CharField(max_length=50, verbose_name='Описание роли')

    def __str__(self):
        return self.descr

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


# Таблица users
class User(models.Model):
    user_id = models.AutoField(primary_key=True, verbose_name='ID пользователя')
    login = models.CharField(max_length=100, verbose_name='Логин')
    password = models.CharField(max_length=100, verbose_name='Пароль')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name='Роль', related_name='users')

    # Новые поля
    hero_1_cnt = models.IntegerField(default=0, verbose_name='Количество героев типа 1')
    hero_2_cnt = models.IntegerField(default=0, verbose_name='Количество героев типа 2')
    hero_3_cnt = models.IntegerField(default=0, verbose_name='Количество героев типа 3')
    hero_4_cnt = models.IntegerField(default=0, verbose_name='Количество героев типа 4')
    hero_5_cnt = models.IntegerField(default=0, verbose_name='Количество героев типа 5')
    hero_6_cnt = models.IntegerField(default=0, verbose_name='Количество героев типа 6')
    hero_7_cnt = models.IntegerField(default=0, verbose_name='Количество героев типа 7')
    hero_8_cnt = models.IntegerField(default=0, verbose_name='Количество героев типа 8')
    hero_9_cnt = models.IntegerField(default=0, verbose_name='Количество героев типа 9')
    manacost = models.IntegerField(default=0, verbose_name='Стоимость маны')
    date = models.DateField(default=timezone.now, verbose_name='Дата')

    def __str__(self):
        return f"User {self.user_id}: {self.login}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


# Таблица expeditions
class Expedition(models.Model):
    exp_id = models.AutoField(primary_key=True, verbose_name='ID экспедиции')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='expeditions')
    name = models.CharField(max_length=100, verbose_name='Название экспедиции')

    def __str__(self):
        return f"Expedition {self.exp_id}: {self.name}"

    class Meta:
        verbose_name = 'Экспедиция'
        verbose_name_plural = 'Экспедиции'


# Таблица tasks
class Task(models.Model):
    task_id = models.AutoField(primary_key=True, verbose_name='ID задачи')
    exp = models.ForeignKey(Expedition, on_delete=models.CASCADE, verbose_name='Экспедиция', related_name='tasks')
    name = models.CharField(max_length=100, verbose_name='Название задачи')

    def __str__(self):
        return f"Task {self.task_id}: {self.name}"

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


# Таблица subtasks_dir
class SubtaskDir(models.Model):
    TYPE_CHOICES = [
        ('Создание', 'Создание'),
        ('Изменение', 'Изменение'),
    ]
    LEVEL_CHOICES = [
        ('Простой', 'Простой'),
        ('Средний', 'Средний'),
        ('Сложный', 'Сложный'),
    ]

    subtaskdir_id = models.AutoField(primary_key=True, verbose_name='ID подзадачи (справочник)')
    name = models.CharField(max_length=100, verbose_name='Название подзадачи')
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name='Тип подзадачи')
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES, verbose_name='Уровень сложности')
    manacost = models.IntegerField(verbose_name='Стоимость маны')
    strategy = models.IntegerField(verbose_name='Стратегия')
    magic = models.IntegerField(verbose_name='Магия')
    fight = models.IntegerField(verbose_name='Бой')

    def __str__(self):
        return f"SubtaskDir {self.subtaskdir_id}: {self.name} ({self.type}, {self.level})"

    class Meta:
        verbose_name = 'Справочник подзадач'
        verbose_name_plural = 'Справочник подзадач'


# Таблица heroes_dir
class HeroDir(models.Model):
    HERO_ROLE_CHOICES = [
        ('Воин', 'Воин'),
        ('Маг', 'Маг'),
        ('Стратег', 'Стратег'),
    ]
    HERO_TYPE_CHOICES = [
        ('Простой', 'Простой'),
        ('Средний', 'Средний'),
        ('Сложный', 'Сложный'),
    ]

    hero_id = models.AutoField(primary_key=True, verbose_name='ID героя (справочник)')
    hero_type = models.CharField(max_length=50, choices=HERO_TYPE_CHOICES, verbose_name='Тип героя')
    hero_role = models.CharField(max_length=50, choices=HERO_ROLE_CHOICES, verbose_name='Роль героя')

    def __str__(self):
        return f"HeroDir {self.hero_id}: {self.hero_role} ({self.hero_type})"

    class Meta:
        verbose_name = 'Справочник героев'
        verbose_name_plural = 'Справочник героев'


# Таблица subtasks
class Subtask(models.Model):
    subtask_id = models.AutoField(primary_key=True, verbose_name='ID подзадачи')
    subtaskdir = models.ForeignKey(SubtaskDir, on_delete=models.CASCADE, verbose_name='Справочник подзадач', related_name='subtasks')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задача', related_name='subtasks')

    def __str__(self):
        return f"Subtask {self.subtask_id}: {self.subtaskdir.name} (Task {self.task.task_id})"

    class Meta:
        verbose_name = 'Подзадача'
        verbose_name_plural = 'Подзадачи'   