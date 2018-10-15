# vk-raid-tool
123

**[СКАЧАТЬ БЕЗ РЕГИСТРАЦИИ И СМС МОКРЫЕ-МОКРЫЕ ПИСЕЧКИ!!!](https://github.com/naweak/vk-raid-tool/archive/master.zip)**

## Установка
~~Инструкция только для Windows, т.к. с другими системами не тестировалось.~~
Для установки на Linux-системах нужно установить из родного для дистрибутива пакетного менеджера поставить пакеты `python3 python3-pip` и установить зависимости для самого скрипта с помощью `pip3 install vk` и можно запускать с помощью `python3 main.py`
<ol>
  <li>
    Ставим Python 3
    <ol>
      <li>
        Скачиваем установщик Python c https://python.org/
        <img src="https://i.imgur.com/A7cw23B.png" alt="Скачивание Python">
      </li>
      <li>
        Открываем файл установки и приводим настройки к такому виду:
        <img src="https://i.imgur.com/uUwROgs.png" alt="Установка Python"><br />
        Дальше методом тыка по кнопке "Далее"/"Next"
      </li>
    </ol>
  </li>
  <li>
    Ставим зависимости c помощью <code>install.bat</code> <b>ОТ ИМЕНИ АДМИНИСТРАТОРА</b>. Для Debian актуально <code>apt install python3 python3-pip && pip install clipboard vk</code>
  </li>
</ol>

## Использование
1. Получаем токен входа на http://vkhost.github.io/
![Получить токен](https://i.imgur.com/8aYLy6e.png)
2. Заходим в файл `/etc/main.conf` и вставляем его после `accessToken=`
![Вставить токен](https://i.imgur.com/soklOzv.png)
3. Открываем в коммандной строке папку с программой

![Меню файла](https://i.imgur.com/lFaRMCD.png) 

![CMD](https://i.imgur.com/DesLsgW.png)

4. Пишем команду 

```
python main.py --type wallcomments --count количество_постов --owner-id id_автора_поста --message текстовый_файл_в_copypaste
```

`--type wallcomments` означает, что будет выбран метод `wallcomments` (а других нету, АХАХАХХАХАХХАА)

`--count 50` означает, что программа будет оставлять комментарии на первых 50 постах. Количество может быть другим.

`--owner-id 12345` означает, что комментарии будут оставлены **у юзера** с id 12345. ID может быть любым.

`--owner-id -12345` означает, что комментарии будут оставлены **в группе** с id 12345. ID может быть любым.

При указании юзера пишется просто его id, а при указании группы перед ее id ставится "-": **-12345**

`--message ololo` означает, что будет отправлен текст из файла `copypaste/ololo` (**Для тупых:** файл находится в папке copypaste и называется ololo). Можно создавать свои файлы и редактировать готовые. Лучше создавать. **ФАЙЛ ДОЛЖЕН ИМЕТЬ КОДИРОВКУ WINDOWS-1251, ЕСЛИ ПРОГРАММА ЗАПУСКАЕТСЯ ПОД WINDOWS!!!**

В случае ошибок писать в https://github.com/naweak/vk-raid-tool/issues.
