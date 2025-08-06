from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})

def post_detail(request, pk):
    post = Post.objects.get(id=pk) 
    return render(request, 'post_detail.html', {'post': post})  

def create(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('home')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    return render(request, "create.html", {"form": form})

def update(request, pk):
    post_obj = Post.objects.get(id=pk)
    form = PostForm(instance=post_obj)

    if request.method == 'POST':
        form = PostForm(instance=post_obj, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'update.html', {'form':form})

def delete(request, pk):
    post_obj = Post.objects.get(id=pk)
    post_obj.delete()
    return redirect('home')




