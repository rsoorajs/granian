# Granian 3rd party benchmarks

## TechEmpower frameworks benchmarks

[Repository](https://github.com/TechEmpower/FrameworkBenchmarks)    
[Website](http://www.techempower.com/benchmarks/)

Run at: Thu 06 Feb 2025, 06:43    
Run ID: b90cfa63-3def-4c89-a6c1-f19b3ca3608e ([visualize](https://www.techempower.com/benchmarks/#section=test&runid=b90cfa63-3def-4c89-a6c1-f19b3ca3608e))


### Plain text


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Granian (ASGI) | 1360168 | 0.77 |
| Granian (RSGI) | 1755643 | 1.0 |
| Robyn | 444882 | 0.25 |
| Uvicorn (httptools) | 1001470 | 0.57 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 4052942 | 2.14 |
| Granian (WSGI) | 1889892 | 1.0 |
| uWSGI | 181462 | 0.1 |
| uWSGI + Nginx | 27863 | 0.01 |



### JSON


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| FastWSGI (ASGI) | 1163744 | 0.97 |
| Granian (ASGI) | 1009791 | 0.84 |
| Granian (RSGI) | 1205076 | 1.0 |
| Robyn | 336031 | 0.28 |
| Uvicorn (httptools) | 847456 | 0.7 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 2328575 | 1.66 |
| Granian (WSGI) | 1404360 | 1.0 |
| uWSGI | 187966 | 0.13 |
| uWSGI + Nginx | 15059 | 0.01 |


