### Spring
##### 1. 解释Spring框架中的IoC（控制反转）和DI（依赖注入）的概念
- IOC 控制反转是一个设计概念思想, Spring 的实现是将Java Bean 对象的生命周期进行全权托管, 托管给Spring容器
- DI 依赖注入是IOC生命周期中的一环, 在bean 生命周期中 的属性注入阶段, Bean依赖的属性通过不同的注入策略注入依赖的Bean 

##### 2. Spring框架中Bean的生命周期是怎样的？
- BeanDefinition 解析, 这个阶段主要是 XML 解析/ Annotation注解的解析 
- BeanDefinition 注册, 主要是将Definition添加到容器中, 设定唯一的Bean名称
- BeanDefinition 合并,  子Bean对父Bean的一些属性进行覆盖
- Bean class 加载, 确保Bean Class 被加载，这种情况发生在XML模式下
- Bean 实例化, 整体分前中后三个阶段 支持 InstantiationAwareBeanPostProcessor 进行切面拦截回调, 后置完成后会提前进行Bean 的曝光，来解决部分循环依赖问题
- Bean 属性设置阶段   
- Bean 初始化
- Bean 销毁 


##### 3. 请解释Spring AOP（面向切面编程）的原理和应用场景。
面向切面编程是一种编程范式 主要是目的是为了将应用程序的横向关注点从业务代码中剥离, 减少重复代码的编写
 - 拦截代理方式，Spring 有两种代理方式
    - JDK动态代理
    - Cglib 方式
- 执行切入点
- 通知场景
 
应用场景
- 日志切面，执行前后日志打印
- 统一事务管理
- 性能统计
- 异常处理
- 方法级别数据缓存

##### 4. 什么是Spring Security，它是如何工作的？
##### 5. Spring和Spring MVC的区别在哪里？
Spring 是一个大的集合框架提供核心的
- Bean 管理容器, IOC思想范式
- DI
- AOP
- 统一事务管理
- 多模块化： SpringJDBC/SpringORM/Spring Web MVC 等


SpringWebMVC 是建立在SpringFramework上的一套全功能的WebMVC框架
- 模型-视图-控制器架构：采用 MVC 模式，分离业务逻辑、用户界面和控制逻辑。
- 强大的配置功能：支持基于注解的控制器和路由配置。
- 数据绑定：自动将请求参数绑定到模型对象。
- 数据验证：支持强大的数据验证框架集成。
- 灵活的视图解析：支持多种视图技术，包括 JSP, Thymeleaf, FreeMarker 等。
- RESTful 服务构建：提供了构建 RESTful 服务的支持，简化了 REST API 开发

##### 6. 解释@Transactional注解在Spring中的作用。
@Transactional 是Spring中声明式事务注解, 支持声明在类和方法上
- 自动事务管理：Spring 管理的事务包括自动提交或回滚事务。当被 @Transactional 注解的方法正常完成后，事务将被提交；如果方法抛出异常，则事务将被回滚。
- 事务传播行为：控制事务的传播性是 @Transactional 注解的关键特征。Spring 定义了多种传播行为
   -  REQUIRED（默认）：支持当前事务，如果当前没有事务，就新建一个事务。
   -  SUPPORTS：支持当前事务，如果当前没有事务，就以非事务方式执行。
   -  MANDATORY：支持当前事务，如果当前没有事务，就抛出异常。
   -  REQUIRES_NEW：新建事务，如果当前存在事务，把当前事务挂起。
   -  NOT_SUPPORTED：以非事务方式执行操作，如果当前存在事务，就把当前事务挂起。
   -  NEVER：以非事务方式执行，如果当前存在事务，则抛出异常。
   -  NESTED：如果当前存在事务，则在嵌套事务内执行。如果当前没有事务，则表现和 REQUIRED 一样。
- 事务隔离级别：事务的隔离级别定义了一个事务可能受其他并发事务影响的程度。Spring 支持所有的标准事务隔离级别：
    - DEFAULT：使用后端数据库默认的隔离级别。
    - READ_UNCOMMITTED、READ_COMMITTED、REPEATABLE_READ、SERIALIZABLE 等。

 
