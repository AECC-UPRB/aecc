# UPRB-AECC

Sitio web para la Asociación Estudiantes de Ciencias de Computas de la UPRB

## Reportar errores, sugerencias y otros comentarios

Si tienes una idea de como mejorar esta plataforma o si has encontrado algún error déjanos saber creando un "issue" en el repositorio.

[Issues](https://github.com/eluciano11/aecc/issues) - para reportar problemas, errores, sugerencias, etc.

### Cómo usar "issues" en GitHub

Aquí un [vídeo](http://www.youtube.com/watch?v=TJlYiMp8FuY) que explica como crear "issues". Recuerda que primero necesitas [crear una cuenta de GitHub](https://github.com/join), es gratis.

## Developers

Este proyecto no sería posible sin la colaboración de otros developers que han donado su tiempo para crear esta aplicación. Si  encuentras un error por favor crea un [issue](https://github.com/eluciano11/aecc/issues) y si puedes arreglarlo te invitamos a hacer y someter un pull request.

### Para correr el proyecto

Debes tener instalado **Python 2.7** en tu máquina. También es recomendado que crees un [virtualenv](http://www.virtualenv.org/) para el proyecto pero no es un requisito.

```bash
$ git clone https://github.com/jpadilla/notaso.git
$ cp .env.example .env
$ pip install -r requirements.txt
$ python manage.py syncdb --migrate
$ python manage.py runserver
```

Abre tu browser en [http://localhost:8000/](http://localhost:8000/). 

Para accesar la sección de administración debes de crear un super usuario.

```bash
$ python manage.py createsuperuser
$ python manage.py runserver
```

Luego ve a [http://localhost:8000/admin/](http://localhost:8000/admin/).
