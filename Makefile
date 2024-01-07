


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

.PHONY: build-imgs build-tex-img build-py-img 

build-imgs: build-tex-img build-py-img 

build-tex-img:
	$(RUNNER) build -t $(TAG_TEX) -f $(DOCKERFILE_TEX) .

build-py-img:
	$(RUNNER) build -t $(TAG_PYT) -f $(DOCKERFILE_PYT) .

.PHONY: clean clean-pycache

clean:
	rm -rf documents/
	mkdir documents 

clean-pycache:
	find . -type d -name '__pycache__' | xargs -I W rm -r W


## Esta sección contiene una regla que genera los targets
## para la creación de los documentos.

PEC_TARGETS = pec3 pec4 pec5 pec6 

.PHONY: pec3 pec4 pec5 pec6 

define pecn_doc_rule
$(1):
	mkdir -p documents/$(1)
	cd ./pecs/$(1) && \
		pdflatex --syntex=1 --interaction=nonstopmode \
		--output-directory=../../documents/$(1) \
		$(1).tex 
	cd ./pecs/$(1) && \
		pdflatex --syntex=1 --interaction=nonstopmode \
		--output-directory=../../documents/$(1) \
		$(1).tex 
endef 

$(foreach pec,$(PEC_TARGETS),$(eval $(call pecn_doc_rule,$(pec))))

## generar los documentos (pdfs) en documents/
.PHONY: gen-documents 
gen-documents: build-tex-img clean 
	$(foreach pec,$(PEC_TARGETS), \
		@echo "generating $(pec)"; \
		$(RUNNER) run \
			--rm \
			-v $(shell realpath documents):/project/documents \
			$(TAG_TEX) \
			make $(pec) \
	)


## Esta sección contiene algunos comandos 
## para ejecutar el código de las pecs o 
## un entorno de desarrollo/trabajo.

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
	poetry run python -m code.pecs.pec6.ex10
	poetry run python -m code.pecs.pec6.ex11
