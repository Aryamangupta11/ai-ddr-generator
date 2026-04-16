def merge_data(inspection_data, thermal_data):
    prompt = f"""
    You are an expert building diagnostic analyst.

    Merge the following datasets into structured area-wise insights.

    RULES:
    - Use inspection data as primary source
    - Thermal data has NO area mapping → treat it as general observation
    - Do NOT assign thermal data to specific areas unless clearly stated
    - Avoid duplicate issues
    - Highlight uncertainty where needed

    OUTPUT FORMAT:
    Structured JSON with:
    - area
    - issues (combined)
    - thermal_insight
    - notes

    Inspection Data:
    {inspection_data}

    Thermal Data:
    {thermal_data}
    """

    return prompt

def generate_ddr(merged_data):
    prompt = f"""
    You are a professional building inspection consultant.

    Generate a Detailed Diagnostic Report (DDR).

    Structure:

    1. Property Issue Summary
    2. Area-wise Observations
    3. Thermal Observations   
    4. Probable Root Cause
    5. Severity Assessment (with reasoning)
    6. Recommended Actions
    7. Additional Notes
    8. Missing or Unclear Information

    IMPORTANT RULES:
    - Do NOT invent facts
    - If something is missing → write "Not Available"
    - If thermal mapping is unclear → explicitly mention it
    - Keep language simple and client-friendly

    Thermal Rules:
    - Add a separate section called "Thermal Observations"
    - Do NOT repeat thermal insights under each area
    - Summarize all thermal findings in one place

    Severity Rules:
    - Use ONLY: Low, Medium, High
    - Do NOT use terms like Positive/Negative
    - Assign severity based on impact (e.g., dampness = Medium/High)

    Formatting Rules:
    - Make the report concise and structured
    - Use bullet points for clarity
    - Keep language simple and client-friendly
    - Avoid repetition
    - Each area should have:
        - Issue
        - Severity
        - Short note

    The report should look like a professional inspection report given to a client.

    DATA:
    {merged_data}
    """

    return prompt