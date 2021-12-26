from fastapi import APIRouter
from typing import Optional
from fastapi import FastAPI , status, Response
from enum import Enum

router = APIRouter(
    prefix = '/blog',
    tags = ['blog']
)

@router.get(
    '/all',
    summary = 'Retrieve all blogs',
    description='This api call simulates fetching all blogs.'
)

@router.get('/all')
def get_all_blogs(page = 1, page_size : Optional[int] = None):
    return {'message' : f'All {page_size} on page {page}'}

@router.get('/{id}/comments/{comment_id}', tags = ['comment'])
def get_comment(id: int, comment_id : int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog
    
    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter
    """
    
    return {'message' : f'blog_id ; {id}, comment_id {comment_id}, valid {valid}, username {username}'}
    

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'
    
@router.get('/type/{type}')
def get_blog_type(type:BlogType):
    return {'message' : f'Blog type {type}'}

#query parameters : page and page_size
#status code -> 우리의 요청에 따라서 status를 return 할 수가 있다.
@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id : int, response : Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error' : f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message' : f'Blog with id {id}'}