"""
Generates a draw.io (.drawio) XML file for the Refinance user-flow swimlane diagram,
based on 03_User_Flow_Refinance.md. Open in https://app.diagrams.net (File > Open from Device),
then export to PNG/SVG (and optionally VSDX). Mirrors the styling/sizing conventions
established in generate_purchase_flow.py (font 15, 5-lane pool, lane width auto-fit).
"""
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Styles (match generate_purchase_flow.py)
PROCESS = "rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=15;"
APP_STEP = "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;fontSize=15;"
DECISION = "rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=15;"
DOCUMENT = "shape=document;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=15;"
ENDPOINT = "ellipse;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=15;"
LANE_HEADER = "swimlane;horizontal=0;whiteSpace=wrap;html=1;fontSize=15;fontStyle=1;fillColor=#f5f5f5;startSize=40;"

LANES = [
    "Visitor / Homeowner",
    "Marketing Site",
    "Rocket Application\n(Launchpad)",
    "Home Loan Expert /\nBanker",
    "Underwriting &\nProcessing",
]

LANE_HEIGHT = 180
LANE_LABEL_W = 160

# Each step: (id, label, lane_index, x, style)
W, H = 160, 60
steps = [
    ("s1",  "Visitor lands on\nrefinance page (search, ad,\nrate alert email)",  0, 200,  PROCESS),
    ("s2",  "Site shows CTA:\n'See what I qualify for'\n(refi rate teaser)",     1, 400,  PROCESS),
    ("s3",  "Visitor clicks CTA",                                                 0, 600,  PROCESS),
    ("s4",  "'What are you looking\nto do?' -> Refinance",                       2, 800,  APP_STEP),
    ("s5",  "Select refinance goal:\nlower rate, cash-out,\nshorten term, consolidate\ndebt, remove PMI", 2, 1000, APP_STEP),
    ("d1",  "Goal = cash-out or\ndebt consolidation?",                           2, 1200, DECISION),
    ("s6",  "Branches to Home\nEquity product path\n(see sitemap)",              1, 1200, ENDPOINT),
    ("s7",  "Property address\n(auto-pulled via AVM)",                           2, 1500, APP_STEP),
    ("s8",  "Current mortgage details:\nlender, balance, rate,\nloan type",      2, 1700, APP_STEP),
    ("s9",  "Create account /\nsign in",                                         2, 1900, APP_STEP),
    ("s10", "Soft credit pull\nconsent",                                         2, 2100, APP_STEP),
    ("s11", "Income & employment\ninfo",                                         2, 2300, APP_STEP),
    ("s12", "Desired cash amount\n(cash-out only)",                              2, 2500, APP_STEP),
    ("d2",  "Sufficient equity &\nqualification met?",                           2, 2700, DECISION),
    ("s13", "Alternative options:\nsmaller cash-out,\nrate-and-term only,\nconnect with banker", 3, 2900, ENDPOINT),
    ("s14", "Generate refinance\nloan options",                                  2, 2900, APP_STEP),
    ("s15", "Visitor compares current\nvs. new payment\n(side-by-side)",         0, 3100, DOCUMENT),
    ("s16", "Visitor selects\npreferred option",                                 0, 3300, PROCESS),
    ("d3",  "Talk to Home\nLoan Expert?",                                        0, 3500, DECISION),
    ("s17", "Connect with Home\nLoan Expert",                                    3, 3700, PROCESS),
    ("s18", "Full application,\ndoc upload",                                     2, 3700, APP_STEP),
    ("s19", "Order home appraisal\n(or AVM/desktop)",                            4, 3900, PROCESS),
    ("d4",  "Appraisal supports\nloan amount?",                                  4, 4100, DECISION),
    ("s20", "Renegotiate loan\namount/terms with\nHome Loan Expert",             3, 4300, PROCESS),
    ("s21", "Underwriting review ->\nClear to close",                            4, 4300, PROCESS),
    ("s22", "Visitor reviews\nClosing Disclosure\n(3-day TRID)",                 0, 4500, DOCUMENT),
    ("s23", "Schedule closing\n(in-person/notary/RON)",                          3, 4700, PROCESS),
    ("s24", "Visitor signs\ndocuments",                                          0, 4900, PROCESS),
    ("d5",  "Cash-out\nrefinance?",                                              0, 5100, DECISION),
    ("s25", "3-day rescission\nperiod, then funds\ndisbursed",                   4, 5300, PROCESS),
    ("s26", "Loan funds, old\nloan paid off",                                    0, 5300, ENDPOINT),
    ("s27", "Refinance complete",                                                0, 5500, ENDPOINT),
]

