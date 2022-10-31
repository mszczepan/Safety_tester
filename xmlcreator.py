from lxml import etree

xml_file = "D:\\01_TIA_tester\\safety_tester12.xml"

tree = etree.parse(xml_file)
element = tree.getroot()
#x = etree.tostring(element, pretty_print=True)
#x.find("dziecko")
#print(tree.find("atrapa"))

#z = element.find(".//StructuredText")
#x = tree.xpath(".//*[name() = 'StructuredText']")
x = tree.xpath(".//*[name() = 'StructuredText']")[0]
#y = x.find("child1")
#y = element.iter("child1")
print(x[0].tag)


x.append(etree.Element("child2"))
# x = etree.tostring(element, pretty_print=True)
# print(x)
tree.write('output.xml', pretty_print=True)


#root = etree.Element("korzen")
#root.append(etree.Element("dziecko", interesujacy="Trzecie"))

#el = element.find("korzen")
#el.append(etree.Element("dziecko"))
#el = element.findall("dziecko")
#print(el)
#print(el.tag)
#for item in el:
#    print(item.text)


#
