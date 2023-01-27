from api.models.base import database
from api.models.books import UserModel, CategoryModel, TagModel, TagBookModel, BookModel
from sqlalchemy import select, insert, update, delete
from sqlalchemy.dialects.postgresql import insert


async def get_user(name=None):
    query = select(UserModel)
    if name:
        query = query.where(UserModel.name == name)
    users = await database.fetch_all(query)
    result = [{"id": user[0], "name": user[1]} for user in users]
    return result


async def create_user(user_data):
    query = insert(UserModel).values(name=user_data.name)
    user = await database.execute(query)
    return {"id": user}


async def update_user(user_data):
    query = update(UserModel).where(UserModel.name == user_data.old_name).values(name=user_data.new_name)
    user = await database.execute(query)
    return {"id": user}


async def delete_user(user_data):
    query = delete(UserModel)
    if user_data.id:
        query = query.where(UserModel.id == user_data.id)
    if user_data.name:
        query = query.where(UserModel.name == user_data.name)
    user = await database.execute(query)
    return {"id": user}


async def get_category(name=None):
    query = select(CategoryModel)
    if name:
        query = query.where(CategoryModel.name == name)
    categories = await database.fetch_all(query)
    result = [{"id": category[0], "name": category[1]} for category in categories]
    return result


async def create_category(category_data):
    query = insert(CategoryModel).values(name=category_data.name)
    category = await database.execute(query)
    return {"id": category}


async def update_category(category_data):
    query = update(CategoryModel).where(CategoryModel.name == category_data.old_name).values(name=category_data.new_name)
    category = await database.execute(query)
    return {"id": category}


async def delete_category(category_data):
    query = delete(CategoryModel)
    if category_data.id:
        query = query.where(CategoryModel.id == category_data.id)
    if category_data.name:
        query = query.where(CategoryModel.name == category_data.name)
    category = await database.execute(query)
    return {"id": category}


async def get_tag(name=None):
    query = select(TagModel)
    if name:
        query = query.where(TagModel.name == name)
    tags = await database.fetch_all(query)
    result = [{"id": tag[0], "name": tag[1]} for tag in tags]
    return result


async def create_tag(tag_data):
    query = insert(TagModel).values(name=tag_data.name)
    tag = await database.execute(query)
    return {"id": tag}


async def update_tag(tag_data):
    query = update(TagModel).where(TagModel.name == tag_data.old_name).values(name=tag_data.new_name)
    tag = await database.execute(query)
    return {"id": tag}


async def delete_tag(tag_data):
    query = delete(TagModel)
    if tag_data.id:
        query = query.where(TagModel.id == tag_data.id)
    if tag_data.name:
        query = query.where(TagModel.name == tag_data.name)
    tag = await database.execute(query)
    return {"id": tag}


async def get_book(name=None, category_id=None, author_id=None):
    query = select(BookModel)
    if name:
        query = query.where(BookModel.name == name)
    if category_id:
        query = query.where(BookModel.category_id == category_id)
    if author_id:
        query = query.where(BookModel.author_id == author_id)
    books = await database.fetch_all(query)
    result = [{"id": book[0], "name": book[1],
               "category_id": book[2], "author_id": book[3]} for book in books]
    return result


async def create_book(book_data):
    user_name = book_data.author_name
    query = select(UserModel).where(UserModel.name == user_name)
    user = await database.execute(query)
    if not user:
        query = insert(UserModel).values(name=user_name)
        user = await database.execute(query)
    query = insert(BookModel).values(name=book_data.name, category_id=book_data.category_id, author_id=user)
    book = await database.execute(query)
    return {"id": book}


async def update_book(book_data):
    query = update(BookModel).where(BookModel.name == book_data.old_name).values(name=book_data.new_name)
    tag = await database.execute(query)
    return {"id": tag}


async def delete_book(book_data):
    query = delete(BookModel)
    if book_data.id:
        query = query.where(BookModel.id == book_data.id)
    if book_data.name:
        query = query.where(BookModel.name == book_data.name)
    tag = await database.execute(query)
    return {"id": tag}
