from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
import uuid

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Género de la película')

    def __str__(self):
        return self.name


class Cast(models.Model):
    name = models.CharField(
        max_length=200, help_text='Nombre completo de actor-actriz')

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=200, help_text='Idioma')

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=200)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    sinopsis = models.TextField(max_length=1000, help_text='Datos de la pelicula')
    genre = models.ManyToManyField(Genre, help_text='Genero de la pelicula')
    cast = models.ManyToManyField(Cast, help_text='Actor/Actriz principales')
    language = models.ManyToManyField(Language, help_text='Idiomas')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('film-detail', args=[str(self.id)])
    
    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])
    display_genre.short_description = 'Genre'

    def display_cast(sefl):
        return ','.join([cast.name for cast in sefl.cast.all()[:3]])
    display_cast.short_description = 'Cast'
    
class FilmInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Id unico de esta copia')
    film = models.ForeignKey(Film, on_delete=models.SET_NULL, null=True)
    release_date = models.DateField(null=True, blank=True)

    LOAD_STATUS = (
        ('c', 'En cartelera'),
        ('e', 'Estreno'), 
        ('s', 'Fuera de cartelera'),
        ('n', 'Comming soon')
    )

    status = models.CharField(max_length=1, choices=LOAD_STATUS, blank=True, default='s', help_text='Estado')

    PLACE_LOCATION = (
        ('a', 'Abasto'),
        ('p', 'Palermo'),
        ('r', 'Recoleta'),
        ('l', 'Lanus')
    )

    location = models.CharField(max_length=1, choices=PLACE_LOCATION, blank=True, default='a', help_text='Donde se proyecta el film')

    class Meta:
        ordering = ['release_date']

    def __str__(self):
        return f'{self.id} {self.film.title}'


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
    
    def get_absolute_url(self):
        return reverse('director-detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['last_name']