##### 7. Spring中Bean的作用域有哪些？它们分别适用于什么场景？
- singleton 单例模式
- prototype 原型
- request
- session
- application
- websocket


##### 8. 如何在Spring应用中管理事务？
通过@Transactional注解进行声明式事务管理


##### 9. Spring框架中用于处理REST API的工具和方法有哪些？

##### 10. 如何通过Spring Boot实现条件化的Bean注册？

- @ConditionalOnClass
- @ConditionalOnMissingBean 
- @ConditionalOnProperty


##### 11. Spring 为什么需要使用三级缓存来解决循环依赖, 二级不行么?
首先说结论: 二级可以, 但是不符合Spring的设计
- 因为Spring

### Spring Boot
##### 1. Spring Boot 的自动配置是如何工作的？
##### 2. 请解释Spring Boot中的Starter POMs的作用。
##### 3. 在Spring Boot中如何自定义白标错误页面？
##### 4. 如何在Spring Boot应用中集成数据库？
##### 5. Spring Boot 的核心优势有哪些？
##### 6. 解释Spring Boot中的Actuator是什么及其用途。
##### 7. 如何在Spring Boot中使用profiles来管理不同环境的配置？
##### 8. 如何在Spring Boot项目中使用命令行运行器？
##### 9. 请描述Spring Boot的微服务架构支持。
##### 10. Spring Boot 中如何实现安全性配置？

### MyBatis
##### 1. MyBatis的核心组件有哪些？
- SqlSession/SqlSessionFactory
- SQL隐射XML文件, 这里对应实体是  MappedStatement
- Mapper 接口, 也是关联到 XML上
- Plugins



##### 2. MyBatis与Hibernate的区别及优劣势是什么？

##### 3. 在MyBatis中，如何实现动态SQL？
Mybatis 提供了一些列 SQL 标签，支持基于条件的SQL组装
比较核心的是 <if> 标签 来对此进行支持的
- <if> 
- <foreach>
- <where>
- <choosen>、when


##### 4. MyBatis是如何实现结果映射的？
- 通过在XML中定义 resultMap
- 通过 @Results 注解

##### 5. 解释MyBatis中的缓存机制。
- 一级缓存, SqlSession 级别, 默认开启 基于PerpetualCache, 底层是一个 Map 对象存储, key 
- 二级缓存, 默认不开，通过配置 enableCache, 缓存是事务级别 

##### 6. MyBatis中的映射文件有哪些部分组成？
核心就一个 <mapper> 标签, 头文件说明
其他可以定制增加
<select> / <update> 等

##### 7. 如何在MyBatis中实现分页？
- 手动分页 select * from limit 10, 20;
- PageHelper 插件
- Rowbounds mybatis原生

##### 8. 在MyBatis中，$和#的区别是什么？
- $ 文本替换
- # 会先替换成? 然后通过参数替换方式进行实际SQL生成, 可以防止 SQL 注入
    - 隔离数据与命令：在使用预处理语句时，数据（即 SQL 语句的参数）是独立于命令（即 SQL 语句本身）的。因为数据不是通过简单的字符串拼接进入 SQL 语句，而是作为参数传递，所以注入恶意的 SQL 命令（如 'OR '1'='1）将不会影响 SQL 语句的结构
    - 类型安全：
        预处理语句还强制数据类型正确匹配 SQL 语句中预期的数据类型。例如，如果一个字段预期是整数类型，试图插入一个字符串将会失败，这进一步减少了 SQL 注入的风险
    - 效率：
        预编译的 SQL 语句可以在不改变模板的情况下重复使用，只是替换参数。这不仅提高了执行效率，还减少了每次执行查询时解析 SQL 的需要，从而降低了注入的机会

##### 9. 如何在MyBatis中使用注解而不是XML？
通过注解在 mapper 接口的方法上, 声明 SQL 语句
- @Select
- @Insert
- @Update
- @Delete

