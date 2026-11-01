import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

prs = pptx.Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(blank_layout)

# Color Palette (Crisp High-Tech Theme)
C_DARK = RGBColor(15, 23, 42)        # Slate 900
C_MUTED = RGBColor(71, 85, 105)      # Slate 600
C_LIGHT_BG = RGBColor(248, 250, 252) # Slate 50
C_WHITE = RGBColor(255, 255, 255)
C_BORDER = RGBColor(203, 213, 225)   # Slate 300
C_BORDER_DARK = RGBColor(148, 163, 184)

# Semantic Accent Colors
C_BLUE_HDR = RGBColor(2, 132, 199)   # Sky 600
C_CARD_BLUE = RGBColor(224, 242, 254)# Sky 100
C_NAVY_BOX = RGBColor(186, 230, 253) # Sky 200
C_PURPLE_BOX = RGBColor(243, 232, 255) # Purple 100
C_ARROW = RGBColor(14, 116, 144)     # Cyan 700

def style_card(shape, fill_color, border_color=C_BORDER, border_width=1):
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(border_width)

# ----------------- SLIDE HEADER -----------------
# Header Title
tx_title = slide.shapes.add_textbox(Inches(3.2), Inches(0.18), Inches(6.933), Inches(0.75))
tf_t = tx_title.text_frame
tf_t.word_wrap = True
p = tf_t.paragraphs[0]
p.text = "TECHNICAL APPROACH"
p.font.name = "Georgia"
p.font.size = Pt(26)
p.font.bold = True
p.font.color.rgb = C_DARK
p.alignment = PP_ALIGN.CENTER

p_sub = tf_t.add_paragraph()
p_sub.text = "Centralized Architecture, Multi-Modal Forensics & Autonomous Scrutiny Workflow"
p_sub.font.name = "Arial"
p_sub.font.size = Pt(10)
p_sub.font.color.rgb = C_MUTED
p_sub.alignment = PP_ALIGN.CENTER

# Top Left: Team Info
tx_team = slide.shapes.add_textbox(Inches(0.35), Inches(0.2), Inches(2.6), Inches(0.75))
tf_team = tx_team.text_frame
p_tm = tf_team.paragraphs[0]
p_tm.text = "TRIAD 7"
p_tm.font.name = "Arial"
p_tm.font.size = Pt(18)
p_tm.font.bold = True
p_tm.font.color.rgb = C_DARK

p_tm2 = tf_team.add_paragraph()
p_tm2.text = "PS ID: 26265 | AICTE Regulation"
p_tm2.font.name = "Arial"
p_tm2.font.size = Pt(9)
p_tm2.font.bold = True
p_tm2.font.color.rgb = C_BLUE_HDR

# Top Right: SIH Logo text
tx_sih = slide.shapes.add_textbox(Inches(10.4), Inches(0.2), Inches(2.55), Inches(0.75))
tf_sih = tx_sih.text_frame
p_sih = tf_sih.paragraphs[0]
p_sih.text = "SMART INDIA HACKATHON 2026"
p_sih.font.name = "Arial"
p_sih.font.size = Pt(12)
p_sih.font.bold = True
p_sih.font.color.rgb = C_DARK
p_sih.alignment = PP_ALIGN.RIGHT

p_sih2 = tf_sih.add_paragraph()
p_sih2.text = "Regulation Bureau | Software | Idea Deck"
p_sih2.font.name = "Arial"
p_sih2.font.size = Pt(8.5)
p_sih2.font.color.rgb = C_MUTED
p_sih2.alignment = PP_ALIGN.RIGHT

# Bottom Accent Strip
bb = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(7.18), Inches(13.333), Inches(0.32))
style_card(bb, C_BLUE_HDR, C_BLUE_HDR, 0)

tx_num = slide.shapes.add_textbox(Inches(12.7), Inches(7.15), Inches(0.5), Inches(0.32))
p_n = tx_num.text_frame.paragraphs[0]
p_n.text = "3"
p_n.font.name = "Arial"
p_n.font.size = Pt(12)
p_n.font.bold = True
p_n.font.color.rgb = C_WHITE


