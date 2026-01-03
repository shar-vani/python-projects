from django.db import models

# Create your models here.



class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    movie_review = models.TextField(max_length=50)
    movie_img = models.FileField(upload_to="movie/")

    
