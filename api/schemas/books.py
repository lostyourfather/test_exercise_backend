from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str


class UserGet(BaseModel):
    id: int
    name: str


class UserUpdate(BaseModel):
    old_name: str
    new_name: str


class TagCreate(BaseModel):
    name: str


class TagGet(BaseModel):
    id: int
    name: str


class TagUpdate(BaseModel):
    old_name: str
    new_name: str


class CategoryCreate(BaseModel):
    name: str


class CategoryGet(BaseModel):
    id: int
    name: str


class CategoryUpdate(BaseModel):
    old_name: str
    new_name: str


class BookCreate(BaseModel):
    name: str
    category_id: int
    author_name: str


class BookGet(BaseModel):
    id: int
    name: str
    category_id: int
    author_id: int


class BookUpdate(BaseModel):
    old_name: str
    new_name: str
    old_category_id: int
    new_category_id: int
    old_author_id: int
    new_author_id: int
