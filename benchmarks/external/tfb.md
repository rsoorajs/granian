# Granian 3rd party benchmarks

## TechEmpower frameworks benchmarks

[Repository](https://github.com/TechEmpower/FrameworkBenchmarks)    
[Website](http://www.techempower.com/benchmarks/)

Run at: Sun 09 Mar 2025, 06:04    
Run ID: fbbca85f-b389-4b17-8dbe-d8e3a79e9dbd ([visualize](https://www.techempower.com/benchmarks/#section=test&runid=fbbca85f-b389-4b17-8dbe-d8e3a79e9dbd))


### Plain text


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Granian (ASGI) | 1367239 | 0.78 |
| Granian (RSGI) | 1759845 | 1.0 |
| Robyn | 444834 | 0.25 |
| Uvicorn (httptools) | 1008959 | 0.57 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 3946900 | 2.1 |
| Granian (WSGI) | 1883544 | 1.0 |
| uWSGI | 179507 | 0.1 |
| uWSGI + Nginx | 26344 | 0.01 |



### JSON


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| FastWSGI (ASGI) | 1154063 | 0.95 |
| Granian (ASGI) | 1006765 | 0.83 |
| Granian (RSGI) | 1212748 | 1.0 |
| Robyn | 334761 | 0.28 |
| Uvicorn (httptools) | 853221 | 0.7 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 2308523 | 1.66 |
| Granian (WSGI) | 1392933 | 1.0 |
| uWSGI | 188306 | 0.14 |
| uWSGI + Nginx | 15983 | 0.01 |


