#main app luokkamallit

from django.db import models
from django.contrib.auth.models import User

#Julkaisut luokkamalli
class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} liked {self.post.content[:20]}...'

#Kommentti luokka
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    #palauttaa käyttäjän nimen sekä kommentin ensimmäiset 20 merkkiä, ([:20] python syntaksin mukainen merkkijonon 'slicing').
    #self viittaa ks luokan olioon, jolloin voidaan tuoda luokka oliosta user, username sekä content
    #def __str__ on ns 'dunder metodi'
    def __str__(self):
        return f'{self.user.username} - {self.content[:20]}...'
    
#Tykkäys toiminnon luokkamalli    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.user.username} liked {self.post.content[:20]}...'
    

#ok    