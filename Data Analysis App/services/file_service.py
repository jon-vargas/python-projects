import json
import xml.etree.ElementTree as ET

def parse_json(file_path):
    with open(file_path) as f:
        return json.load(f)

def parse_xml(file_path):
    tree = ET.parse(file_path)
    return tree.getroot()
