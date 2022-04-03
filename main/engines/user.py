from typing import Dict

from main import db
from main.models.user import UserModel


def find_user_by_username(username: str) -> UserModel:
    return UserModel.query.filter_by(username=username).first()


def find_user_by_id(id: int) -> UserModel:
    return UserModel.query.get(id)


def create_user(data: Dict) -> UserModel:
    user = UserModel(
        username=data["username"],
        password_hash=data["password_hash"],
        password_salt=data["password_salt"],
        name=data["name"]
    )

    db.session.add(user)
    db.session.commit()

    return user


def update_user(data: Dict, user: UserModel) -> UserModel:
    user.name = data["name"]

    db.session.commit()

    return user
