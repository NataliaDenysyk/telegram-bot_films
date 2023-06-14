from datetime import datetime
import peewee as pw


db = pw.SqliteDatabase('lecture.db')


class ModelBase(pw.Model):
    created_at = pw.DateField(default=datetime.now())

    class Meta():
        database = db


class History(ModelBase):
    """
    Создание модели в базе данных
    """
    id = pw.PrimaryKeyField(null=False)
    id_user = pw.IntegerField()
    genre = pw.TextField()
    message = pw.TextField()


with open('readme.md', 'w', encoding='utf-8') as file:
    result = 'class History\n' + History.__doc__
    file.write(result)

