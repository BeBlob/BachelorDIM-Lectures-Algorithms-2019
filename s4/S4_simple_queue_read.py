"""
@author: BeBlob
"""

import os
import pika

nb_messages_read = 0

"""Documentation for read_messages
Read the messages send to pika's queue
"""
def read_messages():

    def callback(ch, method, properties, body):
        global nb_messages_read
        nb_messages_read += 1
        print(" [x] Received %r" % body, ",That is the",nb_messages_read,"message read")
        
    amqp_url='amqp://bqygjgys:pGzBRHgoIlv8tj8VlMUXkETDx2qGsUdg@dove.rmq.cloudamqp.com/bqygjgys'

    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    connection = pika.BlockingConnection(params) # Connect to CloudAMQP

    channel = connection.channel()

    pres = channel.queue_declare(queue='presentation')
            
    channel.basic_consume(queue='presentation',
                        on_message_callback=callback,                          
                        auto_ack=True)

    print(' [*] You have:',pres.method.message_count,'messages, Waiting for messages...To exit press CTRL+C')
    channel.start_consuming()