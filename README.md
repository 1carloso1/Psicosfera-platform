# Psicosfera - Plataforma para Psicólogos y Pacientes

**Psicosfera** es una plataforma web diseñada para facilitar la interacción entre psicólogos y pacientes, brindando un espacio integral para la gestión de consultas, citas y la comunicación eficiente entre ambas partes.

## Descripción del Proyecto

La plataforma permite a los pacientes buscar y conectarse con psicólogos de acuerdo a su especialidad, ubicación y disponibilidad. Los psicólogos pueden gestionar sus citas, horarios, y mantener un registro de las sesiones de sus pacientes. Además, los usuarios (pacientes y psicólogos) pueden interactuar a través de un sistema de mensajería y tener un perfil público y privado para gestionar su información.

### Características Principales:

#### Para Pacientes:
- **Perfil Público**: Los pacientes pueden crear un perfil con información básica que los psicólogos pueden ver antes de aceptar una solicitud de amistad.
- **Búsqueda de Psicólogos**: Los pacientes pueden buscar psicólogos según especialidad, ubicación y disponibilidad.
- **Gestión de Citas**: Los pacientes pueden programar, ver y cancelar citas con los psicólogos con los que están conectados.
- **Mensajería Interna**: Comunicación directa con los psicólogos para resolver dudas o coordinar citas.
  
#### Para Psicólogos:
- **Perfil Público**: Los psicólogos pueden crear un perfil con detalles sobre su experiencia, especialidad y datos de su consultorio.
- **Gestión de Citas**: Los psicólogos pueden gestionar su agenda, aceptar o rechazar solicitudes de citas y ver las citas futuras.
- **Área de Notas**: Espacio para que los psicólogos mantengan registros y notas de las sesiones con sus pacientes.
- **Consultorio Virtual**: Los psicólogos pueden actualizar su información, horarios y otros detalles de su consultorio en su perfil privado.

### Tecnologías utilizadas

- **Backend**: Django
- **Frontend**: JavaScript, Ajax
- **Base de Datos**: Docker

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas en tu sistema:

- **Docker** y **Docker Compose** para la gestión de contenedores.
- **Python 3** y **pip** para instalar dependencias.

## Inicialización del Proyecto

Sigue los pasos a continuación para levantar el proyecto:

### 1. Clonar el Repositorio

Clona el repositorio en tu máquina local:

```bash
git clone <repositorio-url>
cd <nombre-del-directorio-del-proyecto>
```
### 2. Levantar los Contenedores de Docker

Utiliza `docker-compose` para iniciar los contenedores:

```bash
docker-compose up -d
```
### 3. Acceder al Contenedor de la Aplicación

Entra al contenedor de la aplicación con el siguiente comando:

```bash
docker-compose exec app bash
```
### 4. Navegar al Directorio del Proyecto

Dentro del contenedor, ve al directorio del proyecto:

```bash
`cd psicosfera`
```

### 5. Iniciar el Servidor de Desarrollo

Inicia el servidor de desarrollo de Django:

```bash
python3 manage.py runserver 0:8000
```

El servidor estará disponible en `http://localhost:8000`.

### 6. Crear un Super Usuario (Administrador)

Si necesitas crear un super usuario para acceder al panel de administración de Django:

```bash
python3 manage.py createsuperuser
```

Sigue las instrucciones para completar la creación del superusuario.

## Notificaciones por Correo Electrónico

La plataforma envía notificaciones automáticas tanto dentro de la plataforma como a través de correo electrónico. Estas notificaciones incluyen:

- **Solicitudes de amistad**: Notificación cuando se aceptan o rechazan solicitudes de amistad.
- **Solicitudes de citas**: Notificación cuando un psicólogo acepta o rechaza una solicitud de cita.
- **Mensajes recibidos**: Notificación cuando se recibe un nuevo mensaje en el sistema de mensajería.

Este sistema de notificaciones asegura que los usuarios se mantengan informados sobre todas las interacciones importantes, incluso si no están activos en la plataforma.