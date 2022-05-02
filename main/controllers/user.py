from flask import jsonify

from main import app
from main.commons.decorators import authenticate_user, pass_data
from main.commons.exceptions import BadRequest
from main.engines import user as user_engine
from main.libs.jwt import create_access_token
from main.libs.password import gen_salt, generate_password_hash
from main.schemas.dump.user import DumpUserSchema
from main.schemas.load.user import (
    LoadUserChangePasswordSchema,
    LoadUserSchema,
    LoadUserUpdateSchema,
)


@app.post("/users")
@pass_data(LoadUserSchema)
def register_user(data):
    if user_engine.find_user_by_username(data["username"]):
        raise BadRequest(error_message="Username is already registered")

    data["password_salt"] = gen_salt()
    data["password_hash"] = generate_password_hash(
        data["password"], data["password_salt"]
    )

    user = user_engine.create_user(data)

    return jsonify({"access_token": create_access_token({"id": user.id})})


@app.put("/users/<int:id>")
@authenticate_user()
@pass_data(LoadUserUpdateSchema)
def update_user(data, user, id):
    user = user_engine.update_user(data, user)

    return DumpUserSchema().jsonify(user)


@app.put("/users/<int:id>/change_password")
@authenticate_user()
@pass_data(LoadUserChangePasswordSchema)
def update_user_password(data, user, id):
    data["password_salt"] = gen_salt()
    data["password_hash"] = generate_password_hash(
        data["password"], data["password_salt"]
    )

    user = user_engine.update_user_password(data, user)

    return {"message": "Changed user's password successfully"}
