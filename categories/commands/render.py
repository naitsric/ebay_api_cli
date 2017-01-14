from .base import Base



class Render(Base):
    """Rebuild command!"""

    def run(self):
        from categories.database.models import Category
        import os
        import jinja2

        category_id = self.options.get("<category_id>", None)

        print('redering.. finding {0} in {1} items!'.format(category_id, Category.select().count()))

        loader = jinja2.PackageLoader('categories', 'templates')

        env = jinja2.Environment(
            loader=loader
        )
        template = env.get_template('template.html')
        try:
            category = Category.get(Category.category_id == category_id)
            categories = Category.select().where(Category.category_parent_id == category_id)
            output = template.render(**{'category': category, 'categories': categories})

            with open("{0}.html".format(category.category_id), 'w') as f:
                f.write(output)

        except Category.DoesNotExist:
            print("No category with ID: {0}".format(category_id))

