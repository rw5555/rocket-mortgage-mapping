"""
Generates a draw.io (.drawio) XML file for the Rocket Mortgage sitemap,
based on 01_Sitemap.md. Open the output in https://app.diagrams.net
(File > Open from Device), then export to .vsdx (Visio) or PNG/SVG.
"""
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Color styles (matches 00_README.md color-coding)
BLUE = "fillColor=#dae8fc;strokeColor=#6c8ebf;"      # marketing/informational
GREEN = "fillColor=#d5e8d4;strokeColor=#82b366;"     # tools/calculators
ORANGE = "fillColor=#ffe6cc;strokeColor=#d79b00;"    # application/forms
GRAY = "fillColor=#f5f5f5;strokeColor=#666666;"      # account/dashboard
ROOT_STYLE = "fillColor=#fff2cc;strokeColor=#d6b656;"

BASE_STYLE = "rounded=1;whiteSpace=wrap;html=1;fontSize=15;"

BOX_W, BOX_H = 200, 50
COL_W = 230
ROW1_Y = 80
ROW2_Y = 220
CHILD_GAP = 85
FIRST_CHILD_OFFSET = 40

sections = [
    ("Buy", BLUE, [
        ("Buy a Home", BLUE),
        ("Get Started\n(Preapproval)", ORANGE),
        ("Calculators", GREEN),
        ("Learn (Buying)", BLUE),
        ("Espanol", BLUE),
        ("Popular: VA, First-Time\nBuyer, Redfin, Chat", BLUE),
    ]),
    ("Refinance", BLUE, [
        ("Refinance a Home", BLUE),
        ("Get Started", ORANGE),
        ("Calculators", GREEN),
        ("Learn (Refinance)", BLUE),
        ("Espanol", BLUE),
        ("Popular: VA Refi, Debt\nConsolidation, Chat", BLUE),
    ]),
    ("Home Equity", BLUE, [
        ("Access Home Equity", BLUE),
        ("Calculators", GREEN),
        ("Learn (Home Equity)", BLUE),
        ("Get Started", ORANGE),
        ("Popular: HEL, Cash-Out\nRefi, Debt Consol., Chat", BLUE),
    ]),
    ("Rates", GREEN, [
        ("Purchase Rates", GREEN),
        ("Refinance Rates", GREEN),
        ("Rate Calculator /\nBuild Your Estimate", GREEN),
    ]),
    ("Loan Options", BLUE, [
        ("All Home Loans", BLUE),
        ("Personal Loans", BLUE),
        ("By Product: 15/30yr,\nARM, Bridge, VA, HEL,\nJumbo, HomeReady", BLUE),
    ]),
    ("Account", GRAY, [
        ("Sign In ->\nLaunchpad (gated)", ORANGE),
        ("Apply Now (CTA)", ORANGE),
    ]),
    ("Footer", GRAY, [
        ("About / Careers /\nPress / Investors", GRAY),
        ("Legal: Privacy, Terms,\nLicensing, Accessibility", GRAY),
        ("Help / Learn Center /\nGlossary", GRAY),
    ]),
]

mxfile = ET.Element("mxfile", host="app.diagrams.net")
diagram = ET.SubElement(mxfile, "diagram", name="Rocket Mortgage Sitemap", id="sitemap1")
model = ET.SubElement(diagram, "mxGraphModel", dx="1400", dy="900", grid="1", gridSize="10",
                       guides="1", tooltips="1", connect="1", arrows="1", fold="1",
                       page="1", pageScale="1", pageWidth="1700", pageHeight="1200", math="0", shadow="0")
root = ET.SubElement(model, "root")
ET.SubElement(root, "mxCell", id="0")
ET.SubElement(root, "mxCell", id="1", parent="0")

def add_box(_id, label, style, x, y, w=BOX_W, h=BOX_H):
    cell = ET.SubElement(root, "mxCell", id=_id, value=label,
                          style=BASE_STYLE + style, vertex="1", parent="1")
    ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h), **{"as": "geometry"})
    return _id

def add_edge(_id, source, target):
    cell = ET.SubElement(root, "mxCell", id=_id,
                          style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;fontSize=15;", edge="1",
                          parent="1", source=source, target=target)
    ET.SubElement(cell, "mxGeometry", relative="1", **{"as": "geometry"})

total_width = len(sections) * COL_W
home_x = total_width / 2 - BOX_W / 2
add_box("home", "Home\n(rocketmortgage.com)", ROOT_STYLE, home_x, ROW1_Y, w=240, h=60)

eid = 100
for i, (name, color, children) in enumerate(sections):
    x = i * COL_W
    sec_id = f"sec{i}"
    add_box(sec_id, name, color, x, ROW2_Y)
    add_edge(f"e{eid}", "home", sec_id)
    eid += 1
    prev_id = sec_id
    for j, (child_label, child_color) in enumerate(children):
        child_id = f"sec{i}_c{j}"
        cy = ROW2_Y + BOX_H + FIRST_CHILD_OFFSET + j * CHILD_GAP
        add_box(child_id, child_label, child_color, x, cy, h=60)
        add_edge(f"e{eid}", prev_id, child_id)
        eid += 1
        prev_id = child_id

xml_str = ET.tostring(mxfile, encoding="unicode")
pretty = minidom.parseString(xml_str).toprettyxml(indent="  ")

out_path = r"C:\Users\ryann\Documents\Claude\Visio - Rocket Mortgage Project\01_Sitemap.drawio"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(pretty)

print(f"Wrote {out_path}")
