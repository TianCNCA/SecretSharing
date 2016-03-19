all: run

build:
	pip install numby

run:
	python Source/Dealer.py

clean:
	rm Source/*.pyc
	rm Tests/*.pyc
