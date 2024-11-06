from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import datetime
from firebase_config import firestoreDb

router = APIRouter()


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
        author = "Admin"  # Default author
        print(title)
        # Prepare the data
        data = {
            "title": title,
            "content": content,
            "author": author,
            "created_at": date,
            "updated_at": date
        }

        # Auto-generate a blog ID and firestoreDb the post
        blog_ref = firestoreDb.collection("Blogs").document().set(data)
        print(blog_ref)

        return {"message": "Blog post created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating blog post: {e}")

# Get all blogs
@router.get("/blogs")
async def get_all_blogs():
    try:
        blogs_data = []
        blogs_ref = firestoreDb.collection("Blogs")
        query_snapshot = blogs_ref.get()
        for doc in query_snapshot:
            blogs_data.append({"id": doc.id, **doc.to_dict()})

        return {"blogs": blogs_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving blogs: {e}")

# Get a blog by ID
@router.get("/blogs/{id}")
async def get_blog_by_id(id: str):
    try:
        blog_ref = firestoreDb.collection("Blogs").document(id)
        doc = blog_ref.get()
        if doc.exists:
            return {"blog": {"id": id, **doc.to_dict()}}
        else:
            raise HTTPException(status_code=404, detail="Blog not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving blog: {e}")

# Delete a blog by ID
@router.delete("/blogs/{id}")
async def delete_blog(id: str):
    try:
        blog_ref = firestoreDb.collection("Blogs").document(id)
        if not blog_ref.get().exists:
            raise HTTPException(status_code=404, detail="Blog not found")

        blog_ref.delete()
        return {"message": "Blog post deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting blog post: {e}")

# Update a blog post by ID
@router.patch("/blogs/{id}")
async def update_blog(post: Post, id: str):
    try:
        blog_ref = firestoreDb.collection("Blogs").document(id)
        if not blog_ref.get().exists:
            raise HTTPException(status_code=404, detail="Blog not found")

        data = {
            "title": post.title,
            "content": post.content,
            "updated_at": datetime.datetime.now()
        }
        blog_ref.update(data)
        return {"message": "Blog post updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating blog post: {e}")