# =========================================================================
# COLUMN 1 (LEFT): TECH STACK & DETERMINISTIC ALGORITHMS
# Bounds: x = 0.35, width = 3.35, y = 1.05 to 7.05
# =========================================================================

col1_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.35), Inches(1.05), Inches(3.35), Inches(5.98))
style_card(col1_box, C_WHITE, C_BORDER, 1)

# Tech Stack Header
tx_ts = slide.shapes.add_textbox(Inches(0.45), Inches(1.10), Inches(3.15), Inches(0.30))
p_ts = tx_ts.text_frame.paragraphs[0]
p_ts.text = "TECH STACK"
p_ts.font.name = "Arial"
p_ts.font.size = Pt(13)
p_ts.font.bold = True
p_ts.font.color.rgb = C_DARK
p_ts.alignment = PP_ALIGN.CENTER

# 1. DATA SOURCES & BANK INTEGRATION
box_ds = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.45), Inches(1.42), Inches(3.15), Inches(0.72))
style_card(box_ds, C_LIGHT_BG, C_BORDER, 1)
tf_ds = box_ds.text_frame
tf_ds.margin_top = Inches(0.04)
tf_ds.margin_left = Inches(0.06)
p_ds1 = tf_ds.paragraphs[0]
p_ds1.text = "DATA SOURCES & BANK INTEGRATION"
p_ds1.font.name = "Arial"
p_ds1.font.size = Pt(8.5)
p_ds1.font.bold = True
p_ds1.font.color.rgb = C_DARK

p_ds2 = tf_ds.add_paragraph()
p_ds2.text = "• AICTE APH Portal (Affidavit-6, RO Master)\n• Core Banking CBS (SBI, PNB, Canara APIs)\n• NeSL DDE (e-BG / e-FDR) & RBI IFSC Graph"
p_ds2.font.name = "Arial"
p_ds2.font.size = Pt(7.5)
p_ds2.font.color.rgb = C_MUTED

# 2. CORE BACKEND & ORCHESTRATION
box_be = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.45), Inches(2.20), Inches(3.15), Inches(0.72))
style_card(box_be, C_LIGHT_BG, C_BORDER, 1)
tf_be = box_be.text_frame
tf_be.margin_top = Inches(0.04)
tf_be.margin_left = Inches(0.06)
p_be1 = tf_be.paragraphs[0]
p_be1.text = "CORE BACKEND & ORCHESTRATION"
p_be1.font.name = "Arial"
p_be1.font.size = Pt(8.5)
p_be1.font.bold = True
p_be1.font.color.rgb = C_DARK

p_be2 = tf_be.add_paragraph()
p_be2.text = "• Python 3.12 / FastAPI (Async High-SLA Gateway)\n• LangGraph (Stateful Scrutiny Cyclic Workflow)\n• PostgreSQL 16 + pgvector & Redis 7 Queue"
p_be2.font.name = "Arial"
p_be2.font.size = Pt(7.5)
p_be2.font.color.rgb = C_MUTED

# 3. FORENSICS & COMPUTATION
box_fc = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.45), Inches(2.98), Inches(1.53), Inches(0.70))
style_card(box_fc, C_LIGHT_BG, C_BORDER, 1)
tf_fc = box_fc.text_frame
tf_fc.margin_top = Inches(0.04)
tf_fc.margin_left = Inches(0.05)
p_fc1 = tf_fc.paragraphs[0]
p_fc1.text = "AI FORENSICS"
p_fc1.font.name = "Arial"
p_fc1.font.size = Pt(8)
p_fc1.font.bold = True
p_fc1.font.color.rgb = C_DARK
p_fc2 = tf_fc.add_paragraph()
p_fc2.text = "• LayoutLMv3 OCR\n• ELA Forgery Scan\n• Merkle SHA-256"
p_fc2.font.name = "Arial"
p_fc2.font.size = Pt(7)
p_fc2.font.color.rgb = C_MUTED

