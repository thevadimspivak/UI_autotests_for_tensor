# README.md

## Запуск тестов с созданием отчёта

Тесты с отчётом можно запускать с помощью bash скрипта `run_tests_with_report.sh.sh`. Этот скрипт генерирует отчет с текущим временем и сохраняет его в папке `reports`.

Чтобы запустить тесты, выполните следующую команду в терминале:
```bash
./run_tests_with_report.sh
```

### Запустить все тесты с выводом логов в консоль
```bash
pytest ./tests -s -v
```

### Все логи хранятся в папке logs в соответствующих файла для каждого браузера:
[logs_chrome.log](logs%2Flogs_chrome.log)

[logs_edge.log](logs%2Flogs_edge.log)

[logs_firefox.log](logs%2Flogs_firefox.log)
