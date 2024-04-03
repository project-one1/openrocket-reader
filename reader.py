import zipfile
from xml.etree import ElementTree as ET
import sys
import orhelper

def extract_and_parse_openrocket_file(file_path):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        xml_file_name = zip_ref.namelist()[0]
        with zip_ref.open(xml_file_name) as xml_file:
            tree = ET.parse(xml_file)
            root = tree.getroot()

            rocket_name = root.find('.//rocket').get('name')
            print(f"Rocket Name: {rocket_name}")

            for component in root.findall('.//component'):
                component_type = component.get('type')
                component_name = component.get('name')
                print(f"Component Type: {component_type}, Name: {component_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py path_to_openrocket_file.ork")
        sys.exit(1)

    file_path = sys.argv[1]
    extract_and_parse_openrocket_file(file_path)
