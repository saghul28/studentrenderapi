from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from firebase_admin import firestore
import  datetime

router = APIRouter()
store = firestore.client()

class Post(BaseModel):
    title: str
    content: str

# Create a blog post
@router.post("/posts")
async def create_post(post: Post):
    try:
        title = post.title
        content = post.content
        date = datetime.datetime.now()
        author = "Admin"  # Set a default author if no user information is required

        data = {"title": title, "content": content, "author": author}
        post_id = store.collection("Blogs").document().id  # Auto-generate a blog ID
        blog_ref = store.collection("Blogs").document(post_id)

        blog_ref.set(data)
        return {"message": "Blog post created successfully"}
    except Exception as e:
        return {"message": f"Error: {e}"}

# Get all blogs
@router.get("/blogs")
async def get_all_blogs():
    try:
        blogs_data = []
        blogs_ref = store.collection("Blogs")
        query_snapshot = blogs_ref.get()
        for doc in query_snapshot:
            blogs_data.append({"id": doc.id, **doc.to_dict()})

        return {"blogs": blogs_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")

# Get a blog by ID
@router.get("/blogs/{id}")
async def get_blog_by_id(id: str):
    try:
        blog_ref = store.collection("Blogs").document(id)
        doc = blog_ref.get()
        if doc.exists:
            return {"blog": doc.to_dict()}
        else:
            raise HTTPException(status_code=404, detail="Blog not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")

# Delete a blog by ID
@router.delete("/blogs/{id}")
async def delete_blog(id: str):
    try:
        blog_ref = store.collection("Blogs").document(id)
        blog_ref.delete()
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
        blog_ref = store.collection("Blogs").document(id)
        blog_ref.update(data)
        return {"message": "Blog post updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
