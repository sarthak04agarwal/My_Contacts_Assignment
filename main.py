
contact_Names = ["Jon Doe", "Sarthak Agarwal", "Mary Poppins", "Tom Hanks"]
contact_Number = ["(907) 376-0073", "(982) 964-3068", "(292) 350-9921", "(629) 246-5416"]
contact_Email = ["jondoe@gmail.com", "s.agarwal1@share.epsb.ca", "marypoppins234@outlook.com", \
    "thanks@yahoo.com"]

def display_contact():
    for x in contact_Names:
        print(x)

def search_contact():
    search_name = input("Please enter the name you want to search: ")
    for x in range(len(contact_Names)):
        if(contact_Names[x] == search_name):
            print("Name: " + contact_Names[x] + "Contact Email: " + contact_Email[x] +\
                 "Contact Phono number: " + contact_Number[x])

def edit_contact():
    search_name = input("Please enter the name you want to search: ")
    for x in range(len(contact_Names)):
        if(contact_Names[x] == search_name):
            edited_Name = input("Please enter the new name: ")
            edited_Phone = input("Please enter the new phone number: ")
            edited_Email = input("Please enter the new email address: ")
            contact_Names[x] = edited_Name
            contact_Email[x] = edited_Email
            contact_Number[x] = edited_Phone

def new_contact():
    add_Name = input("Please enter the new name: ")
    add_Phone = input("Please enter the new phone number: ")
    add_Email = input("Please enter the new email address: ")
    contact_Names.append(add_Name)
    contact_Number.append(add_Phone)
    contact_Email.append(add_Email)


def remove_contact():
    search_name = input("Please enter the name you want to search: ")
    for x in range(len(contact_Names)):
        if(contact_Names[x] == search_name):
            






menu = ("1. Display Contact Names \n2. Search for Contact \n3. \
Edit Contact \n4. New Contact \n5. Remove Contact \n6. Exit" + "\n Please type your number: ")

loop = True
while(loop):
    selection = input(menu)
    if selection == "1":
        display_contact()
    elif selection == "2":
        search_contact()
    elif selection == "3":
        edit_contact()
    elif selection == "4":
        new_contact()
    elif selection == "5":
        remove_contact()
    else:
        loop = False


