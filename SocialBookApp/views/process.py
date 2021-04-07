'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''


from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet, ViewSet
from SocialBookApp.models.bookmodels import (Book)
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from SocialBookApp.models.usermodels import (App_User)
from SocialBookApp.serializers.serializers import (BookSerializer,App_UserSerializer)
from rest_framework.response import Response
import logging
from django.contrib.auth.models import User
from rest_framework.authtoken.models import (Token)
import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rest_framework.permissions import AllowAny
from django.core.files.base import ContentFile
import base64
import json
import random
import string


logger = logging.getLogger("book.request")

class LoginCheckSet(ModelViewSet):

    queryset = App_User.objects.all()
    serializer_class = App_UserSerializer
    permission_classes = [AllowAny]

    def login(self, request):
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                item = App_User.objects.get(username=username.lower())
                logger.info(item.password)

                if (item.active == False):
                    return Response("Account is not activated please check your mail", status=404)

                if (item.password == password):
                    response ={}
                    response ={}
                    list = User.objects.get(username=username.lower())
                    auth = Token.objects.get(user=list.id)
                    response['message'] ="User Verification Successful"
                    response['username'] = item.username.lower()
                    response['email'] = item.email.lower()
                    response['usertype'] = item.usertype

                    tokenJson={}
                    tokenJson["token"] = auth.key
                    response['auth_token'] = tokenJson
                    return Response(response, status=200)

                else:
                    return Response("Username or Password MisMatch", status=404)


            except App_User.DoesNotExist:
                return Response("Username does not Exist. Please Register", status=404)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)

    def change_pass(self, request):
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            try:
                item = App_User.objects.get(username=username.lower())
                logger.info(item.email)

                if (item.active == False):
                    return Response("Account is not activated please check your mail", status=404)

                if (item.email == email):

                    return Response("verified", status=200)

                else:
                    return Response("not available", status=404)


            except App_User.DoesNotExist:
                return Response("Username does not Exist. Please Register", status=404)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)

    def generate_pass(self, request):
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            try:
                item = App_User.objects.get(username=username.lower())
                logger.info(item.email)
                letters = string.ascii_letters
                passwd = ''.join(random.choice(letters) for i in range(10))

                item.password = passwd
                item.save()
                smtpsenderforpass(passwd, item.email)
                return Response("Check Mail For Pass", status=200)



            except App_User.DoesNotExist:
                return Response("Username does not Exist. Please Register", status=404)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)

@api_view(['POST'])
@permission_classes((AllowAny, ))
def create_Dp(request):
    try:
        username = request.POST.get('username')
        email = request.POST.get('email')


        return Response("gg", status=200)
    except Exception as e:
        logger.info("Error")
        logger.info(str(e))
        return Response(str(e), status=200)


def smtpsenderforpass(data,email):
    smtphost = 'smtp.gmail.com'
    smtpport = 587
    smtpuser = 'indbookstagram@gmail.com'
    smtppasswd = 'bookserver12345@'
    smtpfromaddr = 'noreply@bookstagram.com'
    smtptoaddr = email
    smtptype = 'html'
    smtpsubject = "Temporary Password Mail From Bookstagram"
    mail_content = data

    try:
        if smtptype == "text":
            logger.info("Sending Text Email")

        else:
            logger.info("Sending HTML Email")
            emailtemp = """\
                        <html>
<head>
<style>
table, th, td {
border: 2.5px solid #7b887c;
border-collapse: collapse;
color: black;
}
td
{
background-color: #eee;
}
td:hover {background-color:#949494;}
</style>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<body> 
   <br><br>
   Hello Bookstagramer,<br>
     <p>          Use the temporary password to login. Please do <b>Update password after loging in</b></p>  
      <br>  <br>      

    <h3><b>Tempprary Password:</b></h3>         
<table>
  <tr>  
    <td>
    <i><b>password</b></i>
    </td>
    <td>
    <i>""" + mail_content + """</i>
    </td>
  </tr>
   </table> 
<br>  <br> <br>  <br> 

  <i>Thanks and Regards,<br>
  Mail Bot,<br>
  Bookstagram.</i>
</body>
</html>
                        """
            SMTPCON(smtphost, smtpport, smtpuser, smtppasswd, smtpfromaddr, smtptoaddr, smtptype, smtpsubject,
                    emailtemp).SendHtmlEmail()
    except Exception as e:
        logger.info(e)


