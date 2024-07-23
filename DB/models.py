from config import *
from peewee import *


"""В модуле реализованы модели базы банных
   с помощью библиотеки PEEWEE"""

DB = PostgresqlDatabase(database=DB_NAME,
                        user=USER_NAME,
                        password=PASSWORD,
                        host=HOST,
                        port=PORT,)


class BaseModel(Model):
    class Meta:
        database = DB


class Users(BaseModel):
    id = IntegerField(primary_key=True)
    username = CharField(max_length=256)
    password = CharField(max_length=64)
    email = CharField(max_length=512)
    edu_name = CharField(max_length=512)

