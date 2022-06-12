scrape:
	docker-compose exec web bash -c "cd scrapy && \
	scrapy crawl otodom"

makemigrations:
	docker-compose exec web bash -c "cd scrapy/tychy && \
	alembic revision --autogenerate"

migrate:
	docker-compose exec web bash -c "cd scrapy/tychy && \
	alembic upgrade head"