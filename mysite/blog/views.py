from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator


def post_list(request):
    post_list = Post.published.all()
    
    # Pagination with 3 posts per page
    # instantiates the Paginator class
    paginator = Paginator(post_list, 3)
    # retrieves the page GET HTTP parameter
    page_number = request.GET.get('page', 1)
    # obtains the objects for desired page by calling page() method of paginator
    posts = paginator.page(page_number)
    
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

def post_detail(request, year, month, day, post):
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("Post does not exist")
    
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})