.PHONY: build run restart

build:
	docker build -t email-host .

run:
	docker run -d --name email-host-container -p 8000:8000 email-host

restart:
	@docker stop email-host-container || true
	@docker rm email-host-container || true
	make build
	make run