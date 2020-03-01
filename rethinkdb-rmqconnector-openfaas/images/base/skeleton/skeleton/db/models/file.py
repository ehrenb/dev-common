"""RethinkDB models go here"""

from .base import BaseModel
from schema import Schema, And, Use, Optional

class File(BaseModel):
    schema = Schema({
        'fdata': str, # a string of base64 encoded file data
        Optional('md5'): str, # md5sum of the file data
        Optional('sha256'): str # sha256sum of the file data
    })