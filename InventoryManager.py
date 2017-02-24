# This class is responsible for specifying the inputs to inventory and datasource class
# and calling the inventory allocator class to process allocating logic
# and displaying the data

from inventory import Inventory
from InventoryAllocator import Allocator
from DataSource import DataSource

def printOrders(orderList):
    print("Output format - Header: Order quantity(per line)::Order Allocated::OrderBackOrdered")
    if(orderList):
        headers, orders, ordersAllocated, ordersBackOrdered = orderList
        for i in range(len(orders)):
            print(headers[i], end=': ')
            print("".join(map(str,orders[i].values())), end = '::')
            print("".join(map(str, ordersAllocated[i].values())), end = '::')
            print("".join(map(str, ordersBackOrdered[i].values())))
    else:
        pass

# Start assigning inventory and orders
if __name__ == "__main__":
    inventoryList = {'A':150,'B':150,'C':100,'D':100,'E':200} # Dummy inventory List
    inventory = Inventory(inventoryList)
    # Get Datasource object which randomly creates a datasource for each product type
    # with quantity randomly ranging from 0 - 7 where 1-5 is valid and 0,6,7 is invalid
    datasource = DataSource()
    allocator = Allocator(datasource,inventory)
    orderList = allocator.allocateOrders()
    printOrders(orderList)


