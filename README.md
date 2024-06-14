
# RabbitMQ Example Python

## Description

This repository provides an example of using RabbitMQ with Python. It demonstrates how to set up and use RabbitMQ for message brokering in a Python application, which is useful for developers looking to implement message queues for decoupling and scaling their applications.

## Requirements

- Python
- RabbitMQ
- pip for package management

## Mode of Use

1. Clone the repository:
   ```bash
   git clone https://github.com/ferrerallan/rabbitmq-example-python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd rabbitmq-example-python
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure you have RabbitMQ installed and running on your local machine.

5. Run the producer application:
   ```bash
   python producer.py
   ```

6. Run the consumer application:
   ```bash
   python consumer.py
   ```

## Implementation Details

- **producer.py**: Contains code to send messages to the RabbitMQ queue.
- **consumer.py**: Contains code to receive messages from the RabbitMQ queue.
- **requirements.txt**: Configuration file for the project dependencies.

### Example of Use

Here is an example of how to send a message to the RabbitMQ queue using Python:

```python
import pika

def send_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()

if __name__ == "__main__":
    send_message()
```

This code connects to a RabbitMQ server, declares a queue, and sends a "Hello World" message to the queue.

## License

This project is licensed under the MIT License.

You can access the repository [here](https://github.com/ferrerallan/rabbitmq-example-python).
