from django.urls import re_path
import main.views as main

app_name = 'main'

urlpatterns = [
    re_path('$', main.index, name='index'),
    re_path('search/(?P<search>.*\s*)/$', main.search, name='search'),
    re_path('about/$', main.about, name='about'),
    re_path('postaddlike/$', main.post_add_like, name='post_add_like'),
    re_path('checkcomments/$', main.check_comments, name='check_comments')
]

