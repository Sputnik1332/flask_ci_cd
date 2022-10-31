# flask_ci_cd


## Linter

`pip install pylint`

### Подготовка репозитория
- `git clone https://github.com/Sputnik1332/flask_ci_cd.git`


- `git status`


- `git add .`

[после каждого изменения, которое хотим запушить в репу]
- `git commit -am "initial commit"`

- `git push`

-----

### Добавление конфигурации для Actions (Linter)

**GitHub** --> **Actions** [--> New workflow]:

- Выбираем **Pylint** (configure)


- **Commit** file

    создаётся файл конфигурации
`.github/workflows/pylint.yml`


- `git pull` [локально]


## Tests

GitHub --> Actions --> New workflow

- Выбираем **Python application**


