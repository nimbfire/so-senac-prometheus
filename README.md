Demontrando brevemente como funciona o prometheus

## running

Para levantar

`docker compose up -d`

Para desligar

`docker compose down`


## Como funciona

- 1 levantar o prometheus
- 2 levantar um app exporter
- 3 configurar prometheus (via yml) para saber onde buscar os dados do exporter
- 4 novo app exporter (dados fake)
- 5 levantar grafana
- 6 configurar grafana para enxergar prometheus como source
- 7 criar um dashboard usando os dados do prometheus


## Containers
Levantamos containers docker:

- prometheus
- grafana
- app exporter generico
- app exporter fake

