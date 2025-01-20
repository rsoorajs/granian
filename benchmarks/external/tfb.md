# Granian 3rd party benchmarks

## TechEmpower frameworks benchmarks

[Repository](https://github.com/TechEmpower/FrameworkBenchmarks)    
[Website](http://www.techempower.com/benchmarks/)

Run at: Sat 11 Jan 2025, 06:37    
Run ID: 967babf5-cf1a-4b3f-a6d0-1cd49ef2c424 ([visualize](https://www.techempower.com/benchmarks/#section=test&runid=967babf5-cf1a-4b3f-a6d0-1cd49ef2c424))


### Plain text


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Robyn | 445268 | 445268.0 |
| Uvicorn (httptools) | 1001806 | 1001806.0 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 4031846 | 2.14 |
| Granian (WSGI) | 1887238 | 1.0 |
| uWSGI | 181351 | 0.1 |
| uWSGI + Nginx | 25620 | 0.01 |



### JSON


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| FastWSGI (ASGI) | 1154402 | 0.84 |
| Granian (ASGI) | 1121474 | 0.82 |
| Granian (RSGI) | 1374991 | 1.0 |
| Robyn | 337833 | 0.25 |
| Uvicorn (httptools) | 845903 | 0.62 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 2365472 | 1.68 |
| Granian (WSGI) | 1405100 | 1.0 |
| uWSGI | 189551 | 0.13 |
| uWSGI + Nginx | 16121 | 0.01 |


