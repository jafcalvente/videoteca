from django.shortcuts import get_object_or_404, get_list_or_404, redirect, render_to_response, RequestContext
from videoteca.models import Movie
from videoteca.forms import MovieForm
import urllib
import json
import codecs


URL_API = "http://www.omdbapi.com/?r=json&plot=full&t="

def home(request):
    """Vista de inicio."""
    return render_to_response('videoteca/home.html')

def list_movies(request):
    """Vista que lista las peliculas."""
    movie_list = Movie.objects.order_by('title')
    return render_to_response('videoteca/list_movies.html', {'movie_list': movie_list})

def consult_movie(request, movie_id):
    """Vista que consulta una pelicula mediante su identificador."""
    movie = get_object_or_404(Movie, pk=movie_id)
    return render_to_response('videoteca/consult_movie.html', {'movie': movie})

def create_movie(request):
    """Vista que introduce una nueva pelicula a la videoteca."""
    if request.method == 'POST':
        # Traemos la informacion
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_movies')
    else:
        # Todavia no se ha introducido la informacion
        form = MovieForm()

    return render_to_response('videoteca/create_movie.html', {'form': form},
                              context_instance=RequestContext(request))

def edit_movie(request, movie_id):
    """Actualiza la informacion de una pelicula de la videoteca."""
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        # Traemos la informacion actualizada
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('list_movies')
    else:
        # Todavia no se ha introducido la nueva informacion
        form = MovieForm(instance=movie)

    return render_to_response('videoteca/edit_movie.html',
                              {'form': form, 'movie_id': movie_id},
                              context_instance=RequestContext(request))

def delete_movie(request, movie_id):
    """Elimina una pelicula de la videoteca."""
    movie = get_object_or_404(Movie, pk=movie_id)
    Movie.delete(movie)
    movie_list = Movie.objects.order_by('title')
    return render_to_response('videoteca/list_movies.html', {'movie_list': movie_list})

def import_movie_details(request, movie_id):
    """Obtiene la informacion detallada de la pelicula a traves de la API de IMDB."""
    movie = get_object_or_404(Movie, pk=movie_id)
    movie = _get_movie_info_from_imdb(movie)
    movie.save()
    return render_to_response('videoteca/consult_movie.html', {'movie': movie})

def import_all_movies(request):
    """Obtiene la informacion detallada de todas las peliculas a traves de la API de IMDB."""
    movies = get_list_or_404(Movie)

    for movie in movies:
        new_movie = _get_movie_info_from_imdb(movie)
        new_movie.save()

    return redirect('list_movies')

def _get_movie_info_from_imdb(movie):

    # Se obtiene la informacion de la pelicula
    title = (URL_API + movie.original_title).replace(" ", "+")
    str_response = urllib.request.urlopen(title).read().decode("utf-8")

    # Se construye el objeto JSON
    json_info = json.loads(str_response)

    # Se incluye la nueva informacion en la pelicula
    try:
        movie.year = json_info['Year']
        movie.plot = json_info['Plot']
        movie.genre = json_info['Genre']
        movie.actors = json_info['Actors']
        movie.director = json_info['Director']
        movie.runtime = json_info['Runtime']
        movie.poster = json_info['Poster']
    except KeyError:
        pass

    return movie