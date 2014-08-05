#Manejo del proyecto

El manejamiento de este proyecto se basa en este [modelo](http://nvie.com/posts/a-successful-git-branching-model/), para cualquier feature, bug o mejoramiento que se le pueda hacer para cualquier parte del mismo.

##Branching

El branching se utiliza para separar tu espacio de trabajo sea para un feature, bug o mejoramiento. Esto se hace para tener todo tu trabajo separado del trabajo de los demas contribuyentes al proyecto. Esto ayuda a cuando termines tu branch, se pueda evaluar para luego incluirlo en el branch de devbranch.

Ejemplo:
Si quiere trabajar en un feature, se haria lo siguiente. Crea un branch con un nombre corto y descriptivo para el feature. Todo development se hara en ese branch para ese feature **solamente**. Luego, cuando entienda que ya el feature tiene todo lo que necesita. Favor de someter un pull request. De esta manera se sabra que ya termino con ese feature y otros contribuidores, pueden verificar su trabajo para luego incluirlo en el proyecto.

###Master branch

Este branch, **solamente** se toca cuando se valla hacer un nuevo release y se hace un merge del ultimo snapshot del pasado release.

##Dev Branch

Este branch se utiliza para hacer merge de todos los branches que tengan que ver con features, bugs o mejoramientos. Luego de hacer el merge, se debe verificar que no existan ningun problema con el proyecto en el devbranch.

##Releases

Los releases son **snapshots** del proyecto en desarollo para llegar a produccion. Esto se hara solamente cuando ya llegue el momento para sacar una version nueva del proyecto. Cuando esto occura, pasara lo siguiente. Se crea un branch con nombre de la siguiente version, ejemplo 0.1.0, y en este branch, se trabajara todos los arreglos que se tengan que hacer al proyecto. Cuando llegue al momento, de que no se encuentran mas problemas con el proyecto. Se publica a Heroku o cualquier host y se verifica que no hallan problemas en production. Luego, si hubiese algun problema en production. Se crea otro branch que se llamara hotfix#. Esto indica que ese problema tiene mucha prioridad y debe ser resolvido lo antes posible.

**Finalmente, cuando se valla a crear una version nueva para un release. Antes, se debe de hacer un merge con lo que hay hasta el snapshot del ultimo release a el mastr branch.**

##Hotfixes

Los hotfixes son aquellos arreglos que se tengan que hacer de inmediato ya que el problema estara en produccion.
