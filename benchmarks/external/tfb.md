# Granian 3rd party benchmarks

## TechEmpower frameworks benchmarks

[Repository](https://github.com/TechEmpower/FrameworkBenchmarks)    
[Website](http://www.techempower.com/benchmarks/)

Run at: Fri 28 Mar 2025, 09:57    
Run ID: 1e0e5b2f-e9e3-4204-8ce9-073c3558cbee ([visualize](https://www.techempower.com/benchmarks/#section=test&runid=1e0e5b2f-e9e3-4204-8ce9-073c3558cbee))


### Plain text


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Granian (ASGI) | 1378505 | 0.79 |
| Granian (RSGI) | 1734614 | 1.0 |
| Robyn | 445147 | 0.26 |
| Uvicorn (httptools) | 1005877 | 0.58 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 3994423 | 2.13 |
| Granian (WSGI) | 1878379 | 1.0 |
| uWSGI | 179338 | 0.1 |
| uWSGI + Nginx | 27400 | 0.01 |



### JSON


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| FastWSGI (ASGI) | 1177739 | 0.97 |
| Granian (ASGI) | 1024094 | 0.84 |
| Granian (RSGI) | 1216021 | 1.0 |
| Robyn | 334414 | 0.28 |
| Uvicorn (httptools) | 853472 | 0.7 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 2335544 | 1.66 |
| Granian (WSGI) | 1404104 | 1.0 |
| uWSGI | 189080 | 0.13 |
| uWSGI + Nginx | 15484 | 0.01 |