##### 10. MyBatis中如何进行事务管理？

Mybatis 将事务委托给了外部

### Netty 概述

##### 1. Netty 是什么？
Netty 是一个高性能的 NIO 客户端服务器框架，它提供了异步事件驱动的网络应用程序框架和工具，用以快速开发高性能、高可靠性的网络服务器和客户端程序。

##### 2. 为什么要用 Netty？
使用 Netty 的原因有很多，主要包括：
- **高性能**：Netty 提供了高性能的 I/O 处理能力，能够承受高并发连接。
- **高可靠性**：Netty 的设计注重可靠性，提供了多种机制来确保数据的可靠传输。
- **灵活性**：Netty 提供了丰富的组件和扩展点，可以根据业务需求灵活定制。
- **易用性**：Netty 的 API 设计简洁易懂，使得开发网络应用变得更加容易。

##### 3. Netty 应用场景了解么？
Netty 被广泛应用于各种网络应用场景，包括：
- 服务器端：如 Web 服务器、游戏服务器、分布式服务等。
- 客户端：如 HTTP 客户端、数据库客户端、消息队列客户端等。
- 工具类：如网络通信组件、协议转换工具等。

##### 4. Netty 核心组件有哪些？分别有什么作用？
Netty 的核心组件包括：
- **Channel**：表示一个网络通道，可以是服务器端或客户端的网络连接。
- **ChannelPipeline**：处理 Channel 事件的处理器链，负责事件的过滤和处理。    
- **ChannelHandler**：定义了具体的事件处理逻辑。
- **EventLoop**：负责 I/O 操作和事件的触发，是 Netty 的核心 I/O 处理组件。
- **ByteBuf**：字节容器，用于网络数据的读写操作。

##### 5. EventLoopGroup 了解么? 和 EventLoop 啥关系?
EventLoopGroup 是 EventLoop 的集合，它包含了多个 EventLoop。EventLoop 是单线程的 I/O 处理组件，负责处理 Channel 的 I/O 操作和事件触发。EventLoopGroup 可以包含一个或多个 EventLoop，以支持多线程的并发处理。

##### 6. Bootstrap 和 ServerBootstrap 了解么？
Bootstrap 是 Netty 用于初始化客户端程序的辅助类，而 ServerBootstrap 用于初始化服务器端程序。它们提供了丰富的配置选项，以便定制化地设置网络参数和处理器。

##### 7. NioEventLoopGroup 默认的构造函数会起多少线程？
NioEventLoopGroup 默认的构造函数会根据 CPU 核心数创建线程。具体线程数可以通过方法 `Runtime.getRuntime().availableProcessors()` 获取。

##### 8. Netty 线程模型了解么？
Netty 的线程模型是基于 Reactor 模式的，它使用了多 Reactor 多线程模型。在这种模型中，有专门的 I/O 线程处理网络事件，而业务线程则处理具体的业务逻辑。这种分离可以提高系统的整体性能和稳定性。


##### 9. Netty 服务端和客户端的启动过程了解么？
Netty 服务端和客户端的启动过程都涉及以下几个步骤：
- 配置 `EventLoopGroup`：用于处理网络事件的线程组。
- 配置 `Channel`：指定使用的网络传输通道，如 NIO、Epoll 等。
- 配置 `ChannelPipeline`：添加业务处理器。
- 绑定或连接到远程服务器：服务端通过 `bind` 方法，客户端通过 `connect` 方法。


##### 10. Netty 长连接、心跳机制了解么？
- Netty 天然支持基于socket的长连接
- 心跳机制可以基于长连接对对端发起请求检测，可以基于一个队列轮询发起，或者基于HashedWheelTimer的方式


##### 11. Netty 的零拷贝了解么？
零拷贝是 Netty 中的一个重要特性，它允许数据在传输过程中不需要在用户空间和内核空间之间进行拷贝。
- ByteBuf
- Composite ByteBuf
- 
