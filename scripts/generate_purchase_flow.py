"""
Generates a draw.io (.drawio) XML file for the Purchase user-flow swimlane diagram,
based on 02_User_Flow_Purchase.md. Open in https://app.diagrams.net (File > Open from Device),
then export to PNG/SVG (and optionally VSDX).
"""
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Styles
PROCESS = "rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=15;"
APP_STEP = "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;fontSize=15;"
DECISION = "rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=15;"
DOCUMENT = "shape=document;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=15;"
ENDPOINT = "ellipse;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=15;"
LANE_HEADER = "swimlane;horizontal=0;whiteSpace=wrap;html=1;fontSize=15;fontStyle=1;fillColor=#f5f5f5;startSize=40;"

LANES = [
    "Visitor / Applicant",
    "Marketing Site",
    "Rocket Application\n(Launchpad)",
    "Home Loan Expert /\nBanker",
    "Underwriting &\nProcessing",
]

LANE_HEIGHT = 180
LANE_LABEL_W = 160

# Each step: (id, label, lane_index, x, style, width, height)
W, H = 160, 60
steps = [
    ("s1",  "Visitor lands on Home\nor /purchase page",            0, 200,  PROCESS),
    ("s2",  "Site shows CTA:\n'See what I qualify for'",           1, 400,  PROCESS),
    ("s3",  "Visitor clicks CTA",                                    0, 600,  PROCESS),
    ("d1",  "Has existing\nRocket account?",                         0, 800,  DECISION),
    ("s4",  "Sign in (pre-filled\napplication)",                     2, 1000, PROCESS),
    ("s5",  "'What are you looking\nto do?' -> Buy a home",          2, 800,  APP_STEP),
    ("s6",  "Property details:\nlocation, type, use",                2, 1000, APP_STEP),
    ("s7",  "Purchase timeline\n(researching/under contract)",       2, 1200, APP_STEP),
    ("d2",  "Already have an\nagent / found home?",                  2, 1400, DECISION),
    ("s8",  "Capture property\naddress / MLS info",                  2, 1600, PROCESS),
    ("s9",  "Create account\n(email, phone, password)",              2, 1800, APP_STEP),
    ("s10", "Soft credit pull\nconsent (zero impact)",                2, 2000, APP_STEP),
    ("s11", "Income & employment\ninfo",                              2, 2200, APP_STEP),
    ("s12", "Assets / down\npayment amount",                          2, 2400, APP_STEP),
    ("s13", "Credit score range /\nsoft pull result",                 2, 2600, APP_STEP),
    ("d3",  "Meets minimum\nqualification?",                          2, 2800, DECISION),
    ("s14", "Alternative options:\nFHA, credit resources,\nbanker review", 3, 3000, PROCESS),
    ("s15", "Generate personalized\nloan options",                    2, 3000, APP_STEP),
    ("s16", "Visitor reviews &\nselects loan option",                 0, 3200, PROCESS),
    ("s17", "Generate Preapproval\nLetter (PDF)",                     2, 3400, DOCUMENT),
    ("d4",  "Wants to talk\nto a person?",                            0, 3600, DECISION),
    ("s18", "Connect with Home\nLoan Expert",                         3, 3800, PROCESS),
    ("s19", "Continue full\napplication, doc upload",                 2, 3800, APP_STEP),
    ("s20", "Document upload:\npay stubs, W-2s,\nbank statements, ID", 2, 4000, APP_STEP),
    ("s21", "Loan Expert reviews\ndocs, requests\nmissing items", 3, 4200, PROCESS),
    ("s22", "Underwriting review\n(auto + manual)",                   4, 4400, PROCESS),
    ("d5",  "Approved as\nsubmitted?",                                 4, 4600, DECISION),
    ("s23", "Conditional approval:\nrequest additional docs", 4, 4800, PROCESS),
    ("s24", "Clear to close",                                          4, 4800, PROCESS),
    ("s25", "Visitor reviews\nClosing Disclosure\n(3-day TRID)",       0, 5000, DOCUMENT),
    ("s26", "Schedule closing\n(in-person/notary/RON)", 3, 5200, PROCESS),
    ("s27", "Sign documents,\nloan funds",                             0, 5400, ENDPOINT),
]

# Edges: list of (source, target, label)
edges = [
    ("s1", "s2", ""),
    ("s2", "s3", ""),
    ("s3", "d1", ""),
    ("d1", "s4", "Yes"),
    ("d1", "s5", "No"),
    ("s4", "s15", ""),
    ("s5", "s6", ""),
    ("s6", "s7", ""),
    ("s7", "d2", ""),
    ("d2", "s8", "Yes"),
    ("d2", "s9", "No"),
    ("s8", "s9", ""),
    ("s9", "s10", ""),
    ("s10", "s11", ""),
    ("s11", "s12", ""),
    ("s12", "s13", ""),
    ("s13", "d3", ""),
    ("d3", "s14", "No / Marginal"),
    ("d3", "s15", "Yes"),
    ("s15", "s16", ""),
    ("s16", "s17", ""),
    ("s17", "d4", ""),
    ("d4", "s18", "Yes"),
    ("d4", "s19", "No"),
    ("s18", "s19", ""),
    ("s19", "s20", ""),
    ("s20", "s21", ""),
    ("s21", "s22", ""),
    ("s21", "s20", "Missing items"),
    ("s22", "d5", ""),
    ("d5", "s23", "No"),
    ("d5", "s24", "Yes"),
    ("s23", "s20", "Conditional approval:\nadditional docs needed"),
    ("s24", "s25", ""),
    ("s25", "s26", ""),
    ("s26", "s27", ""),
]

