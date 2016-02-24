from flask import Flask


def create_app():
    from features_app.db import db
    from features.features_views import features

    from product_areas.product_areas_views import product_areas
    from clients.clients_views import clients

    app = Flask(__name__, static_url_path='', static_folder='../frontend')

    app.register_blueprint(features, url_prefix='/api/v1/features')
    app.register_blueprint(product_areas, url_prefix='/api/v1/product_areas')
    app.register_blueprint(clients, url_prefix='/api/v1/clients')

    db.init_app(app)


    @app.route('/')
    def send_index():
        return app.send_static_file('index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
