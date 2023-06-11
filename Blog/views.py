from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

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

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by = 5

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


    