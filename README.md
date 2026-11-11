# CI/CD practice

[![CI](https://github.com/DiDo1107/ci-cd-practice/actions/workflows/ci.yml/badge.svg)](https://github.com/DiDo1107/ci-cd-practice/actions/workflows/ci.yml)

Простое Flask-приложение для практических заданий по CI/CD.

## Запуск локально

```bash
pip install -r requirements-dev.txt
pytest -v
python -m app.main   # http://localhost:5000
```

## Эндпоинты

| URL | Описание |
|---|---|
| `/` | приветствие и версия |
| `/health` | проверка работоспособности |
| `/calc/<add\|sub\|mul\|div>/<a>/<b>` | калькулятор |
