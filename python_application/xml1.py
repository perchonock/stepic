from xml.etree import ElementTree

xml_str = '<cube color="blue"><cube color="red"><cube color="green"></cube><cube color="blue"></cube></cube><cube color="red"></cube></cube>'
#xml_str = input()

root = ElementTree.fromstring(xml_str)
cubes = {'red': 0, 'green': 0, 'blue': 0}
cubes[root.attrib['color']] = 1

def getChildren(element, level):
    level += 1
    cubes[element.attrib['color']] += level
    for child in element:
        getChildren(child, level)

for element in root:
    level = 1
    getChildren(element, level)

print(cubes['red'], cubes['green'], cubes['blue'])