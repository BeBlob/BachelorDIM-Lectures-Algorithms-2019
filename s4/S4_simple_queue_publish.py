"""
@author: BeBlob
"""

import os
import pika

mode='SEND' 

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

channel.basic_publish(exchange='',
                    routing_key='presentation',
                    body='Coucou, moi c\'est BeBlob')
                          
print(" [x] Sent 'Coucou, moi c\'est BeBlob'")
    
connection.close()
