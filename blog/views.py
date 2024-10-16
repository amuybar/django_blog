from django.shortcuts import render, redirect, get_object_or_404

from .models import Blog
from .forms import BlogForm

def blog_view(request):
    if request.method=='POST':
        form=BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('/')
    else:
        blogs = Blog.objects.all()
        form=BlogForm()

    return render(request,
                  'index.html',
                  {'blogs': blogs, 'form': form})
def update_blog(request,blog_id):
    blog=get_object_or_404(Blog,id=blog_id)
    if request.method=='POST':
        form=BlogForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=BlogForm(instance=blog)
    return render(request,
                  'update_blog.html',
                  {'form': form, 'blog': blog})

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')

    return render(request,
                  'confirm_delete.html',
                  {'blog': blog})