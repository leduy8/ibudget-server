from flask import jsonify

from main import app
from main.commons.decorators import authenticate_user, pass_data
from main.commons.exceptions import Forbidden, NotFound
from main.engines import budget as budget_engine
from main.engines import category as category_engine
from main.engines import wallet as wallet_engine
from main.models.budget import BudgetModel
from main.schemas.dump.budget import DumpBudgetSchema
from main.schemas.dump.category import DumpCategorySchema
from main.schemas.dump.wallet import DumpWalletSchema
from main.schemas.load.budget import LoadBudgetSchema
from main.schemas.paginate import BudgetPaginationSchema


def get_budget_data(budget: BudgetModel):
    data = DumpBudgetSchema().dump(budget)
    category = category_engine.find_category_by_id(data["category_id"])
    wallet = wallet_engine.find_wallet_by_id(data["wallet_id"])
    data["category"] = DumpCategorySchema().dump(category)
    data["wallet"] = DumpWalletSchema().dump(wallet)
    return data


@app.post("/budgets")
@authenticate_user()
@pass_data(LoadBudgetSchema)
def create_budget(data, user):
    if not category_engine.find_category_by_id(data["category_id"]):
        raise NotFound(error_message="Category not found")

    if not wallet_engine.find_wallet_by_id(data["wallet_id"]):
        raise NotFound(error_message="Wallet not found")

    budget = budget_engine.create_budget(data, user.id)

    return DumpBudgetSchema().jsonify(budget)


@app.get("/budgets")
@authenticate_user()
@pass_data(BudgetPaginationSchema)
def get_budgets(data, user):
    budgets, total_items = budget_engine.get_budgets(data, user.id)

    return jsonify(
        {
            "budgets": [get_budget_data(budget) for budget in budgets],
            "page": data["page"],
            "items_per_page": data["items_per_page"],
            "total_items": total_items,
        }
    )


@app.get("/budgets/<int:id>")
@authenticate_user()
def get_budget_by_id(user, id):
    budget = budget_engine.find_budget_by_id(id)

    if not budget:
        raise NotFound(error_message="Budget not found")

    return DumpBudgetSchema().jsonify(budget)


@app.put("/budgets/<int:id>")
@authenticate_user()
@pass_data(LoadBudgetSchema)
def update_budget_by_id(data, user, id):
    budget = budget_engine.find_budget_by_id(id)

    if not budget:
        raise NotFound(error_message="Budget not found")

    if budget.user_id != user.id:
        raise Forbidden(
            error_message="User doesn't have permission to update this budget"
        )

    if not category_engine.find_category_by_id(data["category_id"]):
        raise NotFound(error_message="Category not found")

    if not wallet_engine.find_wallet_by_id(data["wallet_id"]):
        raise NotFound(error_message="Wallet not found")

    updated_budget = budget_engine.update_budget(data, budget)

    return DumpBudgetSchema().jsonify(updated_budget)


@app.delete("/budgets/<int:id>")
@authenticate_user()
def delete_budget_by_id(user, id):
    budget = budget_engine.find_budget_by_id(id)

    if not budget:
        raise NotFound(error_message="Budget not found")

    if budget.user_id != user.id:
        raise Forbidden(
            error_message="User doesn't have permission to delete this budget"
        )

    budget_engine.delete_budget(budget)

    return jsonify({})
