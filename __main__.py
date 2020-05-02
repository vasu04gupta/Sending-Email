from .python import email

def run():
    sender_email=input()       #"abcd@mail.com"
    receiver_email=input()     #"abcd@mail.com"
    sender_password=input()    #abcd1412
    subject=input()            #Heading"
    body=input()               # "Any Text "
    filename=input()           #"Name of file"
    address_of_file=input()    # "C:/Users/Vasu Gupta/Desktop"

    k=email(sender_email,receiver_email,sender_password,subject,body,filename,address_of_file)
    k.email_send()
    print("Done")

if __name__ == '__main__':
    run()
    
