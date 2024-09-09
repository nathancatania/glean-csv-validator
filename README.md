# Glean CSV Validator for People Data
This is a quick script to escape all data in a CSV file that contains people data to be uploaded to Glean. The script will also check to ensure all mandatory header fields are present, and warn if a header field is spelt incorrectly (e.g. `managerEmail` instead of `manager_email`)

## Usage
```
python escape_csv.py <input_filename>
```

The escaped file will be saved in the same location as the input filename and will have `_escaped` suffixed.

For example:

```
python escape_csv.py people_data.csv

CSV escaping complete. Result saved to 'people_data_escaped.csv'.
```

## Field Validation
The script will check to ensure all mandatory header fields are present:

* `email`
* `first_name`
* `last_name`
* `department`

It will also check if a field is spelt incorrectly. For example:

* `managerEmail` ❌ -> `manager_email` ✅
* `firstName` ❌ -> `first_name` ✅

```
python escape_csv.py people.csv

Warning: 'startDate' should be 'start_date'
Warning: 'managerEmail' should be 'manager_email'
Error: Missing required fields: first_name
Aborting due to header errors.
```
