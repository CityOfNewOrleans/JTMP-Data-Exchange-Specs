# Introduction to [NIEM](https://www.niem.gov/)
**NOTE**: This IEPD is using NIEM v5.2

The **National Information Exchange Model** (NIEM) is a standardized framework that facilitates data sharing and interoperability across different organizations and systems. It provides a common vocabulary and data structure to enable efficient and accurate information exchanges, particularly in government and public sector applications.

---

## Understanding an IEPD
An **Information Exchange Package Documentation** (IEPD) is a comprehensive set of artifacts that define the structure, content, and rules for data exchanges within the NIEM framework. An IEPD includes schemas, documentation, and sample messages to ensure consistent implementation and understanding of the data exchange requirements.

### Key Artifacts in an IEPD

    1. NIEM Schema: Defines the root structure and any extensions for the data exchange.
    2. NIEM Subset: Contains the specific NIEM elements used in the exchange.
    3. Mapping Spreadsheet: Maps the visual data model to the physical NIEM schema elements and instance message paths.
    4. Class Diagram: A visual representation of the data model.
    5. Sample Message: An annotated example of an instance message in XML or JSON format, validated against the schemas.

## Folder Structure and Contents
The IEPD is organized into several folders, each containing essential artifacts needed for the data exchange:
### ./api/xml_schema/

    - Root XML Schema: Primary schema defining the data structure.
    - Extensions Schema: Additional custom elements or modifications.
    - NIEM Subset Folder: XML schema files with NIEM elements specific to this IEPD.

### ./api/json_schema/

    - Root JSON Schema: Primary schema in JSON format. Using yaml.
    - Extensions Schema: Additional custom elements or modifications in JSON format.
    - NIEM Subset Folder: YAML files for schemas and JSON-LD files for mapping JSON names to NIEM names.

### ./artifacts/

    - Class Diagram Image: Visual representation of the data model.
    - Mapping Spreadsheet: Maps elements from the class diagram to NIEM schema elements and instance message paths (XPath, JsonPath).

### ./examples/

    - Annotated Sample Instance Message: Sample data message in XML or JSON format, validated against the schema, 
	with annotations showing class and attribute names as per the class diagram.

## Detailed Artifact List
1. NIEM Schema
	Root XML Schema
	Extensions Schema
2. NIEM Subset
	XML Schema files (in ./api/xml_schema/niem_subset)
	YAML files (in ./api/json_schema/niem_subset)
	JSON-LD files (in ./api/json_schema/niem_subset)
3. Mapping Spreadsheet
	Located in ./artifacts/
4. Class Diagram
	Image file in ./artifacts/
5. Sample Message
	Annotated XML or JSON file in ./examples/

---

# Getting Started

Before diving into the IEPD, familiarize yourself with the NIEM framework and the purpose of each artifact. The NIEM [training resources](https://niem.github.io/training/) provide valuable background information. Review the folder structure and contents to understand how the data exchange is defined and implemented.

## Usage
    1. Schemas: Refer to the schemas in ./api/xml_schema/ and ./api/json_schema/ to understand the data structures.
    2. Subset: Check the NIEM subset files for the specific elements used.
    3. Mapping: Use the mapping spreadsheet to see how the visual model maps to schema elements and instance paths.
    4. Class Diagram: Study the class diagram for a high-level view of the data model.
    5. Sample Message: Review the annotated sample message for a concrete example of the data exchange.

**By following this guide, developers can effectively navigate and utilize the IEPD to implement consistent and accurate data exchanges within the NIEM framework.**

---

# Using the SSGT Tool to Create NIEM Subset Files and Wantlist

The **Schema Subset Generation Tool** (SSGT) is a powerful utility for creating NIEM subset files and wantlists. The [SSGT](https://niem.github.io/reference/tools/ssgt/) simplifies the process of generating tailored subsets of NIEM schemas by allowing users to select only the elements and types relevant to their specific data exchange needs. This targeted approach helps reduce complexity and improve performance by excluding unnecessary elements.
(https://tools.niem.gov/niemtools/ssgt/index.iepd)
## Steps to Use SSGT

    1. Access the SSGT: Navigate to the SSGT website.

    2. Create a New Subset:
        Click on "Create a New Subset."
        Choose the version of NIEM you are working with.

    3. Select Components:
        Use the interface to browse or search for the elements and types you need for your subset.
        Add these elements to your subset by selecting them and clicking "Add to Subset."

    4. Generate Wantlist:
        Once you have added all necessary elements, click on "Generate Wantlist."
        Review and adjust your selections if needed.

    5. Download Subset Files:
        After finalizing your wantlist, click on "Download Subset."
        The SSGT will generate and provide a zip file containing your subset schema files and wantlist.

### Benefits of Using SSGT

    - Efficiency: Streamlines the process of creating NIEM subsets by providing an intuitive interface for selecting required elements.
    - Customization: Ensures that only relevant components are included, reducing schema size and complexity.
    - Consistency: Helps maintain consistency in data exchanges by providing standardized subsets tailored to specific needs.

By leveraging the SSGT tool, developers can efficiently create NIEM subset files and wantlists that align with their data exchange requirements, facilitating smoother and more effective interoperability.
