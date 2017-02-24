# This class is responsible for creating Inventory object which contains
# total amount of inventory for each product type
class Inventory(object):

    def __init__(self,inventoryList):

        self.items = inventoryList.copy()

    def returnItems(self):
        return self.items






