# KB — F&O Production Process

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Production Process.docx`
**Conversiedatum:** 2026-04-24

---

1.  Create Production order manually, from a SO-line or firm a planned order in Masterplanning.

    - Add Production remarks if applicable.

2.  Estimate production order.

    - Via **Production order (details) \> Production order \> Estimate.**

    - Check component availability via **All production orders** \> column **Component availability** or via **Production order (details) \> Manage costs \> Inventory transactions.**

> In case of component unavailability:

- Replace component in BOM with on-hand alternatives if possible

- Switch reservations if possible (via **reservation allocation center**)

- Postpone production until after next inbound delivery of the missing component (see reservation allocation center)

3.  Schedule production order.

    - Via **Production order (details) \> Schedule \> Schedule operations.**

    - This step is not mandatory for MTO-productions

4\. Assign **work place** to the production order.

- Via **Production order (details) \> Schedule \> Assign work place.**

- Necessary to make the production order visible in Shopfloor.

5\. Release to warehouse:

+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| **MTS**                                                                              | **MTO**                                                                                      |
+:=====================================================================================+:=============================================================================================+
| Release via **Production order (details) \> Production order \> Process \> Release** | First add the SO-line to an **outbound load** (this is only possible when load advice = OK). |
|                                                                                      |                                                                                              |
|                                                                                      | Add load remarks if applicable (e.g. weigh/measure remark).                                  |
|                                                                                      |                                                                                              |
|                                                                                      | Then release the **outbound load.**                                                          |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Print production picking list (+ production report) and give it to assigned operator                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

6\. Process picking via scanner.

7\. Start Production order in Shopfloor.

8\. Register produced goods in Shopfloor.

- Determine number of license plates.

- Print and attach PRODUCT labels if applicable.

9\. Declare consumed goods in Shopfloor.

- Return remaining raw materials with scanner (via **Production \> Return components to stock)** if applicable.

10\. **MTO**: Weigh/measure produced goods if necessary.

- See load remark on production report or in Shopfloor.

11\. Return pick list to Customer Service or production manager (optional)

11\. Move produced goods out of production area.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **MTS**   Move produced goods from Prodout to stock via scanner: **Production \> Move finished pallet to stock**
  --------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------
            

  **MTO**   Move produced goods from Pstage to outbound gate area (no scanflow required) where they will wait to be loaded in the truck.

            Or if already possible attach the pack list + load the produced goods directly in the truck via **Outbound load list** & scanner: **Outbound \> Load in truck**
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

12\. End production order.

- Via **Production order (details) \> Production order \> End.**

- This step can be automated in batch.

**[Status changes:]{.underline}**

- **Production order status:**

![A diagram of a flowchart Description automatically generated](media/image2.png){width="6.268055555555556in" height="1.7881944444444444in"}
