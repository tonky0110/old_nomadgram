# nomadgram

Cloning Instagram with Python Django and React / React Native


Http

Client: google.com/users/
Server: GET google.com/users/ => (look) => URL => View() 

Requests : 
    Header - get, post, put, delete
        {get host: google.com}
        {post host: google.com}
    body - 
        Cosume a resource => GET
        (가지고 오는것.)
        create a resource => POST
        Update a resource => PUT(POST 쓸수는 있음)
        Delete a resource => 서버에서 해당 resource를 삭제해달라고 요청
        {username: "nico", passwordL "****"}

Responses :  can use Method
    Header 
    body

REST API:
  --> Representational state transfer

API 규칙(query parameter of the url)
명사에 집중
NOUNS ARE GOOD : http request에서만 사용하고 url에서는 사용하지 않는다.
VERBS ARE BAD : 동사는 CRUD액션에서 발생.
※ CRUD: CREATE - POST, READ - GET, UPDATE - PUT, DELETE - DELETE


collection / element
집합       / 개별


ex)
collection
/dogs
DB        http
CREATE  / POST      ---> /dogs
READ    / GET       ---> /dogs
UPDATE  / PUT       ---> /dogs
DELETE  / DELETE    ---> /dogs

element
/dogs/kung
DB        http
UPDATE  / GET    --> /dogs/kung
CREATE  / POST   --> /dogs/kung (error 이미 존재함.)
UPDATE  / PUT    --> /dogs/kung (if kung exists update, if not error)
DELETE  / DELETE --> /dogs/kung



GET -> /dogs/search?color=brown

GET    /owners/nicolas/dogs -> List of all the dogs that Nicolas has.
POST   /owners/nicolas/dogs -> Create a dog for Nicolas
PUT    /owners/nicolas/dogs -> Update all of Licolas' dogs.
DELETE /owners/nicolas/dogs -> Bye bye :(

Nicolas가 주인인 갈색강아지
GET    /owners/nicolas/dogs/search?color=brown


버전이 바뀔 수 있기 때문에....
/v1/dogs/search?color=brown
/v2/dogs/search?color=brown


////
1-29
api는 json과 일함, frontend에서 json을 요청함.
시리얼라이저(erializers) - 
장고 rest framework의 시리얼라이저는 python object <--> json으로 변환
프론트엔드(react) - 동일.



1-36
Django: Backend

Get user feed
Like an image / Unlike an image
Comment on an image
Find people to follow on Explore
See profile with images
Get list of followers
Get list of following
search images by hashtag
Search User
Follow user / Unfollow user
See notifications
Create notification(for follow, comment and like)
Update profile
Delete a comment that I created
Delete a comment from my photos
Get single photo
Edit a photo
Delete a photo
Upload a photo
List photo likes
Log in with Facebook
log in
sign up 
change password
JWT Token Authentication

1-42)
RegEx: https://regex101.com
