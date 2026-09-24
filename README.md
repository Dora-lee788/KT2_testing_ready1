# КТ — тестирование файлов

## CSV

Выполнен расчёт среднего арифметического оценок из столбца `Final`.
При проверке исходного CSV найдена ошибка в строке 10. После исправления среднее арифметическое `Final` составило `53.00`.

![Результат работы с CSV](screenshots/04_csv_result.png)

## Проверка через pytest

Проверка выполнена через `pytest -v`. Все 5 тестов пройдены успешно.

![Результат pytest](screenshots/05_pytest_result.png)

## JSON

В `SuperHero.json` добавлены 2 новых супергероя. Все супергерои отсортированы по возрасту. Результат сохранён в `superhero_new.json`.

![Результат superhero_new.json — часть 1](screenshots/06_superhero_new_1.png)

![Результат superhero_new.json — часть 2](screenshots/07_superhero_new_2.png)

Результат запуска программы:

![Результат работы с JSON](screenshots/08_json_program_result.png)
