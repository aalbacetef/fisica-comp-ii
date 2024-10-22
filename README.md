# Introducción

En este repo hay dos Dockerfiles. `tex.Dockerfile` se usa para generar los documentos y `python.Dockerfile` para tener un entorno de desarrollo, independiente de la máquina en la que estés.

**Mirror of [gitlab.com/aalbacetef/fisica-comp-ii](gitlab.com/aalbacetef/fisica-comp-ii).**

## Entregas

Para ver las entregas, ir a "Releases" 
([link](https://gitlab.com/aalbacetef/fisica-comp-II/-/releases)).

## Comandos

La forma más fácil de interactuar con este repo es con `make`. 

### Generar documentos

El siguiente comando generará pdf de las PEC en la carpeta `documents/`:

```bash
make gen-documents 
```

### Entorno de desarrollo 

El siguiente comando ejecutará un entorno de desarrollo. 

```bash
make run-py
```

Nota: los cambios no se guardarán. 

Si se desea, el siguiente comando hará lo mismo que el anterior pero con el directorio montado (por ende los cambios no quedan aislados).

```bash
make run-py-dev
```

