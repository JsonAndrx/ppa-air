# PPA AIR

## Descripción General

Este proyecto es una API para la búsqueda de vuelos, desarrollada con FastAPI y desplegada en Railway. La API permite buscar rutas de vuelo entre diferentes aeropuertos, especificando el origen, destino, fecha de viaje y el número máximo de escalas.

## URL de la Documentación

La documentación de la API está disponible en la siguiente URL: [Documentación de la API](https://ppa-air-production.up.railway.app/docs)

## Abordaje del Problema

Punto de Pago Air (PPA), una aerolínea en fase de lanzamiento planea iniciar operaciones en 8 aeropuertos nacionales colombianos: BOG, MDE, BAQ, BGA, SMR, CTG, CLO y EOH. La aerolínea ha establecido un itinerario semanal fijo, es decir, los mismos vuelos operarán los mismos días cada semana. Sin embargo, debido al tamaño inicial de la flota, no todos los aeropuertos estarán conectados por vuelos directos.

## Solución Implementada

### Algoritmo de Búsqueda en Profundidad (Depth-First Search, DFS)

El algoritmo DFS se implementó para encontrar todas las rutas posibles entre el aeropuerto de origen y el aeropuerto de destino. A continuación se describe cómo se implementó el algoritmo:

1. **Inicialización de Aeropuertos y Vuelos**: En el archivo `app/data/initial_data.py`, se inicializan los aeropuertos y los vuelos disponibles.

    ```python
    def initialize_airports_and_flights():
        airports = {
            "BOG": Airport("BOG"),
            "MDE": Airport("MDE"),
            ...
        }
        flights = [
            Flight("BOG", "MDE", 60, datetime(2024, 11, 9, 6, 0)),
            ...
        ]
        for flight in flights:
            airports[flight.origin].connections.append(flight)
        return airports
    ```

2. **Búsqueda de Rutas**: En el archivo `app/services/flight_search.py`, se implementó la función `find_all_routes_dfs` que utiliza DFS para encontrar todas las rutas posibles.

    ```python
    def find_all_routes_dfs(origin: str, destination: str, airports: dict, travel_date: datetime, max_stops: int = 2):
        routes = []
        dfs_find_routes(origin, destination, airports, [], routes, max_stops, timedelta(), travel_date)
        return routes
    ```

3. **Función Recursiva DFS**: La función `dfs_find_routes` realiza la búsqueda en profundidad recursiva para encontrar las rutas.

    ```python
    def dfs_find_routes(current: str, destination: str, airports: dict, path: List[Flight], routes: List[Dict], max_stops: int, total_duration: timedelta, travel_date: datetime):
        if current == destination:
            route_info = {
                "segments": [
                    {
                        "origin": flight.origin,
                        "destination": flight.destination,
                        "departure_time": flight.departure_time.strftime("%Y-%m-%d %H:%M"),
                        "arrival_time": (flight.departure_time + timedelta(minutes=flight.duration)).strftime("%Y-%m-%d %H:%M"),
                        "duration": flight.duration
                    } for flight in path
                ],
                "total_duration": total_duration.total_seconds() // 60
            }
            routes.append(route_info)
            return
        if len(path) > max_stops:
            return
        for flight in airports[current].connections:
            if flight.departure_time.date() == travel_date.date() and not any(f.destination == flight.destination for f in path):
                path.append(flight)
                dfs_find_routes(
                    flight.destination,
                    destination,
                    airports,
                    path,
                    routes,
                    max_stops,
                    total_duration + timedelta(minutes=flight.duration),
                    travel_date
                )
                path.pop()
    ```

### Explicación de la Función `dfs_find_routes`

La función `dfs_find_routes` es una implementación del algoritmo de búsqueda en profundidad (DFS) que se utiliza para encontrar todas las rutas posibles entre dos aeropuertos. Aquí se explica paso a paso lo que hace la función:

1. **Condición de Finalización**: Si el aeropuerto actual (`current`) es igual al aeropuerto de destino (`destination`), se ha encontrado una ruta válida. La información de la ruta se agrega a la lista de rutas (`routes`).

2. **Límite de Escalas**: Si el número de vuelos en la ruta actual (`path`) excede el número máximo de escalas permitidas (`max_stops`), la función retorna sin hacer nada.

3. **Iteración sobre Conexiones**: La función itera sobre todas las conexiones (vuelos) del aeropuerto actual. Para cada vuelo, verifica si la fecha de salida del vuelo coincide con la fecha de viaje especificada y si el destino del vuelo no está ya en la ruta actual (para evitar ciclos).

4. **Recursión**: Si el vuelo es válido, se agrega a la ruta actual (`path`) y se llama recursivamente a `dfs_find_routes` con el aeropuerto de destino del vuelo como el nuevo aeropuerto actual.

5. **Backtracking**: Después de la llamada recursiva, el vuelo se elimina de la ruta actual (`path`) para explorar otras posibles rutas.

## Despliegue

El proyecto está desplegado en Railway y se puede acceder a la documentación de la API en la siguiente URL: [Documentación de la API](https://ppa-air-production.up.railway.app/docs)