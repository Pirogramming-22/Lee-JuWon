from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=200)  
    release_year = models.IntegerField()      
    director = models.CharField(max_length=100, default="Unknown")  
    actors = models.CharField(max_length=300, default="Unknown")
    genre = models.CharField(max_length=100, default="Unknown")  
    rating = models.FloatField()              
    running_time = models.CharField(max_length=50, default="Unknown")  
    content = models.TextField()              
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title
