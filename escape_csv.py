import csv
import os
import sys

REQUIRED_FIELDS = {'email', 'first_name', 'last_name', 'department'}
FIELD_MAPPINGS = {
    'managerEmail': 'manager_email',
    'firstName': 'first_name',
    'lastName': 'last_name',
    'businessUnit': 'business_unit',
    'startDate': 'start_date',
    'endDate': 'end_date'
}

def check_header(header):
    warnings = []
    errors = []
    header_set = set(field.lower() for field in header)

    # Check for required fields
    missing_fields = REQUIRED_FIELDS - header_set
    if missing_fields:
        errors.append(f"Error: Missing required fields: {', '.join(missing_fields)}")

    # Check for field naming issues
    for field in header:
        if field in FIELD_MAPPINGS:
            warnings.append(f"Warning: '{field}' should be '{FIELD_MAPPINGS[field]}'")

    return warnings, errors

def escape_csv_fields(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Read and check the header
        header = next(reader, None)
        if header:
            warnings, errors = check_header(header)
            
            for warning in warnings:
                print(warning)
            for error in errors:
                print(error)
            
            if errors or warnings:
                print("Aborting due to header errors.")
                sys.exit(1)
            
            # Write the header without escaping
            writer.writerow(header)
        
        # Write the rest of the rows with escaping
        writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
        for row in reader:
            writer.writerow(row)

def generate_output_filename(input_filename):
    base, ext = os.path.splitext(input_filename)
    return f"{base}_escaped{ext}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_csv_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = generate_output_filename(input_file)
    
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    
    escape_csv_fields(input_file, output_file)
    print(f"CSV escaping complete. Result saved to '{output_file}'.")

if __name__ == "__main__":
    main()
