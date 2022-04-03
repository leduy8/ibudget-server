from flask import jsonify

from main import app
from main.commons.decorators import pass_data
from main.commons.exceptions import Unauthorized
from main.engines import user as user_engine
from main.libs.jwt import create_access_token
from main.libs.password import check_password_hash
from main.schemas.load.auth import LoadAuthSchema


@app.post("/auth")
@pass_data(LoadAuthSchema)
def login_user(data):
    user = user_engine.find_user_by_username(data["username"])

    if not user or not check_password_hash(
        user.password_hash, data["password"], user.password_salt
    ):
        raise Unauthorized(error_message="Wrong username or password")

    return jsonify({"access_token": create_access_token({"id": user.id})})
