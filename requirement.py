import google.generativeai as genai

api_key = "AIzaSyB01ouUyKFz7IGzCgEnBdHnEY9QRQXPfIQ"
genai.configure(api_key=api_key)

def generate_requirements(project_description: str):
    prompt = f"""
    Given the following project description, generate a detailed requirement analysis.
    If any of the sections below are not applicable to the project, please ignore them and do not include them in the analysis:

    Project Description:
    {project_description}
    
    The analysis should include:
    1. Project Overview
    2. Scope of Services
    3. Performance Period and Contract Terms
    4. Geographical and Accessibility Requirements
    5. Key Deliverables and Milestones
    6. Service Provider Qualifications
    7. Evaluation Criteria
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

requirements = generate_requirements(description)
print(requirements)