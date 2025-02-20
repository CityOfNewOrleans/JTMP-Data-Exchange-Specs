from lxml import etree

def validate_xml(xml_path, xsd_path):
    try:
        xml_doc = etree.parse(xml_path)
        xsd_schema = etree.XMLSchema(file=xsd_path)
        xsd_schema.assertValid(xml_doc)
        return True
    except etree.DocumentInvalid as e:
        print(f"Validation error: {e}")
        return False
    except etree.XMLSchemaParseError as e:
         print(f"XSD parsing error: {e}")
         return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

# Example usage
xml_file = 'CaseInitiation_Annotated.xml'
xsd_file = '../api/xml_schema/CaseInitiation_NOLA.xsd'

if validate_xml(xml_file, xsd_file):
    print(f"{xml_file} is valid against {xsd_file}")
else:
    print(f"{xml_file} is invalid against {xsd_file}")