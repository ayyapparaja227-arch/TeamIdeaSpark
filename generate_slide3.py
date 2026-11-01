import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

prs = pptx.Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(blank_layout)

# Colors matching the reference image theme
COLOR_BG = RGBColor(248, 250, 252) # Light neutral background
COLOR_PRIMARY = RGBColor(15, 23, 42) # Slate 900
COLOR_BLUE_HEADER = RGBColor(2, 132, 199) # Blue 600
COLOR_BOX_BG = RGBColor(255, 255, 255) # White card
COLOR_BORDER = RGBColor(203, 213, 225) # Slate 300
COLOR_PILL_BG = RGBColor(241, 245, 249) # Slate 100
COLOR_HIGHLIGHT_RED = RGBColor(225, 29, 72) # Rose 600
COLOR_HIGHLIGHT_BLUE = RGBColor(14, 116, 144) # Cyan 700
COLOR_GREEN = RGBColor(16, 149, 119) # Emerald 600
COLOR_AMBER = RGBColor(217, 119, 6) # Amber 600
COLOR_ACCENT_BG = RGBColor(224, 242, 254) # Light Sky Blue

def add_header():
    # Top title: TECHNICAL APPROACH
    txBox = slide.shapes.add_textbox(Inches(3.0), Inches(0.25), Inches(7.333), Inches(0.8))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "TECHNICAL APPROACH"
    p.font.name = "Georgia"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY
    p.alignment = PP_ALIGN.CENTER

    # Subtitle
    p2 = tf.add_paragraph()
    p2.text = "Centralized Architecture, Multi-Modal Forensics & Autonomous Scrutiny Workflow"
    p2.font.name = "Arial"
    p2.font.size = Pt(11)
    p2.font.color.rgb = RGBColor(100, 116, 139)
    p2.alignment = PP_ALIGN.CENTER

    # Top Left: Team Name / ID
    tb_left = slide.shapes.add_textbox(Inches(0.4), Inches(0.25), Inches(2.5), Inches(0.8))
    tf_l = tb_left.text_frame
    p_l = tf_l.paragraphs[0]
    p_l.text = "TRIAD 7"
    p_l.font.name = "Arial"
    p_l.font.size = Pt(18)
    p_l.font.bold = True
    p_l.font.color.rgb = COLOR_PRIMARY

    p_l2 = tf_l.add_paragraph()
    p_l2.text = "Problem ID: 26265 | AICTE"
    p_l2.font.name = "Arial"
    p_l2.font.size = Pt(9)
    p_l2.font.color.rgb = RGBColor(100, 116, 139)

    # Top Right: SIH 2026 Badge
    tb_right = slide.shapes.add_textbox(Inches(10.6), Inches(0.25), Inches(2.3), Inches(0.8))
    tf_r = tb_right.text_frame
    p_r = tf_r.paragraphs[0]
    p_r.text = "SMART INDIA\nHACKATHON 2026"
    p_r.font.name = "Arial"
    p_r.font.size = Pt(13)
    p_r.font.bold = True
    p_r.font.color.rgb = COLOR_PRIMARY
    p_r.alignment = PP_ALIGN.RIGHT

    # Bottom Right Page Number
    tb_num = slide.shapes.add_textbox(Inches(12.7), Inches(7.1), Inches(0.5), Inches(0.3))
    p_num = tb_num.text_frame.paragraphs[0]
    p_num.text = "3"
    p_num.font.name = "Arial"
    p_num.font.size = Pt(12)
    p_num.font.bold = True
    p_num.font.color.rgb = RGBColor(255, 255, 255)

add_header()

# Bottom bar for slide number
bb = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(7.15), Inches(13.333), Inches(0.35))
bb.fill.solid()
bb.fill.fore_color.rgb = RGBColor(2, 132, 199)
bb.line.fill.background()

# Slide 3 number text
num_box = slide.shapes.add_textbox(Inches(12.7), Inches(7.12), Inches(0.5), Inches(0.35))
p_nb = num_box.text_frame.paragraphs[0]
p_nb.text = "3"
p_nb.font.name = "Arial"
p_nb.font.size = Pt(12)
p_nb.font.bold = True
p_nb.font.color.rgb = RGBColor(255, 255, 255)

# Save presentation
prs.save('/Users/ayyapparaja/Documents/SIH/technical_approach_slide_test.pptx')
print("Base slide created successfully")
