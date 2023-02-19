    +-----------------+
    |       User      |
    +--------+--------+
             | HTTP requests
             |
    +--------v--------+
    | Image Upload API|
    +--------+--------+
             | Calls
             |
    +--------v--------+
    |   Application   |
    +--------+--------+
             | Queries/updates
             |
    +--------v--------+
    |    Database     |
    +-----------------+
