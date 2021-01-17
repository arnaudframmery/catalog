from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from engine import Base


class Data(Base):
    """
    Store values of the different components of an article
    """

    __tablename__ = 'data'

    id = Column(Integer, primary_key=True)
    value = Column(String, nullable=False)
    component_id = Column(Integer, ForeignKey('component.id'), nullable=False)
    article_id = Column(Integer, ForeignKey('article.id'), nullable=False)

    component = relationship("Component", back_populates="data")
    article = relationship("Article", back_populates="data")

    def __repr__(self):
        return "<Data(value='%s')>" % self.value


class Article(Base):
    """
    Store articles from a catalog
    """

    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    catalog_id = Column(Integer, ForeignKey('catalog.id'), nullable=False)

    catalog = relationship("Catalog", back_populates="article")

    data = relationship(
        "Data", order_by=Data.id, back_populates="article", cascade="all, delete, delete-orphan"
    )

    def __repr__(self):
        return "<Article(title='%s')>" % self.title


class Component(Base):
    """
    Store the different common components of the article from a catalog
    """

    __tablename__ = 'component'

    id = Column(Integer, primary_key=True)
    label = Column(String, nullable=False)
    default = Column(String)
    is_sortable = Column(Boolean, default=False)
    catalog_id = Column(Integer, ForeignKey('catalog.id'), nullable=False)
    type_id = Column(Integer, ForeignKey('type.id'), nullable=False)

    catalog = relationship("Catalog", back_populates="component")
    type = relationship("Type", back_populates="component")

    data = relationship(
        "Data", order_by=Data.id, back_populates="component", cascade="all, delete, delete-orphan"
    )

    def __repr__(self):
        return "<Component(label='%s')>" % self.label


class Type(Base):
    """
    Store the possible types of the components
    """

    __tablename__ = 'type'

    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False)

    component = relationship(
        "Component", order_by=Component.id, back_populates="type", cascade="all, delete, delete-orphan"
    )

    def __repr__(self):
        return "<Type(code='%s')>" % self.code


class Catalog(Base):
    """
    Container of a set of similar articles with the same components
    """

    __tablename__ = 'catalog'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    theme = Column(String)

    article = relationship(
        "Article", order_by=Article.id, back_populates="catalog", cascade="all, delete, delete-orphan"
    )
    component = relationship(
        "Component", order_by=Component.id, back_populates="catalog", cascade="all, delete, delete-orphan"
    )

    def __repr__(self):
        return "<Catalog(name='%s', theme='%s')>" % (self.name, self.theme)
