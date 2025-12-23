formatter = "{} {} {} {}" #this is a template that reads as blank 1, blank 2, blank 3, blank 4

print(formatter.format(1,2,3,4)) #now we are saying, take my template and fill the blanks with 1, 2, 3, 4

#my example
email_template = "Dear {}. Thank you for your purchase of {} on {}"
print(email_template.format(input("Enter name: "), input("Enter Item: "), input("Enter date (dd/mm/yyyy): ")))