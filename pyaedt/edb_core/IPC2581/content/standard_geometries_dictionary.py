import xml.etree.cElementTree as ET

from pyaedt.edb_core.IPC2581.ipc2581 import IPC2581


class Type(object):
    (Circle, Rectangle) = range(1, 2)


class StandardCircle(object):
    def __init__(self):
        self.diameter = ""
        self.fill_id = ""

    def write_xml(self, entry_standard):
        if entry_standard:
            standard_circle = ET.SubElement(entry_standard, "Circle")
            standard_circle.set("diameter", self.diameter)
            fill = ET.SubElement(standard_circle, "FillDescRef")
            fill.set("id", self.fill_id)


class Rectangle(object):
    def __init__(self):
        self.width = ""
        self.height = ""
        self.fill_id = ""

    def write_xml(self, entry_standard):
        if entry_standard:
            standard_rectanlgle = ET.SubElement(entry_standard, "RectCenter")
            standard_rectanlgle.set("width", self.width)
            standard_rectanlgle.set("height", self.height)
            fill = ET.SubElement(standard_rectanlgle, "FillDescRef")
            fill.set("id", self.fill_id)


class Oval(object):
    pass


class StandardGeometriesDictionary(object):
    def __init__(self):
        self.units = IPC2581.units
        self.standard_circ_dict = {}
        self.standard_rect_dict = {}
        self.standard_oval_dict = {}

    def write_xml(self, content_section=None):
        if content_section:
            standard_dict = ET.SubElement(content_section, "DictionaryStandard")
            standard_dict.set("units", self.units)
        for standard_circle in list(self.standard_circ_dict.values()):
            standard_circle.write_xml(standard_dict)
        for standard_rect in list(self.standard_rect_dict.values()):
            standard_rect.write_xml(standard_dict)
