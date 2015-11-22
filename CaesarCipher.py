# Krzysztof Kuziel www.krzykustudio.pl
# Python 3.5
# Caesar Cipher - Wariation about
# File Encryption and Decription with given key

import os.path

#cryptography alphabet
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']

def encrypt(input_file, output_file, key=0):
    """
    Encrypt file with given key
    @param input_file
    @param output_file
    @param key 
    """
    #dividing key to chars
    key_list = [int(i) for i in str(key)]

    try:
        file_source = open(input_file, 'r')
        file_destination = open(output_file, 'w')
        key_index = 0 #key start index
        alphabet_count = len(alphabet)

        #dividing file to lines
        for line in file_source:
            encrypted_line = ""
            #divide line to chars and encrypt
            for char in line:

                #if char is not in alphabet than do encrypt
                try:
                    char_index = alphabet.index(char)
                    moving_index = char_index + key_list[key_index]
                    
                    if moving_index >= alphabet_count:
                        moving_index = abs(alphabet_count - moving_index)
                    encrypted_line += alphabet[moving_index]

                    if key_index >= len(key_list)-1:
                        key_index = 0  
                    else:
                      key_index+=1         
                except:
                    encrypted_line += char
            #write to file
            file_destination.writelines(encrypted_line)
            
            #write to last_key.txt used ked
            file_key = open("last_key.txt" , "w")
            file_key.writelines(key)
            file_key.close()

    except:
        raise Exception("Error opening file")
    finally:
        #clean up
        file_destination.close()
        file_source.close()

def decrypt(input_file, output_file, key=0):
    """
    Decrypt file with given key
    @param input_file 
    @param output_file 
    @param key 
    """
    
    #divide key to chars
    key_list = [int(i) for i in str(key)]

    try:
        file_source = open(input_file, 'r')
        file_destination = open(output_file, 'w')
        key_index = 0 
        alphabet_count = len(alphabet)

        for line in file_source:
            encrypted_line = ""
            for char in line:
                try:
                    char_index = alphabet.index(char)
                    moving_index = char_index - key_list[key_index]
                    
                    if moving_index < 0:
                        moving_index = abs(alphabet_count - moving_index)
                    encrypted_line += alphabet[moving_index]

                    if key_index >= len(key_list)-1:
                        key_index = 0  
                    else:
                      key_index+=1         
                except:
                    encrypted_line += char
            
            file_destination.writelines(encrypted_line)

    except:
        raise Exception("Error opening file")
    finally:
        #clean up
        file_destination.close()
        file_source.close()
    
def menu_encryption():
    print("- - - -")
    print("Encryption Menu:")
    print("-------")

    while True:
        input_file = input("Enter input file name: ")
        
        # check if file exist
        if(os.path.isfile(input_file)):
            break
        print("File not exist. Try again.")

    output_file = input("Please enter output file name.")
    key = input("Enter the encoding key: ")

    try:
        encrypt(input_file, output_file, key)
        print("- - - -")
        print("Encryption success")
        print("-------")
    except Exception as ex:
        print(ex)

def menu_decryption():
    print("- - - -")
    print("Decryption Menu:")
    print("-------")
    
    while True:
        input_file = input("Enter input file name: ")
		# check if file exist
        if(os.path.isfile(input_file)):
            break
        print("File not exist. Try again.")

    output_file = input("Please enter output file name.")
    key = input("Enter the decoding key: ")

    try:
        decrypt(input_file, output_file, key)
        print("- - - -")
        print("Decryption Success")
        print("-------")
    except Exception as ex:
        print(ex)

def menu_main():
    """
    User interface
    """
    #loop until press 'q'
    while True:
        print("- - - -")
        print("Menu:")
        print("-------")
        print("Choose:")
        print("s - To Encrypt File")
        print("d - To Decrypt File")
        print("-------")
        print("q - Quit")
        print("- - - -")
        menu = input()
        if(menu == "s"):
            menu_encryption()
        elif(menu == "d"):
            menu_decryption()
        elif(menu == "q"):
            break
        else:
            print("Wrong choice")

#start
menu_main()