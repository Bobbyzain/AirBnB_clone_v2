#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan', backref="cities")
