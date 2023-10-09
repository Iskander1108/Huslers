from django.shortcuts import get_object_or_404, render , redirect


from .models import Post, Comment
from .forms import CommentForm

# Create your views here.

def index(request):
    posts = Post.objects.all()

    context = {
        "posts": posts,
    }

    return render(request, "index.html", context )

def post_detail(request, post_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, id=post_id)
            comment.save()
            return redirect("card_post", post_id=post_id)
    else:
        form = CommentForm()


    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form
    }

    return render(request, "post_detail.html", context)





