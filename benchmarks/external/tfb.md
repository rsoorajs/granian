# Granian 3rd party benchmarks

## TechEmpower frameworks benchmarks

[Repository](https://github.com/TechEmpower/FrameworkBenchmarks)    
[Website](http://www.techempower.com/benchmarks/)

Run at: Sun 13 Oct 2024, 01:11    
Run ID: d1a1c295-4e46-44b0-b850-f89cbc6fb063 ([visualize](https://www.techempower.com/benchmarks/#section=test&runid=d1a1c295-4e46-44b0-b850-f89cbc6fb063))


### Plain text


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Granian (ASGI) | 1410287 | 0.67 |
| Granian (RSGI) | 2106708 | 1.0 |
| Robyn | 413696 | 0.2 |
| Uvicorn (httptools) | 1047961 | 0.5 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 5369271 | 5.56 |
| Granian (WSGI) | 965479 | 1.0 |
| uWSGI | 180589 | 0.19 |
| uWSGI + Nginx | 27713 | 0.03 |



### JSON


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| FastWSGI (ASGI) | 1232471 | 1.0 |
| Granian (ASGI) | 1131707 | 0.92 |
| Granian (RSGI) | 1231943 | 1.0 |
| Robyn | 294505 | 0.24 |
| Uvicorn (httptools) | 884960 | 0.72 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 2663927 | 3.01 |
| Granian (WSGI) | 886371 | 1.0 |
| uWSGI | 188804 | 0.21 |
| uWSGI + Nginx | 15619 | 0.02 |


