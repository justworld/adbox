- redis底层实现原理  
String(简单动态字符串、List(链表、压缩列表)、Hash(字典、压缩列表)、Set(整数集合、字典)、ZSet(跳跃表、压缩列表)
- redis阻塞  
Redis是单线程的, 大量的慢查询可能会导致阻塞, 可以通过 slowlog get n获取慢日志  
时间复杂度为O(N)的命令不要在生产上随便使用, 例如flushdb、flushall、config、keys、hgetall、lrange、smembers、zrange、sinter  
