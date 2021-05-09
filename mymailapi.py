import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


def email_sender():
    user_email = 'makewinmeditech@gmail.com'
    user_pwd = 'mkwin12@Em'
    recver_mail = 'smahajan2898@gmail.com'
    subject = "Your Wishlist is Fullfilled."

    body = "Dear Sir/Madam,\n\n\n Please visit url:\nhttps://www.amazon.in/Apple-Watch-GPS-Cellular-40mm/dp/B07XWZ681Q/ref=sr_1_1?crid=1PASPEACYWJK9&dchild=1&keywords=apple+iwatch&qid=1620500785&sprefix=apple+iwa%2Caps%2C302&sr=8-1\n\nHave Good Day."

    # Mail Body Setup.
    msg = MIMEMultipart()
    msg["From"] = user_email
    msg["To"] = recver_mail
    msg["Subject"] = subject
    # msg["Signature"] = signature
    msg.attach(MIMEText(body, 'plain'))


    # # Attachment Section.
    # filenamea = 'Shubham_Jain_CovidReport.pdf'
    # filenameb = 'Shanu_Bilala_CovidReport.pdf' 
    # filenamec = 'Drishti_Jain_CovidReport.pdf' 

    # rcp_list = [filenamea, filenameb, filenamec]

    # for i in range(len(rcp_list)):
    #     attachment = open(rcp_list[i], 'rb')
    #     part = MIMEBase('application', 'octet-stream')
    #     part.set_payload(attachment.read())
    #     encoders.encode_base64(part)
    #     part.add_header('Content-Disposition', "attachment; filename="+rcp_list[i])
    #     msg.attach(part)

    text_msg = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user_email, user_pwd)
    server.sendmail(user_email, recver_mail, text_msg)
    server.quit()

    print("Hi there, Email Sent Successfully.")


if __name__ == "__main__":
    email_sender()