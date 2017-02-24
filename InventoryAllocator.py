# This class is responsible for the logic of allocating orders
import collections

class Allocator(object):
    def __init__(self,datasource,inventory):
        self.orderStream = datasource.returnData() # Total List of Orders
        self.inventory = inventory.returnItems()  # Total amount of inventory
        self.inventoryOver = False # To check whether inventory is empty
        self.orders = [] # List of orders generated per line
        self.ordersAllocated = [] # List of orders Allocated per line
        self.ordersBackOrdered = [] # List of orders Backordered per line
        self.headers = []

    def allocateOrders(self):
        for stream in self.orderStream:  # Process every line in order Stream

            line = stream["Lines"]
            self.tempheader = stream["Header"]
            self.tempDictOrder = collections.OrderedDict()
            self.tempDictOrder['A'] = 0
            self.tempDictOrder['B'] = 0
            self.tempDictOrder['C'] = 0
            self.tempDictOrder['D'] = 0
            self.tempDictOrder['E'] = 0
            #self.tempDictOrder = {'A':0,'B':0,'C':0,'D':0,'E':0} # Temporary dictionaries to store order, order allocated, order backordered per line
            self.tempDictAllocated = self.tempDictOrder.copy()
            self.tempDictBackOrdered = self.tempDictOrder.copy()
            for order in line: # Check for every order in a line

                orderproduct = order["Product"]
                orderquantity = order["Quantity"]

                if orderquantity>0 and orderquantity<6: # If order quantity is invalid, dont allocate it or backorder it
                    self.tempDictOrder[orderproduct] += orderquantity
                    if self.inventory[orderproduct]<orderquantity: # If inventory of particular product is less than quantity ordered, put it in backordered queue
                        self.tempDictBackOrdered[orderproduct] = orderquantity
                    else: # If inventory of particular item is greater than quantity ordered, allocate it and subtract quantity from inventory
                        self.tempDictAllocated[orderproduct] = orderquantity
                        self.inventory[orderproduct] -=  orderquantity

            self.headers.append(self.tempheader)
            self.orders.append(self.tempDictOrder)
            self.ordersAllocated.append(self.tempDictAllocated)
            self.ordersBackOrdered.append(self.tempDictBackOrdered)

            if self.isInventoryOver(): # If inventory got over, return the total list of orders processed
                return [self.headers,self.orders,self.ordersAllocated,self.ordersBackOrdered]

    def isInventoryOver(self): # Checks if inventory quantity is 0
        sum = 0
        orderType = ['A', 'B', 'C', 'D', 'E']
        for order in orderType:
            sum += self.inventory[order]
        if (sum == 0):
            self.inventoryOver = True
        return self.inventoryOver





