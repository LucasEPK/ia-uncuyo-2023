# Trabajo Practico 2

*Lucas MOYANO*

## Ejercicio A
A) Para cada una de las siguientes actividades, describa en PEAS el entorno de la tarea y caracterizarlo en términos de las propiedades enumeradas.
- Jugar al CS (o cualquier otro 3d Shooter).
- Explorar los océanos.
- Comprar y vender tokens crypto (alguno).
- Practicar el tenis contra una pared.
- Realizar un salto de altura.
- Pujar por un artículo en una subasta.

| Tipo de agente | Medida de Performance | Entorno | Actuadores | Sensores |
| ----- | ----- | ----- | ----- | ----- |
| Bot que juega CS | Numero de kills, puntaje en el tablero y winrate | Mapa de juego, jugadores | Disparo, movimiento, plantar bomba, desactivar bomba, lanzar granadas, comunicación con el equipo | Sensor del mapa, sensor de jugadores, sensor de bomba, sensor de disparos, sensor de granadas |
| Explorador de océanos | Información nueva recolectada | Animales marinos, océano, corales, arena, plantas | Sistema de movimiento, cámaras, recolectores de materia, luces | Cámaras, sensores de movimiento, sensores de profundidad, sensores de contacto |
| Bot vendedor de tokens crypto | Ganancias | Market crypto, internet | Vendedor de crypto, comprador de crypto | Analizador de gráficos de crypto, analizador de situaciones contemporáneas relevantes |
| Robot que juega tenis contra una pared | Numero de golpes a la pelota concretados consecutivamente | Pared, pelota de tenis | Raqueta de tenis, brazo robotico, calculador de trayectoria de la pelota | Cámara, sensor de tacto en la raqueta |
| Robot de salto en altura | Altura del salto | Listón, colchoneta, saltometro | Piernas roboticas, calculador de salto | Cámara |
| Bot de puje de artículos de subastas | Artículos comprados, precio con relación a un articulo nuevo | Subastas, otras personas, otros bots | Pujador de precio | Comparador de precios, detector de pujes |