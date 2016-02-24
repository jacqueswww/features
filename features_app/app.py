from flask import Flask


def create_app():
    from features_app.db import db
    from features.features_views import features
 
    app = Flask(__name__, static_url_path='', static_folder='../frontend')
    app.register_blueprint(features, url_prefix='/api/v1/features')

    db.init_app(app)


    @app.route('/')
    def send_index():
        return app.send_static_file('index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
