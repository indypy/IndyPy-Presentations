all: notes.html notes.pdf

notes.html: README.md
	pandoc $< -o $@ --standalone -t html5

notes.pdf: README.md
	pandoc $< -o $@ --latex-engine=xelatex

clean:
	rm -f notes.pdf

.PHONY: clean
