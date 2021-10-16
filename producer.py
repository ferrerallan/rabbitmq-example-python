import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='ressuprimento')

messages = ["{ name:'Allan', "+
            "   products:[ "+
            "      {id:'123', quantity:'32' }, "+
            "      {id:'234', quantity:'12' }, "+
            "   ]"+
            " }"]

for message in messages:
  channel.basic_publish(exchange='', routing_key='ressuprimento',body=message)
  print(f" * Enviada {message} ")