# Edges: list of (source, target, label)
edges = [
    ("s1", "s2", ""),
    ("s2", "s3", ""),
    ("s3", "s4", ""),
    ("s4", "s5", ""),
    ("s5", "d1", ""),
    ("d1", "s6", "Cash-out / Debt\nconsolidation"),
    ("d1", "s7", "Lower rate / Shorten\nterm / Remove PMI"),
    ("s7", "s8", ""),
    ("s8", "s9", ""),
    ("s9", "s10", ""),
    ("s10", "s11", ""),
    ("s11", "s12", ""),
    ("s12", "d2", ""),
    ("d2", "s13", "No"),
    ("d2", "s14", "Yes"),
    ("s14", "s15", ""),
    ("s15", "s16", ""),
    ("s16", "d3", ""),
    ("d3", "s17", "Yes"),
    ("d3", "s18", "No"),
    ("s17", "s18", ""),
    ("s18", "s19", ""),
    ("s19", "d4", ""),
    ("d4", "s20", "No"),
    ("d4", "s21", "Yes"),
    ("s20", "s14", "Loop back:\nrenegotiate options"),
    ("s21", "s22", ""),
    ("s22", "s23", ""),
    ("s23", "s24", ""),
    ("s24", "d5", ""),
    ("d5", "s25", "Yes (cash-out)"),
    ("d5", "s26", "No"),
    ("s25", "s27", ""),
    ("s26", "s27", ""),
]

# Compute lane width from the actual rightmost step (+ its width + margin)
def step_width(style):
    return 140 if style == DECISION else W

LANE_WIDTH = max(x + step_width(style) for _, _, _, x, style in steps) + 120

mxfile = ET.Element("mxfile", host="app.diagrams.net")
diagram = ET.SubElement(mxfile, "diagram", name="Refinance Flow", id="refinance1")
model = ET.SubElement(diagram, "mxGraphModel", dx="2000", dy="1200", grid="1", gridSize="10",
                       guides="1", tooltips="1", connect="1", arrows="1", fold="1",
                       page="1", pageScale="1", pageWidth=str(LANE_WIDTH + LANE_LABEL_W + 100),
                       pageHeight=str(LANE_HEIGHT * len(LANES) + 100), math="0", shadow="0")
root = ET.SubElement(model, "root")
ET.SubElement(root, "mxCell", id="0")
ET.SubElement(root, "mxCell", id="1", parent="0")

# Pool container
pool = ET.SubElement(root, "mxCell", id="pool", value="Refinance Journey",
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

# Steps that get pushed toward the bottom of their lane (e.g. branch endpoints
# that sit off to the side of the main flow) so edges route cleanly around them.
LOWER_IN_LANE = {"s6"}

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

# Edges that need to be routed around other shapes get an explicit path plus
# fixed exit/entry sides so they don't cut through boxes between source and
# target. Coordinates are page-absolute.
ROUTES = {
    # d3 -> s17 ("Yes") drops from lane0 to lane3 at the same x as s18 (lane2);
    # detour right of s18 before entering s17.
    ("d3", "s17"): {
        "waypoints": [(3650, 425), (3960, 425), (3960, 700)],
        "style": "exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;",
    },
    # s18 -> s19 drops from lane2 to lane4 at the same x as s17 (lane3);
    # detour right of s17 before entering s19.
    ("s18", "s19"): {
        "waypoints": [(3860, 610), (3970, 610), (3970, 790), (4060, 790)],
        "style": "exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;",
    },
    # s21 -> s22 jumps from lane4 to lane0 at the same x as s20 (lane3);
    # detour right of s20 before entering s22.
    ("s21", "s22"): {
        "waypoints": [(4460, 850), (4560, 850), (4560, 160)],
        "style": "exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;",
    },
    # d2 -> s13 ("No") sits directly below s14 (lane2, same x as s13); exit
    # right of d2 and drop down past s14's right edge so the "No" label
    # doesn't land on top of s14.
    ("d2", "s13"): {
        "waypoints": [(2960, 520), (2960, 700)],
        "style": "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;",
    },
    # d4 -> s20 ("No") exits the top of d4 (going up to the Home Loan Expert
    # lane to renegotiate), entering s20 from below. d4 -> s21 ("Yes") stays
    # a short same-lane edge to the right, so "Yes" (continue forward) and
    # "No" (go up a lane) are visually distinct.
    ("d4", "s20"): {
        "waypoints": [(4250, 700), (4460, 700)],
        "style": "exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;",
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

out_path = r"C:\Users\ryann\Documents\Claude\Visio - Rocket Mortgage Project\03_User_Flow_Refinance.drawio"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(pretty)

print(f"Wrote {out_path}")
