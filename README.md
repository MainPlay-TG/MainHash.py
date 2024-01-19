# MainHash
## Описание
Удобные команды для контрольных сумм
## Установка
Для установки через PIP используйте
```bash
pip install -U mainhash
```
## Использование
Для импорта рекомендуется сокращённое название
```python
import MainHash as mh
```
Встроенная информация о модуле
```python
ms.__version__ -> str # Версия модуля
ms.__functions__ -> list # Функции, которые существуют в модуле
ms.__variables__ -> list # Переменные, которые существуют в модуле
ms.__depends__ -> dict # Обязательные и необязательные зависимости
```
#### Доступные алгоритмы
```python
mh._algs
# [...]
```
В примерах даже используется `sha256`, но его можно заменить на любой алгоритм из списка в переменной
### Контрольная сумма для текста
Для создания контрольной суммы из текста, текст сначала преобразуется в байты
```python
mh.sha256.text("Привет",encoding="utf-8")
# 'dd679c0b9fd408a04148aa7d30c9df393f67b7227f65693fffe0ed6d0f0ade59'
```
Кодировка по умолчанию: `utf-8`
### Контрольная сумма для локального файла
```python
mh.sha256.path("LICENSE")
# '340204d649a396644d27507047d9bd8b48d71e642aaae8d39c4c8806e231bf03'
```
### Контрольная сумма для открытого файла
```python
with open("LICENSE","rb") as file:
  ms.sha256.file(file)
# '340204d649a396644d27507047d9bd8b48d71e642aaae8d39c4c8806e231bf03'
```