## [Kafka quickstart](http://kafka.apache.org/documentation.html#quickstart)


Start zookeeper

```
> bin/zookeeper-server-start.sh config/zookeeper.properties
```

Start the Kafka server:

```
> bin/kafka-server-start.sh config/server.properties
```

Create a topic:

```
> bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
```

List the topics:

```
> bin/kafka-topics.sh --list --zookeeper localhost:2181
test
```

Send some messages (treated as one message per line):

```
> bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
This is a message
This is another message
```

Start a consumer:

```
> bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic test --from-beginning
```
