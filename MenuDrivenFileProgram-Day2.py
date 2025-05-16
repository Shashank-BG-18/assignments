
#This is a Meny Driven Program working on files
import file_module

print("Below are the choices : ")
print("1. Write a file")
print("2. Read a file")
print("3. Append to a file")
print("4. Exit")

while True:
    #Asking the user his choice
    choice = input("Enter your choice : ")
    #Writing a file
    if choice == '1' :
        filename = input("Enter the filename with .txt extension : ")
        if not filename.endswith('.txt'):
            print("You have not entered a valid filename\n")
            continue
        texts = input("Enter the text to be inserted into the file "+filename+" :\n ")
        file_module.write_to_a_file(filename,texts)
        print("\nFile written successfully\n")
    #Reading a file
    elif choice == '2' :
        filename=input("Enter the filename to be read with .txt extensiom : ")
        file_module.read_a_file(filename)

    #Appending to a file
    elif choice=='3':
        filename=input("Enter the filename to append with a .txt extensiom : ")
        texts=input("Enter the text to be appended to the file : \n ")
        file_module.append_to_a_file(filename,texts)
        print("\nFile appended successfully\n")

    #Exit
    elif choice=='4':
        print("\nYou have successfully exited the program\n")
        break
    else:
        print("Wrong Choice, u will have to enter your choice again\n")