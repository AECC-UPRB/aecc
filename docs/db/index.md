# Base de datos

## Desarollando el proyecto

Para el desarollo del proyecto normalmente usamos [SQLite](http://www.sqlite.org) ya que python viene con un driver para [SQLite](http://www.sqlite.org) y Django ya viene con [SQLite](http://www.sqlite.org) configurado como base de datos por default, pero puede usar otra base de datos que desee.

## En produccion

Para produccion, el proyecto utiliza [Postgres](http://www.postgresql.org/) en [Heroku](https://www.heroku.com/). Si desea usar [Postgres](http://www.postgresql.org/) desarollando el proyecto lo puede usar tambien. Para esto, necesitaria instalar [Postgres](http://www.postgresql.org/) en su computadora y instalar el driver de python para poder usar postgres con Django. Para instalar [Postgres](http://www.postgresql.org/) puede buscar por Google para como hacerlo para su OS. Para instalar el driver de python para [Postgres](http://www.postgresql.org/), si no lo tiene,  debes de tener pip instalado y correger lo siguiente en el terminal dentro de su ambiente virtual.

```bash
pip install psycopg2
```

## Migracciones de la base de datos

Esto es super importante y lo tiene que hacer sin importar la base de datos. Al menos que sea una base de datos noSQL como mongoDB. Para ver todos los detalles favor de visitar este enlace [Migracciones](https://github.com/AECC-UPRB/aecc/blob/devbranch/docs/db/migrations.md).
