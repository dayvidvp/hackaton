# KB — WIP F&O Hive   Special scenarios

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `WIP F&O Hive - Special scenarios.docx`
**Conversiedatum:** 2026-04-24

---

Some scenarios are not implemented in hive because the frequence of the scenario is rather low and the development time in Hive too high.

# Enkel trap 

# 

1.  Create Hive product masters in the product staging

- AX3 Trigger the interface by sending a (random) configuration

- Complete the product master in the product staging

  - **Prod dimension**: ConfigWoPr

  - **Configuration technology**: Constraint-based configuration

  - **Invent unit:** if the item can be packaged multipallet: PCS +

  - **Coverage group:** RTD

[Raw slats]{.underline}

2.  Create raw slat items in the product staging

- **product staging template**: item stock batch

- Inventory unit: MAT

- Unit seq. group id: MAT

- Batch dimension: BatchAbove

3.  Complete the released product

    a.  

[Machine slats]{.underline}

After releasing the product:

- planning type 1: color slat

- Planning type 2: length raw slat

- Attribute name: SlatMachDeckSawing
