# Title: 
- *Please write title here e.g. ```DRF Framework```.*

### Date:
- *Please write date in format ```YYYY-MM-DD```. Change it after update.*

### Status:
 - Broker for celery

### Context and Problem Statement
- To run celery we need to have broker.
### Considered Options:
- Redis, RabbitMQ

### Decision:
- We will be using Redis.

### Reasons for the decision:
- Redis is easy more lightweight than RabbitMQ. And this is enough for our project.
