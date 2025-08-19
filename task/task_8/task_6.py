"""
UNILAG Admission Eligibility Checker for 2025/2026 Academic Session

This program collects user details and checks if the candidate is eligible for admission
based on Federal Government and UNILAG requirements:
- Minimum age: 16 years
- UTME score: 200 or above
- UNILAG as first choice
- Five O'Level credits at one sitting (including English and Mathematics)
- Post-UTME participation (simulated here)
- Departmental cut-off mark (simulated, user inputs their department's cut-off)
"""

# Collect user details
age = int(input("Enter your age: "))
utme_score = int(input("Enter your UTME score: "))
first_choice = input("Is UNILAG your first choice? (yes/no): ").lower()
olevel_credits = int(input("Enter the number of O'Level credits you have (at one sitting): "))
eng_credit = input("Do you have credit in English Language? (yes/no): ").lower()
math_credit = input("Do you have credit in Mathematics? (yes/no): ").lower()
physics_credit = input("Do you have credit in Physics? (yes/no): ").lower()
chemistry_credit = input("Do you have credit in Chemistry? (yes/no): ").lower()
biology_credit = input("Do you have credit in Biology? (yes/no): ").lower()
post_utme_participation = input("Did you participate in the Post-UTME? (yes/no): ").lower()
dept_cutoff = int(input("Enter your department's cut-off mark (between 200 and 320): "))
post_utme_score = int(input("Enter your Post-UTME score: "))

# Check all conditions using logical operators only (no if/else)
eligible_age = age >= 16
eligible_utme = utme_score >= 200
eligible_first_choice = first_choice == "yes"
eligible_olevel = olevel_credits >= 5 and eng_credit == "yes" and math_credit == "yes"
eligible_post_utme = post_utme_participation == "yes"
eligible_dept_cutoff = (utme_score + post_utme_score) / 2 >= dept_cutoff

eligible = all([eligible_age, eligible_utme, eligible_first_choice, eligible_olevel, eligible_post_utme, eligible_dept_cutoff])

print("\nAdmission Eligibility Result:")
print(f"Eligible for Admission: {eligible}")

