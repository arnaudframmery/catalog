from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from constant import DEFAULT_ROW_NUMBER, DEFAULT_COLUMN_NUMBER

Base = declarative_base()


class Value(Base):
    """
    Store values of the different components of an article
    """

    __tablename__ = 'value'

    id = Column(Integer, primary_key=True)
    value = Column(String, nullable=False)
    component_id = Column(Integer, ForeignKey('component.id'), nullable=False)
    article_id = Column(Integer, ForeignKey('article.id'), nullable=False)

    component = relationship("Component", back_populates="value")
    article = relationship("Article", back_populates="value")

    def __repr__(self):
        return "<Value(value='%s')>" % self.value


class Article(Base):
    """
    Store articles from a catalog
    """

    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    catalog_id = Column(Integer, ForeignKey('catalog.id'), nullable=False)

    catalog = relationship("Catalog", back_populates="article")

    value = relationship(
        "Value", order_by=Value.id, back_populates="article", cascade="all, delete, delete-orphan"
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
    filter_id = Column(Integer, ForeignKey('filter.id'), nullable=False)
    value_type_id = Column(Integer, ForeignKey('value_type.id'))
    # display settings
    from_row = Column(Integer)
    from_column = Column(Integer)
    row_span = Column(Integer, default=1)
    column_span = Column(Integer, default=1)

    catalog = relationship("Catalog", back_populates="component")
    filter = relationship("Filter", back_populates="component")
    value_type = relationship("ValueType", back_populates="component")

    value = relationship(
        "Value", order_by=Value.id, back_populates="component", cascade="all, delete, delete-orphan"
    )

    def __repr__(self):
        return "<Component(label='%s')>" % self.label


class Filter(Base):
    """
    Store the possible filters of the components
    """

    __tablename__ = 'filter'

    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False, unique=True)

    component = relationship(
        "Component", order_by=Component.id, back_populates="filter", cascade="all, delete, delete-orphan"
    )

    def __repr__(self):
        return "<Filter(code='%s')>" % self.code


class ValueType(Base):
    """
    Store the possible types for the values of a component
    """

    __tablename__ = 'value_type'

    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False, unique=True)

    component = relationship(
        "Component", order_by=Component.id, back_populates="value_type", cascade="all, delete, delete-orphan"
    )

    def __repr__(self):
        return "<ValueType(code='%s')>" % self.code


class Catalog(Base):
    """
    Container of a set of similar articles with the same components
    """

    __tablename__ = 'catalog'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    theme = Column(String)
    row_number = Column(Integer, default=DEFAULT_ROW_NUMBER)
    column_number = Column(Integer, default=DEFAULT_COLUMN_NUMBER)

    article = relationship(
        "Article", order_by=Article.id, back_populates="catalog", cascade="all, delete, delete-orphan"
    )
    component = relationship(
        "Component", order_by=Component.id, back_populates="catalog", cascade="all, delete, delete-orphan"
    )

    def __repr__(self):
        return "<Catalog(name='%s', theme='%s')>" % (self.name, self.theme)
