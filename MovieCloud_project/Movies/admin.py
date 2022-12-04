from django.contrib import admin
from Movies.models import Movie,watch_links
# Register your models here.

#class MovieAdmin(admin.ModelAdmin):
    #list_display=['id','title','description','image','category','language','status','year_of_prod','views_count']

admin.site.register(Movie)
admin.site.register(watch_links)
