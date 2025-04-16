from lxml import etree
import os
import fnmatch
import sys

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


base_directory = '../schemas/'
pattern = "*_iepd"
schemas = set()
for entry in os.listdir(base_directory):
    full_path = os.path.join(base_directory, entry)
    if os.path.isdir(full_path) and fnmatch.fnmatch(entry, pattern):
        if full_path.endswith('EnterpriseModel_iepd'):
            continue
        schemas.add(full_path)

exmaples_and_schemas = {
    # ArrestReport
    "../schemas/ArrestReport_iepd/examples/ArrestSample.xml":
        "../schemas/ArrestReport_iepd/api/xml_schema/Arrest_NOLA.xsd",
    "../schemas/ArrestReport_iepd/examples/ArrestSampleConcise.xml":
        "../schemas/ArrestReport_iepd/api/xml_schema/Arrest_NOLA.xsd",

    # AsyncResponse
    "../schemas/AsyncResponse_iepd/examples/Complete_AsyncResponse.xml":
        "../schemas/AsyncResponse_iepd/api/xml_schema/Asynchronous_NOLA.xsd",
    "../schemas/AsyncResponse_iepd/examples/ContentError_AsyncResponse.xml":
        "../schemas/AsyncResponse_iepd/api/xml_schema/Asynchronous_NOLA.xsd",
    "../schemas/AsyncResponse_iepd/examples/EndpointError_AsyncResponse.xml":
        "../schemas/AsyncResponse_iepd/api/xml_schema/Asynchronous_NOLA.xsd",
    "../schemas/AsyncResponse_iepd/examples/FinalAccept_AsyncResponse.xml":
        "../schemas/AsyncResponse_iepd/api/xml_schema/Asynchronous_NOLA.xsd",
    "../schemas/AsyncResponse_iepd/examples/Intermediate_AsyncResponse.xml":
        "../schemas/AsyncResponse_iepd/api/xml_schema/Asynchronous_NOLA.xsd",

    # BookingAndRelease
    "../schemas/BookingAndRelease_iepd/examples/Booking Sample.xml":
        "../schemas/BookingAndRelease_iepd/api/xml_schema/Booking_NOLA.xsd",

    # CaseInitiation
    "../schemas/CaseInitiation_iepd/examples/CaseInitiation_Annotated.xml":
        "../schemas/CaseInitiation_iepd/api/xml_schema/CaseInitiation_NOLA.xsd",

    # CaseUpdates
    "../schemas/CaseUpdates_iepd/examples/BondUpdate_example.xml":
        "../schemas/CaseUpdates_iepd/api/xml_schema/BondUpdate_NOLA.xsd",
    "../schemas/CaseUpdates_iepd/examples/CaseActivityUpdate_example.xml":
        "../schemas/CaseUpdates_iepd/api/xml_schema/CaseActivityUpdate_NOLA.xsd",
    "../schemas/CaseUpdates_iepd/examples/ChargeUpdate_example.xml":
        "../schemas/CaseUpdates_iepd/api/xml_schema/ChargeUpdate_NOLA.xsd",
    "../schemas/CaseUpdates_iepd/examples/EntityUpdate_example.xml":
        "../schemas/CaseUpdates_iepd/api/xml_schema/EntityUpdate_NOLA.xsd",

    # ChargeFiling
    "../schemas/ChargeFiling_iepd/examples/ChargeFiling.xml":
        "../schemas/ChargeFiling_iepd/api/xml_schema/ChargeFiling_NOLA.xsd",

    # CourtEvent
    "../schemas/CourtEvent_iepd/examples/SampleCourtEventXML.xml":
        "../schemas/CourtEvent_iepd/api/xml_schema/CourtEvent_NOLA.xsd",

    # CourtOrder
    "../schemas/CourtOrder_iepd/examples/Annotated_CourtOrder.xml":
        "../schemas/CourtOrder_iepd/api/xml_schema/CourtOrder_NOLA.xsd",

    # Subpoena
    "../schemas/Subpoena_iepd/examples/SubpoenaSample.xml":
        "../schemas/Subpoena_iepd/api/xml_schema/Subpoena_NOLA.xsd",

    # UniformChargeTable
    "../schemas/UniformChargeTable_iepd/examples/ChargeTableUpdate1.xml":
        "../schemas/UniformChargeTable_iepd/api/xml_schema/ChargeTableUpdate_NOLA.xsd",

    # UniformCommitmentOrder
    "../schemas/UniformCommitmentOrder_iepd/examples/UnformCommitmentOrder1.xml":
        "../schemas/UniformCommitmentOrder_iepd/api/xml_schema/UniformCommitmentOrder_NOLA.xsd"
}

schema_keys = set([os.path.dirname(key) for key in exmaples_and_schemas if key.count("_iepd")>0])
if len(schemas) != len(schema_keys):
    print(len(schema_keys))
    print(f'There are scheams that have not set up for validation. Update the examples_and_schemas table.')
    sys.exit(1)


valid_examples = []
invalid_examples = []
for k in exmaples_and_schemas:
    xml_file = k
    xsd_file = exmaples_and_schemas[k]
    if validate_xml(xml_file, xsd_file):
        #print(f"{xml_file} is valid against {xsd_file}", file=sys.stderr)
        valid_examples.append(xml_file)
    else:
        #print(f"{xml_file} is invalid against {xsd_file}")
        invalid_examples.append(xml_file)
        #sys.exit(1)

#print(valid_examples)
if len(invalid_examples) > 0:
    print('Some examples failed to validate.')
    print(invalid_examples)
    sys.exit(1)