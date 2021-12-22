#path parameters
from typing import Optional
from fastapi import FastAPI , status, Response
from enum import Enum

from starlette.responses import Response

app = FastAPI()

@app.get('/hello')
def index():
    return "Hello World!"

# @app.get('/blog/all')
# def get_all_blogs():
#     return {'message' : 'All blogs provided'}

@app.get('/blog/all')
def get_all_blogs(page = 1, page_size : Optional[int] = None):
    return {'message' : f'All {page_size} on page {page}'}

@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id : int, valid: bool = True, username: Optional[str] = None):
    return {'message' : f'blog_id ; {id}, comment_id {comment_id}, valid {valid}, username {username}'}
    

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'
    
@app.get('/blog/type/{type}')
def get_blog_type(type:BlogType):
    return {'message' : f'Blog type {type}'}

#query parameters : page and page_size
#status code -> 우리의 요청에 따라서 status를 return 할 수가 있다.
@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_blog(id : int, response : Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error' : f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message' : f'Blog with id {id}'}

