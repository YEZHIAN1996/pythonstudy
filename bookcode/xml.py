from lxml import etree

# 传入文件名 fromstring
tree = etree.parse('products.xml')
# fromstring 传入字符串形式的xml文档

print(type(tree))

print(str(etree.tostring(tree, encoding='utf-8'), 'utf-8'))
root = tree.getroot()
print(type(root))

print(root.tag)

children = root.getchildren()
print('--------输出产品信息---------')

for child in children:
    print(child.get('id'))
    print(child[0].text,':', child[1].text)
