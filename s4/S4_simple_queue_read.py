"""
@author: BeBlob
"""

import os
import pika

"""Documentation for read_messages
Read the messages send to pika's queue
"""
def read_messages():

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    amqp_url='amqp://bqygjgys:pGzBRHgoIlv8tj8VlMUXkETDx2qGsUdg@dove.rmq.cloudamqp.com/bqygjgys'

    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    connection = pika.BlockingConnection(params) # Connect to CloudAMQP

    channel = connection.channel()

    channel.queue_declare(queue='presentation')
            
    channel.basic_consume(queue='presentation',
                        on_message_callback=callback,                          
                        auto_ack=True)
        
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()