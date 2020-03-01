from remodel.models import Model
from schema import Schema, And, Use, Optional

class BaseModel(Model):
    schema = Schema({})

    def validate(self):
        try:
            self.schema.validate(self.fields.as_dict())
        except Exception as e:
            raise

    def before_save(self):
        self.validate()