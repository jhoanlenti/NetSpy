# Scan-IP
Projecto de programacion

1. Coordinador del Proyecto y Módulo Principal
	•	Diseñar la estructura principal del programa (archivo principal que une todos los módulos). --> Jhoan
	•	Implementar la lógica para coordinar el escaneo de IPs y puertos. --> Jhoan
	•	Integrar los módulos desarrollados por los demás participantes. --> Jhoan
	•	Realizar pruebas iniciales para asegurarse de que todo funcione de manera conjunta. --> Ethan y Sergi y Jordi

2. Módulo de Escaneo de IPs
	•	Implementar el escaneo de rangos de IPs (e.g., 192.168.1.1 a 192.168.1.255). --> Jhoan
	•	Usar ping o ICMP requests para detectar IPs activas. --> Ethan y Jhoan
	•	Optimizar el manejo de respuestas lentas o nulas para evitar bloqueos. (nmap default)--> 
	•	Devolver una lista de IPs activas al módulo principal. --> Sergi

3. Módulo de Escaneo de Puertos
	•	Crear la lógica para escanear los puertos abiertos de una IP dada. (netcat)--> Nuria
	•	Usar sockets para enviar y recibir datos de los puertos. --> Jhoan y Nuria
	•	Soportar rangos de puertos especificados por el usuario.  (petar contraseña) --> 
	•	Optimizar el escaneo con concurrencia (hilos o asincronía). --> Todos

4. Interfaz de Usuario (CLI o GUI)
	•	Diseñar una interfaz para que el usuario: (Banner de bienvenida y roles usuario ) --> Ethan y Sergi
	•	Ingrese rangos de IPs y puertos y sistema operativo. --> Nuria y Jordi
	•	Elija opciones como tipo de escaneo (rápido, completo, etc.). (Más info) --> Jordi y Nuria
	•	Vea los resultados en tiempo real o al final. -->Sergi y ayuda de Ethan
	•	Trabajar en la salida del programa (tabla de resultados, exportar a un archivo, etc.). --> Nuria y Jhoan
	•	Visualizar servicios --> Jhoan y Jordi y Nuria

6. Pruebas y Optimización de Código
	•	Diseñar casos de prueba para verificar cada módulo por separado (IPs, puertos, interfaz). --> Todos
	•	Buscar y corregir errores en la integración de los módulos. --> Todos
	•	Documentar las funciones y sugerir optimizaciones.  (GitHub) --> Todos

7. Extras
	•	API para IP pública --> Jhoan y Nuria
	•	Petar contraseña --> Nuria y Ethan y Jhoan

Metodología de Trabajo
	•	Jira --> Jhoan
	•	Scrum --> Todos -Jhoan
	•	GitHub --> Jhoan y Jordi
 	•	Memo --> Ethan y Nuria
   	•	

Roles 
 	•	Scrum Master --> Jhoan

  Pedro --> https://github.com/nomespaladin/portsniffer 
