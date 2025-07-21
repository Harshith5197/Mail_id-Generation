First_name=input("Enter your first name: ")
Last_name=input("Enter your last name: ")
Email_domain=input("Enter your email domain (e.g., @gmail.com): ")
Email_id = First_name.lower() + Last_name.lower() + Email_domain
lst=list(map(str,input("Enter your list of email IDs separated by space : ").split()))
if Email_id in lst:
    print("Email ID already exists.")
else:
    lst.append(Email_id)
    print("Email ID generated successfully:", Email_id)
    print("Updated list of email IDs:", lst)