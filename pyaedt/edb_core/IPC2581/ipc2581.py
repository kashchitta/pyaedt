from pyaedt.edb_core.IPC2581.content.content import Content
from pyaedt.edb_core.IPC2581.ecad.ecad import Ecad
import xml.etree.cElementTree as ET


class IPC2581(object, file_path=None):
    def __init__(self, file_path):
        self.revision = "C"
        self._units = self.Units().Inch
        self.content = Content(units=self.units)
        self.ecad = Ecad()
        self.file_path = file_path


    @property
    def units(self):
        return self.units

    @units.setter
    def units(self, value):
        if isinstance(value, int):
            self._units = value

    def write_xml(self):
        if self.file_path:
            ipc = ET.Element("IPC-2581")
            ipc.set("revision", self.revision)
            ipc.set("xmlns", "http://webstds.ipc.org/2581")
            ipc.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
            ipc.set("xmlns:xsd", "http://www.w3.org/2001/XMLSchema")
            self.content.write_wml(ipc)

    class Units(object):
        (Inch, MM) = range(1, 2)

