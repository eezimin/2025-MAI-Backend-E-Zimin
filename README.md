# 2025-MAI-Backend-E-Zimin

Для лабораторных работ по курсу "Программная инженерия".

Лабораторная работа 2.

**Тестирование Gunicorn**

Running 10s test @ http://localhost:8000/
  2 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    14.90ms   14.77ms 175.75ms   97.77%
    Req/Sec     3.45k   842.18     4.27k    87.23%
  16330 requests in 10.08s, 2.38MB read
Requests/sec:   1620.18
Transfer/sec:    242.08KB

**Тестирование Nginx**

Running 10s test @ http://localhost:8080/
  2 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    87.71ms  258.35ms   1.63s    93.51%
    Req/Sec     1.40k   198.14     1.63k    91.18%
  23778 requests in 10.03s, 15.30MB read
  Non-2xx or 3xx responses: 23711
Requests/sec:   2370.41
Transfer/sec:      1.52MB