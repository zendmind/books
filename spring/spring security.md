# Spring Security

## Security today

### 1.1 Spring Security: The what and the why

Spring Security is the primary choice for implementing application-level security in Spring applications. Generally, its purpose is to offer you a highly customizable way of implementing authentication, authorization, and protection against common attacks.



### 1.2 What is software security?

![image-20210421142009381](spring security.assets/image-20210421142009381.png)

### 1.3 Why is security important?

The cost of an attack is usually higher than the investment cost of avoiding the vulnerability.

### 1.4 Common security vulnerabilities in web applications

- Broken authentication
- Session fixation
- Cross-site scripting (XSS)
- Cross-site request forgery (CSRF) 
- Injections
- Sensitive data exposure
- Lack of method access control
- Using dependencies with known vulnerabilities

#### 1.4.1 Vulnerabilities in authentication and authorization

​	![image-20210425100511694](spring security.assets/image-20210425100511694.png)

#### 1.4.2 What is session fixation?

*Session fixation* vulnerability is a more specific, high-severity weakness of a web applica- tion. If present, it permits an attacker to impersonate a valid user by reusing a previ- ously generated session ID. 

#### 1.4.3 What is cross-site scripting (XSS)?

*Cross-site scripting*, also referred to as XSS, allows the injection of client-side scripts into web services exposed by the server, thereby permitting other users to run these.

![image-20210425100923198](spring security.assets/image-20210425100923198.png)

![image-20210425100933602](spring security.assets/image-20210425100933602.png)

#### 1.4.4 What is cross-site request forgery (CSRF)?

![image-20210425102049531](spring security.assets/image-20210425102049531.png)

#### 1.4.5 Understanding injection vulnerabilities in web applications

Injection attacks on systems are widespread. In an *injection* attack, the attacker employ- ing a vulnerability introduces specific data into the system. The purpose is to harm the system, to change data in an unwanted way, or to retrieve data that’s not meant to be accessed by the attacker.

#### 1.4.6 Dealing with the exposure of sensitive data

Most of the time, developers learn continuously from theoretical examples. Generally, examples are simplified to allow the reader to focus on a specific topic. But a downside of this simplification is that developers get used to wrong approaches. Developers might mistakenly think that everything they read is a good practice.

#### 1.4.7 What is the lack of method access control?

![image-20210425110800371](spring security.assets/image-20210425110800371.png)

#### 1.4.8 Using dependencies with known vulnerabilities

When developing any piece of software, we have to take all the needed measures to avoid the use of any dependency that has known vulnerabilities. If we discover that we’ve used such a dependency, then we not only have to correct this fast, we also have to investigate if the vulnerability was already exploited in our applications and then take the needed measures.

### 1.5 Security applied in various architectures

#### 1.5.1 Designing a one-piece web application

![image-20210425111938352](spring security.assets/image-20210425111938352.png)

#### 1.5.2 Designing security for a backend/frontend separation

![image-20210425112408230](spring security.assets/image-20210425112408230.png)

**A short reminder of application scalability**

*Scalability* refers to the quality of a software application in which it can serve more or fewer requests while adapting the resources used, without the need to change the application or its architecture. Mainly, we classify scalability into two types: vertical and horizontal.

When a system is scaled vertically, the resources of the system on which it executes are adapted to the need of the application (for example, when there are more requests, more memory and processing power are added to the system).

We accomplish horizontal scalability by changing the number of instances of the same application that are in execution (for example, if there are more requests, another instance is started to serve the increased need). Of course, I assume the newly spun-up application instances consume resources offered by additional hard- ware, sometimes even in multiple data centers. If the demand decreases, we can reduce the instance numbers.

#### 1.5.3 Understanding the OAuth 2 flow

1. The user accesses a use case in the application (also known as the client). The application needs to call a resource in the backend.
2. To be able to call the resource, the application first has to obtain an access token, so it calls the authorization server to get the token. In the request, it sends the user credentials or a refresh token, in some cases.
3. If the credentials or the refresh token are correct, the authorization server returns a (new) access token to the client.
4. The header of the request to the resource server uses the access token when calling the needed resources.

![image-20210425113215602](spring security.assets/image-20210425113215602.png)

The following lists some of the advantages of this flow:

