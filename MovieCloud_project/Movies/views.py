from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.dates import YearArchiveView
from Movies.models import Movie,watch_links
from datetime import date
# Create your views here.

class HomeView(ListView):
    model=Movie
    template_name='Movies/home.html'
    
    def get_context_data(self, **kwargs):
        context=super(HomeView,self).get_context_data(**kwargs)
        context['top_rated']=Movie.objects.filter(status='TR')
        context['most_watched']=Movie.objects.filter(status='MW')
        context['recently_added']=Movie.objects.filter(status='RA')
        print(context)
        return context


class MovieList(ListView):
    model=Movie
    paginate_by=1
    #context_object_name: ''
    #template_name: 'movie_list.html'


class MovieDetail(DetailView):
    model=Movie
    
    def get_object(self):
        object=super(MovieDetail,self).get_object()
        object.views_count += 1
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context=super(MovieDetail,self).get_context_data(**kwargs)
        context['links']=watch_links.objects.filter(movie=self.get_object())
        context['related_movies']=Movie.objects.filter(category=self.get_object().category)#.order_by('created')[0:6]
        print(context)
        return context


class MovieCategory(ListView):
    model=Movie
    paginate_by=2
    
    def get_queryset(self):
        self.category=self.kwargs['category']
        return Movie.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context=super(MovieCategory,self).get_context_data(**kwargs)
        context['movie_category']=self.category
        
        return context


class MovieLanguage(ListView):
    model=Movie
    paginate_by=2
    
    def get_queryset(self):
        self.language=self.kwargs['lang']
        return Movie.objects.filter(language=self.language)

    def get_context_data(self, **kwargs):
        context=super(MovieLanguage,self).get_context_data(**kwargs)
        context['movie_language']=self.language
        
        return context


class MovieSearch(ListView):
    model=Movie
    paginate_by=1
    
    def get_queryset(self):
        query=self.request.GET.get('query')
        if query:
            object_list=self.model.objects.filter(title__icontains=query)
            print(query)
            print(object_list)
        else:
            object_list=self.model.objects.none()
        return object_list

class MovieYear(YearArchiveView):
    model=Movie
    queryset=Movie.objects.all()
    date_field='year_of_prod'
    make_object_list=True
    allow_future=True
    print(queryset)
    print(date_field)