# Compute lane width from the actual rightmost step (+ its width + margin)
def step_width(style):
    return 140 if style == DECISION else W

LANE_WIDTH = max(x + step_width(style) for _, _, _, x, style in steps) + 120

mxfile = ET.Element("mxfile", host="app.diagrams.net")
diagram = ET.SubElement(mxfile, "diagram", name="Purchase Flow", id="purchase1")
model = ET.SubElement(diagram, "mxGraphModel", dx="2000", dy="1200", grid="1", gridSize="10",
                       guides="1", tooltips="1", connect="1", arrows="1", fold="1",
                       page="1", pageScale="1", pageWidth=str(LANE_WIDTH + LANE_LABEL_W + 100),
                       pageHeight=str(LANE_HEIGHT * len(LANES) + 100), math="0", shadow="0")
root = ET.SubElement(model, "root")
ET.SubElement(root, "mxCell", id="0")
ET.SubElement(root, "mxCell", id="1", parent="0")

# Pool container
pool = ET.SubElement(root, "mxCell", id="pool", value="Purchase Preapproval Journey",
                      style="swimlane;startSize=30;horizontal=1;html=1;fontSize=15;fontStyle=1;",
                      vertex="1", parent="1")
ET.SubElement(pool, "mxGeometry", x="40", y="40", width=str(LANE_WIDTH + LANE_LABEL_W),
               height=str(LANE_HEIGHT * len(LANES) + 30), **{"as": "geometry"})

# Lanes
for i, lane_name in enumerate(LANES):
    lane = ET.SubElement(root, "mxCell", id=f"lane{i}", value=lane_name,
                          style=LANE_HEADER, vertex="1", parent="pool")
    ET.SubElement(lane, "mxGeometry", x="0", y=str(i * LANE_HEIGHT), width=str(LANE_WIDTH + LANE_LABEL_W),
                   height=str(LANE_HEIGHT), **{"as": "geometry"})

# Steps that get skipped over by a branch edge (e.g. d2 "No" -> s9 skips s8)
# get pushed toward the bottom of their lane so skip-edges can route above them cleanly.
LOWER_IN_LANE = {"s8"}

# Steps placed inside their lane
for sid, label, lane_idx, x, style in steps:
    h = 70 if style == DECISION else 60
    w = 140 if style == DECISION else W
    if sid in LOWER_IN_LANE:
        y = LANE_HEIGHT - h - 10
    else:
        y = (LANE_HEIGHT - h) / 2
    cell = ET.SubElement(root, "mxCell", id=sid, value=label, style=style,
                          vertex="1", parent=f"lane{lane_idx}")
    ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h),
                   **{"as": "geometry"})

# Edges that need to be routed around other shapes (long jumps/loop-backs) get
# an explicit path plus fixed exit/entry sides so they don't cut through boxes
# that sit between their source and target. Coordinates are page-absolute.
pool_offset = 40  # pool's x/y position on the page
pool_bottom = pool_offset + LANE_HEIGHT * len(LANES) + 30
ROUTES = {
    # Long loop-back below all lanes (s23 -> s20)
    ("s23", "s20"): {
        "waypoints": [(pool_offset + 4880, pool_bottom + 40), (pool_offset + 4080, pool_bottom + 40)],
        "style": "exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;",
    },
    # d3 -> s14 drops into the Banker lane; route around the boxes between them
    ("d3", "s14"): {
        "waypoints": [(pool_offset + 2870, pool_offset + 510), (pool_offset + 3080, pool_offset + 510)],
        "style": "exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;",
    },
    # s4 -> s15 jumps across the entire Launchpad lane; route along the bottom
    # margin of the lane (below all the boxes in that row)
    ("s4", "s15"): {
        "waypoints": [(1160, 600), (3160, 600)],
        "style": "exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;",
    },
    # d4 -> s18 ("Yes") drops two lanes down at the same x as s19; detour
    # right of s19 so the line doesn't cut through it
    ("d4", "s18"): {
        "waypoints": [(3750, 425), (4060, 425), (4060, 700)],
        "style": "exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;",
    },
}

for i, (src, tgt, label) in enumerate(edges):
    style = "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;fontSize=15;"
    route = ROUTES.get((src, tgt))
    waypoints = route["waypoints"] if route else None
    if route:
        style += route["style"]
    cell = ET.SubElement(root, "mxCell", id=f"edge{i}", value=label,
                          style=style, edge="1", parent="1", source=src, target=tgt)
    geom = ET.SubElement(cell, "mxGeometry", relative="1", **{"as": "geometry"})
    if waypoints:
        points_el = ET.SubElement(geom, "Array", **{"as": "points"})
        for px, py in waypoints:
            ET.SubElement(points_el, "mxPoint", x=str(px), y=str(py))

xml_str = ET.tostring(mxfile, encoding="unicode")
pretty = minidom.parseString(xml_str).toprettyxml(indent="  ")

out_path = r"C:\Users\ryann\Documents\Claude\Visio - Rocket Mortgage Project\02_User_Flow_Purchase.drawio"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(pretty)

print(f"Wrote {out_path}")
