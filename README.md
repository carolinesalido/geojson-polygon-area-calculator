# Calculadora de Área de Polígonos GeoJSON

Este projeto Python utiliza a biblioteca GeoPandas para calcular a área de polígonos em um arquivo GeoJSON e salvar os resultados em um novo arquivo GeoJSON.

## Funcionalidades

* Lê um arquivo GeoJSON de entrada contendo polígonos.
* Calcula a área de cada polígono em metros quadrados.
* Cria um novo arquivo GeoJSON de saída com os mesmos polígonos e uma coluna adicional contendo as áreas calculadas.

## Como usar

1.  Certifique-se de ter o Python e a biblioteca GeoPandas instalados.
2.  Crie um arquivo GeoJSON contendo os polígonos dos quais deseja calcular a área.
3.  Execute o script `calcula_area.py`.
4.  O script criará um novo arquivo GeoJSON com as áreas calculadas.

## Requisitos

* Python 3.x
* GeoPandas

## Instalação

```bash
pip install geopandas