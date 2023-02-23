from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Blog
from .forms import CommentForm

# Create your views here.

def blog(request):
    blog = Blog.objects.filter(status = Blog.ACTIVE)
    return render(request,'blog/blog.html',{'blog':blog})


def detail(request,slug):
    details = get_object_or_404(Blog,slug = slug,status = Blog.ACTIVE)
    

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = details
            comment.save()

            return redirect('detail', slug = slug)         

    else:
        form = CommentForm()

    return render(request,'blog/blog_detail.html',{'details':details, 'form':form})
