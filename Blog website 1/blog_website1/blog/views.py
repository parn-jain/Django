from datetime import date
from django.shortcuts import render
from .models import Post , Author



def get_date(post):
    return post['date']

# Create your views here.
def home(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    # sorted_posts =sorted(all_posts,key=get_date)
    # latest_posts = sorted_posts[-3:]
    return render(request,"blog/index.html",{
        "posts": latest_posts
    })
def posts(request):
    return render(request,"blog/all-posts.html",{
        "all_posts":Post.objects.all()
    })
def post_details(request,slug):
    identified_post = next(post for post in Post.objects.all() if post.slug==slug)
    identify_author =  identified_post.author
    return render(request, "blog/post-detail.html",{"post":identified_post, 'author':identify_author})