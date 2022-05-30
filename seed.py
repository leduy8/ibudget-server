from main.engines.category import create_category
from main.libs.log import ServiceLogger

logger = ServiceLogger(name="seed.py")

logger.info(message="Creating category seeds...")

# * All
create_category({"name": "All categories", "type": "All", "icon_name": "ic_all.png"})

# * Expenses
create_category({"name": "Transportation", "type": "Expense",
                 "icon_name": "ic_transportation.png"})
create_category({"name": "Gifts & Donation", "type": "Expense",
                 "icon_name": "ic_gift_donation.png"})
create_category({"name": "Food & Beverage", "type": "Expense",
                 "icon_name": "ic_food_beverage.png"})
create_category({"name": "Bills", "type": "Expense", "icon_name": "ic_bills.png"})
create_category({"name": "Shopping", "type": "Expense", "icon_name": "ic_shopping.png"})
create_category({"name": "Friends & Lover", "type": "Expense",
                 "icon_name": "ic_friend_lover.png"})
create_category({"name": "Entertainment", "type": "Expense",
                 "icon_name": "ic_entertainment.png"})
create_category({"name": "Travel", "type": "Expense", "icon_name": "ic_travel.png"})
create_category({"name": "Health & Fitness", "type": "Expense",
                 "icon_name": "ic_health_fitness.png"})
create_category({"name": "Family", "type": "Expense", "icon_name": "ic_family.png"})
create_category({"name": "Education", "type": "Expense",
                 "icon_name": "ic_education.png"})
create_category({"name": "Investment", "type": "Expense",
                 "icon_name": "ic_investment.png"})
create_category({"name": "Business", "type": "Expense", "icon_name": "ic_business.png"})
create_category({"name": "Other Expense", "type": "Expense",
                 "icon_name": "ic_other_expense.png"})

# * Incomes
create_category({"name": "Salary", "type": "Income", "icon_name": "ic_salary.png"})
create_category({"name": "Selling", "type": "Income", "icon_name": "ic_selling.png"})
create_category({"name": "Interest Money", "type": "Income",
                 "icon_name": "ic_interest_money.png"})
create_category({"name": "Gifts", "type": "Income", "icon_name": "ic_gift.png"})
create_category({"name": "Awards", "type": "Income", "icon_name": "ic_award.png"})
create_category({"name": "Funding", "type": "Income", "icon_name": "ic_funding.png"})
create_category({"name": "Other Income", "type": "Income",
                 "icon_name": "ic_other_income.png"})

logger.info(message="Finished creating catogory seeds!")
