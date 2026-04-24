# KB — F&O Reverse project on load

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Reverse project on load.docx`
**Conversiedatum:** 2026-04-24

---

# How to cancel project line in load

- **[Load is not yet released]{.underline}**

<!-- -->

- Select load line and click **Delete**

![A screenshot of a web page AI-generated content may be incorrect.](media/image2.png){width="6.268055555555556in" height="2.9833333333333334in"}

- **[Load Is released (work Is automatically executed for projects) but not loaded]{.underline}**

  - Select load line and click \'Reduce picked quantity\'

![A screenshot of a computer AI-generated content may be incorrect.](media/image3.png){width="7.033547681539807in" height="2.619073709536308in"}

- Set **Move to location** to ASM.M1.OUT and **Inventory quantity to unpick** = Inventory quantity [per license plate]{.underline}. Click **OK**

![A screenshot of a computer AI-generated content may be incorrect.](media/image4.png){width="6.268055555555556in" height="1.5368055555555555in"}

Example multipallet:

![A screenshot of a computer AI-generated content may be incorrect.](media/image5.png){width="6.268055555555556in" height="1.6527777777777777in"}

- Refresh the load to see the changes. Then delete the line from the load.

<!-- -->

- **[Project Is loaded]{.underline}**

<!-- -->

- If the packing slip Is already generated, It Is too late, you cannot reverse the process. You need to follow the return flow In that case

- If the status = Shipped, you need to click the **Reverse shipment confirmation** button first

- Unload the loaded license plates of the project with the scanner or warehouse app via Outbound \> Unload truck

![A screenshot of a computer AI-generated content may be incorrect.](media/image6.png){width="4.597095363079615in" height="2.7248468941382327in"}

- \'Unpick\' the project via \'Reduce picked quantity\' In D365 as explained In the previous scenario

- Refresh the load and delete the line from the load
