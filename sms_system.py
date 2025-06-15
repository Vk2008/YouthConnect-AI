from clicksend_client import SmsMessageCollection, SmsMessage
#from clicksend_client.rest import ApiException
#from clicksend_client.api.sms_api import SmsApi
import clicksend_client
import pandas as pd

configuration = clicksend_client.Configuration()
configuration.username = 'vanshika09116@vvdav.info'
configuration.password = '77E96A6A-3AE3-0385-4D85-1C40767E9659'

api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))

message = SmsMessage(source = 'python', body='Hey! Election season is here! Which issue do you think needs the most attention? \n(1)Education \n(2)Employment \n(3)Climate \n(4)Transportation', to ='919811818850')

sms_messages = SmsMessageCollection(messages = [message])

try: 
    api_response = api_instance.sms_send_post(sms_messages= sms_messages)
    print('Successfully sent')

except Exception as e:
    print('Exception when calling SMSApi ->sms_send_post: %s\n' % e)

try:
    api_response = api_instance.sms_inbound_get()
    for message in api_response['data']['messages']:
        received_mess= message['body']
        user_data = pd.read_csv(r'C:\Users\Harish\OneDrive\Desktop\policy\user_data.csv', sep = ',')
        existing_entries = len(user_data)
        entry = {'user_no': existing_entries +1, 'issue_faced_in': received_mess}
        user_data = user_data.append(entry, ignore_index= True)
        user_data.to_csv(r'C:\Users\Harish\OneDrive\Desktop\policy\user_data.csv')

        if received_mess == 'A':
            message = SmsMessage(source = 'python', body='What improvement do you think is mot needed in our local education system? \n(1)More funding \n(2)Better technological access \n(3)Curriculum Reform', to ='919811818850')

            sms_messages = SmsMessageCollection(messages = [message])

            try: 
                api_response = api_instance.sms_send_post(sms_messages= sms_messages)
                print('Successfully sent')

            except Exception as e:
                print('Exception when calling SMSApi ->sms_send_post: %s\n' % e)

            try:
                api_response = api_instance.sms_inbound_get()
                for message in api_response['data']['messages']:
                    reform= message['body']
            except Exception as e:
                print('Exception when calling SMSApi->sms_inbound_get: %s\n' % e)


        elif received_mess == 'B':
            message = SmsMessage(source = 'python', body='What kind of support do you think would help youth find employment more easily? \n(1)Job training programs \n(2)Career Counseling \n(3)Financial Assistance for starting enterprises', to ='919811818850')

            sms_messages = SmsMessageCollection(messages = [message])

            try: 
                api_response = api_instance.sms_send_post(sms_messages= sms_messages)
                print('Successfully sent')

            except Exception as e:
                print('Exception when calling SMSApi ->sms_send_post: %s\n' % e)

            try:
                api_response = api_instance.sms_inbound_get()
                for message in api_response['data']['messages']:
                    reform= message['body']
            except Exception as e:
                print('Exception when calling SMSApi->sms_inbound_get: %s\n' % e)


        elif received_mess == 'C':
            message = SmsMessage(source = 'python', body='Do you support government initiatives to improve air quality? \n(1)Support \n(2)Neutral \n(3)Oppose', to ='919811818850')

            sms_messages = SmsMessageCollection(messages = [message])

            try: 
                api_response = api_instance.sms_send_post(sms_messages= sms_messages)
                print('Successfully sent')

            except Exception as e:
                print('Exception when calling SMSApi ->sms_send_post: %s\n' % e)

            try:
                api_response = api_instance.sms_inbound_get()
                for message in api_response['data']['messages']:
                    reform= message['body']
            except Exception as e:
                print('Exception when calling SMSApi->sms_inbound_get: %s\n' % e)

        elif received_mess == 'D':
            message = SmsMessage(source = 'python', body='Would you like to see more investment in public transit infrastructure? \n(1)Yes, definitely \n(2)Neutral \n(3)No, not really', to ='919811818850')

            sms_messages = SmsMessageCollection(messages = [message])

            try: 
                api_response = api_instance.sms_send_post(sms_messages= sms_messages)
                print('Successfully sent')

            except Exception as e:
                print('Exception when calling SMSApi ->sms_send_post: %s\n' % e)

            try:
                api_response = api_instance.sms_inbound_get()
                for message in api_response['data']['messages']:
                    reform= message['body']
            except Exception as e:
                print('Exception when calling SMSApi->sms_inbound_get: %s\n' % e)
        else:
            message = SmsMessage(source = 'python', body='Please enter the number that matches your top priority', to ='919811818850')

            sms_messages = SmsMessageCollection(messages = [message])

            try: 
                api_response = api_instance.sms_send_post(sms_messages= sms_messages)
                print('Successfully sent')

            except Exception as e:
                print('Exception when calling SMSApi ->sms_send_post: %s\n' % e)

        message = SmsMessage(source = 'python', body='Thank you for the cooperation! Do you think voting is a \n (1)Fundamental right \n (2)Civic duty?', to ='919811818850')

        sms_messages = SmsMessageCollection(messages = [message])

        try: 
            api_response = api_instance.sms_send_post(sms_messages= sms_messages)
            print('Successfully sent')

        except Exception as e:
            print('Exception when calling SMSApi ->sms_send_post: %s\n' % e)

        try:
            api_response = api_instance.sms_inbound_get()
            for message in api_response['data']['messages']:
                resp= message['body']
        except Exception as e:
            print('Exception when calling SMSApi->sms_inbound_get: %s\n' % e)

        message = SmsMessage(source = 'python', body='How likely are you to vote in the upcoming election? \n (1)Unikely \n (2)Neutral \n (3)Likely', to ='919811818850')

        sms_messages = SmsMessageCollection(messages = [message])

        try: 
            api_response = api_instance.sms_send_post(sms_messages= sms_messages)
            print('Successfully sent')

        except Exception as e:
            print('Exception when calling SMSApi ->sms_send_post: %s\n' % e)

        try:
            api_response = api_instance.sms_inbound_get()
            for message in api_response['data']['messages']:
                resp= message['body']
                if resp == '1' or '2':
                    message = SmsMessage(source = 'python', body='What is the biggest barrier for you to participate in the election process? \n (1)Limited access to voter registration and polling stations \n (2)Lack of information about candidates \n (3)Feeling like my vote doesn\'t matter', to ='919811818850')
                    sms_messages = SmsMessageCollection(messages = [message])

                    try: 
                        api_response = api_instance.sms_send_post(sms_messages= sms_messages)
                        print('Successfully sent')

                    except Exception as e:
                        print('Exception when calling SMSApi ->sms_send_post: %s\n' % e)

                    try:
                        api_response = api_instance.sms_inbound_get()
                        for message in api_response['data']['messages']:
                            resp= message['body']
                    except Exception as e:
                        print('Exception when calling SMSApi->sms_inbound_get: %s\n' % e)
        except Exception as e:
            print('Exception when calling SMSApi->sms_inbound_get: %s\n' % e)

        message = SmsMessage(source = 'python', body='Thank you for sharing your opinion! Remember, your voice matters!', to ='919811818850')

        sms_messages = SmsMessageCollection(messages = [message])

        try: 
            api_response = api_instance.sms_send_post(sms_messages= sms_messages)
            print('Successfully sent')

        except Exception as e:
            print('Exception when calling SMSApi ->sms_send_post: %s\n' % e)




except Exception as e:
    print('Exception when calling SMSApi->sms_inbound_get: %s\n' % e)



