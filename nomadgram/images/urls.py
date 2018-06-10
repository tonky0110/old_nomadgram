from django.conf.urls import url
from . import views

app_name = "images"
urlpatterns = [
    url(
        regex=r'^$', 
        view=views.Feed.as_view(), 
        name='feed'
    ),
    url(
        regex=r'(?P<image_id>[0-9]+)/like/', 
        view=views.LikeImage.as_view(), 
        name='like_image'
    ),
    url(
        regex=r'(?P<image_id>[0-9]+)/comment/', 
        view=views.CommentOnImage.as_view(), 
        name='comment_image'
    ),
]


# /images/3/like/

# 0 create the url and the view
# 1 take the id from the url
# 2 we want to find and image with this id
# 3 we want to create a like for that image

# 정규식 표현 : https://regex101.com