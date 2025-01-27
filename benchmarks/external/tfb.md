# Granian 3rd party benchmarks

## TechEmpower frameworks benchmarks

[Repository](https://github.com/TechEmpower/FrameworkBenchmarks)    
[Website](http://www.techempower.com/benchmarks/)

Run at: Fri 17 Jan 2025, 18:25    
Run ID: aac17d8f-9e72-4274-8b64-f0788b47e97e ([visualize](https://www.techempower.com/benchmarks/#section=test&runid=aac17d8f-9e72-4274-8b64-f0788b47e97e))


### Plain text


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Robyn | 446145 | 446145.0 |
| Uvicorn (httptools) | 1009507 | 1009507.0 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 3946558 | 2.07 |
| Granian (WSGI) | 1910009 | 1.0 |
| uWSGI | 180094 | 0.09 |
| uWSGI + Nginx | 27009 | 0.01 |



### JSON


#### Async

| Server | RPS | Change (rate) |
| --- | --- | --- |
| FastWSGI (ASGI) | 1146062 | 0.83 |
| Granian (ASGI) | 1121034 | 0.82 |
| Granian (RSGI) | 1373533 | 1.0 |
| Robyn | 334243 | 0.24 |
| Uvicorn (httptools) | 849283 | 0.62 |

#### Sync

| Server | RPS | Change (rate) |
| --- | --- | --- |
| Fastwsgi | 2309165 | 1.64 |
| Granian (WSGI) | 1409990 | 1.0 |
| uWSGI | 188273 | 0.13 |
| uWSGI + Nginx | 15194 | 0.01 |


