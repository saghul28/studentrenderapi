from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import  datetime
from firebase_config import pyredb

import datetime
router = APIRouter()

store = pyredb


class Post(BaseModel):
    title: str
    content: str


# Create a blog post
@router.post("/posts")
async def create_post(post: Post):
    try:
        blog_data = {
             "title" : post.title,
        "content" : post.content,
        "date" : datetime.datetime.now().isoformat(),
        "author" : "Admin"  
        }
        try:
            store.child("Blogs").push(blog_data)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
            
        return {"message": "Blog post created successfully"}
    except Exception as e:
        return {"message": f"Error: {e}"}


# Get all blogs
@router.get("/blogs")
async def get_all_blogs():
    try:
        blogs_ref = store.child("Blogs")  
        blogs_data = blogs_ref.get().val()
        if not blogs_data:
            raise HTTPException(status_code=404,detail="No blog found")

        blog_list = []
        for blog_id,blog_info in blogs_data.items():
            blog_list.append({"id":blog_id,**blog_info})
        return {"blogs": blogs_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


# Get a blog by ID
@router.get("/blogs/{id}")
async def get_blog_by_id(id: str):
    try:
        blog_ref = store.child("Blogs").child(id)
        doc = blog_ref.get().val()
        if doc:
            return {"blog": doc}
        else:
            raise HTTPException(status_code=404, detail="Blog not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


# Delete a blog by ID
@router.delete("/blogs/{id}")
async def delete_blog(id: str):
    try:
        blog_ref = store.child("Blogs").child(id)
        blog_ref.remove()
        return {"message": "Blog post deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


# Update a blog post by ID
@router.patch("/blogs/{id}")
async def update_blog(post: Post, id: str):
    try:
        data = {
            "title": post.title,
            "content": post.content
        }
        blog_ref = store.child("Blogs").child(id)
        blog_ref.update(data)
        return {"message": "Blog post updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
