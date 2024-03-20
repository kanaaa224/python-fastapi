Docker image 作成
```
$ docker-compose build
```

```pyproject.toml``` 作成
```
$ docker-compose run --entrypoint "poetry init --name python --dependency fastapi --dependency uvicorn[standard]" python
```

FastAPIのインストール
```
$ docker-compose run --entrypoint "poetry install --no-root" python
```

再ビルド
```
$ docker-compose build --no-cache
```

起動
```
$ docker-compose up
```
```
http://localhost:8000/docs
```

データベースの起動確認
```
$ docker-compose exec database mysql main
```

mysqlクライアントのインストール
```
$ docker-compose exec python poetry add sqlalchemy aiomysql
```

DB テーブル 作成
```
$ docker-compose exec python poetry run python -m api.database_migrate
```

コンテナ削除
```
$ docker-compose down --volumes --remove-orphans
```