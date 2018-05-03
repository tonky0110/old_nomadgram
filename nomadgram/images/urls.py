from django.conf.urls import url
from . import views

urlpatterns = [
    # url 패턴은 3가지 타입(1. regular expression, 2. view, 3. name)
    url(
        regex=r'^$',
        view=views.Feed.as_view(),
        name='feed'
    ),
]
