from featues.models.feature import Feature


class FeatureQueries:

    @staticmethod
    def get_all():
        res = Feature.objects.all()

        return res
