from flask import jsonify

from main import app
from main.commons.decorators import pass_data
from main.commons.exceptions import BadRequest, NotFound
from main.engines import user as user_engine
from main.libs.jwt import create_access_token
from main.libs.password import gen_salt, generate_password_hash
from main.schemas.dump.user import DumpUserSchema
from main.schemas.load.user import LoadUserSchema, LoadUserUpdateSchema


@app.post("/users")
@pass_data(LoadUserSchema)
def register_user(data):
    if user_engine.find_user_by_username(data["username"]):
        raise BadRequest(error_message="Username is already registered")

    print("1")

    data["password_salt"] = gen_salt()
    data["password_hash"] = generate_password_hash(
        data["password"], data["password_salt"]
    )

    user = user_engine.create_user(data)

    return jsonify({"access_token": create_access_token({"id": user.id})})


@app.put("/users/<int:id>")
@pass_data(LoadUserUpdateSchema)
def update_user(data, id):
    user = user_engine.find_user_by_id(id)

    if not user:
        raise NotFound(error_message="User's not found")

    user = user_engine.update_user(data, user)

    return DumpUserSchema().jsonify(user)
