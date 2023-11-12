FROM bitnami/minideb:latest AS base

ENV DEBIAN_FRONTEND noninteractive
ENV TEXMFHOME /project/texdir 

WORKDIR /project 

RUN mkdir $TEXMFHOME
RUN apt update && \
  apt install -yq --no-install-recommends \
    make \
    texlive-latex-recommended \
    texlive-fonts-recommended \
    texlive-pictures \
    texlive-lang-spanish \
    curl \
    wget \
    xz-utils 

COPY texpkgs.txt .

## Instalar los paquetes que necesitaremos. Dado que 
## la versión de texlive que viene instalada es del 2022, 
## configuraremos para usar el repository correspondiente.
RUN tlmgr --usermode init-usertree 
RUN tlmgr --usermode option repository ftp://tug.org/historic/systems/texlive/2022/tlnet-final
RUN tlmgr --usermode install $(cat texpkgs.txt | tr -s '\n' ' ')

FROM base as build

COPY . . 

