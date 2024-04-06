import json
import re

def replace_nan_with_null(proposal):
    """
    Replace 'NaN' string values with None in a proposal dictionary.
    """
    return {k: (None if v == 'NaN' else v) for k, v in proposal.items()}

def correct_and_format_json(file_path):
    # Read the original malformed JSON data
    with open(file_path, 'r') as file:
        content = file.read()
        # Correct the structure by wrapping objects in an array
        # This regex replaces '}{', which indicates the end of one object and the start of another, with '},{'
        corrected_content = '[' + re.sub(r'}\s*{', '},{', content) + ']'

    # Parse the corrected JSON string into a Python object
    proposals = json.loads(corrected_content)

    # Process each proposal to replace 'NaN' with None
    formatted_proposals = [replace_nan_with_null(proposal) for proposal in proposals]

    # Create a new dictionary with top-level keys
    final_proposals = {str(i): proposal for i, proposal in enumerate(formatted_proposals)}

    # Write the formatted JSON data back to a new file
    with open('FormattedProposals.json', 'w') as file:
        json.dump(final_proposals, file, indent=4)
        
    with open('FormattedProposals.json', 'r') as file:
        content = json.load(file)

    # Iterate through each proposal and replace 'NaN' with None (null in JSON)
    for key, proposal in content.items():
        for sub_key, value in proposal.items():
            if value == 'NaN':  # Check if the value is 'NaN'
                content[key][sub_key] = None  # Replace 'NaN' with None
    
    with open('FormattedProposals_Final.json', 'w') as file:
        json.dump(content, file, indent=4)

# Correct the structure of the JSON data and replace 'NaN' with 'null'
correct_and_format_json('Proposals.json')