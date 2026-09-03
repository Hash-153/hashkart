.PHONY: help install dev test test-backend test-frontend build lint clean docker-up docker-down

help:
	@echo "NovaMart Platform Build System"
	@echo "  make install       Install backend and frontend dependencies"
	@echo "  make dev           Start both backend and frontend development servers"
	@echo "  make test          Run full test suite (pytest + vitest)"
	@echo "  make test-backend  Run backend pytest suite"
	@echo "  make test-frontend Run frontend vitest suite"
	@echo "  make build         Build frontend production bundle"
	@echo "  make docker-up     Start platform via Docker Compose"
	@echo "  make docker-down   Stop Docker containers"

install:
	cd backend && pip install -r requirements.txt
	cd frontend && npm install

dev:
	python app.py

test: test-backend test-frontend

test-backend:
	cd backend && pytest --cov=app --cov-report=term-missing

test-frontend:
	cd frontend && npm test -- --run

build:
	cd frontend && npm run build

lint:
	cd backend && flake8 app tests --max-line-length=120
	cd frontend && npm run lint

docker-up:
	docker-compose up -d --build

docker-down:
	docker-compose down

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf frontend/dist backend/.pytest_cache
