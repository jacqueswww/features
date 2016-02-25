from product_areas.models.product_area import ProductArea


class ProductAreaQueries:

    def get_all():
        results = ProductArea.query.all()

        return results
