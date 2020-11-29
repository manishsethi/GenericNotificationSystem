# -*- coding: utf-8 -*-
"""
Consumer script
"""
import datetime
import json
from kafka import KafkaConsumer


# START EMAIL ALERT FUNCTION
def send_email(mail_from,mail_to,mail_sub):
    import smtplib
    from smtplib import SMTPException

    sender = mail_from
    receivers = mail_to
    message = mail_sub

    #-PRINTING LOGS-#
    print (datetime.datetime.now(), " - Alert Email - '",sender, ", ", receivers, ", ",message,"'" )

    # SMTP server to send email
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)
        print ("Successfully sent email")
    except SMTPException:
            print ("Error: unable to send email")


# START SLACK ALERT FUNCTION
def send_slack(mail_from,mail_to,mail_sub):

    sender = mail_from
    receivers = mail_to
    message = mail_sub

    #-PRINTING LOGS-#
    print (datetime.datetime.now(), " - Alert Slack - '",sender, ", ", receivers, ", ",message,"'" )

#START UNKNOWN ALERT FUNCTION
def send_unknown():
    #-PRINTING LOGS-#
    print (datetime.datetime.now(), " - Alert Unknown - ''" )


# START CONSUMER


#-Working without offset-#
#consumer = KafkaConsumer('Target', bootstrap_servers='104.42.236.61:9092',auto_offset_reset='earliest',consumer_timeout_ms=5000)

#-Testing for JSON parsing-#
consumer = KafkaConsumer('Target', bootstrap_servers='104.42.236.61:9092',auto_offset_reset='latest',consumer_timeout_ms=5000, value_deserializer=lambda m: json.loads(m.decode('utf-8')))


# START LOOP TO READ MSG FROM KAFKA TOPICS
for msg in consumer:
    #print (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    data = msg.value
    if len(data) == 4:
        if data['index'] == "email":
            send_email(data['from'],data['to'],data['sub'])
        elif data['index'] == "slack":
            send_slack(data['from'],data['to'],data['sub'])
        else:
            send_unknown()

    else:
        send_unknown()
    #print (msg)
