# Granian 3rd party benchmarks

## TechEmpower frameworks benchmarks

[Repository](https://github.com/TechEmpower/FrameworkBenchmarks)    
[Website](http://www.techempower.com/benchmarks/)

Run at: Mon 16 Dec 2024, 17:55    
Run ID: c2d6592c-7a21-4f69-8ac0-249f8a4f4897 ([visualize](https://www.techempower.com/benchmarks/#section=test&runid=c2d6592c-7a21-4f69-8ac0-249f8a4f4897))


### Plain text


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Granian (ASGI) | 1372925 | 0.77 |
| Granian (RSGI) | 1788405 | 1.0 |
| Robyn | 445591 | 0.25 |
| Uvicorn (httptools) | 1011159 | 0.57 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 3994184 | 4.03 |
| Granian (WSGI) | 991876 | 1.0 |
| uWSGI | 178977 | 0.18 |
| uWSGI + Nginx | 28034 | 0.03 |



### JSON


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| FastWSGI (ASGI) | 1167054 | 1.01 |
| Granian (ASGI) | 1008042 | 0.87 |
| Granian (RSGI) | 1155391 | 1.0 |
| Robyn | 335362 | 0.29 |
| Uvicorn (httptools) | 853084 | 0.74 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 2364310 | 2.67 |
| Granian (WSGI) | 884823 | 1.0 |
| uWSGI | 187210 | 0.21 |
| uWSGI + Nginx | 15634 | 0.02 |


