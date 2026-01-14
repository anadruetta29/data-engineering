# Sales Data Pipeline – Data Engineering Case Study

Este proyecto simula un pipeline de Data Engineering para el análisis de ventas
en un e-commerce. El objetivo es transformar datos crudos provenientes de
distintas fuentes en información confiable para la toma de decisiones de negocio.

El área comercial necesita analizar las ventas diarias para:
- Medir el rendimiento del negocio
- Identificar productos más vendidos
- Analizar ingresos por país y período
- Calcular métricas clave (KPIs)

Actualmente, los datos provienen de múltiples fuentes y no se encuentran
normalizados ni listos para análisis, lo que dificulta la obtención de métricas
confiables.

Fuentes de datos
Las fuentes de datos utilizadas en el pipeline son:
- **Ventas (CSV)**  
  Archivo batch diario con información de las transacciones realizadas
  (producto, cantidad, precio, fecha y país).
- **Pagos (API simulada)**  
  API que representa un proveedor externo de pagos, utilizada para validar
  qué ventas fueron efectivamente cobradas.
- **Usuarios (Base de datos)**  
  Tabla relacional con información de los clientes (usuario, país, fecha de alta),
  utilizada para enriquecer el análisis y permitir segmentaciones por tipo de cliente.
La clave de negocio `sale_id` permite vincular las ventas con los pagos, mientras
que `user_id` relaciona las ventas con los usuarios.

Objetivo del pipeline
Construir un pipeline ETL batch que:
- Integre datos de múltiples fuentes (CSV, API y base de datos)
- Aplique reglas de negocio para validar ingresos reales
- Genere un modelo analítico orientado a KPIs
- Cargue los datos en un Data Warehouse para su posterior análisis en herramientas BI

Tecnologías utilizadas
- Python
- Pandas
- SQL
- PostgreSQL
- Git
- Power BI (visualización)