# 4. FRONTEND
box_fe = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.07), Inches(2.98), Inches(1.53), Inches(0.70))
style_card(box_fe, C_LIGHT_BG, C_BORDER, 1)
tf_fe = box_fe.text_frame
tf_fe.margin_top = Inches(0.04)
tf_fe.margin_left = Inches(0.05)
p_fe1 = tf_fe.paragraphs[0]
p_fe1.text = "FRONTEND (GIGW)"
p_fe1.font.name = "Arial"
p_fe1.font.size = Pt(8)
p_fe1.font.bold = True
p_fe1.font.color.rgb = C_DARK
p_fe2 = tf_fe.add_paragraph()
p_fe2.text = "• React 19 + TypeScript\n• Tailwind (WCAG AA)\n• Bilingual i18n + PWA"
p_fe2.font.name = "Arial"
p_fe2.font.size = Pt(7)
p_fe2.font.color.rgb = C_MUTED

# DETERMINISTIC ALGORITHMS Header
tx_da = slide.shapes.add_textbox(Inches(0.45), Inches(3.72), Inches(3.15), Inches(0.28))
p_da = tx_da.text_frame.paragraphs[0]
p_da.text = "DETERMINISTIC ALGORITHMS"
p_da.font.name = "Arial"
p_da.font.size = Pt(11.5)
p_da.font.bold = True
p_da.font.color.rgb = C_DARK
p_da.alignment = PP_ALIGN.CENTER

# 4 Algorithmic Boxes (2x2 Grid)
b_alg1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.45), Inches(4.02), Inches(1.53), Inches(0.92))
style_card(b_alg1, C_WHITE, C_BORDER, 1)
tf_a1 = b_alg1.text_frame
tf_a1.margin_top = Inches(0.04)
tf_a1.margin_left = Inches(0.05)
p_a1_1 = tf_a1.paragraphs[0]
p_a1_1.text = "Forensic ELA Scan:"
p_a1_1.font.name = "Arial"
p_a1_1.font.size = Pt(7.5)
p_a1_1.font.bold = True
p_a1_1.font.color.rgb = C_DARK
p_a1_2 = tf_a1.add_paragraph()
p_a1_2.text = "Δ_ELA = |I_orig - I_recomp|\nThreshold τ > 0.08 flags forged bank seals & altered digit fonts"
p_a1_2.font.name = "Arial"
p_a1_2.font.size = Pt(6.5)
p_a1_2.font.color.rgb = C_MUTED

b_alg2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.07), Inches(4.02), Inches(1.53), Inches(0.92))
style_card(b_alg2, C_WHITE, C_BORDER, 1)
tf_a2 = b_alg2.text_frame
tf_a2.margin_top = Inches(0.04)
tf_a2.margin_left = Inches(0.05)
p_a2_1 = tf_a2.paragraphs[0]
p_a2_1.text = "Statutory Yield Formula:"
p_a2_1.font.name = "Arial"
p_a2_1.font.size = Pt(7.5)
p_a2_1.font.bold = True
p_a2_1.font.color.rgb = C_DARK
p_a2_2 = tf_a2.add_paragraph()
p_a2_2.text = "A = P(1 + r/n)^(nt)\nLocks P >= APH Norm (₹15L-₹1Cr) with non-callable 10-yr maturity"
p_a2_2.font.name = "Arial"
p_a2_2.font.size = Pt(6.5)
p_a2_2.font.color.rgb = C_MUTED

b_alg3 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.45), Inches(5.00), Inches(1.53), Inches(0.95))
style_card(b_alg3, C_WHITE, C_BORDER, 1)
tf_a3 = b_alg3.text_frame
tf_a3.margin_top = Inches(0.04)
tf_a3.margin_left = Inches(0.05)
p_a3_1 = tf_a3.paragraphs[0]
p_a3_1.text = "IFSC Merge Graph:"
p_a3_1.font.name = "Arial"
p_a3_1.font.size = Pt(7.5)
p_a3_1.font.bold = True
p_a3_1.font.color.rgb = C_DARK
p_a3_2 = tf_a3.add_paragraph()
p_a3_2.text = "DAG traversal resolves bank mergers (e.g., Syndicate → Canara) across 10-yr decadal lock-in"
p_a3_2.font.name = "Arial"
p_a3_2.font.size = Pt(6.5)
p_a3_2.font.color.rgb = C_MUTED

