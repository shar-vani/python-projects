from django.shortcuts import render, redirect
from .models import *

def movie(request):

    if request.method == "POST":
        data = request.POST

        movie_name = data.get("movie_name")
        movie_review = data.get("movie_review")
        movie_img = request.FILES.get("movie_img")


        data_query = Movie.objects.create(movie_name=movie_name, movie_review=movie_review, movie_img=movie_img)


    query_set = Movie.objects.all()

    return render(request, "movie.html", context = {"movie":query_set}) #html

def update_movie(request, id):
    query_set = Movie.objects.get(id = id)
    
    if request.method == "POST":
         data = request.POST
         
         movie_name = data.get("movie_name")
         movie_review = data.get("movie_review")
         movie_img = request.FILES.get("movie_img")
         
         query_set.movie_name = movie_name
         query_set.movie_review = movie_review
         
         if movie_img:
             query_set.movie_img = movie_img
            
         query_set.save()
         return redirect('/movie/') #represent the movie function from the above repeats -- also shows html but processes is seen 
        
    context = {'movie': query_set}
        
        
    return render(request, 'update_movies.html', context)
        
    
def delete_movie(request, id):
    
    query_set = Movie.objects.get(id = id)
    query_set.delete()
    
    return redirect('/movie/')
    

# Create your views here.
