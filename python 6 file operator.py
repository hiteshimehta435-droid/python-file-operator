while True:
    print("Welcome to file operator!.")
    print("1. create a file")
    print("2. write in file & read file")
    print("3. line appened in fil")
    print("4. exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("---Create a file---")

        file = open("Sample.txt", "w")
        file.write("python is a versatile programming language.")
        file.close()

        print("File created successfully.")

    elif choice == 2:
        print("---write in file & read file---")

        file = open("sample.txt", "r")
        print("Old Content:")
        print(file.read())
        file.close()

        file= open("sample.txt", "w")
        file.write("Learing file handling in python is fun!")
        file.close()

        print("Content overwritten successfully.")

    elif choice == 3:
        print("---line appened in file---")

        file = open("sample.txt", "a")

        file.write("line 3: python supports multiple modes of file handling.\n")

        file.close()

        print("Line appened successfully.")

    elif choice == 4:
        print("---Exit---")
        print("Thank you for use my porject")
        print("Have nice day")

    else:
        print("Invalid choice")
        break
        

        
        

        
        
        
                  
