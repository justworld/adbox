- mysql底层实现原理  
SQL接口, 解析器, 优化器, 缓存, 存储引擎
- 查询回表  
- 聚簇索引和非聚簇索引
- mysql执行计划有哪些要素
select_type(SIMPLE/PRIMARY/SUBQUERY/DERIVED/UNION/UNION RESULT)、table(ALL/index/RANGE/INDEX_MERGE/REFEQ_REF/CONST/SYSTEM)、possible_keys、key、key_len、rows、filtered、extra
- mysql优化手段