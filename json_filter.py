import json

def filter_and_trim_proposals(file_path, output_file_path):
    # Define the keys to keep
    keys_to_keep = [
        "PI Name",
        "School",
        "Department",
        "Sponsor Name",
        "Grant Name",
        " Grant Award Amount "
    ]
    
    # Load the JSON data from the file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Filter each proposal to keep only the specified keys and trim spaces for "Grant Award Amount"
    filtered_data = {}
    for key, proposal in data.items():
        filtered_proposal = {k: proposal[k] for k in keys_to_keep if k in proposal}
        # Check if " Grant Award Amount " is in the proposal and trim spaces
        if " Grant Award Amount " in filtered_proposal:
            # Trim leading and trailing spaces and update the key without spaces
            filtered_proposal["Grant Award Amount"] = filtered_proposal.pop(" Grant Award Amount ").strip()
        filtered_data[key] = filtered_proposal
    
    # Write the filtered JSON data to a new file
    with open(output_file_path, 'w') as file:
        json.dump(filtered_data, file, indent=4)

# Call the function with the path to your input and output JSON files
filter_and_trim_proposals('FormattedProposals_Final.json', 'FilteredProposals.json')