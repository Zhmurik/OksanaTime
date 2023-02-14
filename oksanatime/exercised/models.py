from django.db import models


class Exercise(models.Model):
    name_of_exercise = models.CharField(max_length=200, verbose_name='Название упражнения')
    description_exercise = models.CharField(max_length=400, verbose_name='Описание')
    # video =
    # sport_equipment =

    def __str__(self):
        return self.name_of_exercise

    class Meta:
        verbose_name_plural = 'Упражнения'
        verbose_name = 'Упражнение'


class Equipment(models.Model):
    name_equipment = models.CharField(max_length=100, verbose_name='Инвентарь')

    def __str__(self):
        return self.name_equipment

    class Meta:
        verbose_name_plural = 'Инвентарь'
        verbose_name = 'Инвентарь'



# class Training(models.Model):
#     exersised = models.CharField
#     how_many_times = models.CharField
#     weight = models.IntegerField
#     type = models.TextField
