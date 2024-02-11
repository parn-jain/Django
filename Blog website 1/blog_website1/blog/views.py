from datetime import date
from django.shortcuts import render
all_posts = [
    {
        "slug": "Loving-Vincent",
        "image": "LV.jpg",
        "author": "Parn Jain",
        "date": date(2024, 2, 11),
        "title": "Loving Vincent",
        "excerpt": "A complete hand-painted 94 minutes  movie , took 6+ years to make!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
    "slug":"puss-in-boots",
    "image": "puss_in_boots.jpg",
    "author": "Parn Jain",
    "date": date(2024,2,11),
    "title": "Puss in Boots",
    "excerpt": "A brilliant blend of 3D and hand-paint art, a masterpiece of 2.5D animation and storytelling", 
    "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "Spiderman-into-the-Spiderverse",
        "image": "SPM.jpg",
        "author": "Parn Jain",
        "date": date(2024, 2, 11),
        "title": "Spiderman into the Spiderverse",
        "excerpt": " Elevates animation with its revolutionary style, merging comic book artistry with cinematic brilliance to redefine the superhero genre.",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }

]


def get_date(post):
    return post['date']

# Create your views here.
def home(request):
    sorted_posts =sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request,"blog/index.html",{
        "posts": latest_posts
    })
def posts(request):
    return render(request,"blog/all-posts.html",{
        "all_posts":all_posts
    })
def post_details(request,slug):
    identified_post = next(post for post in all_posts if post['slug']==slug)
    return render(request, "blog/post-detail.html",{"post":identified_post})