b_alg4 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.07), Inches(5.00), Inches(1.53), Inches(0.95))
style_card(b_alg4, C_WHITE, C_BORDER, 1)
tf_a4 = b_alg4.text_frame
tf_a4.margin_top = Inches(0.04)
tf_a4.margin_left = Inches(0.05)
p_a4_1 = tf_a4.paragraphs[0]
p_a4_1.text = "Multi-Bureau Release:"
p_a4_1.font.name = "Arial"
p_a4_1.font.size = Pt(7.5)
p_a4_1.font.bold = True
p_a4_1.font.color.rgb = C_DARK
p_a4_2 = tf_a4.add_paragraph()
p_a4_2.text = "Clearance = (PGRC == 0) ∧ (Vigilance == 0) ∧ (Grants == 0) for zero unauthorized release"
p_a4_2.font.name = "Arial"
p_a4_2.font.size = Pt(6.5)
p_a4_2.font.color.rgb = C_MUTED

# Bottom Algo Banner: Joint-Lien Regex
b_alg5 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.45), Inches(6.01), Inches(3.15), Inches(0.92))
style_card(b_alg5, C_WHITE, C_BORDER, 1)
tf_a5 = b_alg5.text_frame
tf_a5.margin_top = Inches(0.04)
tf_a5.margin_left = Inches(0.05)
p_a5_1 = tf_a5.paragraphs[0]
p_a5_1.text = "Mandatory Joint-Lien Legal Regex Guardrail:"
p_a5_1.font.name = "Arial"
p_a5_1.font.size = Pt(7.5)
p_a5_1.font.bold = True
p_a5_1.font.color.rgb = C_DARK
p_a5_2 = tf_a5.add_paragraph()
p_a5_2.text = "(?=.*Regional Officer, AICTE)(?=.*Irrevocable Lien)(?=.*Joint Account)\nStrict post-OCR regex blocks unilateral encashment without explicit RO NOC."
p_a5_2.font.name = "Arial"
p_a5_2.font.size = Pt(6.5)
p_a5_2.font.color.rgb = C_MUTED


# =========================================================================
# COLUMN 2 (CENTER): SYSTEM WORKFLOW
# Bounds: x = 3.82, width = 5.95, y = 1.05 to 7.05
# =========================================================================

col2_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.82), Inches(1.05), Inches(5.95), Inches(5.98))
style_card(col2_box, C_WHITE, C_BORDER, 1)

# Header
tx_wf = slide.shapes.add_textbox(Inches(3.92), Inches(1.10), Inches(5.75), Inches(0.30))
p_wf = tx_wf.text_frame.paragraphs[0]
p_wf.text = "SYSTEM WORKFLOW"
p_wf.font.name = "Arial"
p_wf.font.size = Pt(13)
p_wf.font.bold = True
p_wf.font.color.rgb = C_DARK
p_wf.alignment = PP_ALIGN.CENTER

# 1. MULTI-SOURCE INGESTION CONTAINER
b_ingest = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.95), Inches(1.42), Inches(5.70), Inches(0.82))
style_card(b_ingest, C_CARD_BLUE, C_BORDER, 1)

# Ingestion Title Textbox
tx_ig_title = slide.shapes.add_textbox(Inches(3.95), Inches(1.43), Inches(5.70), Inches(0.24))
p_igt = tx_ig_title.text_frame.paragraphs[0]
p_igt.text = "MULTI-SOURCE RECORD & INSTRUMENT INGESTION"
p_igt.font.name = "Arial"
p_igt.font.size = Pt(8.8)
p_igt.font.bold = True
p_igt.font.color.rgb = C_DARK
p_igt.alignment = PP_ALIGN.CENTER

