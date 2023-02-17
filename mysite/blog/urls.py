from django.urls import path
from . import views

# Defines an application NAMESPACE with app_name variable.
# Allows you to organize URLS by application & use the name when referring to them.
app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('<int:id>/', views.post_detail, name='post_detail'),
    
    # creating seo-friendly URL
    # int path converter - year, month, day
    # slug path converter - post
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    
]


"""
You use angle brackets to capture the values from the URL.
Any value specified in the URL pattern as a <parameter> is captured as a string.
You use path converters, eg. <int: year>, to specifically match and return an integer.
"""