from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
#


def send_email(mail_subject, mail_msg, to_mail, from_mail='no-reply@buuts.com', reply_to=['no-reply@buuts.com']):
    try:
        email = EmailMessage(
            mail_subject,
            mail_msg,
            from_mail, 
            to_mail,
            reply_to= reply_to
        )
        email.send()
        return True
    except Exception as err:
        print(err)
        return False
    

def send_acc_active_email(request, instance):
    mail_subject = 'Activate Buuts Account.'
    mail_msg = render_to_string('accounts/acc_active_email.html',
        {
            'user': instance,
            'domain': get_current_site(request).domain,
            'uid': urlsafe_base64_encode(force_bytes(instance.pk)),
            'token': default_token_generator.make_token(instance)
        }
    )
    to_mail = [instance.email]

    return send_email(mail_subject, mail_msg, to_mail)

