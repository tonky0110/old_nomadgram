from django.conf.urls import url
from . import views

urlpatterns = [
    # url 패턴은 3가지 타입(1. regular expression, 2. view, 3. name)
    url(
        regex=r'^all/$',
        view=views.ListAllImages.as_view(),
        name='all_images'
    )
]
