﻿# Тест на проверку, что по треку заказа можно получить данные о заказе в Яндекс.Самокат с помощью API Яндекс Самокат.
- Для запуска тестов должны быть установлены пакеты pytest и requests 
- Запуск теста выполянется командой pytest
- Все пути и URL хранятся в файле configuration.py
- Все запросы хранятся в файле sender_stand_request.py
- Тело POST-запросов хранится в файле data.py
- Тест для проверки создания заказа и получения его по трек номеру хранится в файле: create_new_order.py