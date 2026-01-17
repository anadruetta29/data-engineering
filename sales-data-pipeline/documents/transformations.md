## Data Cleaning Rules
Remove Duplicates: Ensure there are no repeated records (especially for sale_id and payment_id).

Validate Nulls: Handle or remove missing values in critical fields like price, user_id, or status.

Convert Data Types: Ensure dates are in datetime format and financial values (price, amount) 
are numeric/float.

## Business Rules
Paid Status Only: Filter for records where status = 'PAID'.

Exclude Unpaid Sales: Perform an Inner Join between Sales and Payments to remove any sales that do
not have a matching payment record.

Total Amount Calculation: Use the formula total_amount = quantity * price to verify or 
generate revenue figures.
