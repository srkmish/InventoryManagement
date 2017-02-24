# InventoryManagement

In order to run this project, simply run the InventoryManager.py file i.e. python InventoryManager.py

The initial order quantities for each product type is as follows :
A : 150
B: 150
C: 100
D: 100
E:200

A datasource class randomly generates an order line 300 times(number chosen so that inventory gets exhausted and data gets printed)
Each order line contains orders for each product type with quantity randomly ranging from 0-7 where 0,6,7 are invalid orders and won't get processed

An inventory allocator class allocates all the inventory as per the order lines and prints the processed orders on the output when the 
inventory gets exhausted.

The output is in the format - Header No: Order Quantity Requested(per line)::Order Allocated::Order Backordererd
The Order quantities are represented as A:B:C:D:E

A sample portion of the output from the middle is as shown below.

![Image](https://github.com/srkmish/InventoryManagement/blob/master/python2.png)

For the first line, the header number is displayed as 65. For product type 'A', the quantity requested is 5. Since the inventory contains more than 5, the inventory is allocated to the order and displayed in the order allocated section of the output. For product type 'C', the quantity requested is 2. However, since the inventory for this product is below 2 , the order is added to the backordered section. For product type 'E', the quantity requested is 7, which is invalid. Hence this order is neither allocated nor backordered.




