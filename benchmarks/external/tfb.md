# Granian 3rd party benchmarks

## TechEmpower frameworks benchmarks

[Repository](https://github.com/TechEmpower/FrameworkBenchmarks)    
[Website](http://www.techempower.com/benchmarks/)

Run at: Fri 01 Nov 2024, 00:49    
Run ID: 6ef367d2-de5c-464a-b3fa-2c3cf4ba1f8f ([visualize](https://www.techempower.com/benchmarks/#section=test&runid=6ef367d2-de5c-464a-b3fa-2c3cf4ba1f8f))


### Plain text


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Granian (ASGI) | 1427044 | 0.67 |
| Granian (RSGI) | 2118177 | 1.0 |
| Robyn | 447820 | 0.21 |
| Uvicorn (httptools) | 1061809 | 0.5 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 5292115 | 5.49 |
| Granian (WSGI) | 964644 | 1.0 |
| uWSGI | 179890 | 0.19 |
| uWSGI + Nginx | 31747 | 0.03 |



### JSON


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| FastWSGI (ASGI) | 1234414 | 0.98 |
| Granian (ASGI) | 1141303 | 0.91 |
| Granian (RSGI) | 1260203 | 1.0 |
| Robyn | 349151 | 0.28 |
| Uvicorn (httptools) | 893712 | 0.71 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 2725962 | 3.04 |
| Granian (WSGI) | 896874 | 1.0 |
| uWSGI | 188469 | 0.21 |
| uWSGI + Nginx | 14377 | 0.02 |


