import re

# ---------------------------------------------------
# 1. re.match(): Check if string starts with EMP + 3 digits
# ---------------------------------------------------
employee_id = "EMP123 works in IT department"

match_emp = re.match(r"(EMP)(\d{3})", employee_id)

if match_emp:
    print("Valid Employee ID found")
    print("Full Match:", match_emp.group(0))
    print("Group 1 (EMP):", match_emp.group(1))
    print("Group 2 (Digits):", match_emp.group(2))
else:
    print("Invalid Employee ID")

print("-" * 50)

# ---------------------------------------------------
# 2. re.search(): Find first valid email address
# ---------------------------------------------------
text = "Please contact us at support_123@example.com for assistance."

email_pattern = r"([\w\.]+)@([\w]+)\.(\w+)"
email_match = re.search(email_pattern, text)

if email_match:
    print("Email Found")
    print("Full Email:", email_match.group(0))
    print("Username:", email_match.group(1))
    print("Domain:", email_match.group(2))
    print("Extension:", email_match.group(3))
else:
    print("No Email Found")

print("-" * 50)

# ---------------------------------------------------
# 3. Meta-characters and Special Sequences Demo
# ---------------------------------------------------
sample_text = "User1 has 2 files."

pattern = r"(\w+)\s(\d+)\s\w+\."

meta_match = re.search(pattern, sample_text)

if meta_match:
    print("Meta-character Pattern Matched")
    print("Word (\\w+):", meta_match.group(1))
    print("Number (\\d+):", meta_match.group(2))

print("-" * 50)

# ---------------------------------------------------
# 4. Demonstrating *, +, ? operators
# ---------------------------------------------------
operator_text = "color colour colouur"

operator_pattern = r"(colou?r)"

operator_matches = re.findall(operator_pattern, operator_text)

print("Matches using ?, *, + operators:")
print(operator_matches)