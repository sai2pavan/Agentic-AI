credit_score = int(input("Enter Your credit score:"))
income = int(input("Enter your income:"))
liability = int(input("Enter your liability value:"))
approval = "Rejected"
#checking for credit score
if credit_score >= 750 and income >= 50000 and liability < 20000:
    approval = "Eligible"
elif 650 <= credit_score <= 749 and income >= 50000 and liability < 20000:
    approval = "Conditionally Eligible"
else:
    approval = "Rejected"
print(f"Your Loan is {approval}")