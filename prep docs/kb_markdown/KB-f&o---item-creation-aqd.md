# KB — F&O   Item creation AQD

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O - Item creation AQD.docx`
**Conversiedatum:** 2026-04-24

---

# General manual

General manual can be found here

[https://polletgroupintranet.sharepoint.com/sites/PG_CORP_IT/Shared Documents/D365/General user manuals/F&O Item Interface AX3 to D365.docx?web=1](https://polletgroupintranet.sharepoint.com/sites/PG_CORP_IT/Shared%20Documents/D365/General%20user%20manuals/F&O%20Item%20Interface%20AX3%20to%20D365.docx?web=1)

# Product type

1.  Only hive configurable, project unique, products are created as a **product master**. All other MTS items must be created as a **distinct product**

# Hive items

1.  Create Hive product masters in the product staging

- AX3 Trigger the interface by sending a (random) configuration

- Distinct product variant can be deleted from the staging

- Complete the product master in the product staging.

- Muy important settings - **cannot be changed after creation**:

  - General product information:

    - **Prod dimension**: ConfigWoPr

    - **Configuration technology**: Constraint-based configuration

  - Inventory

    - **Unit:** if the item can be packaged multipallet: PCS +

- Other settings:

  - Plan:

    - **Coverage group:** RTD

2.  If applicable: add the sales trade agreements

3.  Enable the product for hive: set sync record

4.  Contact support via ticket to interface the item to hive

#  Raw slats

1.  Create raw slat items in the product staging

- **product staging template**: item stock batch

- Inventory unit: MAT

- Unit seq. group id: MAT

- Batch dimension: BatchAbove

REMARK: these settings **cannot be changed after creation.**

- Batch number group: AUTOBATCH

- Component consolidation group: Choose from the dropdown

REMARK: These settings **can** still be changed after creation.

# Sawed slats

1\. Complete the following fields after releasing the product:

- planning type 1: color slat

- Planning type 2: length raw slat

- Attribute name: SlatMachDeckSawing

# Serial no tracked items

1.  Set the product staging template **Item stock SerialNum**: items for which you register the SN (motors, control boxes)

2.  REMARK: these settings **cannot be changed after creation.**

# Backflushed items

1.  Set the product staging template **Item bufferstock**: the items will be consumed without picking from the fixed location

2.  Set the fixed location after product creation

# Production items

1.  Select the Route, after creation of the product

2.  Approve and activate the route after creation

3.  If the item is a subproduction: activate auto release on the item
