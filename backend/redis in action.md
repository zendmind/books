# Redis in Action

## 第一章	初识Redis

### 1.1	Redis简介

#### 1.1.1	Redis与其他数据库和软件的对比

| 名称       | 类型                                    | 数据存储选项                                                 | 查询类型                                                     | 附加功能                                                     |
| ---------- | --------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Redis      | 使用内存存储（in-memory）的非关系数据库 | 字符串、列表、集合、散列表、有序集合                         | 每种数据类型都有自己的专属命令，另外还有批量操作（bulk operation）和不完全（partial）的事务支持 | 发布与订阅，主从复制（master/slave replication），持久化，脚本（存储过程，stored procedure） |
| memcached  | 使用内存存储的键值缓存                  | 键值之间的映射                                               | 创建命令、读取命令、更新命令、删除命令以及其他几个命令       | 为提升性能而设的多线程服务器                                 |
| MySQL      | 关系数据库                              | 每个数据库可以包含多个表，每个表可以包含多个行；可以处理多个表的视图（view）；支持空间（spatial）和第三方扩展 | SELECT、INSERT、UPDATE、DELETE、函数、存储过程               | 支持ACID性质，主从复制和主主复制（master/master replication） |
| PostgreSQL | 关系数据库                              | 每个数据库可以包含多个表，每个表可以包含多个行；可以处理多个表的视图；支持空间和第三方扩展；支持可定制类型 | SELECT、INSERT、UPDATE、DELETE、内置函数、自定义的存储过程   | 支持ACID性质，主从复制，由第三方支持的多主复制（multi-master replication） |
| MongoDB    | 使用硬盘存储（on-disk）的非关系文档存储 | 每个数据库可以包含多个表，每个表可以包含多个无schema（schema-less）的BSON文档 | 创建命令、读取命令、更新命令、删除命令、条件查询命令等       | 支持map-reduce操作，主从复制，分片，空间索引（spatial index） |

#### 1.1.2	附加特性

Redis拥有两种不同形式的持久化方法：第一种持久化方法为时间点转储；第二种持久化方法将所有修改了数据库的命令都写入一个只追加文件里面，用户可以根据数据的重要程度，将只追加写入设置为从不同步、每秒同步一次或者每写入一个命令就同步一次。

### 1.2	Redis数据结构简介

| 结构类型 | 结构存储的值                                                 | 结构的读写能力                                               |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| STRING   | 可以是字符串、整数或浮点数                                   | 对整个字符串或者字符串的其中一部分执行操作；对整数和浮点数执行自增或者自减 |
| LIST     | 一个链表，链表上的每个节点都包含了一个字符串                 | 从链表的两端推入或者弹出元素；根据偏移量对链表进行修剪；读取单个或多个元素；根据值查找或者移除元素 |
| SET      | 包含字符串的无序收集器（unordered collection），并且被包含的每个字符串都是独一无二、各不相同的 | 添加、查找、移除单个元素；检查一个元素是否在于集合中；计算交集、并集、差集；从集合里面随机获取元素 |
| HASH     | 包含键值对的无序散列表                                       | 添加、获取、移除单个键值对；获取所有键值对                   |
| ZSET     | 字符串成员与浮点数分值之间的                                 |                                                              |
