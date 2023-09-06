# Dado dos diccionarios 1 de productos y el 2 de categoría, conocer un 3 que permita tener el nombre del producto y el nombre de su categoría 
# ejemplo.

product={
    'idp':{
        '123':{
            'name': 'PC',
            'price': '2000',
            'cat_id': '1'
        },
        '456':{ 
            'name': 'Aspiradora',
            'price': '3000',
            'cat_id': '2'
        }
    }
}

category={
    'idc':{
        '1':{
            'name':'tecnologia'
        },
        '2':{
            'name':'Aseo'
        }
    }
}

result={
    'id': "No encontrado",
    'name': "No encontrado",
    'category': "No encontrado"
}

index = input("Digite el id del producto: ")

if index in product['idp']:
    if product['idp'][index]['cat_id'] in category['idc']:
        product_name = product['idp'][index]['cat_id']
        result.update({'id': index})
        result.update({'name': product['idp'][index]['name']})
        result.update({'category': category['idc'][product_name]['name']})

print(result)