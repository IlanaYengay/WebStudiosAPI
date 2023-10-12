# WebStudiosAPI

Проект WebStudiosAPI представляет собой систему, которая позволяет пользователям регистрироваться и авторизовываться на портале, редактировать свой профиль, создавать заказы и просматривать информацию о них. <br>
Главные функциональные возможности проекта: <br>
1. Регистрация и авторизация пользователей для доступа к порталу
2. Возможность редактировать профиль и обновлять информацию о себе
3. Создание заказов на портале
4. Просмотр информации о заказах, включая текущий статус и подробности заказа



## Установка

1. Склонируйте репозиторий:
   ```
   git clone https://github.com/WebStudiosAPI.git
   ```
2. Зайдите в проект
    ```
   cd WebStudios
    ```
3. Создайте и активируйте виртуальное окружение:
    ```
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
    ```
4. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
5. Убедитесь что у вас установлен redis:
    ```
   mac@MacBook ~ % redis-cli
   127.0.0.1:6379> ping
   PONG
   ```
   
6. Примените миграции:
   ```
   ./manage.py makemigrations && ./manage.py migrate
   ```
7. Запустите локальный сервер:
   ```
   ./manage.py runserver 
   ```
8. Запустите celery:
   ```
   celery -A WebStudios worker --loglevel=info
   ```
Проект будет доступен по адресу http://127.0.0.1:8000/. <br>

### Настройки доступа
Phone number: 87077776655 <br>
Password: 12345

## Работа с API
 
Документация на swagger:
http://127.0.0.1:8000/swagger/

### Регистрация, авторизация и профиль пользователя
1. **Регистрация и авторизация**: Для начала работы с сервисом пользователи должны зарегистрироваться. Авторизация происходит через JWT, и для входа используется номер телефона. При регистрации пользователя автоматически создается его профиль который в дальнейшем можно редактировать. <br>
 ***Ссылка для регистрации пользователей:*** http://127.0.0.1:8000/api/accounts/users/ 

2. **Редактирование профиля**: Пользователи могут редактировать свой профиль, включая загрузку фотографии профиля. Можно изменить имя, фамилию, дату рождения и биографию, но номер телефона изменить нельзя.<br>
 ***Ссылка для редактирования профиля:*** http://127.0.0.1:8000/api/profiles/profiles/{id}/

3. **Возраст и дата рождения**: При регистрации и заполнении поля "Дата рождения", пользователям младше 18 лет будет отказано в регистрации. При GET запросе на профиль возвращается возраст и дата рождения.


### Создание и управление заказами
1. **Создание заказа**: Авторизованные и не авторизованные пользователи могут создавать заказы. Если заказ был создан авторизованным пользователем, его создатель сохраняется. <br>
 ***Ссылка для создания заказа:*** http://127.0.0.1:8001/api/orders/orders/

2. **Уникальные номера заказов**: Каждый заказ получает уникальный случайный шестизначный номер.
3. **Поиск и просмотр заказов**: Заказы можно искать по номеру. Неавторизованные пользователи могут просматривать только те заказы, у которых нет пользователя. Авторизованные пользователи видят свои заказы и заказы без пользователя.
4. **Вложения к заказам**: Есть возможность прикреплять несколько фотографий к заказу.
5. **Обработка заказов**: В административной панели есть кнопка, которая позволяет передать заказ в "обработку". "Обработка" заказов ждет 10 секунд и изменяет статус заказа.






