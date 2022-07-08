from main.engines.category import create_category
from main.libs.log import ServiceLogger

logger = ServiceLogger(name="seed.py")

logger.info(message="Creating category seeds...")

# * All
create_category({"name": "Tất cả", "type": "All", "icon_name": "ic_all.png"})

# * Expenses
create_category(
    {"name": "Xe cộ", "type": "Expense", "icon_name": "ic_transportation.png"}
)
create_category(
    {"name": "Quà tặng", "type": "Expense", "icon_name": "ic_gift_donation.png"}
)
create_category(
    {"name": "Ăn uống", "type": "Expense", "icon_name": "ic_food_beverage.png"}
)
create_category({"name": "Hóa đơn", "type": "Expense", "icon_name": "ic_bills.png"})
create_category({"name": "Mua sắm", "type": "Expense", "icon_name": "ic_shopping.png"})
create_category(
    {
        "name": "Bạn bè và gia đình",
        "type": "Expense",
        "icon_name": "ic_friend_lover.png",
    }
)
create_category(
    {"name": "Giải trí", "type": "Expense", "icon_name": "ic_entertainment.png"}
)
create_category({"name": "Du lịch", "type": "Expense", "icon_name": "ic_travel.png"})
create_category(
    {
        "name": "Sức khỏe",
        "type": "Expense",
        "icon_name": "ic_health_fitness.png",
    }
)
create_category({"name": "Gia đình", "type": "Expense", "icon_name": "ic_family.png"})
create_category(
    {"name": "Giáo dục", "type": "Expense", "icon_name": "ic_education.png"}
)
create_category({"name": "Đầu tư", "type": "Expense", "icon_name": "ic_investment.png"})
create_category(
    {"name": "Doanh nghiệp", "type": "Expense", "icon_name": "ic_business.png"}
)
create_category(
    {"name": "Chi tiêu khác", "type": "Expense", "icon_name": "ic_other_expense.png"}
)

# * Incomes
create_category({"name": "Lương", "type": "Income", "icon_name": "ic_salary.png"})
create_category({"name": "Bán đồ", "type": "Income", "icon_name": "ic_selling.png"})
create_category(
    {"name": "Lãi suất", "type": "Income", "icon_name": "ic_interest_money.png"}
)
create_category({"name": "Quà được tặng", "type": "Income", "icon_name": "ic_gift.png"})
create_category({"name": "Phần thưởng", "type": "Income", "icon_name": "ic_award.png"})
create_category(
    {"name": "Được đầu tư", "type": "Income", "icon_name": "ic_funding.png"}
)
create_category(
    {"name": "Thu nhập khác", "type": "Income", "icon_name": "ic_other_income.png"}
)

logger.info(message="Finished creating catogory seeds!")
