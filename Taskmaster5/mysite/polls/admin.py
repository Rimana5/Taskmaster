from django.contrib import admin
from .models import Role, Expedition, Task, SubtaskDir, HeroDir, Subtask


# Регистрация новых моделей
admin.site.register(Role)
admin.site.register(Expedition)
admin.site.register(Task)
admin.site.register(SubtaskDir)
admin.site.register(HeroDir)
admin.site.register(Subtask)