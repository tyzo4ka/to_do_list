from django.db import models

STATUS_CHOICES = (
    ("new", "New"),
    ("in_progress", "In progress"),
    ("done", "Done")
)


class Task(models.Model):
    description = models.TextField(max_length=500, null=False, blank=False, verbose_name='Описание')
    detailed = models.TextField(max_length=3000, null=True, blank=True, default="", verbose_name="Подробнее")
    status = models.CharField(max_length=50, null=False, blank=True, default=STATUS_CHOICES[0][0],
                              choices=STATUS_CHOICES, verbose_name='Статус')
    complete_before = models.DateField(max_length=10, null=True, blank=True, default=None, verbose_name='Выполнить до')

    def __str__(self):
        return f"{self.description}"
