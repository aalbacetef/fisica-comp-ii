

.PHONY: build-imgs build-tex-img build-py-img run-dev run-tex gen-documents clean clean-pycache

## si usas docker, cambiar esto a "docker"
RUNNER := podman 

## se usan dos imágenes:
##  - una para desarrollo (python)
##  - una para generar los documentos
TAG_TEX := fisica-comp-ii:tex 
TAG_PYT := fisica-comp-ii:python
DOCKERFILE_TEX := tex.Dockerfile 
DOCKERFILE_PYT := python.Dockerfile


## no generar __pycache__
export PYTHONDONTWRITEBYTECODE := 1

build-imgs: build-tex-img build-py-img 

build-tex-img:
	$(RUNNER) build -t $(TAG_TEX) -f $(DOCKERFILE_TEX) .

build-py-img:
	$(RUNNER) build -t $(TAG_PYT) -f $(DOCKERFILE_PYT) .

clean:
	rm -rf documents/
	mkdir documents 

## generar los documentos (pdfs) en documents/
gen-documents: build-tex-img clean 
	@echo "generating pec3"
	@$(RUNNER) run \
		--rm \
		-v $(shell realpath documents):/project/documents \
		$(TAG_TEX) \
		make pec3
	@echo "generating pec4"
	@$(RUNNER) run \
		--rm \
		-v $(shell realpath documents):/project/documents \
		$(TAG_TEX) \
		make pec4
	@echo "generating pec5"
	@$(RUNNER) run \
		--rm \
		-v $(shell realpath documents):/project/documents \
		$(TAG_TEX) \
		make pec5
	@echo "generating pec6"
	@$(RUNNER) run \
		--rm \
		-v $(shell realpath documents):/project/documents \
		$(TAG_TEX) \
		make pec6

.PHONY: pec3 pec4 pec5 pec6 

pec3:
	mkdir -p documents/pec3 
	cd ./pecs/pec3 && \
		pdflatex \
		--synctex=1 --interaction=nonstopmode \
		--output-directory=../../documents/pec3 \
		pec3.tex 
	cd ./pecs/pec3 && \
		pdflatex \
		--synctex=1 --interaction=nonstopmode \
		--output-directory=../../documents/pec3 \
		pec3.tex 

pec4:
	mkdir -p documents/pec4 
	cd ./pecs/pec4 && \
		pdflatex \
		--synctex=1 --interaction=nonstopmode \
		--output-directory=../../documents/pec4 \
		pec4.tex 
	cd ./pecs/pec4 && \
		pdflatex \
		--synctex=1 --interaction=nonstopmode \
		--output-directory=../../documents/pec4 \
		pec4.tex 

pec5:
	mkdir -p documents/pec5
	cd ./pecs/pec5 && \
		pdflatex \
		--synctex=1 --interaction=nonstopmode \
		--output-directory=../../documents/pec5 \
		pec5.tex 
	cd ./pecs/pec5 && \
		pdflatex \
		--synctex=1 --interaction=nonstopmode \
		--output-directory=../../documents/pec5 \
		pec5.tex 

pec6:
	mkdir -p documents/pec6
	cd ./pecs/pec6 && \
		pdflatex \
		--synctex=1 --interaction=nonstopmode \
		--output-directory=../../documents/pec6 \
		pec6.tex 
	cd ./pecs/pec6 && \
		pdflatex \
		--synctex=1 --interaction=nonstopmode \
		--output-directory=../../documents/pec6 \
		pec6.tex 

.PHONY: run-tex run-py run-py-dev

run-tex: build-tex-img 
	$(RUNNER) run -it --rm $(TAG_TEX) bash

run-py: build-py-img 
	$(RUNNER) run -it --rm $(TAG_PYT) bash 

run-py-dev: build-py-img 
	$(RUNNER) run -it --rm -v $(shell realpath .):/project $(TAG_PYT) bash 

.PHONY: run-pec3 run-pec4 run-pec5 run-pec6

run-pec3: 
	poetry run python -m code.pecs.pec3.ex1
	poetry run python -m code.pecs.pec3.ex3
	poetry run python -m code.pecs.pec3.ex4
	poetry run python -m code.pecs.pec3.ex5
	poetry run python -m code.pecs.pec3.ex6
	poetry run python -m code.pecs.pec3.ex7

run-pec4: 
	poetry run python -m code.pecs.pec4.ex3
	poetry run python -m code.pecs.pec4.ex4
	poetry run python -m code.pecs.pec4.ex5
	poetry run python -m code.pecs.pec4.ex6
	poetry run python -m code.pecs.pec4.ex7

run-pec5: 
	poetry run python -m code.pecs.pec5.ex1 
	poetry run python -m code.pecs.pec5.ex2 
	poetry run python -m code.pecs.pec5.ex3  
	poetry run python -m code.pecs.pec5.ex4 
	poetry run python -m code.pecs.pec5.ex5

run-pec6:
	poetry run python -m code.pecs.pec6.ex4
	poetry run python -m code.pecs.pec6.ex5

.PHONY: clean-pycache
clean-pycache:
	find . -type d -name '__pycache__' | xargs -I W rm -r W
