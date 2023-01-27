from fastapi import FastAPI
from api.models.base import database
from api.routers.books import book_router


app = FastAPI()

queries = ["INSERT INTO public.user (name) VALUES ('user1'), ('user2'), ('user3'), ('user4'), ('user5');",
"INSERT INTO public.category (name) VALUES ('category1'), ('category2'), ('category3'), ('category4'), ('category5');",
"INSERT INTO public.book (name, category_id, author_id) VALUES ('book1', '1', '1'), ('book2', '2', '2'), ('book3', '3', '3');"]


@app.on_event("startup")
async def startup():
    await database.connect()
    for query in queries:
        await database.execute(query)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
async def get_main_page():
    return {"status": "200 OK"}


app.include_router(book_router)
