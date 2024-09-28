APP = restapi

test: 

compose:
	@docker-compose build
	@docker-compose up