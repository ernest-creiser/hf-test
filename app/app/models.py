from django.db import models


class Platform(models.Model):
    name = models.TextField(primary_key=True)


class Studio(models.Model):
    name = models.TextField(primary_key=True)


class Game(models.Model):
    name = models.TextField(blank=False)
    release_date = models.DateField()
    studio = models.ForeignKey(Studio, on_delete=models.SET_NULL, null=True)
    ratings = models.IntegerField()
    platform = models.ManyToManyField(to=Platform, through="GamePlatform")


class GamePlatform(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
