FROM python:3.10-slim

# Copiar código al contenedor
WORKDIR /app
COPY . .

# Dar permisos y ejecutar el script
RUN chmod +x scripts/install_dependencies.sh && \
    scripts/install_dependencies.sh

# Exponer puerto del Tetris
EXPOSE 3000

# Comando por defecto: iniciar servidor Tetris
CMD ["npm", "start", "--prefix", "tetris_server"]
