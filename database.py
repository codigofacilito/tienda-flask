from peewee import *
from decouple import config

import datetime

db = MySQLDatabase(
    'tienda',
    user='root',
    password=config('DBPASSWORD'),
    port=3306,
    host='localhost'
)


class User(Model): # Tablas
    email = TextField()
    password = TextField() # 
    created_at = DateTimeField(default=datetime.datetime.now) # 
    
    class Meta:
        database = db
        db_table = 'users'


    @classmethod
    def create_user(cls, _email, _password):
        # Validar que el correo sea único.
        # Nuestro algoritmo de encrypt
        _password = 'cody_' + _password
        return User.create(email=_email, password=_password)
        
# Migrations
class Product(Model): # Tablas
    name = TextField()
    price = IntegerField() # 
    user = ForeignKeyField(User, backref='products')
    created_at = DateTimeField(default=datetime.datetime.now) # 
    
    
    @property
    def price_format(self):
        return f"$ {self.price // 100} dólares"
    
    class Meta:
        database = db
        db_table = 'products'


db.create_tables( [User, Product] )