# 4 Ingestion Streams
stream_w = 1.32
gap_s = 0.08
for i, (title, desc) in enumerate([
    ("Institutional Upload", "FDR scans, Affidavit-6, Trustee DSC"),
    ("Regulatory APH", "AICTE Handbook, RO Jurisdiction"),
    ("Bank CBS Feeds", "NeSL e-BG / Branch Verification"),
    ("National Bureaus", "PGRC Grievance, Vigilance, Grants")
]):
    sx = 4.03 + i * (stream_w + gap_s)
    sb = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(sx), Inches(1.68), Inches(stream_w), Inches(0.50))
    style_card(sb, C_WHITE, C_BORDER, 1)
    tf_sb = sb.text_frame
    tf_sb.margin_top = Inches(0.02)
    tf_sb.margin_left = Inches(0.04)
    tf_sb.margin_right = Inches(0.04)
    p_sb1 = tf_sb.paragraphs[0]
    p_sb1.text = title
    p_sb1.font.name = "Arial"
    p_sb1.font.size = Pt(6.8)
    p_sb1.font.bold = True
    p_sb1.font.color.rgb = C_DARK
    p_sb2 = tf_sb.add_paragraph()
    p_sb2.text = desc
    p_sb2.font.name = "Arial"
    p_sb2.font.size = Pt(5.6)
    p_sb2.font.color.rgb = C_MUTED

# 2. DATA ACQUISITION LAYER
b_acq = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.95), Inches(2.30), Inches(5.70), Inches(0.38))
style_card(b_acq, C_NAVY_BOX, C_BORDER, 1)
tf_acq = b_acq.text_frame
tf_acq.margin_top = Inches(0.02)
p_acq1 = tf_acq.paragraphs[0]
p_acq1.text = "DATA ACQUISITION LAYER"
p_acq1.font.name = "Arial"
p_acq1.font.size = Pt(8.5)
p_acq1.font.bold = True
p_acq1.font.color.rgb = C_DARK
p_acq1.alignment = PP_ALIGN.CENTER
p_acq2 = tf_acq.add_paragraph()
p_acq2.text = "APIs (REST / Webhooks) | MeriPehchaan SSO | AES-256 KMS Encryption | Format Normalization"
p_acq2.font.name = "Arial"
p_acq2.font.size = Pt(6.8)
p_acq2.font.color.rgb = C_MUTED
p_acq2.alignment = PP_ALIGN.CENTER

# 3. DATA PROCESSING & STORAGE
b_proc = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.95), Inches(2.74), Inches(5.70), Inches(0.82))
style_card(b_proc, C_LIGHT_BG, C_BORDER, 1)

tx_pr_title = slide.shapes.add_textbox(Inches(3.95), Inches(2.75), Inches(5.70), Inches(0.24))
p_prt = tx_pr_title.text_frame.paragraphs[0]
p_prt.text = "DATA PROCESSING & EVIDENCE STORAGE"
p_prt.font.name = "Arial"
p_prt.font.size = Pt(8.8)
p_prt.font.bold = True
p_prt.font.color.rgb = C_DARK
p_prt.alignment = PP_ALIGN.CENTER

for i, (title, desc) in enumerate([
    ("Preprocessing", "Deskew, denoise, contrast clean"),
    ("Spatial Mapping", "AICTE ID to RO & IFSC Remap"),
    ("Forensics OCR", "LayoutLMv3 & ELA pixel scan"),
    ("PostgreSQL 16", "Encrypted store + pgvector")
]):
    px = 4.03 + i * (stream_w + gap_s)
    pb = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(px), Inches(3.00), Inches(stream_w), Inches(0.50))
    style_card(pb, C_WHITE, C_BORDER, 1)
    tf_pb = pb.text_frame
    tf_pb.margin_top = Inches(0.02)
    tf_pb.margin_left = Inches(0.04)
    tf_pb.margin_right = Inches(0.04)
    p_pb1 = tf_pb.paragraphs[0]
    p_pb1.text = title
    p_pb1.font.name = "Arial"
    p_pb1.font.size = Pt(6.8)
    p_pb1.font.bold = True
    p_pb1.font.color.rgb = C_DARK
    p_pb2 = tf_pb.add_paragraph()
    p_pb2.text = desc
    p_pb2.font.name = "Arial"
    p_pb2.font.size = Pt(5.6)
    p_pb2.font.color.rgb = C_MUTED

