"""Rebuild  command, used util ebay api"""

from .base import Base
from categories.utils import api as api_soap

class Rebuild(Base):
    """Rebuild command!"""

    def run(self):
        from categories.database.models import Category, clear_db

        print('Rebuilding!')
        clear_db()
        api = api_soap.EbayAPI()
        categories = api.get_categories()

        for item in categories['GetCategoriesResponse']['CategoryArray']['Category']:
            category = Category.create(
                category_id=item.get('CategoryID', ''),
                category_name=item.get('CategoryName', ''),
                category_level=item.get('CategoryLevel', ''),
                category_parent_id=item.get('CategoryParentID', ''),
                best_offer_enabled=item.get('BestOfferEnabled', ''),
            )

        print("Were imported {0} items".format(Category.select().count()))
