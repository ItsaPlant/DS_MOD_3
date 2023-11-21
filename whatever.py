shops = dict(shop1=['item_1', 'item_12'], shop2=['item_2', 'ite_22'], shop3=['item_3'], shop4=['item_4'])

shop: str
count = 0
for shop in shops:
    count += len(shops[shop])
    items_cap = [item.capitalize() for item in shops[shop]]
    print(f'in {shop.capitalize()} I need to buy: {items_cap}')
print(f'overall there was {count} items')
shopping_dict = {shop: len(shops[shop]) for shop in shops}
print(shopping_dict)

div_5 = [i for i in range(101) if i % 5 == 0]
div_5_3 = [i**3 for i in div_5]
print(div_5)
print(div_5_3)