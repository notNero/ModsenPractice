# **Image Duplicates**
Этот проект предназначен для поиска дублирующихся изображений в указанных папках.

### Описание
Проект Image Duplicates позволяет найти и идентифицировать дублирующиеся изображения на основе их содержимого как в одной папке с изображениями, так и из двух разных
папок. Используя алгоритмы хэширования и сравнения изображений, проект определяет, какие изображения являются идентичными или очень похожими.

### Функциональность
- Загрузка изображений из указанных директорий.
- Поддержка различных форматов изображений (JPEG, PNG, BMP, GIF).
- Визуализация дубликатов.
- Возможность удаления найденных дубликатов для освобождения места.

### Запуск программы

```
python main.py <путь_к_папке1> [<путь_к_папке2>]

```

# **Weather API**
Этот проект представляет собой реализацию веб-сервиса для получения данных о погоде, а так же для получения различных статусов ответов

### Описание
Проект написан с использованием Flask и API OpenWeatherMap и позволяет получить ответы и статусы ответов от API

### Функциональность
- Получение текущей погоды по заданному городу.
- Получение статуса ответа.
- Обработка ошибок(403, 404 и др.) и предоставление информативных сообщений.

### Запуск программы

```
python app.py

```
Адрес работы сервиса после запуска: ``http://127.0.0.1:5000/...``
