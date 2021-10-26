import smtplib
import os
import codecs
import email.message

def create_email(articles):

    """
    Function that creates an email with the scraped articles.
    The article_block is a single email element which is placed
    inside the email.html file
    """

    # Open the article block
    article_template = codecs.open('html/article_block.html', "r", "utf-8").read()

    html_list = []

    # Loop over the articles from the scraper and place them in the temp HTML text
    # create a list with all the articles and then join them
    for key, value in articles.items():

        html_temp = article_template.replace(r"{article_title}" , key)
        html_temp = html_temp.replace(r"{article_url}" , value['article_url'])
        html_temp = html_temp.replace(r"{image_url}" , value['image_url'])
        html_list.append(html_temp)

    articles = "<br>".join(html_list)

    # Open mail email and add the articles, then return the email
    email_template = codecs.open('html/email.html', "r", "utf-8").read()
    email = email_template.replace(r"{articles}", articles)

    # Close the openend files
    article_template.close()
    email_template.close()

    return email


def send_email(email_HTML):

    """Script for sending an email"""

    # Fetch the email values from the os environment settings
    FROM = os.getenv("FROM_ADDRESS")
    TO = os.getenv("TO_ADDRESS")
    SERVER = os.getenv("SMTP")
    MAIL_LOGIN = os.getenv("MAIL_LOGIN")
    MAIL_PW = os.getenv("MAIL_PASSWORD")

    # Create message object to allow HTML to be send
    msg = email.message.Message()
    msg['Subject'] = 'Weekly Hackernews'
    msg['From'] = FROM
    msg['To'] = TO
    msg.add_header('Content-Type','text/html')
    msg.set_payload(email_HTML)

    # send the email through smtp
    try:
        server = smtplib.SMTP(SERVER, 587)
        server.starttls()
        server.login(MAIL_LOGIN, MAIL_PW)
        server.sendmail(FROM, TO, msg.as_string())
        server.quit()
    except Exception as exc:
        print(exc)
