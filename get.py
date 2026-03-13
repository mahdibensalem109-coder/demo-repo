from fastapi import FastAPI ,  Body , Response ,status  
from pydantic import BaseModel
import random 


app=FastAPI()

class post(BaseModel) :
    title : str
    content : str
    published : bool 

my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "favorite foods", "content": "I like pizza", "id": 2}
]

def find_post (id) : 
    for p in my_posts : 
        if p['id']==id :
            return p 
        return None
        
#def find_index_post(id) :
#    for i,p enumerate(my_posts) :
 #
 #       if p['id']==



@app.get("/posts/vote")
def root () :
    return {"message: welcome to api"}

@app.get("/")
def root () :
   return {"message : hello world"}

 
@app.post("/create")
def createposts (payload : dict = Body(...)) :
    print(payload)
    return {"new-posts": f"title {payload['title']} content: {payload['content']} "}

@app.post("/createposts/")
def createposts (payload : post) :
    payload_dict=payload.dict()
    print(payload_dict)
    payload_dict['id']=random.randrange(0,15555)
    my_posts.append(payload_dict)
    print(my_posts)
    return {"DATA : new_post"}
    
@app.get("/posts/{id}")
def get_post(id:int,response:Response) :

    post=find_post(id)
    print(post)
    if not post :
        response.status_code=status.HTTP
    return {"post_details":post}

@app.get("/posts/latetest ")
def get_latest_post () : 

    post=my_posts[len(my_posts)-1] 
    return{"detail":post}




