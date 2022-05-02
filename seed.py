from main.engines.category import create_category
from main.libs.log import ServiceLogger

logger = ServiceLogger(name="Seed.py")

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

logger.info("Creating category seeds...")

create_category({"name": "Transportation"})
create_category({"name": "Gifts & Donation"})
create_category({"name": "Food & Beverage"})
create_category({"name": "Bills"})
create_category({"name": "Shopping"})
create_category({"name": "Friends & Lover"})
create_category({"name": "Entertainment"})
create_category({"name": "Travel"})
create_category({"name": "Health & Fitness"})
create_category({"name": "Family"})
create_category({"name": "Education"})
create_category({"name": "Investment"})
create_category({"name": "Business"})
create_category({"name": "Other Expense"})

logger.info("Finished creating catogory seeds!")
