from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask.ext import login

from features_app.db import db
from features_app.admin_index_view import FAdminIndexView

from clients.models.client import Client
from users.models.user import User

admin = Admin(
    index_view=FAdminIndexView(),
    base_template='my_master.html'
    )

# Create customized model view class
class ProtectedModelView(ModelView):

    def is_accessible(self):
        if not login.current_user.is_active or not login.current_user.is_authenticated:
            return False

        if login.current_user.is_super:
            return True

        return False


admin.add_view(ProtectedModelView(Client, db.session))
admin.add_view(ProtectedModelView(User, db.session))
