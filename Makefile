scrape:
	docker-compose exec web bash -c "cd scrapy && \
	scrapy crawl otodom"
