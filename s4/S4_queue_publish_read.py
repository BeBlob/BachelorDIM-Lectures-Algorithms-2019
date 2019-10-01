"""
@author: BeBlob
"""
import argparse
import os
import pika
import S4_simple_queue_publish as ppub 
import S4_simple_queue_read as rpub 

parser = argparse.ArgumentParser()
parser.add_argument("--read", help="read the messages",
                    action="store_true")
parser.add_argument("--publish", help="write a message",
                    action="store_true")
args = parser.parse_args()

if args.read:
    print("read mode turned on")
    rpub.read_messages()
    
if args.write:
    print("publish mode turned on")
    ppub.publish_message()
