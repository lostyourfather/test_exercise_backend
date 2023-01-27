from fastapi import APIRouter
from api.schemas import books as books_schemas
from api.utils import books as books_utils


book_router = APIRouter()


"""
Books endpoints
"""


@book_router.get('/book', response_model=books_schemas.BookGet)
async def get_book(name=None, category_id=None, author_id=None):
    response = await books_utils.get_book(name, category_id, author_id)
    return response


@book_router.post('/book')
async def add_book(book: books_schemas.BookCreate):
    response = await books_utils.create_book(book)
    return response


@book_router.put('/book')
async def update_book(book: books_schemas.BookUpdate):
    response = await books_utils.update_book(book)
    return response


@book_router.delete('/book')
async def delete_book(book: books_schemas.BookGet):
    response = await books_utils.delete_book(book)
    return response


"""
Tags endpoints
"""


@book_router.get('/tag', response_model=list[books_schemas.TagGet])
async def get_tag(name):
    response = await books_utils.get_tag(name)
    return response


@book_router.post('/tag')
async def add_tag(tag: books_schemas.TagCreate):
    response = await books_utils.create_tag(tag)
    return response


@book_router.put('/tag')
async def update_tag(tag: books_schemas.TagUpdate):
    response = await books_utils.update_tag(tag)
    return response


@book_router.delete('/tag')
async def delete_tag(tag: books_schemas.TagGet):
    response = await books_utils.delete_tag(tag)
    return response


"""
Users endpoints
"""


@book_router.get('/user', response_model=list[books_schemas.UserGet])
async def get_user(name=None):
    response = await books_utils.get_user(name)
    return response


@book_router.post('/user')
async def add_user(user: books_schemas.UserCreate):
    response = await books_utils.create_user(user)
    return response


@book_router.put('/user')
async def update_user(user: books_schemas.UserUpdate):
    response = await books_utils.update_user(user)
    return response


@book_router.delete('/user')
async def delete_user(user: books_schemas.UserGet):
    response = await books_utils.delete_user(user)
    return response


"""
Categories endpoints
"""


@book_router.get('/category', response_model=list[books_schemas.CategoryGet])
async def get_category(category_name=None):
    response = await books_utils.get_category(category_name)
    return response


@book_router.post('/category')
async def add_category(category: books_schemas.CategoryCreate):
    response = await books_utils.create_category(category)
    return response


@book_router.put('/category')
async def update_category(category: books_schemas.CategoryUpdate):
    response = await books_utils.update_category(category)
    return response


@book_router.delete('/category')
async def delete_category(category: books_schemas.CategoryGet):
    response = await books_utils.delete_category(category)
    return response
