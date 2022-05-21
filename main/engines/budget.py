from typing import Dict, List

from main import db
from main.models.budget import BudgetModel


def find_budget_by_id(id: int) -> BudgetModel:
    return BudgetModel.query.get(id)


def get_budget_count() -> int:
    return BudgetModel.query.count()


def get_budgets(params: Dict, user_id: int) -> List[object]:
    """Returns list of list of budget model and count of total items"""
    budgets = BudgetModel.query.filter_by(user_id=user_id).paginate(
        params["page"], params["items_per_page"], False
    )

    return [budgets.items, budgets.total]


def create_budget(data: Dict, user_id: int) -> BudgetModel:
    budget = BudgetModel(
        goal_value=data["goal_value"],
        from_date=data["from_date"],
        to_date=data["to_date"],
        user_id=user_id,
        wallet_id=data["wallet_id"],
        category_id=data["category_id"],
    )

    db.session.add(budget)
    db.session.commit()

    return budget


def update_budget(data: Dict, budget: BudgetModel) -> BudgetModel:
    budget.goal_value = data["price"]
    budget.from_date = data["from_date"]
    budget.to_date = data["to_date"]
    budget.wallet_id = data["wallet_id"]
    budget.category_id = data["category_id"]

    db.session.commit()

    return budget


def delete_budget(budget: BudgetModel):
    db.session.delete(budget)
    db.session.commit()
