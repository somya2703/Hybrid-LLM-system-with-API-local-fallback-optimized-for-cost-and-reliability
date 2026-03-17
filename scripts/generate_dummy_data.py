from pathlib import Path
from fpdf import FPDF
import os

DATA_DIR = Path("dummy_data")
DATA_DIR.mkdir(exist_ok=True)


def create_pdf(filename, title, content):

    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")

    pdf.ln(5)

    # Body text
    pdf.set_font("Helvetica", size=12)

    for i, line in enumerate(content, 1):

        text = f"{i}. {line}"

        pdf.multi_cell(
            180,   # fixed width avoids rendering bug
            8,
            text
        )

        pdf.ln(1)

    os.makedirs("dummy_data", exist_ok=True)

    pdf.output(f"dummy_data/{filename}")

def main():
    safety_content = [
        "Always wear safety gloves when operating machinery.",
        "Protective eyewear is mandatory inside the production floor.",
        "Follow lockout-tagout procedures before machine maintenance.",
        "Report unsafe conditions immediately to your supervisor.",
        "Keep emergency exits clear at all times.",
        "Ensure machines are powered off before cleaning."
    ]

    onboarding_content = [
        "Complete HR documentation on your first day.",
        "Attend the mandatory workplace safety training.",
        "Receive your employee ID and system credentials.",
        "Meet your assigned mentor for the first week.",
        "Review company policies and code of conduct.",
        "Set up your workstation and communication tools."
    ]

    it_support_content = [
        "Contact the IT helpdesk for system access issues.",
        "Use the company VPN when accessing internal systems remotely.",
        "Reset passwords using the internal identity portal.",
        "Report suspicious emails to the security team.",
        "Install required software through the company software center."
    ]

    create_pdf("safety_manual.pdf", "Safety Manual", safety_content)
    create_pdf("onboarding_guide.pdf", "Employee Onboarding Guide", onboarding_content)
    create_pdf("it_support_manual.pdf", "IT Support Manual", it_support_content)

    print("Dummy training PDFs generated in ./dummy_data/")


if __name__ == "__main__":
    main()