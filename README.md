# "Happy Computing"

Happy Computing es un taller de reparaciones electrónicas se realizan las siguientes actividades (el precio de cada servicio se muestra entre paréntesis):
1. Reparación por garantía (Gratis)
2. Reparación fuera de garantía ($350)
3. Cambio de equipo ($500)
4. Venta de equipos reparados ($750)

Se conoce además que el taller cuenta con 3 tipos de empleados: Vendedor, Técnico y Técnico Especializado.

Para su funcionamiento, cuando un cliente llega al taller, es atendido por un vendedor y en caso de que el servicio que requiera sea una Reparación (sea de tipo 1 o 2) el cliente debe ser atendido por un técnico (especializado o no).
Además en caso de que el cliente quiera un cambio de equipo este debe ser atendido por un técnico especializado. Si todos los empleados que pueden atender al cliente están ocupados, entonces se establece una cola para sus servicios. Un técnico especializado sólo realizará reparaciones si no hay ning´un cliente que desee un cambio de equipo en la cola.

Se conoce que los clientes arriban al local con un intervalo de tiempo que distribuye poisson con λ = 20 minuts y que el tipo de servicios que requieren pueden ser descrito mediante la tabla de probabilidades:

Tipo de Servicio | Probabilidad
--- | ---
1   |   0.45
2   |   0.25
3   |   0.1
4   |   0.2

Además se conoce que un técnico tarda un tiempo que distribuye exponecial con λ = 20 minutos, en realizar una reparación cualquiera. Un técnico especializdo tarda un tiempo que distribuye exponencial con λ = 15 minutos para
realizar un cambio de equipos y la vendedora puede atender cualquier servicio en un tiempo que distribuye normal (N(5 min, 2mins)). 

El dueño del lugar desea realizar una simulación de la ganancia que tendría en una jornada laboral si tuviera 2 vendedores, 3 técnicos y 1 técnico especializado.