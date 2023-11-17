# TP7 parte C
*Lucas Moyano*

## A

![](imgs/decision_tree_output.PNG)  
*Salida de consola*

![](imgs/decision_tree.png)  
*Arbol graficado*

## B

Para los datos de tipo real, se necesita un poco de "preprocesamiento" antes de calcularle la ganancia de información o el índice Gini.

Este "preprocesamiento" es simplemente dividir los datos en intervalos que abarquen los valores de los datos reales convirtiendo así los datos reales en datos discretos.  
Existen diferentes maneras de hacer esto, pero una de ellas es ordenar los valores reales de menor a mayor y calcular la media entre los valores adyacentes, ahora estas medias van a hacer de variables discretas, de la forma "atributo < media del valor", para todos los valores del atributo.