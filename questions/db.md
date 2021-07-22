- mysql底层实现原理  
connectors, Management Serveices & Utilities, Connection Pool, SQL Interface, Parser, Optimizer, Cache和Buffer, Engine  
首先程序的请求会通过mysql的connectors与其进行交互, 请求会暂时存放在连接池中并由处理器（Management Serveices & Utilities）管理. 当该请求从等待队列进入到处理队列, 管理器会将该请求丢给SQL接口（SQL Interface）.SQL接口接收到请求后, 它会将请求进行hash处理并与缓存中的结果进行对比, 如果完全匹配则通过缓存直接返回处理结果; 否则, 需要完整的走一趟流程:  
(1)由SQL接口丢给后面的解释器, 解释器会判断SQL语句正确与否, 若正确则将其转化为数据结构;  
(2)解释器处理完, 便来到后面的优化器, 它会产生多种执行计划, 最终数据库会选择最优化的方案去执行, 尽快返会结果;  
(3)确定最优执行计划后, SQL语句此时便可以交由存储引擎处理, 存储引擎将会到后端的存储设备中取得相应的数据, 并原路返回给程序  
- 查询回表  
- 聚簇索引和非聚簇索引
- mysql执行计划有哪些要素
select_type(SIMPLE/PRIMARY/SUBQUERY/DERIVED/UNION/UNION RESULT)、table(ALL/index/RANGE/INDEX_MERGE/REFEQ_REF/CONST/SYSTEM)、possible_keys、key、key_len、rows、filtered、extra
- mysql优化手段
使用索引, 特别是覆盖索引、减少查询数据量、用联表代替子查询、尽可能减少sql执行次数,减少请求网络延时、使用正确而小的数据类型, 比如内建类型存时间, 整数类型存ip、尽量避免null、慢查询日志、冗余数据避免联表、分表分区、业务结构优化、硬件、中间件等支持
- 存储引擎区别  
InnoDB: 默认事务型引擎, 聚簇索引;MyISAM: 非聚簇索引, 5.1之前的默认引擎, 支持很多特性包括全文索引(5.6后InnoDB支持)、压缩、空间函数等, 不支持事务和行级锁, 崩溃不能安全恢复, 某些场景性能很好, 最典型性能问题是表锁