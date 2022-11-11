import uuid

from django.db import models
from django.urls import reverse


class Genre(models.Model):

    name = models.CharField(max_length=80, help_text="write de genre")

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    Director = models.ForeignKey('director', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=500, help_text="movie resume")
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def ge_absolute_url(self):
        return reverse ('movie-detail', args=[str(self.id)])

class MovieInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="id unic for this Movie")
    movie = models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('D','available'),
        ('N','not available'),
        ('R', 'reserved'),
        ('I', 'in comming'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='D',help_text="Movie available")


class Meta:
    ordering =["due-back"]

    def __str__(self):
        return '%s %s' % (self.id, self.movie.title)


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('director-detail',args=[str(self.id)])

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)







