from pyaedt.edb_core.IPC2581.content.standard_geometries_dictionary import StandardGeometriesDictionary
from pyaedt.edb_core.IPC2581.content.layer_ref import LayerRef
from pyaedt.edb_core.IPC2581.content.dictionary_color import DictionaryColor
from pyaedt.edb_core.IPC2581.content.path_width_dictionary import PathWidthDictionary
import xml.etree.cElementTree as ET


class Content(object):
    def __init__(self, units):
        self.mode = self.Mode().Stackup
        self.design_units = units
        self.role_ref = "Owner"
        self.function_mode = self.Mode().Stackup
        self.step_ref = "Ansys_IPC2581"
        self._layer_ref = []
        self.dict_colors = DictionaryColor()
        self.dict_path_width = PathWidthDictionary()
        self.standard_geometries_dict = StandardGeometriesDictionary()

    @property
    def layer_ref(self):
        return self._layer_ref

    @layer_ref.setter
    def layer_ref(self, value):
        if isinstance(value, list):
            if len([lay for lay in value if isinstance(lay, LayerRef)]) == len(value):
                self._layer_ref = value

    def add_layer_ref(self, layer_ref=None):
        if isinstance(layer_ref, LayerRef):
            self._layer_ref.append(layer_ref)
            return True
        return False

    def write_wml(self, root=None):
        if root:
            content = ET.SubElement(root, "Content")
            content.set("roleRef", "Owner")
            if self.mode == self.Mode.Stackup:
                function_mode = ET.SubElement(content, "FunctionMode")
                function_mode.set("mode", "USERDEF")
            step_ref = ET.SubElement(content, "StepRef")
            step_ref.set("name", self.step_ref)
            for lay in self.layer_ref:
                lay.write_xml(content)
            self.dict_colors.write_xml(content)
            self.dict_path_width.write_xml(content)
            self.standard_geometries_dict.write_xml(content)

    class Mode(object):
        (Stackup) = range(1)
