# This class is responsible for specifying the inputs to inventory and datasource class
# and calling the inventory allocator class to process allocating logic
# and displaying the data

from inventory import Inventory
from InventoryAllocator import Allocator
from DataSource import DataSource

def printOrders(orderList):
    print("Output format - Header: Order quantity(per line)::Order Allocated::OrderBackOrdered")
    headers,orders,ordersAllocated,ordersBackOrdered = orderList
    for i in range(len(orders)):
        print(headers[i], end=': ')
        print("".join(map(str,orders[i].values())), end = '::')
        print("".join(map(str, ordersAllocated[i].values())), end = '::')
        print("".join(map(str, ordersBackOrdered[i].values())))

# Start assigning inventory and orders
if __name__ == "__main__":
    inventoryList = {'A':2,'B':3,'C':1,'D':0,'E':0} # Dummy inventory List
    inventory = Inventory(inventoryList)

    # The order stream is a list of unique order streams with each stream containing
    # header and lines as key. Line is a list of orders represented as dictionary
    orderStream = [
    {"Header": 1, "Lines": [{"Product": "A", "Quantity": 1},{"Product": "C", "Quantity": 1}]},
    {"Header": 2, "Lines": [{"Product": "E", "Quantity": 5}]},
    {"Header": 3, "Lines": [{"Product": "D", "Quantity": 4}]},
    {"Header": 4, "Lines": [{"Product": "A", "Quantity": 1},{"Product": "C", "Quantity": 1}]},
    {"Header": 5, "Lines": [{"Product": "B", "Quantity": 3}]},
    {"Header": 6, "Lines": [{"Product": "D", "Quantity": 4}]}
    ]

    datasource = DataSource(orderStream)
    allocator = Allocator(datasource,inventory)
    orderList = allocator.allocateOrders()
    printOrders(orderList)


