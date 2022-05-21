from main.engines.category import create_category
from main.libs.log import ServiceLogger

logger = ServiceLogger(name="seed.py")

logger.info(message="Creating category seeds...")

# * All
create_category({"name": "All categories", "type": "All"})

# * Expenses
create_category({"name": "Transportation", "type": "Expense"})
create_category({"name": "Gifts & Donation", "type": "Expense"})
create_category({"name": "Food & Beverage", "type": "Expense"})
create_category({"name": "Bills", "type": "Expense"})
create_category({"name": "Shopping", "type": "Expense"})
create_category({"name": "Friends & Lover", "type": "Expense"})
create_category({"name": "Entertainment", "type": "Expense"})
create_category({"name": "Travel", "type": "Expense"})
create_category({"name": "Health & Fitness", "type": "Expense"})
create_category({"name": "Family", "type": "Expense"})
create_category({"name": "Education", "type": "Expense"})
create_category({"name": "Investment", "type": "Expense"})
create_category({"name": "Business", "type": "Expense"})
create_category({"name": "Other Expense", "type": "Expense"})

# * Incomes
create_category({"name": "Salary", "type": "Income"})
create_category({"name": "Selling", "type": "Income"})
create_category({"name": "Interest Money", "type": "Income"})
create_category({"name": "Gifts", "type": "Income"})
create_category({"name": "Awards", "type": "Income"})
create_category({"name": "Funding", "type": "Income"})
create_category({"name": "Other Income", "type": "Income"})

logger.info(message="Finished creating catogory seeds!")
