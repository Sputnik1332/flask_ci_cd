# flask_ci_cd


### Подготовка репозитория
- `git clone https://github.com/Sputnik1332/flask_ci_cd.git`


- `git status`


- `git add .`

[после каждого изменения, которое хотим запушить в репу] \
[если добавляли новые файлы, то перед этим ещё делаем `git add .`]
- `git commit -am "initial commit"`
- `git push`

-----

## Linter

`pip install pylint`

### Добавление конфигурации для Actions (Linter)

**GitHub** --> **Actions** [--> New workflow]:

- Выбираем **Pylint** (configure)


- **Start commit** file

    создаётся файл конфигурации
`.github/workflows/pylint.yml`


- `git pull` [локально, для скачивания нового файла]



## Tests

`pip install pytest`

### Добавление конфигурации для Actions (Tests)

GitHub --> Actions --> New workflow

- Выбираем **Python application**

...


### Настройка тестов

- Создаём fixture клиента `./testing/conftest.py` (обязательно такое имя файла)


    from _pytest.fixtures import fixture
    from flask.testing import FlaskClient
    from main import app
    
    
    @fixture
    def client() -> FlaskClient:
        app.config.update(SERVER_NAME='myserver.org')
        with app.test_client() as client:
            with app.app_context():
                yield client

  Теперь client во всех тестах будет браться отсюда ^ \
  (для этого мы и указывали такое имя файла)
  
- Создаём тесты, например `testing/test_main.py`


    from flask import url_for
    import random
    
    
    def test_get_item(client):
        random_id = random.randint(1, 100)
        url = url_for('get_item', item_id=random_id)
        response = client.get(url)
        assert response.status_code == 200
        assert response.json['item']['id'] == random_id


- Запускаем тесты (pytest находит во всех каталогах с именем `test*` все файлы с именем `test*` и все функции с именем `test*` внутри)

  `pytest`