- The client doesn’t have to store the user credentials. The access token and, eventually, the refresh token are the only access details you need to save.
- The application doesn’t expose the user credentials, which are often on the network.
- If someone intercepts a token, you can disqualify the token without needing to invalidate the user credentials.
- A token can be used by a third entity to access resources on the user’s behalf, without having to impersonate the user. Of course, an attacker can steal the token in this case. But because the token usually has a limited lifespan, the time- frame in which one can use this vulnerability is limited.

Many ways to manage the tokens:

- Persisting the tokens in the app’s memory
- Persisting the tokens in a database
- Using cryptographic signatures with JSON Web Tokens (JWT)



#### 1.5.4 Using API keys, cryptographic signatures, and IP validation to secure requests



### Summary

- Spring Security is the leading choice for securing Spring applications. It offers a significant number of alternatives that apply to different styles and architec- tures.
- You should apply security in layers for your system, and for each layer, you need to use different practices.
- Spring Security is the leading choice for securing Spring applications. It offers a significant number of alternatives that apply to different styles and architec- tures.
- You should apply security in layers for your system, and for each layer, you need to use different practices.

## Hello Spring Security

### 2.1 Starting with the first project

>**Calling the endpoint with HTTP Basic authentication**
>
>With cURL, you can set the HTTP basic username and password with the -u flag. Behind the scenes, cURL encodes the string <username>:<password> in Base64 and sends it as the value of the Authorization header prefixed with the string Basic. And with cURL, it’s probably easier for you to use the -u flag. But it’s also essential to know what the real request looks like. So, let’s give it a try and manually create the Authorization header.
>
>In the first step, take the <username>:<password> string and encode it with Base64. When our application makes the call, we need to know how to form the correct value for the Authorization header. You do this using the Base64 tool in a Linux console. You could also find a web page that encodes strings in Base64, like https://www.base64encode.org. This snippet shows the command in a Linux or a Git Bash console:
>
>echo -n user:93a01cf0-794b-4b98-86ef-54860f36f7f3 | base64
>
>Running this command returns this Base64-encoded string:
>
>dXNlcjo5M2EwMWNmMC03OTRiLTRiOTgtODZlZi01NDg2MGYzNmY3ZjM=
>
>You can now use the Base64-encoded value as the value of the Authorization header for the call. This call should generate the same result as the one using the -u option:
>
>curl -H "Authorization: Basic dXNlcjo5M2EwMWNmMC03OTRiLTRiOTgtODZlZi01NDg2MGYzNmY3ZjM=" http://localhost:8080/hello
>
>The result of the call is
>
>Hello!



### 2.2 Which are the default configurations?

![image-20210425165142593](spring security.assets/image-20210425165142593.png)

- The authentication filter delegates the authentication request to the authenti- cation manager and, based on the response, configures the security context.

- The authentication manager uses the authentication provider to process

  authentication.

- The authentication provider implements the authentication logic.

- The user details service implements user management responsibility, which the

  authentication provider uses in the authentication logic.

- The password encoder implements password management, which the authenti-

  cation provider uses in the authentication logic.

- The security context keeps the authentication data after the authentication

  process.

**generate a self-signed certificate**

```shell
$ openssl req -newkey rsa:2048 -x509 -keyout key.pem -out cert.pem -days 365

$ openssl pkcs12 -export -in cert.pem -inkey key.pem -out certificate.p12 -name "certificate"
```



### 2.3 Overriding default configurations

#### 2.3.1 Overriding the UserDetailsService component

```java
@Configuration
public class ProjectConfig {

    @Bean
    public UserDetailsService userDetailsService() {
        var userDetailsService = new InMemoryUserDetailsManager();
        var user = User.withUsername("John")
                .password("111111")
                .authorities("read")
                .build();
        userDetailsService.createUser(user);
        return userDetailsService;
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return NoOpPasswordEncoder.getInstance();
    }
}
```

#### 2.3.2 Overriding the endpoint authorization configuration

