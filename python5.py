inventory=[
    ("laptop",10,44500.0),
    ("smart phone",10,40000.0),
    ("bluetooth headphone",8,2000.0),
]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name,quantity,unit_price=item
    stock_value=quantity*unit_price
    print(f"Item name:{item_name},the stock value is :{stock_value}")
    if stock_value>highest_stock_value:
       highest_stock_value=stock_value
       item_with_highest_stock_value=item_name
       print(f"Highest stock value={stock_value}  and is for the item {item_name}")

