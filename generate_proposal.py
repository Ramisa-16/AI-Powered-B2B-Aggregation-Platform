from openai import OpenAI
from datetime import datetime

DEEPSEEK_API_KEY = "sk-861a0b079e1149b4bbf3dfb3d63fbfc8"

notice_details = {
    "noticeId": "fcfd50c27639416bb40825e8a410da8c",
    "title": "30--WEIGHT,COUNTERBALAN",
    "solicitationNumber": "SPE7M125T8227",
    "fullParentPathName": "DEPT OF DEFENSE.DEFENSE LOGISTICS AGENCY.DLA MARITIME.DLA MARITIME COLUMBUS.DLA LAND AND MARITIME",
    "fullParentPathCode": "097.97AS.DLA MARITIME.DLA MARITIME COLUMBS.SPE7M1",
    "postedDate": "2025-03-16",
    "type": "Combined Synopsis/Solicitation",
    "baseType": "Combined Synopsis/Solicitation",
    "archiveType": "autocustom",
    "archiveDate": "2025-04-26",
    "typeOfSetAsideDescription": "Total Small Business Set-Aside (FAR 19.5)",
    "typeOfSetAside": "SBA",
    "responseDeadLine": "2025-03-27",
    "naicsCode": "333613",
    "naicsCodes": ["333613"],
    "classificationCode": "30",
    "active": "Yes",
    "award": "",
    "pointOfContact": [
        {
            "fax": "",
            "type": "primary",
            "email": "DibbsBSM@dla.mil",
            "phone": "",
            "title": "",
            "fullName": "Questions regarding this solicitation should be emailed to the buyer listed in block 5 of the solicitation document which can be found under the Additional Information link.\nIf the Additional Information link does not work, please go to https://www.dibbs.bsm.dla.mil/Solicitations/ and type the solicitation number in the Global Search box.\n"
        }
    ],
    "description": "https://api.sam.gov/prod/opportunities/v1/noticedesc?noticeid=fcfd50c27639416bb40825e8a410da8c",
    "organizationType": "OFFICE",
    "officeAddress": {
        "zipcode": "43218-3990",
        "city": "COLUMBUS",
        "countryCode": "USA",
        "state": "OH"
    },
    "placeOfPerformance": "",
    "additionalInfoLink": "",
    "uiLink": "https://sam.gov/opp/fcfd50c27639416bb40825e8a410da8c/view",
    "links": [
        {
            "rel": "self",
            "href": "https://api.sam.gov/prod/opportunities/v2/search?noticeid=fcfd50c27639416bb40825e8a410da8c&limit=1"
        }
    ],
    "resourceLinks": ""
}

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

company_details = {
    "companyName": "TechSolutions Inc.",
    "streetAddress": "123 Business Rd.",
    "companyEmail": "info@techsolutions.com",
    "city": "Tech City",
    "companyPhone": "+1 234 567 8901",
    "postalZipcode": "98765",
    "companyWebsite": "https://www.techsolutions.com",
    "stateProvRegion": "TechState"
}

budget = 500000  

def generate_cover_letter_and_proposal(description, notice_details, company_details, budget):
    client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

    prompt = f"""
    Generate a professional government contract submission containing:
    1. Formal Cover Letter
    2. Detailed Service Proposal

    **Contract Opportunity Details:**
    {description}

    **Solicitation Information:**
    - Title: {notice_details['title']}
    - Number: {notice_details['solicitationNumber']}
    - Posted: {notice_details['postedDate']}
    - Due: {notice_details['responseDeadLine']}
    - Set-Aside: {notice_details['typeOfSetAsideDescription']}
    - NAICS: {notice_details['naicsCode']}
    - Contact: {notice_details['pointOfContact'][0]['fullName']}
    - Email: {notice_details['pointOfContact'][0]['email']}

    **Company Details (Only the following info is required):**
    - Name: {company_details['companyName']}
    - Address: {company_details['streetAddress']}, {company_details['city']}, {company_details['stateProvRegion']} {company_details['postalZipcode']}
    - Email: {company_details['companyEmail']}
    - Phone: {company_details['companyPhone']}
    - Website: {company_details['companyWebsite']}

    **Requirements:**
    - Cover Letter (1 page):
      * Company introduction
      * Statement of qualifications
      * Expression of interest
      * Contact information

    - Technical Proposal (2-3 pages):
      * Understanding of requirements
      * Technical approach/methodology
      * Relevant experience
      * Staffing plan
      * Quality control measures

    - Business Proposal (1-2 pages):
      * Pricing structure: Estimated project cost is ${budget}. Detailed budget breakdown available upon request.
      * Payment terms with real amount in USD
      * Timeline
      * Terms and conditions

    **Formatting:**
    - No tables (use bullet points instead)
    - Professional business tone
    - Clear section headings

    **Important Instructions:**
    - Use only the company details as provided in the `company_details` object above. **Do not include any placeholders like `[Your Name]` or `[Your Title]`**, as those are not required for this submission.
    - Ensure that all information is presented clearly and professionally.
    - Only include the details mentioned in the `company_details` field and omit all other extra information that is not part of the data provided.
    - Don't write headings like 'End of Proposal'.
    """

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a government contracts specialist helping to prepare a competitive proposal submission."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=5000,
        stream=False
    )

    return response.choices[0].message.content


try:
    print("Generating government contract proposal...")
    proposal_text = generate_cover_letter_and_proposal(description, notice_details, company_details, budget)
    print("\n" + "=" * 80)
    print(proposal_text)
    print("=" * 80)

    with open("government_proposal.md", "w") as file:
        file.write(proposal_text)
    print("\nProposal saved to government_proposal.md")

except Exception as error:
    print(f"An error occurred: {str(error)}")