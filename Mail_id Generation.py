First_name=input("Enter your first name: ")
Last_name=input("Enter your last name: ")
Email_domain=input("Enter your email domain (e.g., @gmail.com): ")
Email_id = First_name.lower() + Last_name.lower() + Email_domain
email_list = [
    "arya.verma92@gmail.com",
    "john.mathews@outlook.com",
    "sneha.r@infosys.com",
    "karthik.m.tech@gmail.com",
    "emily.dawson24@yahoo.com",
    "ravi.teja@zoho.com",
    "fatima.shaikh@tcs.com",
    "daniel_nguyen@live.com",
    "shruti.bajaj23@gmail.com",
    "michael.owen.dev@protonmail.com",
    "lakshmi.priya@rediffmail.com",
    "rohit_kumar@accenture.com",
    "li.wei2025@gmail.com",
    "jessica.alves@icloud.com",
    "naveen.reddy@hcl.com",
    "amelie.thomas@aol.com",
    "rajat.singh92@wipro.com",
    "oliver.brooks@duck.com",
    "pooja.kale@msn.com",
    "ethan.james.dev@gmail.com"
]

if Email_id in lst:
    print("Email ID already exists.")
else:
    lst.append(Email_id)
    print("Email ID generated successfully:", Email_id)
    print("Updated list of email IDs:", lst)
