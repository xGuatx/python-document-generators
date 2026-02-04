#!/usr/bin/env python3
"""
Template Générateur de CV professionnel en PDF
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

# ==========================================
# CONFIGURATION - REMPLIR ICI
# ==========================================
CANDIDATE_INFO = {
    "name": "Jean DUPONT",
    "title_Line1": "Ingénieur Logiciel",
    "title_Line2": "Spécialisé Python & DevOps",
    "email": "jean.dupont@email.com",
    "phone": "+33 6 00 00 00 00",
    "address_line1": "10 Rue de la Paix",
    "address_line2": "75000 Paris",
    "output_filename": "CV_Jean_Dupont.pdf"
}

QUALITIES = ["Curieux", "Rigoureux", "Autonome"]

LANGUAGES = [
    ("Anglais", 4),
    ("Espagnol", 2),
    ("Français", 5)
]

SKILLS = [
    ("Python", 5),
    ("Docker", 4),
    ("Linux", 4),
    ("AWS", 3),
    ("Git", 5),
    ("SQL", 3),
    ("Agile", 4),
]

INTERESTS = [
    "Voyages", "Photographie", "Randonnée", "Tech"
]

EXPERIENCES = [
    {
        "date": "de janv. 2023 à aujourd'hui",
        "title": "Ingénieur DevOps",
        "company": "Tech Solutions, Paris",
        "tasks": [
            "Mise en place CI/CD (GitLab CI)",
            "Containerisation d'applications (Docker)",
            "Orchestration Kubernetes",
            "Monitoring avec Prometheus/Grafana"
        ]
    },
    {
        "date": "de sept. 2020 à déc. 2022",
        "title": "Développeur Fullstack",
        "company": "Web Agency, Lyon",
        "tasks": [
            "Développement backend (Django)",
            "Frontend React.js",
            "Optimisation base de données PostgreSQL",
            "Tests unitaires et d'intégration"
        ]
    }
]

FORMATIONS = [
    {
        "date": "2020",
        "title": "Master Informatique",
        "subtitle": "Spécialité Génie Logiciel",
        "location": "Université de Lyon"
    },
    {
        "date": "2018",
        "title": "Licence Informatique",
        "subtitle": "",
        "location": "Université de Lyon"
    }
]

# ==========================================
# CONSTANTES GRAPHIQUES
# ==========================================
DARK_GRAY = colors.HexColor("#3D4449")
LIGHT_GRAY = colors.HexColor("#E8E8E8")
WHITE = colors.white
TEXT_GRAY = colors.HexColor("#555555")

def draw_dots(c, x, y, level, max_level=5):
    """Dessine les dots de niveau de compétence"""
    dot_radius = 1.3 * mm
    dot_spacing = 3.8 * mm

    for i in range(max_level):
        if i < level:
            c.setFillColor(LIGHT_GRAY)
        else:
            c.setFillColor(colors.HexColor("#666666"))
        c.circle(x + (i * dot_spacing), y, dot_radius, fill=1, stroke=0)

def draw_header_banner(c, width, height):
    """Dessine le bandeau noir en haut avec le titre"""
    col_width = 85 * mm
    banner_height = 30 * mm

    # Bandeau gris foncé
    c.setFillColor(DARK_GRAY)
    c.rect(0, height - banner_height, col_width, banner_height, fill=1, stroke=0)

    # Titre centré
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 13)
    
    text1 = CANDIDATE_INFO["title_Line1"]
    text_width1 = c.stringWidth(text1, "Helvetica-Bold", 13)
    c.drawString((col_width - text_width1) / 2, height - 13 * mm, text1)

    text2 = CANDIDATE_INFO["title_Line2"]
    text_width2 = c.stringWidth(text2, "Helvetica-Bold", 13)
    c.drawString((col_width - text_width2) / 2, height - 19 * mm, text2)

def draw_left_column(c, width, height):
    """Dessine TOUTE la colonne de gauche sur 1 page"""
    col_width = 85 * mm
    banner_height = 30 * mm

    # Fond gris foncé
    c.setFillColor(DARK_GRAY)
    c.rect(0, 0, col_width, height - banner_height, fill=1, stroke=0)

    x = 15 * mm
    y = height - banner_height - 5 * mm

    c.setFillColor(WHITE)

    # === CONTACT ===
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x, y, "Contact")
    y -= 5 * mm

    c.setFont("Helvetica", 8)
    c.drawString(x, y, CANDIDATE_INFO["name"])
    y -= 3.5 * mm
    c.drawString(x, y, CANDIDATE_INFO["email"])
    y -= 3.5 * mm
    c.drawString(x, y, CANDIDATE_INFO["phone"])
    y -= 3.5 * mm
    c.drawString(x, y, CANDIDATE_INFO["address_line1"])
    y -= 3.5 * mm
    c.drawString(x, y, CANDIDATE_INFO["address_line2"])

    y -= 6 * mm

    # === QUALITÉS ===
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x, y, "Qualités")
    y -= 5 * mm

    c.setFont("Helvetica", 8)
    for q in QUALITIES:
        c.setFillColor(LIGHT_GRAY)
        c.rect(x, y, 1.5 * mm, 1.5 * mm, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.drawString(x + 3 * mm, y, q)
        y -= 3.5 * mm

    y -= 3 * mm

    # === LANGUES ===
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x, y, "Langues")
    y -= 5 * mm

    c.setFont("Helvetica", 8)
    for lang, level in LANGUAGES:
        if level >= 4:
            c.setFillColor(WHITE)
        else:
            c.setFillColor(colors.HexColor("#AAAAAA"))
        c.drawString(x, y, lang)
        draw_dots(c, x + 27 * mm, y + 1 * mm, level, 5)
        y -= 3.5 * mm

    y -= 3 * mm

    # === COMPÉTENCES ===
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x, y, "Compétences")
    y -= 5 * mm

    c.setFont("Helvetica", 7.5)
    for comp, level in SKILLS:
        if level >= 4:
            c.setFillColor(WHITE)
        else:
            c.setFillColor(colors.HexColor("#AAAAAA"))
        c.drawString(x, y, comp)
        draw_dots(c, x + 37 * mm, y + 1 * mm, level, 5)
        y -= 3.3 * mm

    y -= 3 * mm

    # === CENTRES D'INTÉRÊT ===
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x, y, "Centres d'intérêt")
    y -= 5 * mm

    c.setFont("Helvetica", 8)
    for interet in INTERESTS:
        c.setFillColor(LIGHT_GRAY)
        c.rect(x, y, 1.5 * mm, 1.5 * mm, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.drawString(x + 3 * mm, y, interet)
        y -= 3.5 * mm

    return y

def draw_right_column(c, width, height):
    """Colonne de droite"""

    col_start = 85 * mm
    x = col_start + 10 * mm

    # Aligne "Curriculum vitae"
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 16)
    c.drawString(x, height - 18 * mm, "Curriculum vitae")

    # Toute la colonne de droite remonte
    y = height - 32 * mm

    # === EXPÉRIENCE PROFESSIONNELLE ===
    c.setFont("Helvetica-Bold", 13)
    c.drawString(x, y, "Expérience professionnelle")
    y -= 8 * mm

    for exp in EXPERIENCES:
        c.setFont("Helvetica", 8.5)
        c.setFillColor(TEXT_GRAY)
        c.drawString(x, y, exp["date"])
        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(x + 36 * mm, y, exp["title"])
        y -= 3.8 * mm
        c.setFont("Helvetica-Oblique", 8.5)
        c.setFillColor(TEXT_GRAY)
        c.drawString(x + 36 * mm, y, exp["company"])
        c.setFillColor(colors.black)

        y -= 4.5 * mm
        c.setFont("Helvetica", 8)

        for task in exp["tasks"]:
            if task:
                c.drawString(x + 5 * mm, y, "- " + task)
            y -= 3.5 * mm
        
        y -= 3 * mm

    y -= 5 * mm

    # === FORMATION ===
    c.setFont("Helvetica-Bold", 13)
    c.drawString(x, y, "Formation")
    y -= 8 * mm

    for form in FORMATIONS:
        c.setFont("Helvetica", 8.5)
        c.setFillColor(TEXT_GRAY)
        c.drawString(x, y, form["date"])
        c.setFillColor(colors.black)
        
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(x + 36 * mm, y, form["title"])
        y -= 3.8 * mm
        
        if form["subtitle"]:
            c.setFont("Helvetica-Bold", 9.5)
            c.drawString(x + 36 * mm, y, form["subtitle"])
            y -= 3.8 * mm
            
        c.setFont("Helvetica-Oblique", 8.5)
        c.setFillColor(TEXT_GRAY)
        c.drawString(x + 36 * mm, y, form["location"])
        c.setFillColor(colors.black)
        y -= 6 * mm

    return y

def main():
    output_key = CANDIDATE_INFO["output_filename"]
    width, height = A4

    c = canvas.Canvas(output_key, pagesize=A4)
    c.setTitle(f"CV - {CANDIDATE_INFO['name']}")
    c.setAuthor(CANDIDATE_INFO['name'])
    c.setSubject("Curriculum Vitae")

    draw_header_banner(c, width, height)
    y_left = draw_left_column(c, width, height)
    y_right = draw_right_column(c, width, height)

    c.save()

    print(f"CV généré : {output_key}")

if __name__ == "__main__":
    main()
