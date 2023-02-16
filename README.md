# django4-blog-app

## Table of Contents

* [Create Project](#create-django-project)
* [Initial Database Migration](#apply-initial-database-migrations)
* [Running the Development Server](#running-the-development-server)
* [Create Application](#create-an-application)
* [Create Superuser](#create-a-superuser)
* [Create Objects](#create-objects)
* [Update Objects](#update-objects)
* [Retrieve Objects](#retrieve-objects)
* [filter() method](#use-filter)
* [exclude() method](#use-exclude)
* [order_by() method](#use-order_by)
* [Delete Objects](#delete-objects)
* [get_object_or_404() method](#use-get_object_or_404-shortcut)

## Create Django Project
<i>Command:</i>
> `django-admin startproject mysite`

## Apply Initial Database Migrations
To complete the project setup, you need to create the tables associated with the models of the default Django applications included in the INSTALLED_APPS setting.  
<i>Command:</i>
> `cd mysite`   
> `python3 manage.py migrate`

## Running the Development Server
<i>Command:</i> 
> `python3 manage.py runserver` 

* You should see a page stating that the project is successfully running.

## Create an Application
<i>Command:</i> 
> `python3 manage.py startapp blog`     

## Create a Superuser
<i>Command:</i> 
> `python3 manage.py createsuperuser`   

## Create Objects
Option 1:  
> `from django.contrib.auth.models import User`   
> `from blog.models import Post `   

> `user = User.objects.get(username='admin')`   

> **`post = Post(title='Hello Post', slug='hello-post', body='post body', author=user)`**   

> **`post.save()`** --> saves the Post object to the database

* **`get() method`** - retrieves a single object from the database & expects a result that matches the query.     
    * If no results are returned, will raise a `DoesNotExist exception`;    
    * if returns more than 1 result, will raise a `MultipleResultsException` exception.

Option 2: 
> **`Post.objects.create(title='Hello Post', slug='hello-post', body='post body', author=user)`**

* **`create() method`**- creates the object and persist it into the database in a single operation

## Update Objects   
> `post.title = 'New Title'`    
> `post.save()` --> updates the title of the post object

## Retrieve Objects 
Each Django model has at least one manager, & the default manager is called **`objects`**. You get a `QuerySet` object using your model manager.    

* Retrieve **SINGLE** object     
    > user = `User.objects.get(username='admin')`  

* Retrieve **ALL** objects    
    > all_posts = `Post.objects.all()`

## Use **filter()** 
Queries with field lookup methods are built using 2 underscores.
* Filter by single field
    > `Post.objects.filter(publish__year=2022)`

* Filter by multiple fields:
    > `Post.objects.filter(publish__year=2022, author__username='admin')`

## Use **exclude()**     
To exclude certain results from your QuerySet
> `Post.objects.filter(publish__year=2022).exclude(title__startswith('Why')`    

## Use **order_by()**    
Order results by different fields

* Retrieve all objects ordered by their title (ascending order)
> `Post.objects.order_by('title')`

* Indicate descending order with a `negative sign` prefix
> `Post.objects.order_by('-title')`

## Delete Objects   
> post = `Post.objects.get(id=1)`   

> **`post.delete()`**

* Deleting objects will also delete any dependent relationships for `ForeignKey` objects defined with `on_delete` set to `CASCADE`.


## Use **get_object_or_404()** shortcut
Retrieves the object that matches the given parameters or an HTTP 404 exception if no object is found.

> `from django.shortcuts import get_object_or_404`    

> post = **`get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)`**