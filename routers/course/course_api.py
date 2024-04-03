from fastapi import APIRouter ,HTTPException,status

from firebase_config import pyredb
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException
from googleapiclient.discovery import build
import os


router = APIRouter()

# Set up your YouTube Data API key and build the service
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")  # Replace with your own API key
print(YOUTUBE_API_KEY)
youtube_service = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)



@router.get("/youtube/{query}")
async def search_youtube(query: str):
    try:
        # Call the search.list method to retrieve search results based on the query
        search_response = youtube_service.search().list(
            q=query,
            part="snippet",
            maxResults=20
        ).execute()

        # Extract video IDs from search results
        video_ids = [item["id"]["videoId"] for item in search_response["items"] if item["id"]["kind"] == "youtube#video"]

        # Call the videos.list method to retrieve video details
        videos_response = youtube_service.videos().list(
            part="snippet,statistics",
            id=",".join(video_ids)
        ).execute()

        # Extract relevant information from video details
        videos = []
        for item in videos_response["items"]:
            video = {
                "title": item["snippet"]["title"],
                "description": item["snippet"]["description"],
                "thumbnail": item["snippet"]["thumbnails"]["default"]["url"],
                "views": item["statistics"].get("viewCount", 0),
                "likes": item["statistics"].get("likeCount", 0),
                "dislikes": item["statistics"].get("dislikeCount", 0),
            }
            videos.append(video)

        return JSONResponse({"videos": videos},status_code=status.HTTP_302_FOUND)
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while fetching YouTube data.")

