from django.conf.urls import url
from . import views

urlpatterns = [
    # url 패턴은 3가지 타입(1. regular expression, 2. view, 3. name)
    url(
        regex=r'^$',
        view=views.Feed.as_view(),
        name='feed'
    ),
    url(
        regex=r'(?P<image_id>\w+)/like/',
        view=views.LikeImage.as_view(),
        name='like_image'
    )
]



# /images/3/like/

# 0. cate the url and the view
# 1. take the id from the url
# 2. we want to find an image with this id
# 3. we want to create a like form that image