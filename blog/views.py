from django.shortcuts import render,redirect
from .forms import PostsForm
from .models import Posts
from .models import BlogPost


# TODO
# Create a django-admin user to help verify that the post is indeed created and added to the database.

# TODO
# Create a template folder and create_post.html file.

# TODO
# Create a post table. This will be in the form of a class in models.py

# TODO
# Create a Createform in forms.py which will be rendered out in the create_post.html.

# TODO 
# Write logic that will create the post.

# TODO
# Display the posts that have been created.

# This view creates a post
def create_post(request):
    if request.method == 'GET':
        form = PostsForm() #Why inherit from PostForm?
        #How are we getting the input from the form?

        #holder=request.GET.get("name_value", " ")
        
        #context = {'form':form}
        return render(request, "create_post.html", {'context':form}) #context=context)
    
    
    elif request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('create') #Where is create comming from?
        else:
            return render(request, "create_post.html")
    
    else:
        context={
            "information":"We need to add information to the page"
        }
        return render(request, "create_post.html", {"context":context})

# This view displays the posts from the database        
def display_posts(request):
    articles = Posts.objects.all()
    context = {'articles':articles}
    return render(request, "display_posts.html", context=context)






def index(request):
    index_post= BlogPost.objects.all()
    return render(request, 'index.html', {'blog_context':index_post})



def posts(request, pk):
    individual_post=BlogPost.objects.get(id=pk)
    return render(request, 'posts.html', {'post_context':individual_post})

"""
sugestion; only is the user has logged in with their credentials will they be able to write blog posts
and have them added to the site. 
We can use the index page to provide that feature...
"""
    


