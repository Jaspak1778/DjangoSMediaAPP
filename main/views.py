#main/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from .views import Post, Comment, Like
from .forms import PostForm, CommentForm, UsernameChangeForm


#Luo tunnukset funktio
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, 'signup.html', context)


#Kirjaudu funktio
def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('feed')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'login.html', context)


#Uloskirjautuminen
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


#syöte näkymä, eri kirjautuneelle sekä uloskirjautuneelle
def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts': posts}
    template = 'feed.html' if request.user.is_authenticated else 'guest_feed.html'
    return render(request, template, context)


#Luo julkaisu
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('feed')
    else:
        form = PostForm()
    context = {'form':form}    
    return render(request, 'post_create.html', context)


#Julkaisun poisto
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)
    post.delete()
    return redirect('feed')


#Kommentointi
@login_required
def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method  == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('feed')
    else:
        form = CommentForm()
    context = {'form':form, 'post':post}    
    return render(request, 'comment_create.html', context)


#Kommentin poisto
@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    comment.delete()
    return redirect('feed')


#Tykkäys toiminto
@login_required
def like(request, username):
    post = get_object_or_404(User, username=username)
    like_obj, created = Like.objects.get_or_create(user=request.user, post = post)
    if not created:
        like_obj.delete()
    like_count = Like.objects.filter(post=post).count()
    return redirect('feed')


#Käyttäjän profili näkymä
def user_profile(request, username):
    user = get_object_or_404(User, username= username)
    posts =  Post.objects.filter(user=user)
    likes = Like.objects.filter(user=user)
    context = {
        'profile_user' : user,
        'posts' : posts,
        'likes' : likes,
    }
    return render(request, 'user_profile.html', context)


#Profiilin katselu 'vieraana'
def guest_profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user = user)
    context = {'profile_user': user,  'posts': posts}
    return render(request, 'guest_profile.html', context)


#Käyttäjä nimen vaihto
@login_required
def change_username(request):
    if request.method == 'POST':
        form = UsernameChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.succes(request, 'Käyttäjänimi vaihdettu.')
            return redirect('user_profile', user.username)
    else:
        form = UsernameChangeForm(instance=request.user)
    context = {'form': form}    
    return render(request, 'change_username.html', context)


#käyttäjien haku
def search_users(request):
    query = request.GET.get('q',' ')
    users = User.objects.filter(
        Q(username__icontains=query) |
        Q(first_name__icontains=query) |
        Q(last_name__icontains=query)
    )
    context = {'users': users, 'query': query}
    return render(request, 'search_users.html', context)



#ok