import google.generativeai as genai

api_key = "AIzaSyB01ouUyKFz7IGzCgEnBdHnEY9QRQXPfIQ"
genai.configure(api_key=api_key)

def generate_recommendations_for_cover_letter_and_contract(project_description: str):
    prompt = f"""
    Given the following project description, provide a **requirement analysis** and **concise recommendations** for the key elements to include in a cover letter and contract proposal.

    Project Description:
    {project_description}

    **Requirement Analysis**:
    Identify the specific needs and requirements of the project from the description, including any important conditions or constraints.

    **Recommendations for the Cover Letter**:
    1. What to include in the introduction.
    2. Relevant experience to highlight.
    3. How to demonstrate the ability to meet the project's requirements.
    4. Suggestions for expressing interest and fit for the project.

    **Recommendations for the Contract Proposal**:
    1. Key points to include in the project scope and deliverables.
    2. Suggestions for outlining timelines, performance periods, and milestones.
    3. Payment terms and budget recommendations.
    4. Qualifications and experience to emphasize.
    5. Compliance requirements (legal, regulatory, accessibility).
    6. Key evaluation criteria to consider for the provider selection.
    """
    
    response = genai.GenerativeModel("gemini-1.5-flash").generate_content([prompt])
    return response.text.strip()

description = """
The Federal Bureau of Prisons, CTS Contracting Office, Washington, D.C. is seeking quotes from sources
that have the ability to provide community-based outpatient substance use disorder, mental health, and sex offender
treatment services for male and female Adults in Custody (AICs) residing at the local Residential Reentry Center (RRC),
and/or on home confinement, or on Federal Location Monitoring (FLM), or, if applicable, reporting to a Day Reporting Center,
in the Memphis, TN area. All treatment services will be required to be performed within a 10-mile radius of Memphis City Hall
located at 125 N Main Street, Memphis, TN 38103, within a 1/2-mile access to community-based transportation, and within the state of Tennessee.
Performance periods under this contract will be for a one-year base period estimated to begin on October 01, 2024, with four (4) one-year option periods,
with services ending (if all options years are renewed) on September 30, 2029. These services required for this contract include a Base Year;
Option Year One, Option Year Two, Option Year Three, and Option Year Four.
"""

recommendations = generate_recommendations_for_cover_letter_and_contract(description)
print(recommendations)