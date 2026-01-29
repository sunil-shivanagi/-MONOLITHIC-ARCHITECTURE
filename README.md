Route: /events

•	Bottleneck:

The API returned all events for a single user without pagination, causing large responses and increased database load.


•	Optimization:

Pagination was introduced, database queries were optimized using indexes, and user requests were distributed.


•	Result:

Reduced response size and database overhead led to faster response times and improved throughput.




Route: /my-events

•	Bottleneck:

All requests targeted one user and fetched full event histories, resulting in database contention and slow user-specific queries.


•	Optimization:

Pagination was added, requests were spread across multiple users, and user-based queries were indexed and optimized.


•	Result:
Lower database contention, faster query execution, and better scalability under concurre
