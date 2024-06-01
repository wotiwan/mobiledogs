# MobileDogs_API

## Описание проекта

MobileDogs_API представляет собой систему мониторинга и управления собаками, оснащёнными специальными ошейниками, а также взаимодействия с волонтёрами, которые помогают в уходе за собаками. Основная цель системы - обеспечение безопасности и здоровья питомцев с помощью отслеживания их местоположения и активности.

Система включает два основных модуля: "Песики" и "Волонтёры". Эти модули взаимодействуют с сервером на FastAPI через различные запросы и ответы.

## Сценарии использования

1. **Регистрация нового ошейника**
    - Пользователь регистрирует новый ошейник в системе.
    - Сервер сохраняет данные ошейника и возвращает уникальный идентификатор (ID).

2. **Получение списка ошейников**
    - Пользователь запрашивает список всех зарегистрированных ошейников.
    - Сервер возвращает список ошейников в формате JSON.

3. **Архивация записи ошейника**
    - Пользователь удаляет запись об ошейнике.
    - Сервер архивирует запись и возвращает статус операции.

4. **Отправка координат**
    - Ошейник отправляет текущие координаты (широта, долгота, время) на сервер.
    - Сервер сохраняет данные и возвращает статус операции.

5. **Получение трека**
    - Пользователь запрашивает трек перемещения ошейника за определённый период.
    - Сервер возвращает трек в формате JSON.

6. **Регистрация нового волонтёра**
    - Новый волонтёр регистрируется в системе с указанием Telegram и ФИО.
    - Сервер сохраняет данные волонтёра и возвращает уникальный идентификатор (UID).

7. **Привязка песика к волонтёру**
    - Пользователь привязывает ошейник к волонтёру.
    - Сервер обновляет данные и возвращает статус операции.

8. **Удаление привязки**
    - Пользователь удаляет привязку ошейника от волонтёра.
    - Сервер обновляет данные и возвращает статус операции.
