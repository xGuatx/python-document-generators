# Python Document Generators

Project for automatic document generation (PDF and DOCX) using Python, with reusable and anonymized templates.

## Description

This repository contains template scripts to generate:
- **Professional Resume (PDF)**: Modern layout with columns, skills, and timeline.
- **Internship Report (DOCX)**: Formal report with predefined structure.
- **Runbook / Crisis Plan (DOCX)**: 1-page emergency procedure for IT/SOC teams.

**Note:** All scripts are anonymized. You must fill in the `CONFIGURATION` sections in each file before use.

## Structure

```
python-document-generators/
|-- generate_cv_template.py                  # Resume Template (ReportLab)
|-- generate_internship_report_template.py   # Internship Report Template (python-docx)
|-- generate_runbook_template.py             # Runbook Template (python-docx)
+-- README.md
```

## Prerequisites

- Python 3.8+
- Libraries: `python-docx`, `reportlab`

## Installation

```bash
# 1. Create virtual environment
python3 -m venv venv

# 2. Activate the environment
source venv/bin/activate

# 3. Install dependencies
pip install python-docx reportlab
```

## Usage

### 1. Generate a Resume (PDF)

Edit `generate_cv_template.py` to modify the `CANDIDATE_INFO` dictionary and the lists (`SKILLS`, `EXPERIENCES`).

```bash
python3 generate_cv_template.py
# Output: CV_Jean_Dupont.pdf
```

### 2. Generate an Internship Report (DOCX)

Edit `generate_internship_report_template.py` to configure `REPORT_INFO` (Name, Company, Degree, etc.).

```bash
python3 generate_internship_report_template.py
# Output: Rapport_Stage_Template.docx
```

### 3. Generate a Runbook (DOCX)

Edit `generate_runbook_template.py` to customize `COMPANY_NAME` and the `RUNBOOK` steps.

```bash
python3 generate_runbook_template.py
# Output: Runbook_Template.docx
```

## Customization

Each script has a **CONFIGURATION** section at the top of the file.
It is designed to be easily modified without touching the graphical generation logic.

## Security & Privacy

- **No real data** should be committed to this repo.
- Templates use fictitious data ("Jean Dupont", "Company XYZ").
- Add your generated files (`*.pdf`, `*.docx`) to `.gitignore` if necessary (already configured by default).
