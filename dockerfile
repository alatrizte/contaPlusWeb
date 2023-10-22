# Utiliza la imagen oficial de MySQL como base
FROM mysql:8.1.0

# Variables de entorno para configurar la base de datos MySQL
ENV MYSQL_ROOT_PASSWORD=Xrt0_1€dg
ENV MYSQL_DATABASE=contaplus
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=pY4s%/dtRd

# Copia archivos SQL personalizados (si es necesario)
# COPY ./mi_archivo.sql /docker-entrypoint-initdb.d/mi_archivo.sql

# Exponer el puerto de MySQL (3306)
EXPOSE 3306