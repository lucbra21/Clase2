# Clase2

¡Bienvenidos a la primera parte de nuestro módulo sobre Streamlit! En esta clase, aprenderán a utilizar Streamlit, un framework de Python de código abierto que facilita la creación de aplicaciones web interactivas para la visualización de datos y prototipos rápidos. Streamlit es ideal para científicos de datos y desarrolladores que desean compartir análisis o modelos de manera visual y accesible sin necesidad de conocimientos en HTML, CSS o JavaScript.

#### CREAMOS Y ACTIVAMOS UN ENTORNO VIRTUAL


1) Primero, abre una terminal y navega al directorio donde quieres crear el entorno virtual

2) Crea el entorno virtual con el comando:

python -m venv mi_entorno

(Puedes reemplazar "mi_entorno" con el nombre que prefieras)

3) Activa el entorno virtual:

En Windows:
mi_entorno\Scripts\activate

En macOS/Linux:
source mi_entorno/bin/activate

Sabrás que está activado cuando veas (mi_entorno) al inicio de tu línea de comando

4) Para desactivar el entorno virtual cuando termines:

deactivate

### Diferencia entre .ipynb y .py

Principales diferencias entre los archivos .ipynb (Jupyter Notebook) y .py (Python script):


**.py (Python Script)**
- Archivos de texto plano con código Python
- Se ejecutan de manera secuencial, de arriba a abajo
- Ideal para:
  * Desarrollo de aplicaciones
  * Scripts automatizados
  * Módulos y paquetes
- Se ejecutan desde la terminal o IDE
- No guardan resultados de ejecución
- Más ligeros y rápidos de procesar

**.ipynb (Jupyter Notebook)**
- Documentos interactivos que combinan:
  * Código
  * Texto formateado (Markdown)
  * Visualizaciones
  * Resultados de ejecución
- Se ejecutan en celdas individuales (no necesariamente en orden)
- Ideal para:
  * Análisis de datos
  * Visualización
  * Documentación
  * Prototipado
  * Enseñanza
- Se ejecutan en navegador web a través de Jupyter
- Guardan resultados y outputs
- Archivos más pesados por incluir metadatos

**¿Cuándo usar cada uno?**
- Usa **.py** cuando:
  * Necesites crear programas ejecutables
  * Estés desarrollando software
  * Quieras crear módulos reutilizables
  * La eficiencia sea prioritaria

- Usa **.ipynb** cuando:
  * Estés haciendo análisis exploratorio de datos
  * Necesites documentar paso a paso tu proceso
  * Quieras combinar explicaciones con código
  * Necesites visualizar resultados inmediatamente