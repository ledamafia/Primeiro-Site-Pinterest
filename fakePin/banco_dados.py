from fakePin import database, app
from fakePin.models import Usuario, Foto


with app.app_context():
    database.create_all()