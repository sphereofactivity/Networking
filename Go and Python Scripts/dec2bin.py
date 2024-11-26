# python script to convert an inputted decimal to binary
#

def dec_to_binary():
    binary_list = []

def is_valid_ip(ip_input):
    flag = False

    split_ip = ip_input.split('.')
    while flag != True:
        if len(split_ip) == 4 and all(split_ip.isdigit() and 0 <= int(split_ip) <= 255 for split_ip in split_ip):

            ## to do -> return the values of the ip address as a list and call dec_to_binary() to convert the list.

            if flag == True:
                break
            return True
        else:
            print("That is not a valid ip address. Try again.")
            return flag == False

def main():
    while True:
        try:
            ip_input = input("enter an ip address: ")
            is_valid_ip(ip_input)


        except ValueError:
            print("That was not a valid number. Please try again!")



if __name__ == "__main__":
    main()
