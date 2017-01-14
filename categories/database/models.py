from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase('ebay_api.db')

class BaseModel(Model):
    class Meta:
        database = db


class Category(BaseModel):
    category_id = CharField()
    category_name = CharField()
    category_level = CharField()
    category_parent_id = CharField()
    best_offer_enabled = CharField()

db.connect()

def clear_db():
    try:
        db.drop_tables([Category, ])
    except Exception as e:
        print(str(e))

    db.create_tables([Category, ])


try:
    db.create_tables([Category, ])
except Exception as e:
    pass
