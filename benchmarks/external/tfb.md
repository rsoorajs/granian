# Granian 3rd party benchmarks

## TechEmpower frameworks benchmarks

[Repository](https://github.com/TechEmpower/FrameworkBenchmarks)    
[Website](http://www.techempower.com/benchmarks/)

Run at: Sat 19 Oct 2024, 08:07    
Run ID: 592cab59-a9db-463b-a9c9-33d2f9484e92 ([visualize](https://www.techempower.com/benchmarks/#section=test&runid=592cab59-a9db-463b-a9c9-33d2f9484e92))


### Plain text


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Granian (ASGI) | 1421348 | 0.67 |
| Granian (RSGI) | 2120481 | 1.0 |
| Robyn | 412005 | 0.19 |
| Uvicorn (httptools) | 1060432 | 0.5 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 5336906 | 5.56 |
| Granian (WSGI) | 959897 | 1.0 |
| uWSGI | 180404 | 0.19 |
| uWSGI + Nginx | 27802 | 0.03 |



### JSON


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| FastWSGI (ASGI) | 1257898 | 1.01 |
| Granian (ASGI) | 1131712 | 0.91 |
| Granian (RSGI) | 1249050 | 1.0 |
| Robyn | 295843 | 0.24 |
| Uvicorn (httptools) | 893939 | 0.72 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 2653573 | 2.95 |
| Granian (WSGI) | 900910 | 1.0 |
| uWSGI | 189741 | 0.21 |
| uWSGI + Nginx | 14389 | 0.02 |


