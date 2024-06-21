from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField( auto_now_add= True)
    banner = models.ImageField(default="fallback.png", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.title
    
# Use py manage.py migrate to migrate the model or apply to db
# Use py manage.py makemigrations to post the migration

# ORM stand of Object Relational Mapping
# Way to insert select data using orm 
# from posts.models import Post
# >>> p = Post()
# >>> p.title = "My first post!"
# >>> p.save()
# >>> Post.object.all()
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: type object 'Post' has no attribute 'object'. Did you mean: 'objects'?
# >>> Post.objects.all() 
# <QuerySet [<Post: Post object (1)>]>
# Use py manage.py createsuperuser we use it to create user for Django admin panel