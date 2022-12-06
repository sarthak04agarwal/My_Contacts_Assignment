import json

file = open("contact-data.json", "r")
dataStr = file.read()
file.close()

contact_Data = json.loads(dataStr)

def display_contact():
    print("ALL CONTACT NAMES")
    for x in range(len(contact_Data)):
        print(contact_Data[x]['name'])
    print(" ")
        

def search_contact():
    search_name = input("Please enter the name you want to search: ")
    for x in range(len(contact_Data)):
        if(contact_Data[x]['name'] == search_name):
            #print("Name: " + contact_Data[x]['name'] + "\n" + "Contact Email: " + contact_Data[x]['email'] + "\n" +"Contact Phone number: " + contact_Data[x]['number'])
            print(contact_Data[x])
        

def edit_contact():
    search_name = input("Please enter the name you want to edit: ")
    for x in range(len(contact_Data)):
        if(contact_Data[x]['name'] == search_name):
            edited_Name = input("Please enter the new name: ")
            edited_Phone = input("Please enter the new phone number: ")
            edited_Email = input("Please enter the new email address: ")
            contact_Data[x]['name'] = edited_Name
            contact_Data[x]['email'] = edited_Email
            contact_Data[x]['number'] = edited_Phone

def new_contact():
    add_Name = input("Please enter the new name: ")
    add_Phone = input("Please enter the new phone number: ")
    add_Email = input("Please enter the new email address: ")
    contact_Data.append({
            "name" : add_Name,
            "email" : add_Email,
            "number" : add_Phone
        })


def remove_contact():
    search_name = input("Please enter the name you want to search: ")
    for x in range(len(contact_Data)):
        if(contact_Data[x]['name'] == search_name):
            del contact_Data[x]
            break
            
                
            

menu = ("1. Display Contact Names \n2. Search for Contact \n3. \
Edit Contact \n4. New Contact \n5. Remove Contact \n6. Exit" + "\n Please type your number: ")

print(contact_Data)
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


