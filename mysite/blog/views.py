from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm


def post_list(request):
    post_list = Post.published.all()
    
    # PAGINATION with 3 posts per page
    # instantiates the Paginator class
    paginator = Paginator(post_list, 3)
    # retrieves the page GET HTTP parameter
    page_number = request.GET.get('page', 1)
    
    try:
        # obtains objects for desired page by calling page() method of paginator
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        """
        The paginator object throws an EmptyPage exception if the requested 
        page is out of range.
        """
        # If page_number is out of range, deliver last page of results.
        # The total number of pages is the same as the last page number.
        posts = paginator.page(paginator.num_pages)
        
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
    
def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, 
                             status=Post.Status.PUBLISHED)
    
    if request.method == 'POST':
        # Form was submitted
        # form instance created with submitted data (request.POST)
        form = EmailPostForm(request.POST)
        # validates data as per EmailPostForm specified constraints
        # returns True if form is valid, False otherwise
        # List of validation errors can be obtained with "form.errors"
        if form.is_valid():
            # retrieves validated data
            # "cleaned_data" attribute - dictionary of form fields w/ values
            # (cleaned_data contains only valid fields if form doesn't validate)
            cd = form.cleaned_data
            # ... send email
    else:
        # view receives GET request when page loads for 1st time
        form = EmailPostForm()
    
    return render(request, 'blog/post/share.html',
                  {'post': post, 'form': form})