from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from homestay import db
from homestay import app
from homestay.models import models
import api
from script_insert_db import *

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def room_types():
    insert_room_types()


@manager.command
def bed_types():
    insert_bed_types()


@manager.command
def amenity_types():
    insert_amenity_types()


@manager.command
def amenities():
    insert_amenities()


@manager.command
def member():
    insert_member()


@manager.command
def property_type():
    insert_property_type()


@manager.command
def room():
    insert_room()


@manager.command
def images():
    insert_images()


@manager.command
def room_amenities():
    insert_room_amenities()


@manager.command
def price():
    insert_price()


if __name__ == '__main__':
    manager.run()
