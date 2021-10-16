import pika

def callback(ch, method, properties, body):
  print(f"{body}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='ressuprimento')

channel.basic_consume(queue='ressuprimento',auto_ack=True,on_message_callback=callback)

print(f" Waiting for messages...")

channel.start_consuming()