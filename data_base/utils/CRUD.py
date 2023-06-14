from typing import Dict, List, TypeVar
from peewee import ModelSelect

from data_base.common.models import ModelBase
from ..common.models import db


T = TypeVar('T')


def _store_data(i_db: db, model: T, *data: list[Dict]) -> None:
    with i_db.atomic():
        model.insert_many(*data).execute()


def _retrieve_all_data(i_db: db, model: T, *columns: ModelBase) -> ModelSelect:
    with i_db.atomic():
        response = model.select(*columns)

    return response


class CRUDInterface():
    @staticmethod
    def create():
        return _store_data

    @staticmethod
    def retrieve():
        return _retrieve_all_data


if __name__ == '__main__':
    _store_data()
    _retrieve_all_data()
    CRUDInterface()