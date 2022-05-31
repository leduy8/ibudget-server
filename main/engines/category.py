from typing import Dict, List

from main import db
from main.models.category import CategoryModel


def find_category_by_id(id: int) -> CategoryModel:
    return CategoryModel.query.get(id)


def find_category_by_name(name: str) -> CategoryModel:
    return CategoryModel.query.filter_by(name=name).first()


def create_category(data: Dict) -> CategoryModel:
    category = CategoryModel(
        name=data["name"], type=data["type"], icon_name=data["icon_name"]
    )

    db.session.add(category)
    db.session.commit()

    return category


def get_categories() -> List[object]:
    categories = CategoryModel.query.all()

    return [categories, len(categories)]
