
from tools import *

gmail_user = 'youremail@gmail.com'
gmail_password = 'youremailpassword'

switch_invitation_or_main = 'main' # 'invitation' or 'main'

players = ['Rachel Green','Monica Geller', 'Phoebe Buffay',
           'Joey Tribbiani', 'Chandler Bing', 'Ross Geller']

emails = ['rachel.green@gmail.com', 'm.geller@gmail.com', 'smellycat@yahoo.com', 
          'Joey@yahoo.com', 'chandler.bing@gmail.com', 'ross_geller@icloud.com',]

num_players = len(players)

players_perm = assign_ppl(players)
print('starting to send the emails')
for i in range(num_players):
    # get the player stat
    player_this = players[i]
    receiver_this = players_perm[i]    
    player_this_email = emails[i]
    # define the email subject
    subject = 'OMG super important msg: secret santa'
    # invitation
    if switch_invitation_or_main == 'invitation':
        body = "Hi {},\n\nIt's finally holiday szn! Feeling festive yet?! Thank you for playing secret santa with us. ".format(player_this.split(' ')[0])\
             + "You will shortly find out about the lucky person (hopefully lucky! lol) whose secret santa you are. This email is just to make sure that we got the email addresses right, stay tuned!\n\n- Someone's secret santa"
    elif switch_invitation_or_main == 'main':
        body = "Hi {},\n\nFinally it is time to find out who you are buying a gift for this year! Please please please do not reveal this to anyone (even to your best friend)!\n\n".format(player_this.split(' ')[0])\
            +  "You are {}'s secret santa! The budget for this year is about $50! Don't worry, {} is gonna love your gift anyway lol!\n\n".format(receiver_this, receiver_this.split(' ')[0])\
            + "We are gonna gather around xmas time and exchange the gifts (stay tuned for that), so until then please do not share this with anyone! Thank you and can't wait to see you all!"\
            + "\n\n- Someone's secret santa"
    # send the email
    send_email_tool(gmail_user, gmail_password, player_this_email, subject, body)   
    print('email sent to {} ({})'.format(player_this, player_this_email))