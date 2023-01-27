from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)


class CategoryModel(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)


class TagModel(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)


class BookModel(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    category_id = Column(Integer, ForeignKey("category.id", ondelete="CASCADE"))
    author_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))


class TagBookModel(Base):
    __tablename__ = "tagBook"

    tag_id = Column(Integer, ForeignKey("tag.id", ondelete="CASCADE"), primary_key=True)
    book_id = Column(Integer, ForeignKey("book.id", ondelete="CASCADE"), primary_key=True)
