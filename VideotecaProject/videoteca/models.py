# encoding: utf-8

from django.db import models

class MovieType(models.Model):
    type = models.CharField(max_length=10, verbose_name='formato')

    def __str__(self):
        return self.type

class Movie(models.Model):
    title = models.CharField(max_length=25, verbose_name='título')
    original_title = models.CharField(max_length=25, verbose_name='título original')
    type = models.ForeignKey(MovieType, verbose_name='formato')
    year = models.IntegerField(verbose_name='año', null=True, blank=True)
    genre = models.CharField(max_length=25, verbose_name='genero', null=True, blank=True)
    actors = models.TextField(verbose_name='interpretes', null=True, blank=True)
    director = models.CharField(max_length=25, verbose_name='director', null=True, blank=True)
    runtime = models.CharField(max_length=25, verbose_name='duración', null=True, blank=True)
    plot = models.TextField(verbose_name='sinópsis', null=True, blank=True)
    poster = models.CharField(max_length=100, verbose_name='poster', null=True, blank=True)

    def __str__(self):
        return self.title
