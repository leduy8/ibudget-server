from main import db
from main.models.base import BaseModel


class CategoryModel(BaseModel):
    __tablename__ = "category"

    name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    transactions = db.relationship(
        "TransactionModel", backref="category", cascade="all,delete", lazy="dynamic"
    )

    def __str__(self) -> str:
        return f"<CategoryModel {self.id} {self.name}>"
