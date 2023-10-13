BINPATH = /usr/local/bin

install:
	pip install spotdl
	spotdl --download-ffmpeg
	chmod +x src/main.py
	sudo cp src/main.py $(BINPATH)/morg

uninstall:
	sudo rm -f $(BINPATH)/morg

run:
	pip install spotdl
	spotdl --download-ffmpeg
	python3 src/main.py