# 4. AGENT GRAPH & REASONING ENGINE (Left Split) & DOMAIN MODULES (Right Split)
# Left: Agent Graph
b_ag = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.95), Inches(3.62), Inches(2.70), Inches(2.12))
style_card(b_ag, C_PURPLE_BOX, C_BORDER, 1)
tf_ag = b_ag.text_frame
tf_ag.margin_top = Inches(0.05)
tf_ag.margin_left = Inches(0.08)
p_ag1 = tf_ag.paragraphs[0]
p_ag1.text = "AGENT GRAPH & REASONING ENGINE"
p_ag1.font.name = "Arial"
p_ag1.font.size = Pt(8.5)
p_ag1.font.bold = True
p_ag1.font.color.rgb = C_DARK

for title, desc in [
    ("• Intent & Clause Parsing", "Maps queries to APH regulations"),
    ("• Tool & Validator Selection", "Invokes OCR, CBS check, ELA"),
    ("• Context Retrieval (pgvector)", "Pulls exact AICTE handbook clauses"),
    ("• Scrutiny Decision Logic", "Deterministic + Explainable (XAI)")
]:
    p_t = tf_ag.add_paragraph()
    p_t.text = title
    p_t.font.name = "Arial"
    p_t.font.size = Pt(7)
    p_t.font.bold = True
    p_t.font.color.rgb = C_DARK

    p_d = tf_ag.add_paragraph()
    p_d.text = "   " + desc
    p_d.font.name = "Arial"
    p_d.font.size = Pt(6)
    p_d.font.color.rgb = C_MUTED

# Right: Domain Modules
b_dm = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.75), Inches(3.62), Inches(2.90), Inches(2.12))
style_card(b_dm, C_CARD_BLUE, C_BORDER, 1)
tf_dm = b_dm.text_frame
tf_dm.margin_top = Inches(0.05)
tf_dm.margin_left = Inches(0.08)
p_dm1 = tf_dm.paragraphs[0]
p_dm1.text = "DOMAIN REGULATORY MODULES"
p_dm1.font.name = "Arial"
p_dm1.font.size = Pt(8.5)
p_dm1.font.bold = True
p_dm1.font.color.rgb = C_DARK

for title, desc in [
    ("Lien Validity [LIEN]", "Joint name (Trustee+RO), irrevocable lien, 8-10yr lock"),
    ("APH Norms [NORM]", "Statutory quantum (₹15L-₹1Cr), program & type criteria"),
    ("Bank CBS Handshake [BANK]", "Branch maker-checker verification challan & balance audit"),
    ("Multi-Bureau Clearance [DUES]", "Parallel checks: Student dues (PGRC), Vigilance, Grants")
]:
    p_t = tf_dm.add_paragraph()
    p_t.text = title
    p_t.font.name = "Arial"
    p_t.font.size = Pt(7.2)
    p_t.font.bold = True
    p_t.font.color.rgb = C_DARK

    p_d = tf_dm.add_paragraph()
    p_d.text = "   " + desc
    p_d.font.name = "Arial"
    p_d.font.size = Pt(6.2)
    p_d.font.color.rgb = C_MUTED

# 5. APPLICATION LAYER & OUTPUT IMPACT
b_app = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.95), Inches(5.82), Inches(2.40), Inches(1.12))
style_card(b_app, C_LIGHT_BG, C_BORDER, 1)
tf_ap = b_app.text_frame
tf_ap.margin_top = Inches(0.04)
tf_ap.margin_left = Inches(0.06)
p_ap1 = tf_ap.paragraphs[0]
p_ap1.text = "APPLICATION LAYER"
p_ap1.font.name = "Arial"
p_ap1.font.size = Pt(8)
p_ap1.font.bold = True
p_ap1.font.color.rgb = C_DARK

p_ap2 = tf_ap.add_paragraph()
p_ap2.text = "💻 Web Command Dashboard\n   (AICTE HQ / RO Scrutiny Workspace)\n📱 Mobile PWA Verification\n   (College Trustee & Bank Manager)"
p_ap2.font.name = "Arial"
p_ap2.font.size = Pt(6.8)
p_ap2.font.color.rgb = C_MUTED

