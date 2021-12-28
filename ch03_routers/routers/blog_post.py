from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional,List,Dict

router = APIRouter(
    prefix = '/blog',
    tags = ["blog"]
)

#custom subtype
class Image(BaseModel):
    ulr: str
    alias: str

#model to json이 가능함
#read request body as json
#data validation -> automatic
class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]
    
    #complex subtypes
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1' : 'val1'}
    image: Optional[Image] = None

@router.post('/new/{id}')
def create_blog(blog : BlogModel, id: int, version: int = 1):
    #data schema
    return {
        'id' : id,
        'data' : blog,
        'version': version
        }
    
#parameter metadata
#comment_id 파라메터에 대해서 Query로 metadata생성이 가능
@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int, 
                   comment_title: int = Query(None,
                                           title="Title of the comment",
                                           description='Some description for comment_title',
                                           alias="commentTitle",
                                           deprecated=True
                                           ),
                   #validata data passed to parameters
                   #default value, if not Body(...)
                   #set content length
                   #regular expression filtering
                   content: str = Body(... , min_length=10, max_length = 50, regex='^[a-z\s]*$'),
                   
                   #list type으로 multiple values 가능
                   #정적으로도 값 부여 가능 Query(['1.0','2.0'])
                   v: Optional[List[str]] =Query(None),
                   
                   #number validator
                   comment_id: int = Path(None, gt=5, le=10)
                   ):
    
    return {
        'blog':blog,
        'id': id,
        'comment_title': comment_title,
        'content' : content,
        'version': v
    }
    