```java
@Configuration
public class ProjectConfig extends WebSecurityConfigurerAdapter {

    @Bean
    public UserDetailsService userDetailsService() {
        var userDetailsService = new InMemoryUserDetailsManager();
        var user = User.withUsername("John")
                .password("111111")
                .authorities("read")
                .build();
        userDetailsService.createUser(user);
        return userDetailsService;
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return NoOpPasswordEncoder.getInstance();
    }

    @Override
    protected void configure(HttpSecurity httpSecurity) throws Exception {
        httpSecurity.httpBasic();
        httpSecurity.authorizeRequests()
                    .anyRequest()
                    .permitAll();
    }
}
```

#### 2.3.3 Setting the configuration in different ways

```java
@Configuration
public class ProjectConfig extends WebSecurityConfigurerAdapter {

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        var userDetaisService = new InMemoryUserDetailsManager();

        var user = User.withUsername("rico")
                .password("111111")
                .authorities("read")
                .build();
        userDetaisService.createUser(user);

        auth.userDetailsService(userDetaisService).passwordEncoder(NoOpPasswordEncoder.getInstance());
    }

    @Override
    protected void configure(HttpSecurity httpSecurity) throws Exception {
        httpSecurity.httpBasic();
        httpSecurity.authorizeRequests()
                .anyRequest()
                .authenticated();
    }
}
```

#### 2.3.4 Overriding the AuthenticationProvider implementation

```java
@Component
public class CustomAuthenticationProvider implements AuthenticationProvider {


    @Override
    public Authentication authenticate(Authentication authentication) throws AuthenticationException {
        String username = authentication.getName();
        String password = String.valueOf(authentication.getCredentials());

        if ("rico".equals(username) && "11111".equals(password)) {
            return new UsernamePasswordAuthenticationToken(username, password, Arrays.asList());
        } else {
            throw new AuthenticationCredentialsNotFoundException("Error in authentication");
        }
    }

    @Override
    public boolean supports(Class<?> authenticationType) {
        return UsernamePasswordAuthenticationToken.class.isAssignableFrom(authenticationType);
    }
}
```

```java
@Configuration
public class ProjectConfig extends WebSecurityConfigurerAdapter {

    @Autowired
    private CustomAuthenticationProvider customAuthenticationProvider;

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.authenticationProvider(customAuthenticationProvider);
    }

    @Override
    protected void configure(HttpSecurity httpSecurity) throws Exception {
        httpSecurity.httpBasic();
        httpSecurity.authorizeRequests()
                .anyRequest()
                .authenticated();
    }
}
```

#### 2.3.5 Using multiple configuration classes in your project

```java
@Configuration
public class UserManagementConfig {

    @Bean
    public UserDetailsService userDetailsService() {
        var userDetailsService = new InMemoryUserDetailsManager();

        var user = User.withUsername("rico")
                .password("111111")
                .authorities("read")
                .build();
        userDetailsService.createUser(user);
        return userDetailsService;
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return NoOpPasswordEncoder.getInstance();
    }
}

```

```
@Configuration
public class WebAuthorizationConfig extends WebSecurityConfigurerAdapter {

    @Override
    protected void configure(HttpSecurity httpSecurity) throws Exception {
        httpSecurity.httpBasic();
        httpSecurity.authorizeRequests().anyRequest().authenticated();
    }
}
```



## Managing users

### 3.1 Implementing authetication in Spring Security

![image-20210428102816470](spring security.assets/image-20210428102816470.png)

The **UserDetailsService** returns the details of a user, finding the user by its name. The **UserDetails** contract describes the user. A user has one or more authorities, represented by the **GrantedAuthority** interface. To add operations such as create, delete, or change password to the user, the **UserDetailsManager** contract extends **UserDetailsService** to add operations.

### 3.2 Describing the user

#### 3.2.1 Demystifying the definition of the UserDetails contract

```java
public interface UserDetails extends Serializable {
  // These methods return the user credentials.
  String getUsername();
  String getPassword();
  // Returns the actions that the app allows the user to do as a collection.
  // of GrantedAuthority instances
	Collection<? extends GrantedAuthority> getAuthorities();
  // These four methods enable or disable the account for different reasons.
  boolean isAccountNonExpired();
  boolean isAccountNonLocked();
  boolean isCredentialsNonExpired();
  boolean isEnabled();
}
```

#### 3.2.2 Detailing on the GrantedAuthority contract

```java
public interface GrantedAuthority extends Serializable {
}
```

#### 3.2.3 Writing a minimal implementation of UserDetails

```java

```

