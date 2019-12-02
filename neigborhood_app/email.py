from django.core.mail import  EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,reciever):
    subject = 'Welome to neigborhood '
    sender = 'danielevans.karani@gmail.com'
    
    #passing in the context variables
    
    text_content = render_to_string('email/welcome.txt',{"name":name})
    html_content = render_to_string('email/welcome.html',{"name":name})
    
    msg = EmailMultiAlternatives(subject,text_content,sender,[reciever])
    msg.attach_alternative(html_content,'text/html')
    msg.send()