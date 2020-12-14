import smtplib
def send_email_tool(sender_email, sender_password, receiver_email, subject, body):
    '''
    inputs:
    - sender_email: sender email in the format of string
    - sender_password: sender email's password
    - receiver_email: a list of receivers (list of strings)
    - subject: email subject
    - body: email body

    '''
    import smtplib

    #email_text = '\nFrom: {}\nTo: {}\nSubject: {}\n{}'.format(sender_email, receiver_email, subject, body)
    email_text = 'Subject: {}\n\n{}'.format(subject, body)
    if '@gmail.com' in sender_email:
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, email_text)
            server.close()   
        except:
            print('Make sure you email allow less secured apps, turn it on from your email security, you can turn it back off later')

    else:
        'Other email providers are not supported yet' 

def assign_ppl(items) -> None:
    """Sattolo's algorithm.
    items is a list of names
    """
    from random import randrange
    items_perm = [x for x in items]
    i = len(items_perm)
    while i > 1:
        i = i - 1
        j = randrange(i)  # 0 <= j <= i-1
        items_perm[j], items_perm[i] = items_perm[i], items_perm[j]

    return items_perm            