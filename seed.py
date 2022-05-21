from main.engines.category import create_category
from main.engines.currency import create_currency
from main.libs.log import ServiceLogger

logger = ServiceLogger(name="seed.py")

# class CategoryGroup():
#     TRANSPORTATION = "Transportation"
#     GIFT_AND_DONATION = "Gifts & Donation"
#     FOOD_AND_BEVERAGE = "Food & Beverage"
#     BILLS = "Bills"
#     SHOPPING = "Shopping"
#     FRIENDS_AND_LOVER = "Friends & Lover"
#     ENTERTAINMENT = "Entertainment"
#     TRAVEL = "Travel"
#     HEALTH_AND_FITNESS = "Health & Fitness"
#     FAMILY = "Family"
#     EDUCATION = "Education"
#     INVESTMENT = "Investment"
#     BUSINESS = "Business"
#     OTHER_EXPENSE = "Other Expense"

logger.info(message="Creating category seeds...")

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


logger.info(message="Creating currency seeds...")

create_currency({"name": "Vietnam Dong", "abbreviation": "VND"})
create_currency({"name": "United State Dollar", "abbreviation": "USD"})

logger.info(message="Finished creating currency seeds!")
