from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from comments.models import Comment


def index(request):
	# Main page with all posts
	items = Post.objects.all()
	return render(request, 'index.html', {'posts': items})


@login_required(login_url='login')
def post(request, post_id):
	item = get_object_or_404(Post, id=post_id)

	if request.method == 'POST':
		Comment.objects.create(
			post=item,
			author=request.user,
			content=request.POST['content']
		)
		return redirect('post', post_id=post_id)

	comments = item.comments.all()
	return render(request, 'post.html', {'post': item, 'comments': comments})


@login_required(login_url='login')
def add_post(request):
	# Add post
	if request.method == 'POST':
		Post.objects.create(
			author=request.user,
			title=request.POST['header'],
			content=request.POST['content']
		)
		messages.success(request, 'Post added successfully!')
		return redirect('index')

	return render(request, 'add_post.html')


@login_required(login_url='login')
def edit_post(request, post_id):
	# Edit post
	item = Post.objects.get(id=post_id)

	if request.method == 'POST':
		item.title = request.POST['header']
		item.content = request.POST['content']
		item.save()
		return redirect('post', post_id=post_id)

	return render(request, 'edit_post.html', {'post': item})
