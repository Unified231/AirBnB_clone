#!/usr/bin/python3
"""Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
"""Review class
Attributes:
place_id (string): place id
user_id (string): user id of reviewer
text (string): the review itself"""

place_id = ""
user_id = ""
text = ""
