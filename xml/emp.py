import xml.dom.minidom
  
docs = xml.dom.minidom.parse("emp.xml")
  
print(docs.nodeName)
print(docs.firstChild.tagName)
