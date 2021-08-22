# Json Web Token

Json Web Token（缩写 JWT）是目前最流行的跨域认证解决方案。

## 跨域认证的问题

互联网服务离不开用户认证。一般流程是下面这样：

1. 用户向服务器发送用户名和密码。
2. 服务器验证通过后，在当前对话（session）里保存相关数据，比如用户角色、登录时间等。
3. 服务器向用户返回一个session_id，写入用户的Cookie。
4. 用户随后的每一次请求，都会通过Cookie，将session_id传回服务器。
5. 服务器收到session_id，找到前期保存的数据，由此得知用户的身份。

这种模式的问题在于，扩展性（scaling）不好。单机当然没有问题，如果是服务器集群，或者是跨域的服务导向架构，就要求session数据共享，每台服务器都能够读取session。

一种解决方案是session数据持久化，写入数据库或别的持久层。各种服务收到请求后，都向持久层请求数据，这种方案的优点是架构清晰，缺点是工程量比较大，另外，持久层万一挂了，就会单点失败。

另一种解决方案是服务器索性不保存session数据了，所有数据都保存在客户端，每次请求都发回服务器。JWT就是这种方案的一个代表。

## JWT的原理

JWT的原理是，服务认证以后，生成一个JSON对象，发回给用户，就像下面这样：

```json
{
	"姓名": "张三",
	"角色": "管理员",
	"到期时间": "2020年3月1日0点0分"
}
```

## JWT的数据结构

实际的JWT大概就像下面这样：

```
fe8ooiqnuqoun2nfoqjur93n4ij1.0i8jubnoa9iu085nhgpia94hiq9284.901oj231jf0euefnaklijfa
```

它是一个很长的字符串，中间用点分隔成三个部分。JWT的三个部分依次如下：

- Header（头部）
- Payload（负载）
- Signature（签名）

### Header

Header部分是一个JSON对象，描述JWT的元数据，通常是下面的样子：

```json
{
	"alg": "HS256",
	"typ": "JWT"
}
```

其中，alg属性表示签名的算法，默认是HMAC SHA256(写成HS256)；type属性表示这个令牌（token）的类型，JWT令牌统一写成JWT。最后，将上面的JSON对象使用Base64URL算法转成字符串。

### Payload

Payload部分也是一个JSON对象，用来存放实际需要传递的数据。JWT规定了7个官方字段，供选用：

- Iss（issuer）： 签发人
- exp（expiration time）：过期时间
- sub（subject）：主题
- aud（audience)：受众
- nbf（Not Before）：生效时间
- iat（Issued At）：签发时间
- jti（JWT ID)：编号

除了官方字段，还可以在这个部分定义私有字段。注意，JWT默认是不加密的，任何人都可以读到，所以不要把秘密信息放在这个部分。这个JSON对象也要使用Base64URL算法转成字符串。

### Signature

Signature部分是对前两部分的签名，防止数据篡改。

首先，需要制定一个秘钥（secret）。这个秘钥只有服务器才知道，不能泄露给用户，然后，使用Header里面指定的签名算法，按照下面的公式产生签名：

```java
HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload), secret)
```

算出签名以后，把Header，Payload，Signature三个部分拼成一个字符串，每个部分之间用点分隔，就可以返回给用户。

## JWT的使用方式

客户端收到服务器返回的JWT，可以储存在Cookie里面，也可以储存在localStorage。

此后，客户端每次与服务器通信，都要带上这个JWT。你可以把它放在Cookie里面自动发送，但是这样不能跨域，所以更好的做法是放在HTTP请求的头信息Authorization字段里面。

## JWT的几个特点

- JWT默认是不加密，但也是可以加密的。生成原始Token以后，可以用秘钥再加密一次。
- JWT不加密的情况下，不能将密码数据写入JWT
- JWT不仅可以用于认证，也可以用于交换信息。
- JWT的最大缺点是，由于服务器不保存session状态，因此无法在使用过程中废止某个token，或者更改token的权限。也就是说，一旦JWT签发了，在到期之前就会始终有效，除非服务器部署额外的逻辑。
- JWT本身包含了认证信息，一旦泄露，任何人都可以获得该令牌的所有权限。
- 为了减少盗用，JWT不应该使用HTTP协议明码传输，要使用HTTPS协议传输。