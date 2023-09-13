# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET


# Минус этой библиотеки, в том, что при сохранении - ко всем элементам добавляется префкис в виде NameSpace.
# Также теряется декларация xml (<?xml version='1.0' encoding='UTF-8'?>)
def pars_xml():
    constant = "app_ssss_s"
    namespaces2 = {"": "urn:jboss:domain:datasources:5.0"}  # Задаётся пространство имён
    # --------------
    ET.register_namespace("", "")  # Не сработало, не знаю как это должно работать
    tree = ET.parse('standalone-full.xml')
    # --------------
    root = tree.getroot()
    xa_datasource = root.find(".//datasources/xa-datasource[@jndi-name='java:/VteDS']", namespaces2)
    print(xa_datasource)
    # --------------
    user_property = xa_datasource.find("./security/user-name", namespaces2)
    pass_property = xa_datasource.find("./security/password", namespaces2)
    # --------------
    rec_user = xa_datasource.find(".//recover-credential/user-name", namespaces2)
    rec_pass = xa_datasource.find(".//recover-credential/password", namespaces2)
    # --------------
    user_property.text = constant
    pass_property.text = constant
    # --------------
    rec_user.text = constant
    rec_pass.text = constant
    # --------------
    tree.write('output_1.xml', encoding="utf-8")

    # xmlstr = minidom.parseString(ET.tostring(tree.getroot())).toprettyxml()
    # with open('out.xml', 'w') as out:
    # out.write(xmlstr)


if __name__ == '__main__':
    pars_xml()
