from fastapi import APIRouter, Request, Body
from fastapi.responses import JSONResponse
import httpx

router = APIRouter(
    prefix="/jsonplaceholder",
)

API_BASE_URL = "https://jsonplaceholder.typicode.com"


def _query_string(request: Request) -> str:
    if not request.query_params:
        return ""
    return "?" + str(request.query_params)


# --- Posts ---

@router.get("/posts")
async def get_posts(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/posts{_query_string(request)}")
        return response.json()


@router.get("/posts/{post_id}")
async def get_post(post_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/posts/{post_id}")
        return response.json()


@router.get("/posts/{post_id}/comments")
async def get_post_comments(post_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/posts/{post_id}/comments")
        return response.json()


@router.post("/posts")
async def create_post(body: dict = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/posts", json=body)
        return response.json()


@router.put("/posts/{post_id}")
async def update_post(post_id: int, body: dict = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{API_BASE_URL}/posts/{post_id}", json=body)
        return response.json()


@router.patch("/posts/{post_id}")
async def patch_post(post_id: int, body: dict = Body(default={})):
    async with httpx.AsyncClient() as client:
        response = await client.patch(f"{API_BASE_URL}/posts/{post_id}", json=body)
        return response.json()


@router.delete("/posts/{post_id}")
async def delete_post(post_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{API_BASE_URL}/posts/{post_id}")
        return response.json()


# --- Comments ---

@router.get("/comments")
async def get_comments(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/comments{_query_string(request)}")
        return response.json()


@router.get("/comments/{comment_id}")
async def get_comment(comment_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/comments/{comment_id}")
        return response.json()


@router.post("/comments")
async def create_comment(body: dict = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/comments", json=body)
        return response.json()


@router.put("/comments/{comment_id}")
async def update_comment(comment_id: int, body: dict = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{API_BASE_URL}/comments/{comment_id}", json=body)
        return response.json()


@router.patch("/comments/{comment_id}")
async def patch_comment(comment_id: int, body: dict = Body(default={})):
    async with httpx.AsyncClient() as client:
        response = await client.patch(f"{API_BASE_URL}/comments/{comment_id}", json=body)
        return response.json()


@router.delete("/comments/{comment_id}")
async def delete_comment(comment_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{API_BASE_URL}/comments/{comment_id}")
        return response.json()


# --- Albums ---

@router.get("/albums")
async def get_albums(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/albums{_query_string(request)}")
        return response.json()


@router.get("/albums/{album_id}")
async def get_album(album_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/albums/{album_id}")
        return response.json()


@router.get("/albums/{album_id}/photos")
async def get_album_photos(album_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/albums/{album_id}/photos")
        return response.json()


@router.post("/albums")
async def create_album(body: dict = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/albums", json=body)
        return response.json()


@router.put("/albums/{album_id}")
async def update_album(album_id: int, body: dict = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{API_BASE_URL}/albums/{album_id}", json=body)
        return response.json()


@router.patch("/albums/{album_id}")
async def patch_album(album_id: int, body: dict = Body(default={})):
    async with httpx.AsyncClient() as client:
        response = await client.patch(f"{API_BASE_URL}/albums/{album_id}", json=body)
        return response.json()


@router.delete("/albums/{album_id}")
async def delete_album(album_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{API_BASE_URL}/albums/{album_id}")
        return response.json()


# --- Photos ---

@router.get("/photos")
async def get_photos(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/photos{_query_string(request)}")
        return response.json()


@router.get("/photos/{photo_id}")
async def get_photo(photo_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/photos/{photo_id}")
        return response.json()


@router.post("/photos")
async def create_photo(body: dict = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/photos", json=body)
        return response.json()


@router.put("/photos/{photo_id}")
async def update_photo(photo_id: int, body: dict = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{API_BASE_URL}/photos/{photo_id}", json=body)
        return response.json()


@router.patch("/photos/{photo_id}")
async def patch_photo(photo_id: int, body: dict = Body(default={})):
    async with httpx.AsyncClient() as client:
        response = await client.patch(f"{API_BASE_URL}/photos/{photo_id}", json=body)
        return response.json()


@router.delete("/photos/{photo_id}")
async def delete_photo(photo_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{API_BASE_URL}/photos/{photo_id}")
        return response.json()


# --- Todos ---

@router.get("/todos")
async def get_todos(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/todos{_query_string(request)}")
        return response.json()


@router.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/todos/{todo_id}")
        return response.json()


@router.post("/todos")
async def create_todo(body: dict = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/todos", json=body)
        return response.json()


@router.put("/todos/{todo_id}")
async def update_todo(todo_id: int, body: dict = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{API_BASE_URL}/todos/{todo_id}", json=body)
        return response.json()


@router.patch("/todos/{todo_id}")
async def patch_todo(todo_id: int, body: dict = Body(default={})):
    async with httpx.AsyncClient() as client:
        response = await client.patch(f"{API_BASE_URL}/todos/{todo_id}", json=body)
        return response.json()


@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{API_BASE_URL}/todos/{todo_id}")
        return response.json()


# --- Users ---

@router.get("/users")
async def get_users(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/users{_query_string(request)}")
        return response.json()


@router.get("/users/{user_id}")
async def get_user(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/users/{user_id}")
        return response.json()


@router.get("/users/{user_id}/posts")
async def get_user_posts(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/users/{user_id}/posts")
        return response.json()


@router.get("/users/{user_id}/albums")
async def get_user_albums(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/users/{user_id}/albums")
        return response.json()


@router.get("/users/{user_id}/todos")
async def get_user_todos(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/users/{user_id}/todos")
        return response.json()


@router.post("/users")
async def create_user(body: dict = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/users", json=body)
        return response.json()


@router.put("/users/{user_id}")
async def update_user(user_id: int, body: dict = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{API_BASE_URL}/users/{user_id}", json=body)
        return response.json()


@router.patch("/users/{user_id}")
async def patch_user(user_id: int, body: dict = Body(default={})):
    async with httpx.AsyncClient() as client:
        response = await client.patch(f"{API_BASE_URL}/users/{user_id}", json=body)
        return response.json()


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{API_BASE_URL}/users/{user_id}")
        return response.json()
