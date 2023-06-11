class User:
    def __init__(self, name, items=[]):
        self.name = name
        self.items = items


class Driver(User):
    def __init__(self, name, items=[], deliveries=[]):
        super().__init__(name, items)
        self.deliveries = deliveries

    def accept_trade(self, shopper, trade_item):
        if trade_item in shopper.items:
            self.items.append(trade_item)
            shopper.items.remove(trade_item)
            return True
        else:
            return False


class Shopper(User):
    def __init__(self, name, items=[], orders=[]):
        super().__init__(name, items)
        self.orders = orders

    def propose_trade(self, driver, trade_item):
        if trade_item in self.items:
            if driver.accept_trade(self, trade_item):
                print(f"Trade accepted by {driver.name}")
                return True
            else:
                print("Trade rejected")
                return False
        else:
            print("You don't have that item")
            return False


# Usage
driver = Driver("John")
shopper = Shopper("Alice", items=["Book"])

trade_item = "Book"
if shopper.propose_trade(driver, trade_item):
    print(f"{shopper.name} and {driver.name} traded {trade_item}")
else:
    print("Trade failed")
