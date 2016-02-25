import os

from flask import Flask,  render_template, redirect
from flask.ext.login import login_required, current_user
from werkzeug.security import generate_password_hash


def create_app():
    from features_app.db import db
    from features_app.admin import admin

    from features_app.login import login_manager
    from features.features_views import features
    from product_areas.product_areas_views import product_areas
    from clients.clients_views import clients
    from users.models.user import User

    app = Flask(__name__, static_url_path='', static_folder='../frontend', template_folder='../templates')
    app.config.from_object(os.environ.get('F_SETTINGS', 'features_app.settings.DevelopmentConfig'))

    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)

    app.register_blueprint(features, url_prefix='/api/v1/features')
    app.register_blueprint(product_areas, url_prefix='/api/v1/product_areas')
    app.register_blueprint(clients, url_prefix='/api/v1/clients')


    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)

    @app.before_first_request
    def create_tables():
        print('Creating tables...')
        db.create_all()

        if db.session.query(User).count() == 0:
            test_user = User()
            test_user.login="test_admin"
            test_user.password=generate_password_hash("test")
            test_user.is_super = True
            db.session.add(test_user)
            db.session.commit()


    @app.route('/')
    def home():
        if not current_user.is_authenticated:
            return redirect('/admin/login/')
        return app.send_static_file('index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
