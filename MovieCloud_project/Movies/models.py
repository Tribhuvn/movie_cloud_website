from django.db import models
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.

CATEGORY_CHOICE=(
    ('action','ACTION'),
    ('drama','DRAMA'),
    ('romance','ROMANCE'),
    ('comedy','COMEDY'),
)

LANGUAGE_CHOICE=(
    ('hindi','HINDI'),
    ('english','ENGLISH'),

)

STATUS_CHOICE=(
    ('RA','RECENTLY ADDED'),
    ('MW','MOST WATCHED'),
    ('TR','TOP RATED'),
)

class Movie(models.Model):
    title=models.CharField(max_length=100)
    discription=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='Movies')
    banner=models.ImageField(upload_to='Movies_banner')
    category=models.CharField(choices=CATEGORY_CHOICE,max_length=12)
    language=models.CharField(choices=LANGUAGE_CHOICE,max_length=10)
    status=models.CharField(choices=STATUS_CHOICE,max_length=2)
    cast=models.CharField(max_length=100)
    year_of_prod=models.DateField()
    views_count=models.IntegerField(default=0)
    movie_trailer=models.URLField()
    created=models.DateTimeField(default=timezone.now)
    
    

    slug=models.SlugField(blank=True,null=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Movie,self).save(*args,**kwargs)

    def __str__(self):
        return self.title



LINK_CHOICES=(
    ('D','Download'),
    ('W','Watch'),
    
)

class watch_links(models.Model):
    movie=models.ForeignKey(Movie,related_name="movie_watch_link",on_delete=models.CASCADE)
    type=models.CharField(choices=LINK_CHOICES,max_length=1)
    link=models.URLField()

    def __str__(self):
        return str(self.movie)

# class download_links(models.Model):
#     movie=models.ForeignKey(Movie,related_name="movie_watch_link",on_delete=models.CASCADE)
#     link=models.URLField()