# Output & Impact Box
b_out = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.45), Inches(5.82), Inches(3.20), Inches(1.12))
style_card(b_out, C_WHITE, C_BORDER, 1)
tf_out = b_out.text_frame
tf_out.margin_top = Inches(0.04)
tf_out.margin_left = Inches(0.06)
p_ou1 = tf_out.paragraphs[0]
p_ou1.text = "OUTPUT & REGULATORY IMPACT"
p_ou1.font.name = "Arial"
p_ou1.font.size = Pt(8)
p_ou1.font.bold = True
p_ou1.font.color.rgb = C_DARK

p_ou2 = tf_out.add_paragraph()
p_ou2.text = "• Discrepancy Radar: Real-time forgery detection\n• 90/60/30-Day Alerts: Proactive expiry escalation\n• Express Refund NOC: Slashes turnaround 360d → 7d\n• Trust QR Badge: Public tamper-proof accreditation"
p_ou2.font.name = "Arial"
p_ou2.font.size = Pt(6.8)
p_ou2.font.color.rgb = C_MUTED


# =========================================================================
# COLUMN 3 (RIGHT): IMPLEMENTATION PLAN
# Bounds: x = 9.87, width = 3.10, y = 1.05 to 7.05
# =========================================================================

col3_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.87), Inches(1.05), Inches(3.10), Inches(5.98))
style_card(col3_box, C_WHITE, C_BORDER, 1)

# Header
tx_ip = slide.shapes.add_textbox(Inches(9.97), Inches(1.10), Inches(2.90), Inches(0.30))
p_ip = tx_ip.text_frame.paragraphs[0]
p_ip.text = "IMPLEMENTATION PLAN"
p_ip.font.name = "Arial"
p_ip.font.size = Pt(13)
p_ip.font.bold = True
p_ip.font.color.rgb = C_DARK
p_ip.alignment = PP_ALIGN.CENTER

# 6 Phased Milestone Cards
milestones = [
    ("Requirement & Data Sourcing",
     "Map AICTE APH Chapter 4 norms, synthesize 100+ multi-bank FDR datasets (SBI, PNB, Canara), design PostgreSQL 16 schema."),
    ("Adapter & Forensics Development",
     "Build LayoutLMv3 spatial OCR parser, OpenCV Error Level Analysis (ELA) for image forgery detection, and RBI IFSC graph remapper."),
    ("Agent Graph & State Machine",
     "Compile 4-node LangGraph cyclic workflow (Scrutiny → Bank Verification → Multi-Bureau) with human-in-the-loop review interrupts."),
    ("Regulatory Engine & Guardrails",
     "Anchor APH compliance validator to deterministic regex checks; build Celery/Redis cron pipeline for proactive 90/60/30-day alerts."),
    ("Dual-Surface UI Development",
     "Build WCAG 2.1 AA bilingual web command center (React 19) + lightweight mobile verification portal for Branch Managers & Trustees."),
    ("Testing & Live Validation",
     "100% OWASP Top-10 VAPT compliance, SHA-256 Merkle audit trail verification, end-to-end simulation across 10 Regional Offices.")
]

card_y = 1.45
card_h = 0.84
gap = 0.085

for i, (m_title, m_desc) in enumerate(milestones):
    mb = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.97), Inches(card_y), Inches(2.90), Inches(card_h))
    style_card(mb, C_CARD_BLUE, C_BORDER, 1)
    tf_mb = mb.text_frame
    tf_mb.margin_top = Inches(0.04)
    tf_mb.margin_left = Inches(0.06)
    tf_mb.margin_right = Inches(0.06)

    p_m1 = tf_mb.paragraphs[0]
    p_m1.text = f"{i+1}. {m_title}"
    p_m1.font.name = "Arial"
    p_m1.font.size = Pt(8.2)
    p_m1.font.bold = True
    p_m1.font.color.rgb = C_DARK

    p_m2 = tf_mb.add_paragraph()
    p_m2.text = m_desc
    p_m2.font.name = "Arial"
    p_m2.font.size = Pt(6.8)
    p_m2.font.color.rgb = C_MUTED

    card_y += card_h + gap

# Save Presentation
output_path = "/Users/ayyapparaja/Documents/SIH/technical_approach_slide_final.pptx"
prs.save(output_path)
print(f"Presentation saved successfully to: {output_path}")
