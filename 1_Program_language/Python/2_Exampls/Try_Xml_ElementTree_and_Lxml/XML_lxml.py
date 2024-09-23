# -*- coding: UTF-8 -*-

from lxml import etree


def print_tree_info(tree):
    print('+ ' * 40)
    root_elem = tree.getroot()
    print("root_elem.nsmap = {}".format(root_elem.nsmap))
    print("tree = {}".format(etree.tostring(tree)))

    some_tag = etree.QName(root_elem)
    print("some_tag.localname = {}".format(some_tag.localname))
    print("root_elem = {}".format(etree.tostring(root_elem)))

    print(etree.tostring(root_elem))
    print("root_elem.tag = {}".format(root_elem.tag))
    print("root_elem.keys() = {}".format(root_elem.keys()))
    print("root_elem.attrib = {}".format(root_elem.attrib))
    print("root_elem.items() = {}".format(root_elem.items()))
    print("tree.docinfo = {}".format(tree.docinfo))
    print("tree.docinfo.doctype = {}".format(tree.docinfo.doctype))
    print("tree.docinfo.xml_version = {}".format(tree.docinfo.xml_version))
    print("tree.docinfo.public_id = {}".format(tree.docinfo.public_id))
    print("tree.docinfo.system_url = {}".format(tree.docinfo.system_url))
    print("root_elem.text = {}".format(root_elem.text))
    print("root_elem.tail = {}".format(root_elem.tail))
    print('* ' * 40)


def enumeration_example(tree):
    print('+ ' * 40)
    root_elem = tree.getroot()
    # for event, element in etree.iterwalk(tree, events=('start', 'end')):
    #       print(event, element,  element.text)
    for i in list(root_elem):
        if i.tag == '{urn:jboss:domain:8.0}profile':
            for ii in list(i):
                if ii.tag == '{urn:jboss:domain:datasources:5.0}subsystem':
                    for iii in list(ii):
                        if iii.tag == '{urn:jboss:domain:datasources:5.0}datasources':
                            for iiii in list(iii):
                                if iiii.get("jndi-name") == 'java:/VteDS':
                                    print(iiii.get('pool-name'))
                                    for iiiii in list(iiii):
                                        print(iiiii.tag)
                                        if iiiii.tag == '{urn:jboss:domain:datasources:5.0}security':
                                            print("security = {}".format(etree.tostring(iiiii)))
    print('* ' * 40)


# Как только не пробовал использовать. Пока не получилось найти элменты с NS.
# Хотя без NS - поиск выполняется успешно.
def try_use_xpath_with_ns(tree):
    print('+ ' * 40)
    ns = {None: "urn:jboss:domain:8.0"}
    root_elem = tree.getroot()
    print('NS_root_elem.xpath("/server") = {}'.format(root_elem.xpath('/server'), namespaces=ns))
    print('NS_root_elem.findall("./server") = {}'.format(root_elem.findall('./server'), namespaces=ns))
    print('NS_root_elem.xpath("//server") = {}'.format(root_elem.xpath('//server'), namespaces=ns))
    print('root_elem.xpath("/server") = {}'.format(root_elem.xpath('/server')))
    print('tree.xpath("./server") = {}'.format(tree.xpath('./server'), namespaces=ns))

    print('tree.findall("//server") = {}'.format(tree.findall('//server'), namespaces=ns))
    print("tree.findall = {}".format(tree.findall('{urn:jboss:domain:8.0}server')))  # ('{urn:jboss:domain:8.0}server')
    print("root_elem.findall = {}".format(root_elem.findall('{urn:jboss:domain:8.0}server')))
    print('= ' * 40)


# Рабочий пример работы с xpath и NS через lxml.
# Меняет полученный xml.
def worked_xpath_with_ns(tree):
    ROOT_NS = 'urn:jboss:domain:8.0'
    DS_NS = 'urn:jboss:domain:datasources:5.0'

    server_finder = etree.ETXPath("//{%s}server" % ROOT_NS)
    server_element = server_finder(tree)
    print("results = {}".format(server_element))

    ds_finder = etree.ETXPath("//{%s}datasources/{%s}xa-datasource[@jndi-name='java:/VteDS']" % (DS_NS, DS_NS))
    #find = etree.XPath("//n:b", namespaces={'n':'NS'})
    #count_elements = etree.XPath("count(//*[local-name() = $name])") ---> count_elements(root, name = "a")
    ds_element = ds_finder(tree)
    print("ds_element = {}".format(ds_element))
    security_user_name_finder = etree.ETXPath(".//{%s}security/{%s}user-name" % (DS_NS, DS_NS))
    security_password_finder = etree.ETXPath(".//{%s}security/{%s}password" % (DS_NS, DS_NS))
    security_user_name_element = security_user_name_finder(ds_element[0])
    security_password_element = security_password_finder(ds_element[0])
    print('security_user_name_element = {}'.format(security_user_name_element[0]))
    print('security_password_element = {}'.format(security_password_element[0]))
    security_user_name_element[0].text = "app_ssS"
    security_password_element[0].text = "app_ssS"

    recovery_user_name_finder = etree.ETXPath(".//{%s}recovery//{%s}user-name" % (DS_NS, DS_NS))
    recovery_password_finder = etree.ETXPath(".//{%s}recovery//{%s}password" % (DS_NS, DS_NS))
    recovery_user_name_element = recovery_user_name_finder(ds_element[0])
    recovery_password_element = recovery_password_finder(ds_element[0])
    print('recovery_user_name_element = {}'.format(recovery_user_name_element[0]))
    print('recovery_password_element = {}'.format(recovery_password_element[0]))
    recovery_user_name_element[0].text = "app_ssS"
    recovery_password_element[0].text = "app_ssS"


def parse_standelone_full():
    parser = etree.XMLParser(ns_clean=True, remove_blank_text=True)
    tree = etree.parse("standalone-full.xml", parser)  # Тоже не работает, не удаляет NameSpace.
    root_elem = tree.getroot()

    worked_xpath_with_ns(tree)

    bytee = etree.tostring(tree, pretty_print=True)
    # print(etree.tostring(store, encoding='utf-8', xml_declaration=True, pretty_print=True))
    strr = bytee.decode("utf-8")
    print(strr)
    with open("result_1_1.xml", mode='w', encoding='UTF-8') as file:
        file.write(strr)  # Так теряется xml декларация.
    tree.write("result_2_1.xml", encoding='utf-8', xml_declaration=True, pretty_print=True)  # Так все ок.


def parse_product():  # Этот метод работает с xpath - но без nameSpace.
    print("+ " * 80)
    parser = etree.XMLParser(ns_clean=True)
    tree = etree.parse("product_exploitation.xml", parser)

    print(tree)

    print(tree.xpath("/product//failure//name")[0].tag)
    print(tree.xpath("/product//failure//name")[0].text)
    tree.xpath("/product//failure//name")[0].text = "Textttt"
    bytee = etree.tostring(tree, pretty_print=True)
    # print(etree.tostring(store, encoding='utf-8', xml_declaration=True, pretty_print=True))
    strr = bytee.decode("utf-8")
    print(strr)
    with open("result_1.xml", mode='w', encoding='UTF-8') as file:
        file.write(strr)  # Так теряется xml декларация.
    tree.write("result_2.xml", encoding='utf-8', xml_declaration=True, pretty_print=True)  # Так все ок.


if __name__ == '__main__':
    # parse_product()
    parse_standelone_full()
