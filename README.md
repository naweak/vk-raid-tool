# vk-raid-tool

## Установка
1. [Скачиваем архив](https://github.com/naweak/vk-raid-tool/releases) с последнией версией для своей системы
2. Распаковываем
3. Правим `etc/main.conf` под себя: в `access_token` вставляем свой токен авторизации, мнструкция по получению: https://vkhost.github.io/, в `delay` вставляем промежуток между сообщениями в секундах. 

## Использование
1. Заходим в командную строку (какое же название ущербное), пишем в ней `cd c:\путь\до\main.exe`
2. Программа запускается с помощью `main` в Windows или `./main` в Linux

### Пример команды
`main --type confshit --chat-id 123 --message hui` означает, что будет использоваться метод `confshit`, сообщения пойдут в чат с id 123, текст сообщения будет взят из `copypaste/hui`

### Методы
* `wallcomments` - для прохода по комментариям стены
* * **параметры**
* * `--count` количество постов для прохода
* * `--owner-id` id автора поста: для сообществ это **отрицательное число**
* * `--message` файл с сообщением из папки `copypaste`
* * `--attachments` вложения через запятую
* `wallpost` - для сранья на стене
* * **параметры**
* * `--owner-id` id автора стены
* * `--message` файл с сообщением из папки `copypaste`
* * `--attachments` вложения через запятую
* `confshit`
* * **параметры**
* * `--chat-id` id чата
* * `--message` сообщение из папки `copypaste`

## Компиляция из исходников
1. Установить Python 3 и pip3 (для Debian и Ubuntu `sudo apt install python3 python3-pip`)
2. С помощью pip3 поставить пакеты `vk pyinstaller` (`pip install vk pyinstaller` или для Linux ` sudo pip3 install vk pyinstaller`)
3. Перейти в директорию с исходниками
4. Собрать командой `pyinstaller -F main.py`
5. Вычистить все, кроме директорий `copypaste`, `dist`, `etc`
6. Переместить исполняемый файл `main` или `main.exe` из `dist` в директорию на уровень выше


В случае ошибок писать в https://github.com/naweak/vk-raid-tool/issues.
