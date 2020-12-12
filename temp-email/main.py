from t_mail_inbox import mail_inbox
from fake_acc import create_facc
if __name__ == "__main__":

    
    # Create a new mailbox --> Websocket with Dropmail.me
    mailbox = mail_inbox()


    num_email = int(input("Enter Number of Emails to add to current session: ")) + 1
    prev_email = bool(int(input("Add a previous email using a password? 0 (no) or 1(yes): ")))
    #Add a previous email using a hash of the form domanin@.com:HASH
    if prev_email==True:
        val = bool(int(input("Use textfile? 0 (no) or 1(yes): ")))
        if val == False:
            temp_n = input("Number of emails to restore: ")

   
    for x in range(prev_email):
        if val == True:
            with open ('email_acc.txt','r') as inp:
                for acc in inp:
                    mailbox.add_prev_email(acc)
        else:
            hash_t = str(input("Enter email and password: "))
            mailbox.add_prev_email(hash_t)
    
    #Number of emails to add
    for x in range(num_email-1):
        mailbox.add_rand_email()

    #Print the number of emails in socket
    for x in range(len(mailbox.get_email())):
        print(mailbox.get_email()[x])
        #Write to file the email accounts
        with open ('email_acc.txt','a') as out:
            out.write(mailbox.get_email()[x])
            out.write('\n')
    
        #Get fake account information and save it to a textfile with email
        acc_ = create_facc()
        with open ('acc_info.txt','a') as out:
            for acc in acc_:
                out.write((mailbox.get_email()[x] + ":" + acc))
                out.write('\n')


    #Wait for incoming emails
    while True:
        #Get email
        json_val = (mailbox.wait_for_email())
        #Get URL from the json.loads
        matches = mailbox.find_links(json_val)
        with open('emails.txt','a') as out:
            out.write(json_val)
            out.write('\n')
            out.write(matches)
            out.write('\n')

        print(matches)
        print(json_val)
    
    






    


