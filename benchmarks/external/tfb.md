# Granian 3rd party benchmarks

## TechEmpower frameworks benchmarks

[Repository](https://github.com/TechEmpower/FrameworkBenchmarks)    
[Website](http://www.techempower.com/benchmarks/)

Run at: Mon 24 Feb 2025, 06:22    
Run ID: 1a4219d1-07cf-44d6-b25a-92fcd3914017 ([visualize](https://www.techempower.com/benchmarks/#section=test&runid=1a4219d1-07cf-44d6-b25a-92fcd3914017))


### Plain text


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Granian (ASGI) | 1366658 | 0.78 |
| Granian (RSGI) | 1758949 | 1.0 |
| Robyn | 443023 | 0.25 |
| Uvicorn (httptools) | 1008675 | 0.57 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 3972280 | 2.1 |
| Granian (WSGI) | 1892725 | 1.0 |
| uWSGI | 179952 | 0.1 |
| uWSGI + Nginx | 25568 | 0.01 |



### JSON


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| FastWSGI (ASGI) | 1165206 | 0.96 |
| Granian (ASGI) | 1020919 | 0.84 |
| Granian (RSGI) | 1209604 | 1.0 |
| Robyn | 336400 | 0.28 |
| Uvicorn (httptools) | 853467 | 0.71 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 2355755 | 1.67 |
| Granian (WSGI) | 1406844 | 1.0 |
| uWSGI | 186947 | 0.13 |
| uWSGI + Nginx | 15691 | 0.01 |


