"""
Generates a draw.io (.drawio) XML file for the Low-Intent Research / Calculator
user-flow swimlane diagram, based on 04_User_Flow_Research.md. Open in
https://app.diagrams.net (File > Open from Device), then export to PNG/SVG.
Mirrors the styling/sizing conventions established in generate_purchase_flow.py
and generate_refinance_flow.py (font 15, swimlane pool, lane width auto-fit).
"""
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Styles (match generate_purchase_flow.py / generate_refinance_flow.py)
PROCESS = "rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=15;"
APP_STEP = "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;fontSize=15;"
DECISION = "rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=15;"
DOCUMENT = "shape=document;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=15;"
ENDPOINT = "ellipse;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=15;"
LANE_HEADER = "swimlane;horizontal=0;whiteSpace=wrap;html=1;fontSize=15;fontStyle=1;fillColor=#f5f5f5;startSize=40;"
NOTE = "shape=note;whiteSpace=wrap;html=1;fontSize=15;fillColor=#f5f5f5;strokeColor=#666666;dashed=1;size=20;"

LANES = [
    "Visitor",
    "Marketing Site /\nContent",
    "Calculator Tools",
    "Rocket Application\n(Launchpad)",
]

LANE_HEIGHT = 180
LANE_LABEL_W = 160

# Each step: (id, label, lane_index, x, style)
W, H = 160, 60
steps = [
    ("s1",  "Visitor lands on\nHome, /mortgage-rates,\nor Learn/blog article",   0, 200,  PROCESS),
    ("s2",  "Displays 'Build your\nestimate' widget",                            1, 400,  PROCESS),
    ("s3",  "Selects intent\n(e.g., buying +\nresearching)",                     0, 600,  APP_STEP),
    ("s4",  "Displays today's rate\ntable (30yr fixed, FHA,\n15yr, VA, etc.)",   2, 800,  PROCESS),
    ("d1",  "Wants more\ndetail?",                                               2, 1000, DECISION),
    ("s5",  "Exits site /\nnavigates elsewhere\n(bounce)",                       0, 1000, ENDPOINT),
    ("s6",  "Clicks 'Explore all\ncalculators' or a\nspecific calculator",       0, 1200, PROCESS),
    ("s7",  "Inputs home price, down\npayment, term, credit\nscore, location",   2, 1200, APP_STEP),
    ("s8",  "Displays estimated\nmonthly payment\nbreakdown (P&I, taxes,\ninsurance, PMI)", 2, 1400, DOCUMENT),
    ("d2",  "Satisfied /\nwants to act?",                                        2, 1600, DECISION),
    ("s9",  "Visitor leaves\n(soft conversion\nopportunity lost)",               0, 1800, ENDPOINT),
    ("s10", "End: Lead captured\n(rate alerts email,\nno full application)",     1, 1800, ENDPOINT),
    ("s11", "Branches to Purchase\nflow Phase 2\n(see 02_)",                     3, 1800, ENDPOINT),
    ("s12", "Arrives via Learn/\neducation article\n(alternate entry path)",     1, 2000, PROCESS),
    ("s13", "Article shows embedded\nCTAs & related-\narticle links",            1, 2200, PROCESS),
    ("d3",  "Clicks related\narticle?",                                          1, 2400, DECISION),
    ("d4",  "Clicks CTA?",                                                       1, 2600, DECISION),
    ("s14", "Branches to Calculator\nTools or Purchase/\nRefinance flow",        2, 2800, ENDPOINT),
]

# Edges: list of (source, target, label)
edges = [
    ("s1", "s2", ""),
    ("s2", "s3", ""),
    ("s3", "s4", ""),
    ("s4", "d1", ""),
    ("d1", "s5", "No"),
    ("d1", "s6", "Yes"),
    ("s6", "s7", ""),
    ("s7", "s8", ""),
    ("s8", "d2", ""),
    ("d2", "s9", "Exit"),
    ("d2", "s10", "Sign up for\nrate alerts"),
    ("d2", "s11", "Get my estimate /\nSee what I qualify for"),
    ("s12", "s13", ""),
    ("s13", "d3", ""),
    ("d3", "s13", "Yes (loops within\nLearn content)"),
    ("d3", "d4", "No"),
    ("d4", "s14", "Clicks CTA"),
    ("d4", "s13", "No (continues\nbrowsing)"),
]

# Compute lane width from the actual rightmost step (+ its width + margin)
def step_width(style):
    return 140 if style == DECISION else W

LANE_WIDTH = max(x + step_width(style) for _, _, _, x, style in steps) + 120

mxfile = ET.Element("mxfile", host="app.diagrams.net")
diagram = ET.SubElement(mxfile, "diagram", name="Research Flow", id="research1")
model = ET.SubElement(diagram, "mxGraphModel", dx="2000", dy="1200", grid="1", gridSize="10",
                       guides="1", tooltips="1", connect="1", arrows="1", fold="1",
                       page="1", pageScale="1", pageWidth=str(LANE_WIDTH + LANE_LABEL_W + 100),
                       pageHeight=str(LANE_HEIGHT * len(LANES) + 100), math="0", shadow="0")
root = ET.SubElement(model, "root")
ET.SubElement(root, "mxCell", id="0")
ET.SubElement(root, "mxCell", id="1", parent="0")

# Pool container
pool = ET.SubElement(root, "mxCell", id="pool", value="Research / Calculator Journey",
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

LOWER_IN_LANE = set()

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

# Floating annotation for the persistent Rocket Assist chat widget (cross-cutting
# UI element, not part of the linear flow). Placed above the pool.
chat_note = ET.SubElement(root, "mxCell", id="chatNote",
                           value="Rocket Assist chat widget\n(persistent across all pages)\n"
                                 "May answer questions inline,\nor escalate to a live agent",
                           style=NOTE, vertex="1", parent="1")
ET.SubElement(chat_note, "mxGeometry", x="80", y="-110", width="220", height="90", **{"as": "geometry"})

# Edges that need to be routed around other shapes get an explicit path plus
# fixed exit/entry sides so they don't cut through boxes between source and
# target. Coordinates are page-absolute.
ROUTES = {
    # d3 -> s13 ("Yes, loops within Learn content") loops back along the
    # bottom margin of lane1.
    ("d3", "s13"): {
        "waypoints": [(2550, 415), (2360, 415)],
        "style": "exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;",
    },
    # d4 -> s13 ("No, continues browsing") loops back along the bottom margin
    # of lane1, below the d3 -> s13 loop, jumping over d3.
    ("d4", "s13"): {
        "waypoints": [(2750, 425), (2360, 425)],
        "style": "exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;",
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

out_path = r"C:\Users\ryann\Documents\Claude\Visio - Rocket Mortgage Project\04_User_Flow_Research.drawio"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(pretty)

print(f"Wrote {out_path}")
