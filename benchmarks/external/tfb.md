# Granian 3rd party benchmarks

## TechEmpower frameworks benchmarks

[Repository](https://github.com/TechEmpower/FrameworkBenchmarks)    
[Website](http://www.techempower.com/benchmarks/)

Run at: Sat 15 Mar 2025, 18:53    
Run ID: ace9c97f-253c-40d7-a730-c8a3b11b8d68 ([visualize](https://www.techempower.com/benchmarks/#section=test&runid=ace9c97f-253c-40d7-a730-c8a3b11b8d68))


### Plain text


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Granian (ASGI) | 1366177 | 0.77 |
| Granian (RSGI) | 1769458 | 1.0 |
| Robyn | 444579 | 0.25 |
| Uvicorn (httptools) | 1003720 | 0.57 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 4026260 | 2.14 |
| Granian (WSGI) | 1878944 | 1.0 |
| uWSGI | 179867 | 0.1 |
| uWSGI + Nginx | 25199 | 0.01 |



### JSON


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| FastWSGI (ASGI) | 1151730 | 0.95 |
| Granian (ASGI) | 1024199 | 0.84 |
| Granian (RSGI) | 1213872 | 1.0 |
| Robyn | 334619 | 0.28 |
| Uvicorn (httptools) | 855715 | 0.7 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 2376436 | 1.69 |
| Granian (WSGI) | 1406734 | 1.0 |
| uWSGI | 189047 | 0.13 |
| uWSGI + Nginx | 15270 | 0.01 |


