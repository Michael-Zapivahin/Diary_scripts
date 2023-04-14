

## Запуск

Python3 должен быть уже установлен.

В терминале запускаем сайт (если он не запущен).

```
python manage.py runserver
```
открывает новое окно терминала и запускаем shell

```
python manage.py shell
```

Импортируем функции

- Получить пердмет

```
from scripts import get_subject  
```

- Получить ученика
```
from scripts import get_student  
```

- Удаление замечаний

```
from scripts import delete_Chastisements  
```

- Исправление оценок

```
from scripts import update_mark
```

- Создание похвалы

```
from scripts import create_Commendation 
```

Запускаем функции:

update_mark('Белозеров Авдей Федотович', 'Музыка', 6)

delete_Chastisements('Белозеров Авдей Федотович')

create_Commendation('Белозеров Авдей Федотович', 'Музыка')

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
