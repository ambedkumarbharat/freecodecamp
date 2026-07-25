class Category:
    def __init__(self, name):
        """Initializes the budget category with a name and an empty ledger."""
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """Appends a deposit object to the ledger."""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """Appends a withdrawal object as a negative number if funds are available."""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """Returns the current balance based on ledger entries."""
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, other_category):
        """Transfers an amount from this category to another budget category."""
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """Returns False if the amount is greater than the balance, otherwise True."""
        return amount <= self.get_balance()

    def __str__(self):
        """Formats the ledger into a readable budget statement layout."""
        title = f"{self.name:*^30}\n"

        items_str = ""
        for item in self.ledger:
            desc = f"{item['description'][:23]:<23}"
            amt = f"{item['amount']:>7.2f}"
            items_str += f"{desc}{amt}\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + items_str + total


def create_spend_chart(categories):

    # 1. Calculate percentages from withdrawals only
    spent_amounts = []
    for category in categories:
        spent = sum([abs(item['amount']) for item in category.ledger if item['amount'] < 0])
        spent_amounts.append(spent)

    total_spent = sum(spent_amounts)

    percentages = []
    for amount in spent_amounts:
        percent = int((amount / total_spent) * 10) * 10
        percentages.append(percent)

    # 2. Draw the bar chart
    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    # 3. Horizontal line
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # 4. Vertical category names
    max_len = max([len(category.name) for category in categories])

    for i in range(max_len):
        chart += "     "  # 5 spaces to align under the bars
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "

        if i < max_len - 1:
            chart += "\n"

    return chart
