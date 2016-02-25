from features.models.feature import Feature


class FeatureQueries:

    @staticmethod
    def get_all():
        res = Feature.query.all()

        return res

    @staticmethod
    def get_by_id(_id):
        res = Feature.query.get(_id)

        return res
