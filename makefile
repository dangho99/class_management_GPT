TORCH_URL = https://download.pytorch.org/whl/cu118
PROJECT_TYPE = openproject


clean:
	rm -rf $(VENV)
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

install:
	pip install --upgrade pip 
	echo "Upgrade pip successfully."
	echo "Begin installing setuptools ..."
	pip install setuptools
	echo "Install setuptools successfully."
	echo "Begin installing torch ..."
	pip install torch torchvision torchaudio --index-url $(TORCH_URL)
	echo "Install torch successfully."
	echo "Begin installing python libary ..."
	pip install -r requirements.txt
	echo "Install installing python successfully."

up:
	docker compose -f docker-compose.${PROJECT_TYPE}.yml up -d

down:
	docker compose -f docker-compose.${PROJECT_TYPE}.yml down
