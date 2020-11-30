# GenericNotificationSystem

### Problem Statement
Most applications have the need to implement notifications for a variety of use cases and scenarios. Create a centralized generic service for notification that can be used by a variety consuming application for their notification needs e.g. an incident workflow system may use this system when each incident ticket moves from one state to another, similarly a order management system may use this service to notify the customer of the status of the order whenever it changes

The system should allow for the following capabilities:

1.	Accept messages including from, to and subject
2.	Ability to notify on multiple channels (e.g email, slack, you can stub out/mock if required)
3.	Deliver messages in correct order for each consumer of this

Deliverables
1.	The code for the service in github with instructions on how to set it up and run it
*****************************

### Solution
Using Apache Kafka and Python-kafka to design Notification system.

### Architecture

![Alt text](Architecture.jpeg?raw=true)

#### Pre-requisite

* JDF/JRE Installation  - ```sudo apt-get install default-jre```
* Python-kafka installation - ```pip install python-kafka```

#### Installation
* Apache-kafka / Zookeeper installation - Please refer the installation and configuration step defined [here](https://www.digitalocean.com/community/tutorials/how-to-install-apache-kafka-on-ubuntu-18-04).

Once the configuration is updated, execute below commands to kickoff the service.
* Start the kafka service
```
    $ sudo systemctl start kafka
```
* To ensure that the server has started successfully, check the journal logs for the kafka unit:
```
    $ sudo journalctl -u kafka
    $ sudo journalctl -xe
```
* You now have a Kafka server listening on port 9092. To enable kafka on server boot, run:
```
    $ sudo systemctl enable kafka
```

#### How it works:
 * First, create a topic named Target by typing:
```
    $ ~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic Target
    -> Created topic Target.
```
 * You can create a producer from the command line using the kafka-console-producer.sh script. It expects the Kafka server’s hostname, port, and a topic name as arguments.
 Publish the string "Hello, World" to the Target topic by typing:
```
    $ echo "Hello, World" | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic Target > /dev/null
```
or
```
    $ python producer.py   # this script is @notification_system/src/notification_system/producer.py, it will help you generate producer for email/slack.
```
 * Next, you can create a Kafka consumer using the kafka-console-consumer.sh script. It expects the ZooKeeper server’s hostname and port, along with a topic name as arguments.
 The following command consumes messages from Target. Note the use of the --from-beginning flag, which allows the consumption of messages that were published before the consumer was started:
```
    $ ~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic Target --from-beginning
```

##### Validation Screenshot:


![Alt text](screenshot.jpg?raw=true)
