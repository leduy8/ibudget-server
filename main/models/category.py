from main import db
from main.models.base import BaseModel


class CategoryModel(BaseModel):
    __tablename__ = "category"

    name = db.Column(db.String(50), unique=True, nullable=False)
    group_name = db.Column(db.String(50), unique=True)
    transactions = db.relationship(
        "TransactionModel", backref="category", cascade="all,delete", lazy="dynamic"
    )

    def __str__(self) -> str:
        return f"<CategoryModel {self.id} {self.group_name} {self.name}>"