def smtpsender(data,id):


    smtphost = 'smtp.gmail.com'
    smtpport = 587
    smtpuser = 'indbookstagram@gmail.com'
    smtppasswd = 'bookserver12345@'
    smtpfromaddr = 'noreply@bookstagram.com'
    smtptoaddr = data["email"]
    smtptype = 'html'
    smtpsubject = "Verification Mail From Bookstagram"

    first = data["first_name"]
    last = data["last_name"]
    username = data["username"]
    country = data["country"]
    contact = data["contact"]
    mail_content = "http://127.0.0.1:8000/store/activate_user/?pk="+ str(id) + ""

    try:
        if smtptype == "text":
            logger.info("Sending Text Email")

        else:
            logger.info("Sending HTML Email")
            emailtemp = """\
                        <html>
<head>
<style>
table, th, td {
border: 2.5px solid #7b887c;
border-collapse: collapse;
color: black;
}
td
{
background-color: #eee;
}
td:hover {background-color:#949494;}
</style>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<body> 
   <br><br>
   Hello Bookstagramer,<br>
     <p>          Please check the following Details and click the link below to activate your Bookstagram Account</p>  
     <h2><b>Bookstagramer Information:</b></h2>         
<table>
  <tr>  
    <td>
    <i><b>First Name</b></i>
    </td>
    <td>
    <i>"""+first+"""</i>
    </td>
  </tr>
  <tr>  
    <td>
    <i><b>Last Name</b></i>
    </td>
    <td>
    <i>"""+last+"""</i>
    </td>
  </tr>
  <tr>  
    <td>
    <i><b>User Name</b></i>
    </td>
    <td>
    <i>"""+username+"""</i>
    </td>
  </tr>
  <tr>  
    <td>
    <i><b>Country</b></i>
    </td>
    <td>
    <i>"""+country+"""</i>
    </td>
  </tr>
  <tr>  
    <td>
    <i><b>contact</b></i>
    </td>
    <td>
    <i>"""+contact+"""</i>
    </td>
  </tr>
 
  </table>
  <br><br>
    <h3><b>Activate Bookstagram:</b></h3>         
<table>
  <tr>  
    <td>
    <i><b>Activation Link</b></i>
    </td>
    <td>
    <i>"""+mail_content+"""</i>
    </td>
  </tr>
   </table> 
<br>  <br> <br>  <br> 
 
  <i>Thanks and Regards,<br>
  Mail Bot,<br>
  Bookstagram.</i>
</body>
</html>
                        """
            SMTPCON(smtphost, smtpport, smtpuser, smtppasswd, smtpfromaddr, smtptoaddr, smtptype, smtpsubject,emailtemp).SendHtmlEmail()
    except Exception as e:
        logger.info(e)


class SMTPCON(object):

    def __init__(self, smtphost, smtpport, smtpuser, smtppasswd, smtpfromaddr, smtptoaddr, emailtype, subject, content):
        self.smtphost = smtphost
        self.smtpport = smtpport
        self.smtpuser = smtpuser
        self.smtppasswd = smtppasswd
        self.smtpfromaddr = smtpfromaddr
        self.smtptoaddr = smtptoaddr
        self.emailtype = emailtype
        self.subject = subject
        self.content = content
        print(self.smtphost)

    def SendTextEmail(self):

        print("entering here")
        # Contructing a Email Message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['From'] = self.smtpfromaddr
        msg['To'] = self.smtptoaddr


        # Attaching the Content of email

        body = MIMEText(self.content, 'plain')

        # Attaching the body of email

        msg.attach(body)
        logger.info("in py")

        # Connection to SMTP Server
        con = smtplib.SMTP(self.smtphost, self.smtpport)
        if self.smtpuser == '':
            con.sendmail(self.smtpfromaddr, [self.smtptoaddr, self.cc], msg.as_string())
        else:
            con.login(self.smtpuser, self.smtppasswd)
            con.sendmail(self.smtpfromaddr, [self.smtptoaddr, self.cc], msg.as_string())
        return ("Already Sent")

    def SendHtmlEmail(self):
        # Contructing a Email Message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['From'] = self.smtpfromaddr
        msg['To'] = self.smtptoaddr
        print("hi")

        # Attaching the Content of email

        body = MIMEText(self.content, 'html')
        print("hi")
        # Attaching the body of email

        msg.attach(body)

        # Connection to SMTP Server
        logger.info("in py")
        con = smtplib.SMTP(self.smtphost, self.smtpport)
        print(con)
        print("hiiii")
        logger.info(con.starttls())
        print("hi")
        if self.smtpuser == '':
            con.sendmail(self.smtpfromaddr, [self.smtptoaddr], msg.as_string())
        else:
            con.login(self.smtpuser, self.smtppasswd)
            con.sendmail(self.smtpfromaddr, [self.smtptoaddr], msg.as_string())

