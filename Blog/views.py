from django.shortcuts import render
from .models import Post

# Create your views here.

# posts = [
#     {"author": "CoreyMS",
#      "title": "Blog Post 1",
#      "content": "First post content",
#      "date_posted": "August 27, 2021"
#     },
#     {"author": "Jane Doe",
#      "title": "Blog Post 2",
#      "content": "Second post content",
#      "date_posted": "August 28, 2021"
#     },
#     {"author": "John Doe",
#      "title": "Blog Post 3",
#      "content": "Third post content",
#      "date_posted": "August 29, 2021"
#      },
#     {"author": "John Doe",
#      "title": "Blog Post 4",
#      "content": "Fourth post content",
#      "date_posted": "August 30, 2021"
#     },
# ]

def home(request):
    context = {
        "posts": Post.objects.all() 
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

