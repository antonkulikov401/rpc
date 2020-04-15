# Remote procedure call server/client

Python version: 3.7.5

Интерфейс клиента и сервера реализованы в пакете ```rpc```.

```daemon.py``` запускает сервер с задачей ```square``` (которую можно заменить на любую полезную). Этот процесс предполагается скрыть и перенаправить ```stdin``` и ```stdout```.

Пример использования интерфейса клиента приведен в файле ```sample_client.py```.