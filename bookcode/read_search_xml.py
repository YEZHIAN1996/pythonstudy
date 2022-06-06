from xml.etree.ElementTree import parse

doc = parse('products.xml')
for item in doc.iterfind('products/product'):
    name = item.findtext('name')
    price = item.findtext('price')
    print('id', '=', item.get('id'))
    print('name', '=', name)
    print('price', '=', price)
    print('-'*20)
