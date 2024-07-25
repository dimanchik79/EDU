from config import *
from peewee import *

"""В модуле реализованы модели базы банных
   с помощью библиотеки PEEWEE"""

DB = PostgresqlDatabase(database=DB_NAME,
                        user=DB_USER,
                        password=DB_PASSWORD,
                        host=DB_HOST,
                        port=DB_PORT,)


class BaseModel(Model):
    class Meta:
        database = DB


class Users(BaseModel):
    id = IntegerField(primary_key=True)
    username = CharField(max_length=32)
    password = CharField(max_length=64)
    email = CharField(max_length=256)
    edu_name = CharField(max_length=256)
    director = CharField(max_length=256)
    location = TextField()
    code = IntegerField()
