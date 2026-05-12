
# DOCUMENTO MAESTRO DE CRITERIOS DE ARQUITECTURA HÍBRIDA AGÉNTICA

## 0. Propósito del documento

## 1. Principio central: arquitectura antes que automatización

## 2. Qué es un sistema híbrido agéntico

## 3. Problemas que este documento busca evitar

## 4. Capas generales de una arquitectura híbrida

## 5. Separación entre IA y lógica determinista

## 6. Arquitectura técnica no agéntica

## 7. Planificación de dependencias, librerías y stack técnico

## 8. Arquitectura agéntica

## 9. Criterios para crear agentes

## 10. Criterios para crear skills

## 11. Criterios para crear reglas

## 12. Criterios para crear gates

## 13. Patrones de orquestación agéntica

## 14. Fuentes de verdad, memoria y documentos derivados

## 15. Manejo de contexto y aislamiento de subagentes

## 16. MCP, APIs e integraciones externas

## 17. Seguridad, permisos y postura Deny-First

## 18. Testing, validación y evidencia

## 19. Outputs, entregables y ensamblaje final

## 20. Versionado, mantenimiento y evolución del sistema

## 21. Roadmap general para diseñar un sistema desde cero

## 22. Plantillas derivadas

## 23. Prompts derivados del documento maestro

## 24. Checklist final de arquitectura híbrida
Orden de trabajo recomendado
Yo lo desarrollaría así, paso a paso:

Fase 1 — Base conceptual
0. Propósito
1. Principio central
2. Qué es un sistema híbrido agéntico
3. Problemas que evita

Fase 2 — Arquitectura general
4. Capas generales
5. Separación IA vs determinismo
6. Arquitectura técnica no agéntica
7. Dependencias y stack

Fase 3 — Arquitectura agéntica
8. Arquitectura agéntica
9. Agentes
10. Skills
11. Reglas
12. Gates

Fase 4 — Control avanzado
13. Patrones de orquestación
14. Fuentes de verdad
15. Contexto y aislamiento
16. MCP e integraciones
17. Seguridad

Fase 5 — Calidad y uso práctico
18. Testing y evidencia
19. Outputs
20. Versionado
21. Roadmap
22-24. Plantillas, prompts y checklist
Mi recomendación inmediata


DOCUMENTO MAESTRO DE CRITERIOS DE ARQUITECTURA HÍBRIDA AGÉNTICA
0. Propósito del documento
Este documento establece los criterios base para diseñar sistemas híbridos agénticos de forma clara, controlada y mantenible.

Su función es servir como fuente de referencia arquitectónica antes de crear prompts, agentes, skills, workflows, scripts, gates o estructuras técnicas de proyecto.

El objetivo no es imponer una única forma de construir sistemas, sino definir un marco común para tomar mejores decisiones cuando un proyecto combina:

inteligencia artificial;

agentes;

prompts;

skills;

reglas;

gates;

Python;

scripts deterministas;

librerías;

APIs;

MCP;

bases de datos;

memoria documental;

testing;

seguridad;

y revisión humana.

Este documento debe ayudar a responder preguntas fundamentales antes de implementar:

¿Qué debe hacer la IA?

¿Qué debe hacer la lógica determinista?

¿Qué debe validarse con pruebas o scripts?

¿Qué debe revisar una persona?

¿Qué fuentes de verdad gobiernan el sistema?

¿Qué partes deben quedar auditadas?

¿Qué errores deben bloquear el avance?

¿Qué arquitectura técnica necesita el sistema antes de automatizar?

La intención principal es evitar que la creación de sistemas con IA se convierta en una suma desordenada de prompts, agentes, documentos, scripts y automatizaciones sin una estructura común.

Un sistema híbrido agéntico no debe construirse desde la improvisación. Debe partir de una arquitectura que se pueda explicar, revisar, probar y mantener.

Este documento servirá después como base para crear:

prompts maestros;

prompts de agentes;

plantillas de arquitectura;

criterios de auditoría;

checklists técnicos;

matrices de gates;

guías de selección de dependencias;

y roadmaps de implementación.

Su valor está en ordenar el pensamiento antes de producir soluciones.

1. Principio central: arquitectura antes que automatización
El principio central de este documento es:

Antes de automatizar, hay que diseñar la arquitectura.

La automatización no debe ser el primer paso. Tampoco la creación de agentes, prompts o scripts.

Primero debe entenderse qué problema se quiere resolver, qué entradas recibirá el sistema, qué salida debe producir, qué partes requieren interpretación, qué partes requieren exactitud y qué controles deben existir para evitar errores.

Una arquitectura híbrida agéntica no se mide por la cantidad de agentes que tiene, ni por la cantidad de herramientas que conecta. Se mide por su capacidad para producir resultados útiles, trazables, verificables y mantenibles.

La IA puede ayudar mucho en tareas de interpretación, redacción, clasificación, análisis, síntesis y propuesta. Pero no debe reemplazar la arquitectura del sistema.

Un sistema mal diseñado puede parecer avanzado porque usa agentes, MCP, prompts complejos o múltiples automatizaciones. Sin embargo, si no tiene fuentes de verdad claras, validaciones, estructura técnica, control de dependencias, testing y criterios de seguridad, seguirá siendo frágil.

La arquitectura debe definir primero:

el flujo general;

las capas del sistema;

las responsabilidades;

las fuentes de verdad;

los puntos de control;

las tecnologías necesarias;

los límites de la IA;

los límites de los agentes;

los criterios de validación;

y la forma de entregar el output final.

Solo después de eso tiene sentido decidir si se necesitan agentes, skills, scripts, APIs, MCP, bases de datos, modelos locales o servicios externos.

La regla práctica es:

No se debe crear una pieza del sistema sin saber qué responsabilidad cumple, qué entrada recibe, qué salida produce y cómo se valida.

Esto aplica a cualquier pieza:

un agente;

una skill;

un script;

una dependencia;

un workflow;

una base de datos;

una API;

un gate;

un documento;

o un prompt.

La automatización debe ser consecuencia de una decisión arquitectónica, no una reacción impulsiva ante la posibilidad de usar IA.

2. Qué es un sistema híbrido agéntico
Un sistema híbrido agéntico es una arquitectura donde intervienen componentes de inteligencia artificial y componentes deterministas para producir un resultado controlado.

No es simplemente un sistema donde “una IA responde”.

Tampoco es un conjunto de agentes trabajando sin estructura.

Es un sistema donde cada tipo de componente cumple una función distinta.

La IA se usa principalmente para tareas cognitivas, como:

interpretar instrucciones;

analizar contexto;

resumir información;

redactar documentos;

proponer soluciones;

detectar incoherencias conceptuales;

clasificar información ambigua;

comparar alternativas;

explicar decisiones;

asistir en procesos creativos o estratégicos.

La lógica determinista se usa para tareas que requieren exactitud, repetibilidad, seguridad o evidencia, como:

validar rutas;

contar archivos;

revisar formatos;

calcular cifras;

comparar estructuras;

ejecutar pruebas;

generar logs;

verificar dependencias;

transformar datos;

consultar bases de datos;

controlar estados;

producir reportes verificables.

La parte “agéntica” aparece cuando el sistema utiliza roles especializados capaces de ejecutar o coordinar partes del proceso. Estos roles pueden ser agentes completos, skills, workflows o módulos funcionales.

La parte “híbrida” aparece cuando la IA no trabaja sola, sino dentro de una arquitectura que combina criterio cognitivo con control técnico.

Un sistema híbrido agéntico puede incluir:

un orquestador;

agentes especializados;

skills reutilizables;

reglas transversales;

gates de validación;

scripts Python;

adaptadores externos;

memoria documental;

fuentes de verdad;

pruebas técnicas;

revisión humana;

y entregables finales.

La clave no está en usar todos esos elementos siempre. La clave está en decidir cuáles son necesarios para el problema concreto.

Un proyecto pequeño puede necesitar solo un prompt, una checklist y dos scripts.

Un proyecto más grande puede necesitar agentes, memoria externa, workflows, gates, arquitectura hexagonal, pruebas automatizadas y despliegue.

La arquitectura debe crecer según la necesidad real del sistema, no por entusiasmo tecnológico.

La regla práctica es:

Un sistema híbrido agéntico debe usar IA donde aporta criterio flexible y usar lógica determinista donde se necesita control exacto.

Cuando esta separación no existe, el sistema queda expuesto a errores difíciles de detectar:

la IA puede inventar datos;

los agentes pueden pisarse responsabilidades;

los outputs pueden contradecir las fuentes;

las validaciones pueden ser subjetivas;

los cambios pueden no quedar registrados;

y el resultado final puede parecer correcto sin ser verificable.

Por eso, un sistema híbrido agéntico bien diseñado no busca que la IA lo haga todo. Busca que cada parte haga lo que mejor sabe hacer.

3. Problemas que este documento busca evitar
Este documento busca prevenir errores frecuentes en proyectos que combinan IA, agentes, automatización y desarrollo técnico.

El primer problema es empezar por la herramienta antes que por la arquitectura.

Esto ocurre cuando se decide usar agentes, MCP, frameworks, bases de datos o librerías sin haber definido todavía el flujo, las responsabilidades, las fuentes de verdad o los criterios de validación.

El resultado suele ser un sistema con muchas piezas, pero poca claridad.

El segundo problema es cargar demasiado trabajo sobre la IA.

La IA puede interpretar y proponer, pero no debe encargarse sola de tareas que requieren exactitud. Si se usa IA para validar rutas, calcular cifras, revisar estructuras o decidir si un archivo existe, el sistema pierde repetibilidad.

Ese tipo de tareas debe resolverse con lógica determinista.

El tercer problema es crear agentes sin responsabilidad clara.

Un agente no debe existir solo porque suena útil. Debe existir porque cumple una función diferenciada dentro del sistema.

Si un mismo agente interpreta, redacta, audita, decide, ejecuta y valida, el sistema pierde separación de responsabilidades.

Si se crean demasiados agentes sin necesidad, el sistema se vuelve difícil de coordinar.

El cuarto problema es no definir fuentes de verdad.

Cuando no queda claro qué documento, dato o configuración manda, el sistema empieza a mezclar versiones, históricos, outputs derivados y decisiones antiguas.

Esto genera contradicciones y pérdida de control.

Un documento generado no debe convertirse automáticamente en fuente de verdad. Debe haber una decisión explícita para que eso ocurra.

El quinto problema es confundir output con arquitectura.

Un entregable final puede verse bien, pero eso no significa que el sistema esté bien diseñado.

La arquitectura debe poder explicar cómo se llegó a ese output, qué fuentes usó, qué validaciones pasó, qué decisiones se tomaron y qué evidencia quedó.

El sexto problema es no planear la arquitectura técnica no agéntica.

Un sistema híbrido también necesita decisiones tradicionales de software:

estructura de carpetas;

versión de Python;

gestor de dependencias;

librerías;

configuración;

validación;

logging;

testing;

seguridad;

persistencia;

despliegue;

mantenimiento.

Si esta parte se ignora, el sistema puede tener buenos prompts pero mala ingeniería.

El séptimo problema es usar integraciones externas sin justificar su necesidad.

MCP, APIs, bases de datos y servicios externos pueden ser muy útiles, pero también añaden complejidad, permisos, riesgos y mantenimiento.

Antes de integrar una herramienta externa, debe evaluarse si el problema puede resolverse de forma más simple con archivos locales, CLI, Python o una skill bien delimitada.

El octavo problema es no controlar el contexto.

En sistemas con agentes, la ventana de contexto puede saturarse rápidamente. Si todos los agentes reciben todo el historial, todos los documentos y todas las decisiones previas, el sistema se vuelve más lento, más caro y más propenso a confusión.

Cada agente debe recibir solo el contexto necesario y devolver resultados resumidos, claros y auditables.

El noveno problema es declarar éxito sin evidencia.

No basta con que el sistema diga que algo está terminado. Debe existir evidencia:

archivo generado;

log;

reporte;

prueba ejecutada;

gate aprobado;

comparación;

diff;

o revisión documentada.

Sin evidencia, el cierre es solo una afirmación.

El décimo problema es no separar creación, auditoría y aprobación.

La misma pieza que genera un resultado no debería ser la única encargada de aprobarlo. La auditoría debe tener independencia suficiente para detectar errores, bloquear avances o pedir correcciones.

El undécimo problema es no diseñar el mantenimiento.

Un sistema puede funcionar en su primera versión y romperse después por falta de versionado, actualización de dependencias, documentación, pruebas de regresión o limpieza de código muerto.

La arquitectura debe pensar desde el inicio cómo evolucionará el sistema.

En conjunto, este documento busca evitar que los proyectos híbridos agénticos se conviertan en estructuras atractivas pero frágiles.

La regla aplicable es:

Todo sistema debe poder explicar qué hace, por qué lo hace, con qué piezas, bajo qué reglas, con qué evidencia y con qué límites.

4. Capas generales de una arquitectura híbrida
Una arquitectura híbrida agéntica debe organizarse por capas.

Las capas ayudan a separar responsabilidades y evitan que todo el sistema dependa de una sola pieza, un solo agente o un solo prompt.

La estructura base recomendada es:

Input del usuario
↓
Intake y normalización
↓
Orquestación
↓
Fuentes de verdad y memoria
↓
Ejecución híbrida
↓
Auditoría y gates
↓
Ensamblaje de output
↓
Revisión humana
↓
Output final
Esta estructura no significa que todos los proyectos deban ser grandes o complejos. Significa que incluso un proyecto pequeño debe saber qué función cumple cada parte.

4.1 Input del usuario
El input es todo lo que el usuario entrega al sistema.

Puede incluir:

instrucciones;

documentos;

archivos;

imágenes;

audios;

tablas;

código;

requisitos;

restricciones;

ejemplos;

decisiones previas;

preferencias;

correcciones.

El error común es tratar todo input como si tuviera el mismo peso.

No todo lo que entra al sistema tiene la misma autoridad.

Una corrección explícita puede pesar más que un documento antiguo.
Un requisito puede pesar más que una preferencia.
Una fuente de verdad puede pesar más que una nota de apoyo.

Por eso, el input debe clasificarse antes de usarse.

4.2 Intake y normalización
El intake es la capa que ordena la entrada.

No produce todavía el resultado final.

Su función es responder:

qué quiere lograr el usuario;

qué información entregó;

qué información falta;

qué está duplicado;

qué está desactualizado;

qué contradice otra fuente;

qué debe considerarse requisito;

qué debe considerarse contexto;

qué salida espera el usuario.

Esta capa evita que el sistema empiece a trabajar sobre una base confusa.

Un buen intake debe dejar evidencia mínima:

resumen del objetivo;

lista de entradas recibidas;

clasificación de información;

riesgos iniciales;

dudas abiertas;

alcance inicial;

entregables esperados.

Si el intake es débil, todo lo posterior puede parecer correcto mientras se aleja del objetivo real.

4.3 Orquestación
La orquestación coordina el flujo.

No debe confundirse con “hacer todo”.

El orquestador decide:

qué fase está activa;

qué componente participa;

qué agente se activa;

qué skill se usa;

qué script se ejecuta;

qué gate debe validar;

cuándo detener el proceso;

cuándo pedir revisión humana.

La orquestación puede estar implementada como agente, workflow, script, configuración o combinación de varias piezas.

Lo importante es que exista una lógica clara de coordinación.

Sin orquestación, el sistema se convierte en una suma de acciones sueltas.

4.4 Fuentes de verdad y memoria
Esta capa define qué información gobierna el sistema.

Debe separar:

fuentes de verdad;

fuentes de apoyo;

documentos de trabajo;

documentos derivados;

históricos;

memoria externa;

outputs finales;

reportes de auditoría.

El sistema no debe decidir de forma improvisada qué fuente manda.

Si hay contradicción entre documentos, debe existir una regla para resolverla.

Una fuente generada por IA no debe convertirse automáticamente en fuente de verdad. Primero debe revisarse, aprobarse y registrarse como tal.

4.5 Ejecución híbrida
La ejecución híbrida es la capa donde se realiza el trabajo.

Aquí intervienen:

IA;

agentes;

skills;

Python;

scripts;

librerías;

APIs;

bases de datos;

herramientas externas;

validadores;

procesos manuales.

La ejecución debe separar tareas cognitivas y tareas deterministas.

La IA puede interpretar, redactar, comparar y proponer.
La lógica determinista debe validar, calcular, contar, transformar, registrar y probar.

Esta capa no debe funcionar sin controles. Debe estar conectada a reglas, gates y evidencia.

4.6 Auditoría y gates
La auditoría revisa.

Los gates deciden si el proceso puede avanzar.

Un gate no es solo una recomendación. Es una puerta de control.

Puede devolver estados como:

PASS;

WARNING;

FAIL;

BLOCKED;

REQUIERE_APROBACION.

Los gates deben validar aspectos como:

completitud del input;

coherencia con fuentes de verdad;

estructura técnica;

calidad del output;

seguridad;

pruebas;

errores conocidos;

trazabilidad;

permisos.

Cuando un gate falla, el sistema no debe continuar como si nada hubiera ocurrido.

4.7 Ensamblaje de output
El ensamblaje convierte los resultados intermedios en una salida organizada.

Puede producir:

documento;

informe;

prompt;

script;

código;

paquete ZIP;

PDF;

dashboard;

API;

estructura de proyecto;

reporte de auditoría.

El output final no debe construirse desde piezas sueltas sin control.

Debe ensamblarse desde fuentes claras, versiones correctas y resultados validados.

4.8 Revisión humana
No todo debe quedar automatizado.

La revisión humana es necesaria cuando:

hay decisiones estratégicas;

hay impacto económico;

hay riesgo legal;

hay riesgo de pérdida de datos;

hay cambios irreversibles;

hay interpretación delicada;

hay aprobación final de entregables.

La revisión humana no es una debilidad del sistema. Es una capa de control.

Un sistema bien diseñado sabe cuándo puede avanzar solo y cuándo debe detenerse.

4.9 Output final
El output final es la entrega preparada para uso real.

Debe ser:

claro;

limpio;

trazable;

verificable;

coherente con el objetivo;

separado de archivos internos;

versionado si aplica;

acompañado de evidencia cuando sea necesario.

La entrega final no debe mezclar material interno del sistema con material destinado al usuario final.

Regla aplicable
Cada capa debe tener una responsabilidad clara.
Si una capa hace demasiado, el sistema se vuelve difícil de auditar.
Si una capa no existe, otra terminará absorbiendo funciones que no le corresponden.
5. Separación entre IA y lógica determinista
La separación entre IA y lógica determinista es uno de los criterios más importantes de una arquitectura híbrida.

La IA no debe usarse para todo.

La lógica determinista tampoco resuelve todo.

Cada una debe ocupar el lugar donde aporta más valor.

5.1 Qué debe hacer la IA
La IA es útil cuando la tarea requiere interpretación flexible.

Debe usarse para:

analizar intención del usuario;

resumir información;

redactar documentos;

proponer alternativas;

detectar incoherencias conceptuales;

clasificar información ambigua;

explicar decisiones;

comparar enfoques;

generar borradores;

ayudar en tareas creativas;

revisar claridad de lenguaje;

formular hipótesis.

Estas tareas no siempre tienen una única respuesta correcta. Por eso la IA puede aportar valor.

La IA trabaja bien cuando se necesita criterio, lenguaje, contexto o síntesis.

5.2 Qué debe hacer la lógica determinista
La lógica determinista debe usarse cuando la tarea exige exactitud.

Debe encargarse de:

validar si un archivo existe;

revisar rutas;

contar elementos;

calcular cifras;

comparar listas;

verificar formatos;

leer y escribir datos;

ejecutar pruebas;

generar logs;

validar esquemas;

aplicar reglas fijas;

controlar estados;

detectar duplicados;

producir reportes;

transformar archivos;

ejecutar operaciones repetibles.

Estas tareas no deberían depender de una respuesta probabilística.

Si una tarea debe producir el mismo resultado bajo las mismas condiciones, debe resolverse con código, reglas o herramientas deterministas.

5.3 Criterio de decisión
La pregunta clave es:

¿Esta tarea requiere interpretación o requiere exactitud?
Si requiere interpretación, puede intervenir la IA.

Si requiere exactitud, debe intervenir lógica determinista.

Si requiere ambas cosas, se diseña un flujo mixto.

Ejemplo:

Clasificar documentos por relevancia:
IA puede hacer una clasificación inicial.
Python puede verificar nombres, rutas, extensiones, tamaños y duplicados.

Generar un informe:
IA puede redactar el contenido.
Python puede validar estructura, extensión, enlaces, tablas y formato.

Auditar cifras:
IA puede explicar si una hipótesis parece razonable.
Python debe calcular totales, porcentajes, diferencias y consistencia numérica.
5.4 Error común
El error común es usar IA para tareas que deberían ser simples validaciones técnicas.

Por ejemplo:

pedir a la IA que “revise” si existe un archivo;

pedir a la IA que “calcule” cuando debe usarse una fórmula;

pedir a la IA que “verifique” una estructura sin ejecutar pruebas;

pedir a la IA que “confirme” un estado sin evidencia real.

Eso produce una falsa sensación de control.

La IA puede decir que algo está correcto, pero si no hubo prueba real, el sistema no tiene evidencia.

5.5 Relación con gates
Los gates deben apoyarse en lógica determinista siempre que sea posible.

Un gate puede tener parte cognitiva y parte técnica.

Por ejemplo:

Gate de calidad documental:
- IA revisa coherencia y claridad.
- Script valida estructura, longitud, enlaces, tablas y caracteres problemáticos.

Gate de arquitectura:
- IA revisa separación de responsabilidades.
- Script valida existencia de carpetas, archivos requeridos y configuración mínima.

Gate financiero:
- IA revisa prudencia de supuestos.
- Script valida cálculos, totales y consistencia de escenarios.
La auditoría cognitiva ayuda, pero la evidencia técnica debe producirse con herramientas verificables.

Regla aplicable
La IA interpreta.
La lógica determinista verifica.

La IA puede proponer.
La lógica determinista debe probar.

La IA puede explicar.
La lógica determinista debe dejar evidencia.
6. Arquitectura técnica no agéntica
Un sistema híbrido agéntico también es un sistema de software.

Por eso necesita arquitectura técnica tradicional.

La capa agéntica no reemplaza:

estructura de proyecto;

diseño de módulos;

configuración;

validación de datos;

manejo de errores;

pruebas;

persistencia;

seguridad;

documentación;

despliegue;

mantenimiento.

Si esta base no existe, los agentes quedan trabajando sobre una estructura frágil.

6.1 Núcleo del sistema
El núcleo contiene la lógica principal.

Debe ser lo menos dependiente posible de herramientas externas.

En el núcleo deberían vivir:

reglas de negocio;

validaciones principales;

modelos de dominio;

casos de uso;

servicios internos;

decisiones centrales del flujo.

El núcleo no debería depender directamente de un proveedor de IA, una API externa o una herramienta concreta.

Esto permite cambiar piezas externas sin romper el sistema completo.

6.2 Puertos y adaptadores
Cuando el sistema use proveedores externos, conviene separar la lógica interna de las conexiones externas.

Esta separación puede organizarse con un enfoque tipo puertos y adaptadores.

Un puerto define lo que el sistema necesita.

Un adaptador implementa cómo se conecta con una herramienta concreta.

Ejemplo:

Puerto:
llm_provider

Adaptadores:
openai_adapter
anthropic_adapter
ollama_adapter
deepseek_adapter
El núcleo del sistema no debería saber si está usando OpenAI, Claude, DeepSeek u Ollama.

Solo debería saber que existe un proveedor capaz de recibir una entrada y devolver una respuesta bajo un contrato definido.

Este mismo criterio aplica a:

bases de datos;

sistemas de archivos;

APIs externas;

servicios de correo;

memoria documental;

sistemas de búsqueda;

herramientas MCP.

6.3 Configuración
La configuración no debe estar mezclada dentro del código.

Debe separarse según el tipo de dato:

configuración pública;

configuración local;

secretos;

rutas;

parámetros por entorno;

flags de ejecución;

proveedores activos;

límites operativos.

Buenas prácticas:

usar variables de entorno para secretos;

usar archivos .example para mostrar estructura sin exponer credenciales;

separar entorno local, test y producción;

no quemar rutas absolutas dentro del código;

centralizar configuración en un módulo claro.

6.4 Modelos de datos y validación
Todo sistema que recibe input necesita validar datos.

La validación debe ocurrir antes de ejecutar acciones importantes.

Debe comprobar:

tipos de datos;

campos obligatorios;

formatos;

rangos válidos;

valores permitidos;

relaciones entre datos;

estado mínimo para avanzar.

La IA puede ayudar a interpretar un input ambiguo, pero la validación final debe ser estructurada.

Si un dato no cumple el contrato esperado, el sistema debe detenerse o solicitar corrección.

6.5 Manejo de errores
Los errores deben ser comprensibles y trazables.

Un buen error debe indicar:

qué falló;

en qué capa;

cuál fue la causa probable;

qué acción se recomienda;

si el proceso puede continuar;

qué evidencia quedó.

No basta con mostrar mensajes genéricos.

Tampoco conviene ocultar errores técnicos que son necesarios para depurar.

El sistema debe distinguir entre:

error de usuario;

error de configuración;

error de dependencia;

error de proveedor externo;

error de validación;

error interno;

error recuperable;

error bloqueante.

6.6 Logging y trazabilidad
El sistema debe registrar eventos importantes.

No todo debe guardarse, pero sí lo suficiente para reconstruir qué ocurrió.

Eventos que conviene registrar:

inicio de proceso;

input recibido;

validaciones;

decisiones relevantes;

llamadas a proveedores externos;

errores;

gates ejecutados;

outputs generados;

aprobaciones;

bloqueos;

cierre de proceso.

Los logs no deben exponer secretos ni información sensible innecesaria.

La trazabilidad debe ayudar a responder:

¿Qué se hizo?
¿Cuándo se hizo?
Con qué entrada?
Con qué configuración?
Qué resultado produjo?
Qué validaciones pasó?
Dónde quedó la evidencia?
6.7 Persistencia
No todos los sistemas necesitan base de datos.

Antes de proponer persistencia, debe evaluarse qué se necesita guardar.

Opciones posibles:

archivos locales;

JSON;

SQLite;

PostgreSQL;

base documental;

almacenamiento en nube;

vector database;

sistema externo.

La decisión depende de:

volumen de datos;

concurrencia;

necesidad de consultas;

trazabilidad;

seguridad;

facilidad de backup;

despliegue;

coste;

mantenimiento.

Para prototipos o sistemas pequeños, archivos estructurados o SQLite pueden ser suficientes.

Para sistemas multiusuario, con datos relacionales o despliegue real, puede hacer falta PostgreSQL u otra base más robusta.

6.8 Interfaces
El sistema puede necesitar una o varias interfaces:

CLI;

API;

dashboard;

interfaz web;

bot;

panel interno;

integración con otra herramienta;

ejecución programada.

No se debe crear una interfaz más compleja de lo necesario.

La interfaz debe responder a cómo se usará realmente el sistema.

Un CLI puede ser suficiente para herramientas internas.
Una API puede ser necesaria si otros sistemas deben consumir el servicio.
Un dashboard puede ser útil para revisión humana, seguimiento o control operativo.

6.9 Testing técnico
El testing no debe quedar para el final.

Debe planearse desde la arquitectura.

Tipos de pruebas recomendadas:

pruebas unitarias;

pruebas de integración;

smoke tests;

pruebas de contratos;

pruebas de regresión;

pruebas de validadores;

pruebas de adaptadores;

pruebas de gates;

pruebas de seguridad básica.

Las pruebas deben cubrir especialmente las partes donde el sistema puede romperse de forma silenciosa.

Un sistema híbrido necesita probar tanto el código como los puntos de interacción con la IA.

6.10 Documentación técnica
La documentación técnica debe explicar cómo funciona el sistema.

Debe incluir:

propósito;

arquitectura;

instalación;

configuración;

ejecución;

pruebas;

estructura de carpetas;

variables de entorno;

dependencias;

flujos principales;

decisiones relevantes;

limitaciones conocidas.

La documentación no debe ser un adorno final.

Debe ayudar a mantener el sistema y a evitar que las decisiones se pierdan.

Regla aplicable
La capa agéntica opera sobre una arquitectura técnica.
No la reemplaza.

Si la arquitectura técnica es débil, la IA solo acelera el desorden.
7. Planificación de dependencias, librerías y stack técnico
La selección de dependencias es una decisión arquitectónica.

No debe hacerse por costumbre, moda o entusiasmo.

Cada librería que entra al sistema añade:

capacidad;

complejidad;

superficie de fallo;

mantenimiento;

posibles riesgos de seguridad;

dependencia de terceros;

carga de aprendizaje;

problemas futuros de compatibilidad.

Por eso, antes de instalar o recomendar una dependencia, debe justificarse.

7.1 Principio base
La primera pregunta no debe ser:

¿Qué librería usamos?
La primera pregunta debe ser:

¿Qué problema necesitamos resolver?
Después se evalúa si el problema puede resolverse con:

biblioteca estándar;

código propio simple;

librería externa;

herramienta CLI;

servicio externo;

API;

MCP;

base de datos;

framework.

La biblioteca estándar debe considerarse antes de añadir dependencias externas cuando el problema sea simple.

7.2 Criterios para evaluar dependencias
Cada dependencia candidata debe evaluarse con criterios claros:

propósito;

madurez;

mantenimiento;

frecuencia de actualizaciones;

comunidad;

documentación;

compatibilidad con la versión de Python;

facilidad de uso;

curva de aprendizaje;

licencia;

rendimiento;

seguridad;

integración con el stack actual;

complejidad añadida;

alternativas disponibles;

posibilidad de reemplazo;

impacto si deja de mantenerse.

No todas las dependencias deben pasar por una auditoría pesada.

Pero las dependencias críticas sí deben justificarse mejor.

Una dependencia es crítica cuando:

afecta el núcleo del sistema;

maneja datos sensibles;

controla persistencia;

ejecuta acciones externas;

participa en seguridad;

se usa en producción;

sería difícil de reemplazar.

7.3 Tabla mínima de decisión
Para dependencias importantes, conviene usar una tabla como esta:

| Necesidad | Opción recomendada | Alternativas | Motivo | Riesgo | Decisión |
|---|---|---|---|---|---|
| Validación de datos | pydantic | dataclasses, marshmallow | Contratos claros y validación robusta | Dependencia externa | Usar si hay modelos complejos |
| Testing | pytest | unittest | Sintaxis simple y ecosistema amplio | Baja complejidad | Usar |
| CLI | typer | argparse, click | Buena experiencia para comandos internos | Añade dependencia | Usar si el CLI crece |
La tabla no debe ser decorativa. Debe ayudar a decidir.

7.4 Stack técnico base
El stack debe elegirse según el tipo de sistema.

Para un sistema interno basado en Python, puede evaluarse:

Lenguaje:
Python

Gestión de entorno y dependencias:
uv

Testing:
pytest

Formato y linting:
ruff

Validación:
pydantic

CLI:
typer o argparse

API:
FastAPI, solo si hace falta exponer servicios

Base de datos:
SQLite para prototipos o uso local
PostgreSQL para sistemas más robustos o multiusuario

Migraciones:
Alembic, si hay base relacional con cambios de esquema

Configuración:
variables de entorno + archivo de ejemplo

Logging:
logging estándar o structlog si se necesita logging estructurado

Documentación:
README + ADRs + docs técnicas
Este stack no debe copiarse automáticamente.

Debe adaptarse al proyecto.

7.5 Dependencias de IA
Las dependencias relacionadas con IA deben aislarse.

El sistema no debería quedar atado a un único proveedor.

Puede haber adaptadores para:

OpenAI;

Anthropic;

DeepSeek;

Google;

modelos locales con Ollama;

otros proveedores.

La decisión debe considerar:

coste;

calidad;

privacidad;

latencia;

disponibilidad;

límites de uso;

facilidad de cambio;

compatibilidad con el entorno;

posibilidad de pruebas locales.

Para testing y desarrollo, puede convenir usar modelos locales o proveedores más económicos si la calidad requerida lo permite.

7.6 Actualidad de las librerías
Cuando una decisión dependa del estado actual de una librería, debe verificarse información reciente antes de cerrar la recomendación.

Esto aplica especialmente a:

frameworks nuevos;

librerías de IA;

SDKs de proveedores;

herramientas MCP;

bases vectoriales;

frameworks agénticos;

librerías de seguridad;

herramientas de despliegue.

No debe asumirse que una librería sigue siendo buena solo porque fue popular en el pasado.

7.7 Evitar sobrediseño
No todo proyecto necesita:

base de datos;

Docker;

MCP;

FastAPI;

vector database;

orquestador complejo;

cola de tareas;

microservicios;

framework agéntico.

Una arquitectura pequeña y clara puede ser mejor que una arquitectura grande sin necesidad.

La pregunta correcta es:

¿Qué necesita este proyecto ahora sin cerrar el camino para crecer después?
7.8 Política de actualización
El sistema debe definir cómo se mantendrán las dependencias.

Debe decidir:

cada cuánto revisar actualizaciones;

cómo probar cambios;

cuándo fijar versiones;

cuándo permitir rangos;

cómo manejar breaking changes;

cómo registrar decisiones;

cómo retirar dependencias obsoletas.

Las actualizaciones no deben hacerse a ciegas.

Una dependencia puede actualizarse solo si:

el cambio es necesario;

el riesgo está controlado;

hay pruebas;

hay posibilidad de revertir;

se registra la decisión si afecta al sistema.

Regla aplicable
Cada dependencia debe ganar su lugar en la arquitectura.

Si una librería no resuelve un problema real, añade más riesgo que valor.


8. Arquitectura agéntica
La arquitectura agéntica define cómo participan los agentes, skills, reglas, workflows y gates dentro del sistema.

No debe confundirse con “crear muchos agentes”.

Un sistema puede tener una arquitectura agéntica sólida con pocos agentes, siempre que sus responsabilidades estén bien separadas.

También puede tener muchos agentes y seguir siendo débil si no existe coordinación, control, límites ni evidencia.

La arquitectura agéntica debe responder:

qué agentes existen;

por qué existen;

qué responsabilidad tiene cada uno;

qué entrada reciben;

qué salida producen;

qué pueden modificar;

qué no pueden hacer;

qué gates los controlan;

qué reglas deben respetar;

qué evidencia deben dejar.

El objetivo no es que la IA trabaje más.
El objetivo es que trabaje mejor, con límites claros y dentro de una estructura verificable.

8.1 Función de la arquitectura agéntica
La arquitectura agéntica organiza las tareas donde la IA puede aportar valor.

Puede intervenir en:

análisis de requisitos;

clasificación de información;

investigación;

digestión conceptual;

redacción;

revisión;

auditoría;

comparación de alternativas;

generación de propuestas;

control de coherencia;

asistencia a decisiones humanas.

Pero estas tareas no deben ejecutarse de forma libre.

Cada intervención de IA debe tener:

propósito;

contexto suficiente;

límites;

formato de salida;

criterio de éxito;

relación con el flujo general.

Cuando esto no se define, los agentes tienden a improvisar, repetir trabajo o invadir responsabilidades de otras capas.

8.2 Orquestación agéntica
La orquestación agéntica coordina el trabajo entre agentes, skills, scripts, fuentes de verdad y gates.

Puede estar representada por:

un agente orquestador;

un workflow;

un script;

una configuración;

o una combinación de estos elementos.

Su responsabilidad principal es mantener el orden del proceso.

Debe decidir:

qué fase está activa;

qué información se entrega a cada componente;

qué agente participa;

qué skill se ejecuta;

qué gate valida el resultado;

qué salida debe generarse;

cuándo detener el flujo;

cuándo pedir aprobación humana.

El orquestador no debe absorber todas las funciones.

No debería ser al mismo tiempo investigador, redactor, auditor, validador técnico y aprobador final.

Cuando el orquestador hace todo, deja de coordinar y se convierte en un punto único de confusión.

8.3 Separación entre producción y auditoría
Una regla importante de la arquitectura agéntica es separar quien produce de quien audita.

El agente productor puede generar:

documentos;

propuestas;

análisis;

resúmenes;

prompts;

planes;

outputs intermedios.

El agente auditor debe revisar:

coherencia;

cumplimiento de requisitos;

alineación con fuentes de verdad;

calidad del resultado;

riesgos;

omisiones;

contradicciones;

deriva respecto al objetivo.

La misma IA puede asistir en ambas tareas, pero no conviene que el mismo rol se autoapruebe sin control externo.

La auditoría debe poder:

aprobar;

advertir;

pedir corrección;

bloquear;

escalar a revisión humana.

Si la auditoría solo comenta pero no puede detener el proceso, no funciona como control real.

8.4 Agentes mínimos recomendados
No existe una lista universal de agentes obligatorios.

Sin embargo, en muchos sistemas híbridos pueden aparecer estos roles:

Agente Orquestador
Coordina fases, componentes, contexto, gates y estados.

Agente Analista
Interpreta input, requisitos, restricciones y problemas.

Agente Investigador
Trabaja con fuentes externas, documentación o memoria.

Agente Productor
Genera entregables, borradores, propuestas o documentos.

Agente Auditor
Revisa coherencia, calidad, cumplimiento y trazabilidad.

Agente Técnico
Diseña o revisa arquitectura de software, dependencias, scripts y validaciones.

Agente Curador de Fuentes
Controla fuentes de verdad, documentos activos, históricos y memoria.
Estos agentes no deben crearse automáticamente.

Primero debe evaluarse si la responsabilidad puede resolverse con una skill, una regla, un script o una revisión humana.

8.5 Agentes como roles, no como personas digitales
Un agente no debe diseñarse como un personaje decorativo.

Debe entenderse como un rol operativo.

Un buen agente se define por:

responsabilidad;

límites;

entradas;

salidas;

herramientas permitidas;

reglas aplicables;

gates asociados;

condición de cierre.

No basta con decir:

Agente experto en estrategia.
Debe quedar claro:

Qué analiza.
Qué no analiza.
Qué fuente usa.
Qué output produce.
Qué evidencia deja.
Qué decisiones no puede tomar.
Mientras más sensible sea la tarea, más clara debe ser la definición del agente.

8.6 Relación entre agentes y herramientas
Un agente puede usar herramientas, pero no debería tener acceso ilimitado a todo.

Las herramientas deben asignarse según necesidad.

Ejemplos:

Agente Investigador:
puede consultar fuentes externas o memoria documental.

Agente Técnico:
puede leer estructura de archivos, proponer scripts o revisar dependencias.

Agente Auditor:
puede leer outputs y reportes, pero no necesariamente modificarlos.

Agente Productor:
puede generar borradores, pero no aprobarlos como finales.

Agente Orquestador:
puede coordinar fases, pero no saltarse gates.
El principio es permisos mínimos.

Un agente debe tener solo las herramientas necesarias para cumplir su tarea.

8.7 Estados de un agente
Cada agente debe poder declarar su estado final.

Estados recomendados:

completado_con_evidencia
completado_con_advertencias
bloqueado_por_falta_de_datos
bloqueado_por_contradiccion
bloqueado_por_riesgo
requiere_revision_humana
fuera_de_alcance
Estos estados evitan que el agente diga simplemente “listo” cuando no hay evidencia suficiente.

También ayudan al orquestador a decidir el siguiente paso.

8.8 Errores comunes en arquitectura agéntica
Errores frecuentes:

crear agentes sin responsabilidad diferenciada;

usar un solo agente para todo;

permitir que un agente produzca y apruebe su propio trabajo;

no definir límites de herramientas;

no definir condición de cierre;

no registrar evidencia;

no conectar agentes con gates;

no controlar qué contexto recibe cada agente;

crear agentes cuando bastaba una skill;

crear skills cuando hacía falta un gate;

usar reglas solo al final en lugar de integrarlas al flujo.

Estos errores no siempre rompen el sistema de inmediato.
A veces lo vuelven más difícil de auditar, mantener y corregir.

Regla aplicable
Un agente debe existir porque cumple una responsabilidad necesaria,
no porque el sistema quiera parecer más inteligente.
9. Criterios para crear agentes
Antes de crear un agente, debe justificarse su necesidad.

La pregunta principal es:

¿Esta responsabilidad necesita autonomía, criterio propio o capacidad de intervenir el flujo?
Si la respuesta es no, probablemente no hace falta un agente.

Puede bastar con:

una skill;

una regla;

un script;

un workflow;

una plantilla;

una checklist;

una revisión humana.

9.1 Cuándo sí crear un agente
Conviene crear un agente cuando la tarea cumple una o varias condiciones:

requiere criterio propio;

participa en varias fases;

coordina otros componentes;

toma decisiones dentro de límites definidos;

revisa outputs de otros agentes;

necesita herramientas específicas;

debe producir entregables recurrentes;

tiene capacidad de bloquear o escalar;

trabaja con un tipo de información especializada;

representa una responsabilidad estable del sistema.

Ejemplo:

Un sistema que genera planes de negocio puede necesitar un agente auditor financiero si la revisión de cifras, hipótesis y escenarios es recurrente, crítica y distinta de la redacción general.

9.2 Cuándo no crear un agente
No conviene crear un agente cuando:

la tarea es simple;

la tarea es puntual;

la tarea tiene pasos fijos;

la tarea no necesita criterio autónomo;

la tarea puede resolverse con un script;

la tarea puede resolverse con una skill;

la tarea solo aplica una regla;

la tarea solo valida una condición objetiva.

Ejemplo:

No hace falta crear un agente para verificar si existe una carpeta.
Eso debe hacerlo un script o una función determinista.

9.3 Plantilla mínima de definición de agente
Cada agente estable debería definirse con esta estructura:

## Nombre del agente

### Propósito
Qué responsabilidad cumple dentro del sistema.

### Alcance
Qué tareas puede realizar.

### Límites
Qué tareas no puede realizar.

### Entradas
Qué información recibe.

### Salidas
Qué debe producir.

### Herramientas permitidas
Qué herramientas puede usar.

### Fuentes autorizadas
Qué documentos, datos o memorias puede consultar.

### Gates asociados
Qué controles revisan su trabajo.

### Condición de cierre
Cuándo se considera completada su tarea.

### Estados posibles
Qué estados puede declarar al finalizar.

### Riesgos
Qué puede salir mal si el agente falla.
Esta plantilla evita agentes ambiguos.

9.4 Capacidad de veto
No todos los agentes deben tener capacidad de veto.

Un agente productor normalmente no debería bloquear todo el sistema.
Un agente auditor sí puede necesitar esa capacidad.
Un agente técnico puede bloquear si detecta un riesgo de ejecución, seguridad o pérdida de datos.
Un agente orquestador puede detener el flujo si no existe evidencia mínima.

La capacidad de veto debe asignarse con cuidado.

Si nadie puede bloquear, el sistema avanza aunque esté mal.
Si demasiados agentes bloquean sin criterio claro, el sistema se vuelve lento y difícil de operar.

9.5 Agentes temporales y agentes estables
No todos los agentes tienen que ser permanentes.

Puede haber:

Agentes estables:
Forman parte del sistema y tienen prompt oficial, reglas y gates.

Agentes temporales:
Se usan para una tarea puntual y no forman parte del flujo permanente.
Los agentes estables requieren más diseño.

Deben tener:

prompt oficial;

responsabilidad documentada;

salida esperada;

límites;

relación con otros componentes;

criterios de auditoría.

Los agentes temporales pueden ser más ligeros, pero no deben tocar partes críticas sin control.

9.6 Relación con prompts oficiales
Un agente estable necesita un prompt oficial.

El prompt oficial debe definir:

rol;

objetivo;

límites;

tono si aplica;

entradas;

salidas;

formato;

reglas;

condición de parada;

relación con otros agentes.

Si un agente estable trabaja con instrucciones improvisadas, el sistema pierde repetibilidad.

El prompt oficial no debe ser un texto decorativo.
Debe ser una pieza de arquitectura.

Regla aplicable
No se crea un agente hasta demostrar que una skill, regla, script o workflow no basta.
10. Criterios para crear skills
Una skill es una capacidad reutilizable y acotada.

No debe confundirse con un agente.

Una skill no decide el rumbo general del sistema.
Ejecuta una tarea específica bajo reglas claras.

Puede ser usada por un agente, por un workflow o por una persona.

10.1 Función de una skill
Una skill sirve para convertir una tarea repetible en un procedimiento claro.

Puede cubrir tareas como:

hacer intake;

resumir documentos;

clasificar requisitos;

auditar coherencia;

revisar fuentes;

preparar prompts;

generar reportes;

validar estructura;

convertir formatos;

revisar estilo;

analizar riesgos;

preparar un output.

La skill debe tener una frontera clara.

Si intenta cubrir demasiadas tareas, deja de ser reutilizable.

10.2 Cuándo crear una skill
Conviene crear una skill cuando:

la tarea se repite;

tiene pasos relativamente claros;

puede recibir entradas definidas;

puede producir salidas definidas;

no necesita autonomía estratégica;

puede auditarse;

puede reutilizarse en más de un flujo;

ayuda a evitar improvisación.

Ejemplo:

Una skill para “auditar fuentes de verdad” puede reutilizarse en varios proyectos.
Una skill para “redactar una conclusión específica de un informe único” probablemente no hace falta.

10.3 Cuándo no crear una skill
No conviene crear una skill cuando:

la tarea es única;

el procedimiento todavía no está claro;

se está explorando el problema;

la tarea depende demasiado de criterio estratégico;

no hay entrada ni salida definidas;

la tarea debería ser un script determinista;

la tarea debería ser una regla transversal;

la tarea debería ser un gate.

Ejemplo:

No hace falta una skill para contar archivos.
Eso debe hacerlo un script.

Tampoco hace falta una skill para “no inventar datos”.
Eso debe ser una regla transversal.

10.4 Tipos de skills
Las skills pueden clasificarse según su función.

Skills de intake:
ordenan entradas, requisitos y contexto inicial.

Skills de análisis:
interpretan información y detectan patrones o problemas.

Skills de producción:
generan borradores, documentos o entregables intermedios.

Skills de auditoría:
revisan coherencia, trazabilidad, calidad o cumplimiento.

Skills técnicas:
apoyan tareas de estructura, validación, conversión o revisión operativa.

Skills de memoria:
gestionan o consultan fuentes, históricos y memoria documental.

Skills editoriales:
mejoran claridad, tono, linealidad y organización documental.
La clasificación ayuda a evitar que una skill termine haciendo de todo.

10.5 Estructura mínima de una skill
Una skill estable debería documentarse así:

## Nombre de la skill

### Propósito
Qué tarea resuelve.

### Cuándo usarla
En qué situaciones aplica.

### Cuándo no usarla
En qué situaciones no debe activarse.

### Entradas
Qué necesita recibir.

### Salidas
Qué debe devolver.

### Procedimiento
Pasos principales.

### Criterios de calidad
Cómo se sabe que la salida es útil.

### Errores que debe evitar
Riesgos conocidos.

### Evidencia esperada
Qué rastro deja.

### Relación con gates
Qué gate puede revisar su resultado.
Esta estructura permite que la skill sea reutilizable y auditable.

10.6 Skills y scripts
Una skill puede apoyarse en scripts.

Pero no debe reemplazarlos cuando la tarea exige exactitud.

Ejemplo:

Skill:
Analizar la calidad general de un documento.

Script:
Contar palabras, detectar caracteres problemáticos, validar enlaces y revisar estructura Markdown.
La skill interpreta.
El script verifica.

Cuando se combinan bien, el sistema gana claridad y evidencia.

10.7 Skills y prompts
Una skill puede contener instrucciones de IA, pero no debe ser solo un prompt suelto.

Debe definir:

propósito;

alcance;

entrada;

salida;

límites;

criterios de éxito.

Un prompt sin estructura puede servir para una tarea puntual.
Una skill debe servir para repetirse con control.

Regla aplicable
Una skill debe hacer una tarea clara, repetible y verificable.
Si no puede explicar su entrada y su salida, todavía no está lista.
11. Criterios para crear reglas
Una regla es una restricción que debe cumplirse en el sistema.

No es una sugerencia.

Sirve para evitar errores conocidos, proteger decisiones importantes y mantener coherencia entre componentes.

Las reglas pueden aplicar a:

todo el sistema;

un proyecto específico;

una fase;

un agente;

una skill;

un gate;

una fuente de verdad;

una salida final.

11.1 Función de las reglas
Las reglas establecen límites.

Ayudan a evitar que el sistema dependa solo del criterio puntual de un agente o de una conversación.

Una buena regla deja claro:

qué se permite;

qué se prohíbe;

cuándo aplica;

qué ocurre si se incumple;

qué gate la verifica si aplica.

Ejemplo:

Regla:
Un documento generado no se convierte automáticamente en fuente de verdad.

Consecuencia:
Debe existir aprobación explícita antes de usarlo como documento rector.
11.2 Tipos de reglas
Las reglas pueden organizarse en varios niveles.

Reglas globales:
Aplican a cualquier proyecto.

Reglas de proyecto:
Aplican a un sistema concreto.

Reglas de seguridad:
Protegen acciones sensibles, datos y permisos.

Reglas de memoria:
Controlan fuentes, históricos y contexto.

Reglas técnicas:
Definen estructura, pruebas, dependencias o configuración.

Reglas editoriales:
Controlan claridad, tono, repetición y linealidad documental.

Reglas de output:
Definen cómo debe entregarse el resultado final.
Separarlas ayuda a mantenerlas localizables.

11.3 Cuándo crear una regla
Conviene crear una regla cuando:

un error puede repetirse;

una restricción aplica a varias partes;

una decisión debe mantenerse estable;

un comportamiento no debe depender del criterio del momento;

una acción puede generar riesgo;

una fuente de verdad debe protegerse;

una mala práctica debe quedar prohibida.

Ejemplo:

Si el sistema ya falló por declarar éxito sin prueba, debe existir una regla:

Sin evidencia mínima, no hay cierre de fase.
11.4 Cuándo no crear una regla
No conviene crear reglas para todo.

Una regla innecesaria puede volver el sistema rígido.

No hace falta crear una regla cuando:

la situación es única;

la decisión es puramente contextual;

la restricción ya existe en otra regla;

la regla no se puede verificar;

la regla no tiene consecuencia;

la regla solo repite sentido común sin impacto práctico.

Una regla útil debe cambiar el comportamiento del sistema.

Si no cambia nada, solo añade ruido.

11.5 Reglas con consecuencia
Una regla debe tener consecuencia operativa.

Puede provocar:

advertencia;

bloqueo;

solicitud de aprobación;

ejecución de un gate;

registro de decisión;

cambio de flujo;

rechazo de output;

revisión humana.

Ejemplo:

Regla:
No se ejecutan acciones irreversibles sin aprobación explícita.

Consecuencia:
El gate de seguridad devuelve REQUIERE_APROBACION o BLOCKED.
Sin consecuencia, la regla se vuelve decorativa.

11.6 Reglas y gates
Una regla dice qué debe cumplirse.
Un gate verifica si se cumplió.

Ejemplo:

Regla:
Todo output final debe estar separado de archivos internos.

Gate:
Auditoría de entrega limpia.
No todas las reglas necesitan gate automático, pero las reglas críticas deberían tener algún mecanismo de verificación.

Puede ser:

script;

checklist;

auditoría IA;

revisión humana;

prueba técnica;

combinación de varias.

11.7 Reglas vivas
Las reglas deben poder evolucionar.

Cuando aparece un error nuevo y relevante, debe evaluarse si corresponde convertirlo en:

nueva regla;

nuevo gate;

mejora de una skill;

ajuste de un agente;

prueba técnica;

documentación.

El sistema aprende cuando sus fallos se convierten en controles.

Regla aplicable
Una regla debe proteger una decisión, prevenir un error o controlar un riesgo.
Si no tiene consecuencia, no es una regla operativa.
12. Criterios para crear gates
Un gate es un punto de control que decide si el sistema puede avanzar.

No es solo una revisión.

No es solo un comentario.

Un gate debe poder producir un estado claro.

Estados recomendados:

PASS
WARNING
FAIL
BLOCKED
REQUIERE_APROBACION
La función del gate es proteger el flujo antes de que un error avance a la siguiente fase.

12.1 Función de un gate
Un gate valida una condición importante.

Puede revisar:

input completo;

fuente de verdad definida;

requisitos trazados;

estructura de archivos;

dependencias;

seguridad;

calidad documental;

consistencia de datos;

pruebas;

output final;

aprobación humana.

El gate debe responder:

¿Se puede avanzar?
No basta con decir:

Hay algunas observaciones.
Debe declarar un estado.

12.2 Cuándo crear un gate
Conviene crear un gate cuando:

avanzar con error sería costoso;

una fase depende de otra;

hay riesgo de pérdida de datos;

hay riesgo de contradicción;

hay riesgo de output inválido;

hay decisiones críticas;

hay acciones irreversibles;

hay requisitos obligatorios;

se necesita evidencia antes de continuar.

Ejemplo:

Antes de generar un output final, puede existir un gate que revise:

fuentes usadas;

estructura;

extensión;

formato;

requisitos;

errores conocidos;

evidencia disponible.

12.3 Cuándo no crear un gate
No todo necesita gate.

Un exceso de gates puede hacer lento el sistema.

No conviene crear gates cuando:

la tarea es exploratoria;

el error es trivial;

no hay avance de fase;

no hay impacto real;

basta con una advertencia;

la validación ya ocurre en otro gate;

no existe criterio claro para aprobar o bloquear.

Un gate debe reservarse para puntos donde realmente importa decidir si se continúa o no.

12.4 Estructura mínima de un gate
Un gate debe definirse así:

## Nombre del gate

### Objetivo
Qué protege.

### Momento de ejecución
Cuándo se activa.

### Entrada
Qué información recibe.

### Validaciones
Qué revisa.

### Estados posibles
PASS, WARNING, FAIL, BLOCKED o REQUIERE_APROBACION.

### Criterio de PASS
Condición para avanzar.

### Criterio de WARNING
Condición para avanzar con advertencia.

### Criterio de FAIL/BLOCKED
Condición para detener.

### Evidencia requerida
Qué prueba o reporte debe quedar.

### Responsable
IA, script, humano o combinación.

### Acción posterior
Qué ocurre después del resultado.
Esta estructura evita gates ambiguos.

12.5 Gates deterministas
Cuando un gate valida algo objetivo, debe apoyarse en lógica determinista.

Ejemplos:

existencia de archivos;

estructura de carpetas;

formato JSON;

campos requeridos;

conteo de elementos;

cálculos;

pruebas ejecutadas;

estado de dependencias;

enlaces rotos;

duplicados;

tamaño de archivos.

En estos casos, el gate debe producir evidencia técnica.

Si se implementa como script, el estado textual debe coincidir con el código de salida.

Política mínima:

PASS / OK → exit code 0
FAIL / BLOCKED → exit code 1
WARNING → política definida por el proyecto
Un gate que imprime FAIL pero devuelve exit code 0 está mal diseñado.

12.6 Gates cognitivos
Algunos gates requieren criterio.

Ejemplos:

coherencia estratégica;

claridad documental;

calidad narrativa;

alineación con usuario;

tono;

utilidad del output;

consistencia conceptual;

madurez de una propuesta.

Estos gates pueden apoyarse en IA o revisión humana.

Pero deben tener criterios explícitos.

No basta con decir:

Revisar si está bien.
Debe definirse qué significa “bien”.

12.7 Gates mixtos
Muchos gates combinan parte determinista y parte cognitiva.

Ejemplo:

Gate de documento final:

Parte determinista:
- validar estructura;
- contar palabras;
- detectar secciones faltantes;
- revisar formato;
- verificar enlaces.

Parte cognitiva:
- revisar claridad;
- detectar repetición;
- evaluar coherencia;
- comprobar utilidad para el lector.
Este tipo de gate suele ser más robusto porque no deja todo en manos de una sola forma de validación.

12.8 Gate de aprobación humana
Algunas decisiones deben escalar a revisión humana.

Especialmente cuando hay:

impacto legal;

impacto económico;

riesgo de pérdida de datos;

cambios irreversibles;

publicación externa;

envío de comunicaciones;

modificación de credenciales;

despliegue;

eliminación de información;

decisiones estratégicas importantes.

En estos casos, el gate debe declarar:

REQUIERE_APROBACION
No debe continuar de forma automática.

12.9 Evidencia del gate
Todo gate importante debe dejar evidencia.

Puede ser:

reporte;

log;

checklist;

salida de terminal;

archivo JSON;

tabla de resultados;

diff;

captura;

comentario de auditoría;

estado registrado.

Sin evidencia, el gate no puede auditarse después.

Regla aplicable
Un gate no existe para opinar.
Existe para decidir si el sistema puede avanzar.

13. Patrones de orquestación agéntica
La orquestación agéntica no debe improvisarse.

Antes de diseñar un flujo, debe decidirse qué patrón de trabajo necesita el sistema.

Un patrón de orquestación define cómo se conectan las tareas, agentes, skills, scripts y gates dentro del proceso.

No todos los problemas necesitan el mismo patrón.

Un sistema simple puede funcionar con pasos secuenciales.
Un sistema complejo puede necesitar enrutamiento, paralelismo, trabajadores especializados o ciclos de evaluación y mejora.

El patrón debe elegirse por necesidad, no por apariencia técnica.

13.1 Prompt Chaining
El patrón de encadenamiento de prompts se usa cuando el proceso es secuencial.

Una fase produce la entrada de la siguiente.

Ejemplo general:

Intake
↓
Análisis
↓
Propuesta
↓
Auditoría
↓
Corrección
↓
Output final
Este patrón conviene cuando:

el flujo es claro;

cada paso depende del anterior;

hay bajo nivel de ramificación;

el sistema necesita orden;

se quiere mantener trazabilidad lineal.

Riesgo principal:

Si un paso produce una salida incorrecta, el error puede contaminar toda la cadena.

Control recomendado:

gates entre fases;

evidencia por etapa;

comparación con el input original;

posibilidad de volver a una fase anterior.

13.2 Routing
El patrón de enrutamiento se usa cuando el sistema debe clasificar una entrada y enviarla al flujo correcto.

Ejemplo:

Input del usuario
↓
Clasificador
↓
Ruta técnica / Ruta documental / Ruta legal / Ruta comercial / Ruta de soporte
Conviene cuando:

hay distintos tipos de input;

no todos los casos requieren el mismo tratamiento;

existen agentes o skills especializadas;

se quiere evitar que todo pase por el mismo flujo;

hay reglas claras para derivar tareas.

Riesgo principal:

Una mala clasificación puede enviar el caso al flujo equivocado.

Control recomendado:

clasificación con justificación;

umbral de confianza;

ruta de “caso dudoso”;

revisión humana cuando la clasificación sea ambigua.

13.3 Parallelization
El patrón de paralelización se usa cuando varias tareas pueden ejecutarse de forma independiente.

Ejemplo:

Documento base
↓
Auditoría técnica
Auditoría editorial
Auditoría de seguridad
Auditoría de fuentes
↓
Consolidación de hallazgos
Conviene cuando:

las revisiones no dependen entre sí;

se busca ahorrar tiempo;

diferentes agentes analizan aspectos distintos;

se necesita comparar perspectivas;

el output final requiere varias validaciones.

Riesgo principal:

Las salidas paralelas pueden contradecirse o duplicar observaciones.

Control recomendado:

formato común de reporte;

consolidación posterior;

prioridad entre hallazgos;

gate final de coherencia.

13.4 Orchestrator-Workers
El patrón orquestador-trabajadores se usa cuando una tarea compleja puede dividirse en subtareas.

El orquestador distribuye trabajo.
Los trabajadores ejecutan partes específicas.
Luego el orquestador consolida resultados.

Ejemplo:

Orquestador
↓
Trabajador 1: análisis técnico
Trabajador 2: análisis documental
Trabajador 3: análisis de riesgos
Trabajador 4: propuesta de arquitectura
↓
Síntesis y decisión
Conviene cuando:

el problema es grande;

hay varias especialidades;

se necesita dividir trabajo;

los resultados deben consolidarse;

hay subagentes con contexto limitado.

Riesgo principal:

El orquestador puede perder control si recibe demasiada información, o si los trabajadores no devuelven salidas comparables.

Control recomendado:

instrucciones acotadas;

contexto mínimo necesario;

salida estructurada;

resumen ejecutivo;

evidencia clara;

consolidación con criterios definidos.

13.5 Evaluator-Optimizer
El patrón evaluador-optimizador se usa cuando la calidad del output es crítica.

Un componente genera.
Otro evalúa.
El sistema mejora el resultado hasta cumplir criterios o detenerse.

Ejemplo:

Generador
↓
Evaluador
↓
Corrección
↓
Nueva evaluación
↓
Aprobación o bloqueo
Conviene cuando:

la salida debe cumplir estándares altos;

hay criterios de calidad definidos;

se espera iteración;

el primer resultado puede no ser suficiente;

existe riesgo de errores sutiles.

Riesgo principal:

El sistema puede entrar en bucles de corrección sin cierre claro.

Control recomendado:

número máximo de iteraciones;

criterios de aceptación;

condición de parada;

registro de cambios;

gate final.

13.6 Combinación de patrones
Un sistema puede combinar varios patrones.

Ejemplo:

Routing para clasificar el caso.
Prompt Chaining para ejecutar fases.
Parallelization para auditorías.
Evaluator-Optimizer para mejorar el output.
La combinación debe ser intencional.

No conviene mezclar patrones sin explicar por qué.

Cada patrón añade complejidad.
La complejidad debe compensarse con control, claridad o calidad.

13.7 Criterio de selección
Antes de elegir un patrón, deben responderse estas preguntas:

¿El proceso es lineal o tiene rutas?
¿Las tareas dependen entre sí?
¿Se pueden ejecutar partes en paralelo?
¿Hace falta dividir trabajo entre especialistas?
¿La salida requiere ciclos de mejora?
¿Qué patrón reduce más riesgo?
¿Qué patrón añade menos complejidad?
Regla aplicable
El patrón de orquestación debe elegirse por el tipo de problema,
no por la tecnología disponible.
14. Fuentes de verdad, memoria y documentos derivados
Un sistema híbrido agéntico necesita saber qué información manda.

Sin esta capa, los agentes pueden mezclar documentos antiguos, outputs intermedios, opiniones, históricos y fuentes activas como si todo tuviera el mismo valor.

Eso genera contradicciones.

La gestión de fuentes de verdad define qué información gobierna el sistema y qué información solo sirve como apoyo.

14.1 Fuente de verdad
Una fuente de verdad es el documento, dato, configuración o repositorio que tiene autoridad principal sobre una parte del sistema.

Ejemplos:

Documento rector de arquitectura.
Archivo de configuración activo.
Base de datos principal.
Contrato de requisitos.
Índice de episodios.
Documento de identidad del proyecto.
Matriz financiera validada.
No tiene que existir una sola fuente de verdad para todo.

Puede haber varias, pero cada una debe tener una sede clara.

Ejemplo:

Identidad del proyecto → documento rector de identidad.
Cifras financieras → hoja financiera validada.
Arquitectura técnica → documento de arquitectura.
Dependencias → archivo de dependencias + decisión registrada.
14.2 Fuente de apoyo
Una fuente de apoyo aporta contexto, pero no manda.

Puede incluir:

notas;

investigaciones;

artículos;

conversaciones;

ejemplos;

referencias;

benchmarks;

documentos históricos.

Las fuentes de apoyo pueden enriquecer el análisis, pero no deben contradecir ni reemplazar la fuente de verdad.

Si una fuente de apoyo contiene una idea útil, debe pasar por revisión antes de incorporarse a una fuente de verdad.

14.3 Documento de trabajo
Un documento de trabajo sirve para construir, explorar o preparar una decisión.

No es necesariamente final.

Puede contener:

borradores;

hipótesis;

análisis parciales;

propuestas;

notas internas;

comparaciones;

materiales en revisión.

Debe estar claro que es material de trabajo.

No debe usarse como autoridad final si no ha sido aprobado.

14.4 Documento derivado
Un documento derivado se genera a partir de fuentes previas.

Ejemplos:

resumen;

informe;

versión editada;

PDF compilado;

presentación;

propuesta comercial;

documento final exportado.

Un documento derivado no debe mandar sobre su fuente original.

Si se edita manualmente un documento derivado, hay riesgo de que el sistema pierda trazabilidad.

La regla recomendada es:

El output se regenera desde fuentes controladas.
No se corrige manualmente como si fuera la fuente principal.
14.5 Histórico
El histórico conserva decisiones, versiones y aprendizajes anteriores.

Sirve para entender de dónde viene el sistema.

Pero no siempre debe usarse como contexto activo.

Un histórico puede estar obsoleto.

Por eso debe distinguirse entre:

Histórico consultable
Histórico activo
Histórico congelado
Histórico inválido
Si el proyecto cambia de rumbo, parte del histórico puede dejar de ser válido.

14.6 Memoria documental
La memoria documental puede vivir en herramientas como repositorios, carpetas, bases documentales, notebooks o sistemas externos.

Debe tratarse como una capa viva.

No basta con acumular documentos.

La memoria debe organizarse según función:

Memoria permanente:
Información estable del proyecto.

Memoria sectorial:
Contexto de mercado, industria o dominio.

Memoria técnica:
Arquitectura, decisiones, dependencias, código y pruebas.

Memoria histórica:
Versiones anteriores, aprendizajes y decisiones pasadas.

Memoria de investigación:
Fuentes consultadas, hallazgos y materiales externos.

Memoria de output:
Entregables generados y versiones finales.
Cada tipo de memoria debe tener límites.

El sistema debe saber qué puede usar y qué no debe mezclar.

14.7 Aprobación de nuevas fuentes de verdad
Un documento no se convierte en fuente de verdad por existir.

Tampoco por haber sido generado por IA.

Para convertirse en fuente de verdad, debe existir una decisión explícita.

Esa decisión debería registrar:

qué documento se aprueba;

qué parte gobierna;

desde qué fecha aplica;

qué reemplaza;

qué documentos quedan obsoletos;

quién lo aprobó o bajo qué criterio se aprobó.

Esto evita que los outputs intermedios empiecen a mandar sobre el sistema sin control.

14.8 Contradicciones entre fuentes
Cuando dos fuentes se contradicen, el sistema no debe resolverlo inventando.

Debe declarar conflicto.

Un conflicto de fuentes puede resolverse por:

jerarquía documental;

fecha de actualización;

aprobación explícita;

decisión humana;

regla de proyecto;

gate de coherencia.

Ejemplo de estado:

CONFLICTO_DE_FUENTES
requiere_revision_humana
14.9 Sede de información
Cada concepto importante debe tener una sede principal.

Ejemplo:

Dependencias → sección técnica o archivo de dependencias.
Gates → matriz de gates.
Identidad → documento rector de identidad.
Cifras → fuente financiera validada.
Arquitectura → documento de arquitectura.
Esto evita que la misma información crítica aparezca explicada de diez formas diferentes.

Una idea puede mencionarse en varias partes, pero solo debe desarrollarse completa en su sede principal.

Regla aplicable
El sistema debe saber qué información manda,
qué información apoya,
qué información deriva
y qué información ya no debe gobernar decisiones.
15. Manejo de contexto y aislamiento de subagentes
El contexto es un recurso limitado.

En sistemas agénticos, no todos los componentes deben recibir toda la información disponible.

Dar demasiado contexto puede producir ruido, contradicciones, pérdida de foco, lentitud y costes innecesarios.

El manejo de contexto define qué información recibe cada agente, skill o flujo.

15.1 Principio de contexto mínimo suficiente
Cada componente debe recibir solo el contexto necesario para cumplir su tarea.

No debe recibir:

documentos irrelevantes;

históricos no activos;

outputs antiguos;

conversaciones completas si basta un resumen;

fuentes contradictorias sin advertencia;

datos sensibles innecesarios;

información que pueda sesgar su tarea.

El objetivo no es ocultar información útil.

El objetivo es reducir ruido.

15.2 Contexto por rol
Cada agente necesita un tipo de contexto distinto.

Ejemplo:

Agente Analista:
requisitos, restricciones, objetivo y contexto del usuario.

Agente Técnico:
arquitectura, stack, archivos, dependencias y criterios de validación.

Agente Auditor:
output generado, criterios de evaluación, fuentes de verdad y gates.

Agente Redactor:
estructura esperada, tono, destinatario y fuentes aprobadas.

Agente Curador:
inventario documental, jerarquía de fuentes y versiones.
No todos necesitan todo.

15.3 Resúmenes ejecutivos
Los subagentes no deben devolver todo su historial.

Deben devolver resultados comprimidos.

Una salida útil de subagente puede incluir:

Objetivo recibido.
Contexto usado.
Acciones realizadas.
Hallazgos principales.
Riesgos.
Evidencia.
Estado final.
Recomendación.
Información no verificada.
Esto permite que el orquestador trabaje con señales claras, no con ruido operativo.

15.4 Sidechains o trabajo aislado
Un subagente puede trabajar de forma aislada sobre una tarea específica.

Esto reduce contaminación de contexto.

El orquestador le entrega:

tarea acotada;

contexto mínimo;

formato de salida;

límites;

criterio de cierre.

El subagente devuelve:

resultado;

evidencia;

estado;

advertencias.

No devuelve toda su cadena de trabajo.

15.5 Aislamiento de entorno
Algunos agentes o procesos necesitan aislamiento técnico.

Opciones:

Solo lectura:
Puede inspeccionar, pero no modificar.

Lectura y propuesta:
Puede analizar y proponer cambios, pero no escribir.

Escritura controlada:
Puede modificar archivos permitidos.

Sandbox:
Ejecuta pruebas o comandos en entorno controlado.

Docker:
Aísla dependencias, ejecución y sistema operativo.

Worktree:
Permite trabajar sobre una copia o rama separada.

Entorno de test:
Permite validar sin afectar producción.
El nivel de aislamiento depende del riesgo.

15.6 Permisos mínimos
Cada agente debe tener los permisos mínimos necesarios.

No debe tener acceso total por defecto.

Ejemplo:

Un auditor documental no necesita modificar base de datos.
Un agente redactor no necesita ejecutar comandos del sistema.
Un agente técnico no debería enviar correos.
Un investigador no debería borrar archivos.
Los permisos deben estar ligados a responsabilidades.

15.7 Compresión de contexto
Cuando el sistema trabaja con muchos documentos, debe existir una estrategia de compresión.

Puede incluir:

resúmenes por documento;

índices;

mapas de fuentes;

extractos relevantes;

embeddings;

referencias;

inventarios;

reportes intermedios;

payloads estructurados.

La compresión no debe eliminar información crítica.

Debe conservar:

decisiones;

requisitos;

restricciones;

fuentes usadas;

dudas;

conflictos;

evidencias.

15.8 Riesgo de contexto contaminado
El contexto puede contaminarse cuando mezcla:

documentos viejos con activos;

ejemplos con requisitos;

históricos con decisiones vigentes;

outputs derivados con fuentes de verdad;

hipótesis con datos confirmados;

instrucciones temporales con reglas permanentes.

El sistema debe marcar qué contexto está activo y qué contexto es solo referencia.

Regla aplicable
Más contexto no siempre mejora el sistema.
El contexto correcto mejora el sistema.
16. MCP, APIs e integraciones externas
Las integraciones externas permiten que el sistema interactúe con herramientas, servicios, datos o plataformas fuera de su núcleo.

Pueden aportar mucho valor, pero también añaden complejidad.

Por eso, no deben incorporarse por moda.

16.1 Tipos de integración
Un sistema puede integrarse con:

APIs;

bases de datos;

servicios de correo;

sistemas de archivos;

herramientas de documentación;

repositorios Git;

calendarios;

CRMs;

herramientas de mensajería;

sistemas internos;

memorias externas;

servidores MCP;

servicios de IA;

modelos locales.

Cada integración debe tener un propósito claro.

16.2 Criterio previo
Antes de proponer una integración externa, debe responderse:

¿Qué problema resuelve?
¿Qué operación concreta necesita hacer?
¿La integración será puntual o recurrente?
¿Qué datos leerá?
¿Qué datos escribirá?
Qué permisos necesita?
Qué riesgo introduce?
Puede resolverse con Python local, CLI o archivos?
Qué gate la controla?
Si no se puede responder, la integración todavía no está justificada.

16.3 Uso de APIs
Las APIs son útiles cuando el sistema necesita comunicarse con servicios externos o exponer funcionalidades.

Pueden servir para:

consultar datos;

enviar información;

recibir eventos;

automatizar procesos;

conectar aplicaciones;

publicar servicios internos.

Deben manejarse con cuidado:

autenticación;

límites de uso;

errores;

reintentos;

timeouts;

versionado;

logs;

seguridad;

pruebas;

documentación.

Una API mal integrada puede convertirse en un punto frágil del sistema.

16.4 Uso de MCP
MCP puede ser útil cuando un agente necesita conexión estructurada con herramientas o fuentes externas.

Conviene evaluarlo cuando:

la conexión será recurrente;

el agente necesita operar sobre una herramienta externa;

se requiere una interfaz estándar;

hay varias herramientas que conectar;

se quiere evitar crear integraciones ad hoc para cada caso;

la herramienta externa forma parte estable del flujo.

MCP no debe usarse automáticamente.

No hace falta MCP si el problema puede resolverse mejor con:

archivo local;

script Python;

CLI;

configuración simple;

llamada API puntual;

revisión manual;

skill acotada.

16.5 Servidores MCP
Cuando se proponga MCP, debe definirse qué servidor o conexión se necesita.

Para cada servidor MCP debe registrarse:

Nombre.
Herramienta conectada.
Operaciones permitidas.
Permisos.
Datos accesibles.
Riesgos.
Gates asociados.
Modo lectura/escritura.
Evidencia que deja.
No todos los servidores deben tener permisos de escritura.

Por defecto, debe preferirse lectura limitada y escalar permisos solo si es necesario.

16.6 Integraciones con modelos de IA
Los modelos de IA también deben tratarse como proveedores externos.

El sistema debe evitar quedar acoplado a un solo proveedor.

Debe poder evaluar o cambiar entre:

modelos comerciales;

modelos locales;

modelos especializados;

proveedores alternativos;

entornos de prueba;

entornos de producción.

Esto debe resolverse con adaptadores, configuración y contratos claros.

El núcleo del sistema no debe depender directamente de un SDK concreto si se puede evitar.

16.7 Riesgos de integración
Toda integración externa puede introducir riesgos:

caída del servicio;

cambios de API;

límites de uso;

costes inesperados;

problemas de privacidad;

exposición de datos;

errores de permisos;

dependencia tecnológica;

dificultad de testing;

cambios de versión;

fallos de red.

Estos riesgos deben formar parte del diseño.

No deben descubrirse después de implementar.

16.8 Evidencia de integración
Una integración importante debe dejar evidencia de funcionamiento.

Puede incluir:

prueba de conexión;

respuesta válida;

log de operación;

mock para testing;

contrato de entrada/salida;

documentación de permisos;

manejo de errores;

prueba de fallo controlado.

Sin evidencia, la integración no debe considerarse lista.

Regla aplicable
Una integración externa debe resolver una necesidad real.
Si solo añade complejidad, no pertenece a la arquitectura.
17. Seguridad, permisos y postura Deny-First
La seguridad debe diseñarse desde el inicio.

No debe añadirse al final como una revisión superficial.

En sistemas híbridos agénticos, la seguridad es especialmente importante porque la IA puede proponer o ejecutar acciones sobre archivos, datos, herramientas externas, APIs o entornos reales.

La postura recomendada es Deny-First.

Esto significa:

Todo está denegado por defecto.
Solo se permite lo que esté explícitamente autorizado.
17.1 Acciones sensibles
Una acción sensible es cualquier operación que pueda afectar datos, sistemas, usuarios, costes o entornos.

Ejemplos:

borrar archivos;

sobrescribir documentos;

mover carpetas;

modificar bases de datos;

ejecutar comandos;

instalar dependencias;

enviar correos;

publicar contenido;

desplegar cambios;

modificar permisos;

usar credenciales;

llamar APIs con efecto real;

cambiar configuración;

acceder a datos sensibles.

Estas acciones no deben ejecutarse sin control.

17.2 Clasificación de riesgo
Antes de ejecutar una acción sensible, el sistema debe clasificar el riesgo.

Criterios:

Reversibilidad:
¿Se puede deshacer?

Impacto:
¿Qué puede afectar?

Alcance:
¿Afecta un archivo, un módulo, una base de datos o producción?

Datos:
¿Incluye información sensible?

Permisos:
¿Qué acceso requiere?

Evidencia:
¿Hay respaldo, log o prueba previa?

Entorno:
¿Es local, test, staging o producción?

Aprobación:
¿Requiere autorización humana?
La clasificación ayuda a decidir si se permite, se advierte o se bloquea.

17.3 Estados de seguridad
Los gates de seguridad pueden usar estos estados:

PERMITIDO_SIN_RIESGO
PERMITIDO_CON_EVIDENCIA
WARNING
REQUIERE_APROBACION
BLOCKED
Ejemplo:

Leer un archivo de documentación:
PERMITIDO_SIN_RIESGO

Modificar un archivo de configuración:
REQUIERE_APROBACION

Borrar una carpeta con datos:
BLOCKED o REQUIERE_APROBACION explícita

Ejecutar migración en producción:
REQUIERE_APROBACION + backup + evidencia previa
17.4 Permisos mínimos
El sistema debe aplicar el principio de permisos mínimos.

Cada agente, script o integración debe tener solo el acceso que necesita.

No debe concederse acceso total por comodidad.

Ejemplos:

Lectura antes que escritura.
Sandbox antes que entorno real.
Staging antes que producción.
Mock antes que API real.
Variables de entorno antes que secretos en código.
17.5 Manejo de secretos
Los secretos no deben escribirse en código, prompts, logs ni documentos públicos.

Secretos incluyen:

API keys;

tokens;

contraseñas;

credenciales de base de datos;

claves privadas;

URLs sensibles;

cookies;

datos de acceso.

Buenas prácticas:

usar variables de entorno;

mantener archivos .env fuera de control de versiones;

crear .env.example sin valores reales;

limitar acceso a credenciales;

rotar claves si se exponen;

evitar logs con datos sensibles.

17.6 Validación de input
Todo input externo debe validarse.

Esto aplica a:

formularios;

archivos;

texto de usuario;

JSON;

CSV;

parámetros de API;

rutas;

comandos;

datos generados por IA.

El sistema no debe asumir que un input es seguro solo porque viene de un usuario autorizado o de una IA.

La validación debe revisar:

formato;

tamaño;

tipo;

valores permitidos;

caracteres peligrosos;

rutas no autorizadas;

campos obligatorios;

coherencia básica.

17.7 Ejecución de comandos
La ejecución de comandos debe estar controlada.

Antes de ejecutar comandos, debe saberse:

qué comando se ejecutará;

en qué entorno;

con qué permisos;

qué archivos puede afectar;

si es reversible;

qué salida se espera;

qué hacer si falla.

No debe permitirse que una IA construya y ejecute comandos peligrosos sin revisión.

Acciones como rm, del, migraciones, instalaciones globales o cambios de permisos deben tener control reforzado.

17.8 Seguridad en integraciones externas
Las integraciones externas deben limitar permisos.

Para APIs y MCP, debe definirse:

modo lectura o escritura;

acciones permitidas;

límites de alcance;

datos accesibles;

autenticación;

logs;

revocación de acceso;

manejo de errores;

gate de seguridad.

No se debe conectar una herramienta externa con permisos amplios si solo se necesita una operación puntual.

17.9 Revisión humana obligatoria
Debe existir revisión humana cuando:

la acción no sea reversible;

el impacto sea alto;

haya datos sensibles;

se toque producción;

se envíen comunicaciones externas;

se modifique una fuente de verdad;

se borre información;

se cambie configuración crítica;

haya conflicto entre fuentes;

el sistema no pueda estimar bien el riesgo.

La revisión humana debe ser explícita.

No debe inferirse de frases ambiguas.

Regla aplicable
Si una acción no está claramente permitida,
debe bloquearse o escalarse.

La seguridad no depende de confiar en la IA. 
Depende de limitar permisos, validar entradas y exigir evidencia.

18. Testing, validación y evidencia
El testing no debe verse como una fase final.

Debe formar parte del diseño del sistema desde el inicio.

Un sistema híbrido agéntico puede producir respuestas, documentos, código, decisiones o acciones. Por eso necesita mecanismos que permitan comprobar si lo que hizo es correcto, completo y seguro.

La validación no debe depender solo de una afirmación de la IA.

Debe existir evidencia.

18.1 Función del testing
El testing sirve para comprobar que una parte del sistema funciona bajo condiciones conocidas.

Puede validar:

funciones;

scripts;

adaptadores;

integraciones;

validadores;

gates;

flujos completos;

formatos;

cálculos;

permisos;

outputs;

comportamiento ante errores.

El testing reduce incertidumbre.

También permite cambiar el sistema sin romper funcionalidades anteriores.

18.2 Tipos de pruebas recomendadas
Un sistema híbrido puede necesitar distintos tipos de pruebas.

Pruebas unitarias:
Validan funciones pequeñas y aisladas.

Pruebas de integración:
Validan que varias piezas funcionen juntas.

Smoke tests:
Validan que el flujo mínimo funciona de punta a punta.

Pruebas de regresión:
Validan que un cambio nuevo no rompió algo que ya funcionaba.

Pruebas de contrato:
Validan entradas y salidas entre capas.

Pruebas de adaptadores:
Validan conexiones con proveedores externos.

Pruebas de gates:
Validan que los gates aprueben, adviertan o bloqueen correctamente.

Pruebas de seguridad básica:
Validan permisos, inputs peligrosos y acciones sensibles.

Pruebas de output:
Validan estructura, formato, completitud y criterios de entrega.
No todos los proyectos necesitan todas las pruebas desde el primer día.

Pero todo proyecto debe tener al menos una forma clara de comprobar que lo básico funciona.

18.3 Smoke test
El smoke test valida que el sistema funciona de punta a punta en su forma mínima.

No busca probar todos los casos.

Busca responder:

¿El flujo principal arranca, procesa y entrega algo válido sin romperse?
Ejemplo general:

Input mínimo válido
↓
Proceso principal
↓
Validación básica
↓
Output esperado
Un sistema no debería declararse listo si no tiene al menos un smoke test real.

El smoke test debe dejar evidencia:

comando ejecutado;

input usado;

resultado obtenido;

errores si aparecen;

estado final.

18.4 Pruebas de gates
Los gates también deben probarse.

Un gate no está completo solo porque existe como idea.

Debe validarse con al menos dos casos:

Caso válido:
Debe devolver PASS.

Caso inválido:
Debe devolver FAIL o BLOCKED.
Si el gate es un script, debe revisarse también el código de salida.

Ejemplo:

PASS → exit code 0
FAIL → exit code 1
Un gate que falla pero permite continuar no protege el sistema.

18.5 Pruebas de integración con IA
Las pruebas con IA son más complejas porque las respuestas pueden variar.

Por eso no conviene probar solo el texto exacto.

Debe probarse:

que la respuesta tenga estructura esperada;

que incluya campos obligatorios;

que respete límites;

que no invente datos críticos;

que cite o referencie fuentes cuando aplique;

que devuelva estado claro;

que declare bloqueo si falta información;

que no ejecute acciones no permitidas.

Cuando sea posible, las salidas de IA deben convertirse a formatos estructurados para facilitar validación.

Ejemplo:

JSON con campos esperados.
Markdown con secciones obligatorias.
Reporte con estado final.
Tabla con columnas definidas.
18.6 Datos de prueba
El sistema debe contar con datos de prueba seguros.

No conviene usar datos reales sensibles para probar.

Los datos de prueba deben cubrir:

caso válido mínimo;

caso incompleto;

caso contradictorio;

caso con datos inválidos;

caso con formato incorrecto;

caso con input excesivo;

caso con permisos insuficientes.

Esto ayuda a detectar errores antes de trabajar con información real.

18.7 Evidencia mínima
Toda validación importante debe dejar evidencia.

La evidencia puede ser:

log;

reporte;

archivo generado;

salida de terminal;

resultado de prueba;

diff;

checklist;

tabla de validación;

captura;

estado registrado;

enlace a artefacto;

hash;

timestamp.

La evidencia debe permitir responder:

Qué se validó.
Con qué entrada.
Qué herramienta se usó.
Cuál fue el resultado.
Dónde quedó el output.
Qué errores aparecieron.
Quién o qué aprobó.
18.8 Validación humana
La revisión humana sigue siendo necesaria cuando la validación automática no puede cubrir el juicio completo.

Aplica especialmente a:

estrategia;

tono;

utilidad real del entregable;

interpretación de requisitos ambiguos;

aprobación de decisiones críticas;

publicación externa;

acciones irreversibles;

evaluación de calidad final.

La revisión humana debe quedar registrada cuando afecte el avance del sistema.

No debe quedar como comentario informal perdido.

18.9 Cierre con evidencia
Una fase no debe cerrarse solo porque “parece terminada”.

Debe existir evidencia mínima de cierre.

Ejemplo:

Entregable generado.
Gate aprobado.
Prueba ejecutada.
Reporte guardado.
Riesgos pendientes registrados.
Siguiente paso definido.
Si falta evidencia, el estado correcto no es “terminado”.

Debe ser:

pendiente_de_validacion
bloqueado_por_falta_de_evidencia
requiere_revision
Regla aplicable
Sin prueba o evidencia, no hay cierre real.
Solo hay una afirmación.
19. Outputs, entregables y ensamblaje final
El output final es lo que el usuario, cliente, equipo o sistema recibe para usar.

Puede ser un documento, código, reporte, dashboard, API, paquete comprimido, base de datos, prompt, arquitectura o conjunto de archivos.

El output debe estar separado de los artefactos internos usados para producirlo.

19.1 Diferencia entre output interno y output final
No todo archivo generado es una entrega final.

Puede haber:

Output interno:
Sirve para trabajar, validar o auditar.

Output intermedio:
Sirve como paso entre fases.

Output final:
Está listo para ser usado por su destinatario.

Reporte de auditoría:
Explica validaciones, errores o decisiones.

Artefacto técnico:
Sirve para ejecución, pruebas o mantenimiento.
Confundir estos niveles genera desorden.

Un archivo útil para el equipo interno no siempre debe entregarse al usuario final.

19.2 Ensamblaje de output
El ensamblaje es la fase que organiza los resultados validados en una entrega coherente.

Debe definir:

qué archivos entran;

qué archivos quedan fuera;

qué versión se usa;

qué formato se entrega;

qué evidencia acompaña;

qué estructura final tendrá;

qué elementos son internos;

qué elementos son visibles para el usuario.

El ensamblaje no debe improvisarse al final.

Debe estar previsto desde la arquitectura.

19.3 Formatos de salida
El formato depende del uso real.

Posibles formatos:

Markdown;

PDF;

DOCX;

HTML;

JSON;

CSV;

ZIP;

dashboard;

API;

repositorio;

paquete instalable;

base documental;

presentación;

script ejecutable.

El formato debe elegirse por necesidad, no por costumbre.

Ejemplo:

Markdown:
Bueno para documentación viva y control de versiones.

PDF:
Bueno para entrega final cerrada.

JSON:
Bueno para intercambio estructurado entre sistemas.

CSV:
Bueno para tablas simples e importación.

API:
Buena para consumo por otras aplicaciones.

Dashboard:
Bueno para operación, revisión o seguimiento.
19.4 Entrega limpia
El output final debe estar limpio.

No debe incluir:

archivos temporales;

borradores innecesarios;

logs internos si no se pidieron;

claves o secretos;

carpetas del framework;

prompts internos sensibles;

datos de prueba;

basura de compilación;

duplicados;

versiones obsoletas;

comentarios internos que no correspondan.

La entrega debe contener solo lo necesario para su propósito.

19.5 Trazabilidad del output
El output final debe poder rastrearse.

Debe saberse:

de qué fuentes salió;

qué versión se usó;

qué gates aprobó;

qué pruebas pasaron;

qué cambios se hicieron;

qué decisiones lo afectan;

qué limitaciones conserva;

quién o qué lo aprobó.

Esta trazabilidad no siempre tiene que ir dentro del output final visible.

Puede estar en un reporte de cierre, changelog, log de auditoría o documento técnico.

19.6 Versionado del output
Cuando el output pueda cambiar, debe versionarse.

Esto aplica a:

documentos importantes;

arquitecturas;

prompts maestros;

sistemas de agentes;

scripts;

APIs;

entregables finales;

configuraciones;

plantillas;

modelos de datos.

El versionado permite saber qué se entregó, cuándo y bajo qué criterios.

Un output sin versión puede ser difícil de auditar si después aparecen errores.

19.7 Aprobación del output final
El output final debe pasar por un cierre.

El cierre puede incluir:

validación técnica;

auditoría de contenido;

revisión humana;

gate de seguridad;

checklist de entrega;

prueba de apertura;

prueba de ejecución;

revisión de formato;

confirmación de fuente correcta.

El tipo de cierre depende del riesgo y del uso del output.

Un documento simple puede necesitar solo revisión de contenido.
Un sistema ejecutable necesita pruebas técnicas.
Una acción pública necesita revisión humana y seguridad.

Regla aplicable
El output final no es lo último que se genera.
Es lo que queda después de limpiar, validar, ensamblar y aprobar.
20. Versionado, mantenimiento y evolución del sistema
Un sistema híbrido agéntico cambia con el tiempo.

Puede cambiar porque aparecen nuevos requisitos, nuevas herramientas, nuevos modelos de IA, nuevas dependencias, errores detectados, mejoras de seguridad o ajustes de arquitectura.

Por eso debe existir una política de mantenimiento.

20.1 Qué debe versionarse
No solo se versiona el código.

También pueden versionarse:

arquitectura;

prompts oficiales;

prompts maestros;

agentes;

skills;

reglas;

gates;

workflows;

plantillas;

documentación;

fuentes de verdad;

configuraciones;

contratos de datos;

scripts;

adaptadores;

outputs finales.

Si una pieza afecta el comportamiento del sistema, debe tener algún control de versión.

20.2 Cuándo crear nueva versión
Debe considerarse una nueva versión cuando:

cambia el alcance de un agente;

se añade o elimina una skill importante;

cambia un gate;

cambia una fuente de verdad;

se modifica un contrato de datos;

se cambia un proveedor de IA;

se modifica la arquitectura técnica;

se añade una integración externa;

se cambia una regla crítica;

se altera el flujo principal;

se actualiza una dependencia con impacto relevante.

No todo cambio menor requiere una versión mayor.

Pero todo cambio relevante debe quedar registrado.

20.3 Registro de cambios
El sistema debe registrar cambios importantes.

Un registro mínimo debería incluir:

Fecha.
Versión.
Cambio realizado.
Motivo.
Piezas afectadas.
Riesgo.
Pruebas ejecutadas.
Resultado.
Responsable o fuente de decisión.
Esto puede vivir en:

changelog;

ADR;

reporte de mantenimiento;

commit;

documento de versión;

issue;

ticket;

bitácora técnica.

Lo importante es que la decisión no se pierda.

20.4 ADRs
Un ADR es un registro de decisión arquitectónica.

Debe usarse cuando una decisión afecta el diseño del sistema.

Ejemplos:

elegir FastAPI en lugar de Flask;

usar SQLite o PostgreSQL;

incorporar MCP;

usar arquitectura hexagonal;

cambiar proveedor de IA;

definir política de gates;

introducir Docker;

separar repo y vault;

eliminar una dependencia crítica.

Un ADR no debe ser largo por obligación.

Debe explicar:

Contexto.
Decisión.
Alternativas consideradas.
Motivo.
Consecuencias.
20.5 Mantenimiento de dependencias
Las dependencias deben revisarse de forma controlada.

No conviene actualizar todo sin pruebas.

Tampoco conviene dejar dependencias críticas abandonadas.

La política debe definir:

frecuencia de revisión;

cómo detectar vulnerabilidades;

cómo probar actualizaciones;

cuándo fijar versiones;

cuándo aceptar rangos;

cómo revertir cambios;

cómo retirar dependencias obsoletas.

Cada actualización importante debe pasar por pruebas.

20.6 Mantenimiento de prompts y agentes
Los prompts también deben mantenerse.

Un prompt puede quedar obsoleto si:

cambia el flujo;

cambia una regla;

cambia el output esperado;

cambia el modelo usado;

cambia la fuente de verdad;

aparecen errores recurrentes;

se añade una nueva restricción;

cambia el rol del agente.

Los prompts oficiales no deben modificarse de forma silenciosa si forman parte del sistema estable.

20.7 Limpieza del sistema
Un sistema mantenible necesita limpieza.

Debe eliminar o archivar:

archivos temporales;

outputs viejos sin valor;

scripts duplicados;

código muerto;

prompts obsoletos;

reglas repetidas;

documentación contradictoria;

dependencias innecesarias;

datos de prueba mezclados con datos reales.

La limpieza debe hacerse con cuidado.

No se debe borrar información sin saber si es histórica, activa, derivada o fuente de verdad.

20.8 Evolución sin reescritura total
Una buena arquitectura permite crecer sin rehacer todo desde cero.

Para eso necesita:

capas separadas;

contratos claros;

adaptadores;

pruebas;

versionado;

documentación;

fuentes de verdad definidas;

gates;

decisiones registradas.

El objetivo no es anticipar todo.

El objetivo es no cerrar caminos importantes por una mala decisión inicial.

Regla aplicable
Un sistema que no puede mantenerse,
termina dependiendo de memoria humana e improvisación.
21. Roadmap general para diseñar un sistema desde cero
Este roadmap sirve como guía base para iniciar un sistema híbrido agéntico.

No todos los proyectos necesitan el mismo nivel de profundidad.

Pero el orden ayuda a evitar errores comunes.

21.1 Fase 1 — Intake del proyecto
Objetivo:

Entender qué se quiere construir.

Debe aclarar:

problema;

objetivo;

usuario final;

input esperado;

output esperado;

restricciones;

riesgos;

herramientas disponibles;

alcance inicial;

criterios de éxito.

Entregable recomendado:

informe_intake.md
Estado esperado:

INTAKE_COMPLETO
21.2 Fase 2 — Fuentes de verdad
Objetivo:

Definir qué información manda.

Debe aclarar:

documentos rectores;

datos activos;

fuentes de apoyo;

históricos;

outputs derivados;

responsables de aprobación;

reglas de conflicto.

Entregable recomendado:

mapa_fuentes_verdad.md
Estado esperado:

FUENTES_DE_VERDAD_DEFINIDAS
21.3 Fase 3 — Arquitectura técnica base
Objetivo:

Diseñar la base de software antes de automatizar.

Debe aclarar:

lenguaje;

versión;

estructura de carpetas;

dependencias iniciales;

configuración;

validación;

logging;

testing;

persistencia;

seguridad;

interfaces;

despliegue si aplica.

Entregable recomendado:

arquitectura_tecnica_base.md
Estado esperado:

ARQUITECTURA_TECNICA_DEFINIDA
21.4 Fase 4 — Arquitectura agéntica
Objetivo:

Definir cómo participará la IA.

Debe aclarar:

agentes necesarios;

skills;

reglas;

workflows;

gates;

contexto;

permisos;

herramientas;

condiciones de cierre.

Entregable recomendado:

arquitectura_agentica.md
Estado esperado:

ARQUITECTURA_AGENTICA_DEFINIDA
21.5 Fase 5 — Diseño de gates y pruebas
Objetivo:

Definir cómo se validará el sistema.

Debe aclarar:

gates mínimos;

pruebas unitarias;

smoke tests;

pruebas de integración;

validaciones deterministas;

auditorías cognitivas;

evidencias requeridas;

estados de bloqueo.

Entregable recomendado:

matriz_gates_y_pruebas.md
Estado esperado:

VALIDACION_DISEÑADA
21.6 Fase 6 — Implementación mínima
Objetivo:

Construir solo lo necesario para probar el flujo principal.

Debe evitar:

sobrediseño;

agentes innecesarios;

integraciones prematuras;

dependencias no justificadas;

outputs finales antes de validar el pipeline.

Entregable recomendado:

mvp_tecnico_funcional
Estado esperado:

FLUJO_MINIMO_FUNCIONANDO
21.7 Fase 7 — Auditoría y ajuste
Objetivo:

Detectar fallos antes de crecer.

Debe revisar:

si el flujo cumple el objetivo;

si hay piezas innecesarias;

si faltan controles;

si las fuentes son claras;

si los gates bloquean correctamente;

si las pruebas son suficientes;

si el output es útil;

si la arquitectura permite mantenimiento.

Entregable recomendado:

reporte_auditoria_v1.md
Estado esperado:

SISTEMA_VALIDADO_CON_AJUSTES
21.8 Fase 8 — Escalado controlado
Objetivo:

Añadir complejidad solo donde haga falta.

Puede incluir:

nuevos agentes;

nuevas skills;

nuevas integraciones;

MCP;

base de datos más robusta;

API;

dashboard;

despliegue;

automatizaciones;

observabilidad;

seguridad avanzada.

Entregable recomendado:

roadmap_escalado.md
Estado esperado:

ESCALADO_PLANIFICADO
Regla aplicable
Primero se valida el flujo mínimo.
Después se escala.

No se debe escalar un sistema que todavía no demuestra control.

22. Plantillas derivadas
Las plantillas derivadas convierten los criterios del documento maestro en formatos prácticos de trabajo.

Su función es evitar que cada nuevo proyecto empiece desde cero.

Una plantilla no debe reemplazar el análisis.
Debe ordenar la información mínima necesaria para tomar decisiones.

Las plantillas deben ser simples, reutilizables y fáciles de auditar.

22.1 Plantilla de intake del proyecto
Esta plantilla sirve para iniciar cualquier sistema híbrido agéntico.

# Intake del proyecto

## 1. Nombre del proyecto

## 2. Objetivo principal

## 3. Problema que busca resolver

## 4. Usuario o destinatario final

## 5. Input esperado

## 6. Output esperado

## 7. Restricciones conocidas

## 8. Herramientas disponibles

## 9. Riesgos iniciales

## 10. Criterios de éxito

## 11. Información faltante

## 12. Estado del intake

- COMPLETO
- INCOMPLETO
- BLOQUEADO
- REQUIERE_REVISION
Uso recomendado:

antes de crear arquitectura;

antes de diseñar agentes;

antes de seleccionar dependencias;

antes de crear código;

antes de automatizar procesos.

Regla:

Sin intake suficiente, no debe comenzar la implementación.
22.2 Plantilla de fuente de verdad
Esta plantilla sirve para declarar qué información gobierna el sistema.

# Mapa de fuentes de verdad

## 1. Fuente

Nombre del documento, archivo, base de datos o configuración.

## 2. Tipo

- Fuente de verdad
- Fuente de apoyo
- Documento de trabajo
- Documento derivado
- Histórico
- Temporal
- Reporte de auditoría

## 3. Qué gobierna

Qué parte del sistema controla.

## 4. Estado

- ACTIVA
- EN_REVISION
- OBSOLETA
- CONGELADA
- REEMPLAZADA

## 5. Versión

## 6. Fecha de actualización

## 7. Relación con otras fuentes

## 8. Conflictos conocidos

## 9. Criterio de uso

## 10. Responsable o criterio de aprobación
Uso recomendado:

cuando existen varios documentos;

cuando hay outputs derivados;

cuando se trabaja con históricos;

cuando se usa memoria externa;

cuando el sistema puede mezclar fuentes.

Regla:

Toda fuente importante debe tener rol definido.
22.3 Plantilla de arquitectura técnica base
Esta plantilla sirve para planear la parte no agéntica del sistema.

# Arquitectura técnica base

## 1. Objetivo técnico del sistema

## 2. Lenguaje principal

## 3. Versión recomendada

## 4. Gestor de entorno y dependencias

## 5. Estructura inicial de carpetas

## 6. Núcleo del sistema

## 7. Puertos y adaptadores

## 8. Configuración

## 9. Validación de datos

## 10. Logging y trazabilidad

## 11. Persistencia

## 12. Interfaces

- CLI
- API
- Dashboard
- Bot
- Web
- Otra

## 13. Testing

## 14. Seguridad

## 15. Despliegue

## 16. Dependencias iniciales

## 17. Riesgos técnicos

## 18. Decisiones pendientes
Uso recomendado:

antes de escribir código;

antes de crear agentes;

antes de elegir frameworks;

antes de integrar servicios externos.

Regla:

La arquitectura técnica debe existir antes de automatizar sobre ella.
22.4 Plantilla de evaluación de dependencias
Esta plantilla sirve para justificar librerías, frameworks y herramientas.

# Evaluación de dependencia

## 1. Necesidad técnica

## 2. Dependencia candidata

## 3. Alternativas consideradas

## 4. ¿Puede resolverse con biblioteca estándar?

## 5. Motivo de elección

## 6. Madurez

## 7. Mantenimiento

## 8. Comunidad

## 9. Documentación

## 10. Compatibilidad

## 11. Licencia

## 12. Riesgos

## 13. Coste de reemplazo

## 14. Pruebas necesarias

## 15. Decisión

- APROBADA
- APROBADA_CON_RESERVAS
- RECHAZADA
- PENDIENTE_DE_VERIFICACION
Uso recomendado:

para dependencias críticas;

para SDKs de IA;

para frameworks agénticos;

para bases de datos;

para herramientas de seguridad;

para integraciones externas.

Regla:

Una dependencia debe resolver un problema real y justificar su complejidad.
22.5 Plantilla de agente
Esta plantilla sirve para definir agentes estables.

# Definición de agente

## 1. Nombre del agente

## 2. Propósito

## 3. Responsabilidad principal

## 4. Alcance

## 5. Límites

## 6. Entradas

## 7. Salidas

## 8. Herramientas permitidas

## 9. Fuentes autorizadas

## 10. Reglas aplicables

## 11. Gates asociados

## 12. Permisos

- Solo lectura
- Lectura y propuesta
- Escritura controlada
- Ejecución aislada
- Requiere aprobación

## 13. Condición de cierre

## 14. Estados posibles

- completado_con_evidencia
- completado_con_advertencias
- bloqueado_por_falta_de_datos
- bloqueado_por_riesgo
- requiere_revision_humana
- fuera_de_alcance

## 15. Riesgos si falla

## 16. Prompt oficial asociado
Uso recomendado:

cuando el agente será estable;

cuando participa en workflows;

cuando tiene herramientas;

cuando puede afectar outputs importantes;

cuando necesita trazabilidad.

Regla:

Un agente sin límites claros es una fuente de riesgo.
22.6 Plantilla de skill
Esta plantilla sirve para definir capacidades reutilizables.

# Definición de skill

## 1. Nombre de la skill

## 2. Propósito

## 3. Cuándo usarla

## 4. Cuándo no usarla

## 5. Entradas

## 6. Salidas

## 7. Procedimiento

## 8. Criterios de calidad

## 9. Errores que debe evitar

## 10. Evidencia esperada

## 11. Reglas aplicables

## 12. Gates relacionados

## 13. Scripts o herramientas de apoyo

## 14. Estado

- BORRADOR
- ACTIVA
- EN_REVISION
- OBSOLETA
Uso recomendado:

para tareas repetibles;

para auditorías recurrentes;

para procesos de intake;

para revisión documental;

para generación controlada;

para preparación de outputs.

Regla:

Una skill debe ser más que un prompt: debe tener entrada, salida y criterio de éxito.
22.7 Plantilla de regla
Esta plantilla sirve para registrar restricciones del sistema.

# Regla del sistema

## 1. Nombre de la regla

## 2. Tipo

- Global
- Proyecto
- Seguridad
- Técnica
- Memoria
- Editorial
- Output

## 3. Descripción

## 4. Motivo

## 5. Cuándo aplica

## 6. Qué prohíbe

## 7. Qué permite

## 8. Consecuencia si se incumple

## 9. Gate que la verifica

## 10. Evidencia esperada

## 11. Estado

- ACTIVA
- EN_REVISION
- OBSOLETA
Uso recomendado:

para evitar errores repetidos;

para proteger fuentes de verdad;

para definir seguridad;

para controlar outputs;

para mantener coherencia.

Regla:

Una regla sin consecuencia es solo una recomendación.
22.8 Plantilla de gate
Esta plantilla sirve para definir puntos de control.

# Gate

## 1. Nombre del gate

## 2. Objetivo

## 3. Momento de ejecución

## 4. Entrada requerida

## 5. Validaciones

## 6. Tipo de gate

- Determinista
- Cognitivo
- Mixto
- Humano

## 7. Estados posibles

- PASS
- WARNING
- FAIL
- BLOCKED
- REQUIERE_APROBACION

## 8. Criterio de PASS

## 9. Criterio de WARNING

## 10. Criterio de FAIL/BLOCKED

## 11. Evidencia requerida

## 12. Responsable

## 13. Acción posterior

## 14. Si es script

- Comando de ejecución
- Exit code esperado para PASS
- Exit code esperado para FAIL
- Ubicación del reporte

## 15. Estado del gate

- BORRADOR
- ACTIVO
- EN_REVISION
- OBSOLETO
Uso recomendado:

entre fases;

antes de acciones sensibles;

antes de output final;

para validar dependencias;

para validar fuentes;

para validar seguridad;

para validar testing.

Regla:

Un gate debe decidir si se avanza, no solo describir problemas.
22.9 Plantilla de ADR
Esta plantilla sirve para registrar decisiones arquitectónicas.

# ADR-000 — Título de la decisión

## Estado

- PROPUESTA
- ACEPTADA
- RECHAZADA
- REEMPLAZADA

## Fecha

## Contexto

## Decisión

## Alternativas consideradas

## Motivo

## Consecuencias positivas

## Consecuencias negativas

## Riesgos

## Pruebas o evidencia

## Relación con otros ADRs
Uso recomendado:

decisiones de stack;

arquitectura;

seguridad;

persistencia;

proveedores de IA;

MCP;

cambio de flujo;

gates críticos;

cambios de fuente de verdad.

Regla:

Una decisión importante sin registro se convierte en deuda futura.
23. Prompts derivados del documento maestro
Los prompts derivados aplican los criterios del documento maestro a tareas concretas.

El documento maestro no debe convertirse en un prompt gigante.

Su función es definir criterios.
Los prompts derivados ejecutan esos criterios según el caso.

23.1 Prompt de arquitecto de sistema híbrido
Uso:

diseñar un sistema desde cero;

analizar un proyecto nuevo;

proponer arquitectura inicial;

separar IA y lógica determinista;

definir fases de trabajo.

Debe producir:

diagnóstico;

arquitectura por capas;

responsabilidades;

stack tentativo;

agentes necesarios;

gates mínimos;

riesgos;

roadmap.

Debe evitar:

escribir código de inmediato;

crear agentes sin justificar;

proponer dependencias sin evaluación;

diseñar integraciones externas sin necesidad.

23.2 Prompt de auditor de arquitectura
Uso:

revisar una arquitectura existente;

detectar fallos;

evaluar madurez;

encontrar duplicidades;

revisar fuentes de verdad;

revisar gates y evidencias.

Debe producir:

hallazgos;

severidad;

causa probable;

impacto;

recomendación;

evidencia;

estado final.

Estados recomendados:

ARQUITECTURA_PASS
ARQUITECTURA_WARNING
ARQUITECTURA_FAIL
ARQUITECTURA_BLOCKED
23.3 Prompt de diseñador de arquitectura técnica
Uso:

planear la parte no agéntica;

definir stack;

estructura de carpetas;

dependencias;

configuración;

validación;

testing;

seguridad;

persistencia.

Debe producir:

propuesta técnica;

justificación de stack;

tabla de dependencias;

riesgos;

pruebas mínimas;

decisiones pendientes.

Debe evitar:

depender de IA para validaciones exactas;

elegir frameworks por moda;

ignorar mantenimiento;

ignorar seguridad.

23.4 Prompt de diseñador de agentes y skills
Uso:

definir agentes;

separar roles;

decidir si algo debe ser agente, skill, regla, gate o script;

crear prompts oficiales;

crear skills reutilizables.

Debe producir:

inventario de agentes;

matriz de responsabilidades;

definición de skills;

límites;

permisos;

gates asociados;

condiciones de cierre.

Debe evitar:

agentes decorativos;

agentes con responsabilidades mezcladas;

skills sin entrada o salida;

roles que se autoaprueban.

23.5 Prompt de evaluador de dependencias
Uso:

elegir librerías;

revisar stack;

comparar alternativas;

verificar si una dependencia sigue siendo conveniente;

decidir si se puede usar biblioteca estándar.

Debe producir:

tabla de evaluación;

alternativa recomendada;

riesgos;

justificación;

decisión final o pendiente de verificación.

Debe evitar:

asumir popularidad como calidad;

añadir dependencias sin problema real;

ignorar compatibilidad;

ignorar mantenimiento.

23.6 Prompt de diseñador de gates
Uso:

diseñar gates;

definir validaciones;

separar gates cognitivos, deterministas, humanos y mixtos;

establecer estados;

definir evidencias.

Debe producir:

matriz de gates;

criterios de PASS/WARNING/FAIL;

evidencia requerida;

tipo de validación;

script sugerido si aplica;

política de exit code si aplica.

Debe evitar:

gates que solo opinan;

gates sin consecuencia;

gates sin evidencia;

gates que fallan pero permiten avanzar.

23.7 Prompt de seguridad y permisos
Uso:

revisar acciones sensibles;

aplicar Deny-First;

definir permisos de agentes;

revisar integraciones externas;

clasificar riesgo;

decidir revisión humana.

Debe producir:

matriz de riesgos;

clasificación de acciones;

permisos mínimos;

gates de seguridad;

acciones bloqueadas;

acciones que requieren aprobación.

Debe evitar:

conceder permisos totales por defecto;

ejecutar acciones irreversibles sin aprobación;

exponer secretos;

mezclar producción con pruebas.

23.8 Prompt de roadmap de implementación
Uso:

convertir arquitectura en plan de trabajo;

organizar fases;

priorizar MVP;

decidir qué se implementa primero;

evitar sobrediseño.

Debe producir:

fases;

entregables;

gates;

dependencias entre tareas;

riesgos;

criterios de cierre;

próximos pasos.

Debe evitar:

implementar todo a la vez;

escalar antes de validar;

crear integraciones prematuras;

dejar fases sin evidencia.

Regla aplicable
El documento maestro define criterios.
Los prompts derivados aplican criterios.
Los gates verifican criterios.
Los scripts producen evidencia.
24. Checklist final de arquitectura híbrida
Este checklist sirve para revisar si un sistema híbrido agéntico está suficientemente diseñado antes de implementarse o escalarse.

No reemplaza una auditoría completa.

Sirve como control rápido.

24.1 Intake
[ ] El objetivo del sistema está claro.
[ ] El problema está definido.
[ ] El usuario o destinatario final está identificado.
[ ] El input esperado está descrito.
[ ] El output esperado está descrito.
[ ] Las restricciones están registradas.
[ ] Los riesgos iniciales están identificados.
[ ] Los criterios de éxito están definidos.
[ ] La información faltante está marcada.
24.2 Fuentes de verdad
[ ] Existen fuentes de verdad definidas.
[ ] Las fuentes de apoyo están separadas.
[ ] Los documentos derivados están identificados.
[ ] Los históricos no se mezclan con fuentes activas.
[ ] Hay regla para resolver contradicciones.
[ ] Ningún output generado manda automáticamente sobre su fuente.
24.3 Arquitectura técnica
[ ] El lenguaje principal está definido.
[ ] La versión del lenguaje está definida.
[ ] El gestor de dependencias está definido.
[ ] La estructura de carpetas está propuesta.
[ ] La configuración está separada del código.
[ ] Hay criterio para secretos y variables de entorno.
[ ] Hay validación de datos.
[ ] Hay logging mínimo.
[ ] Hay plan de testing.
[ ] Hay plan de persistencia si aplica.
[ ] Hay plan de seguridad.
[ ] Hay plan de mantenimiento.
24.4 Dependencias
[ ] Las dependencias críticas están justificadas.
[ ] Se evaluó si bastaba la biblioteca estándar.
[ ] Hay alternativas consideradas.
[ ] Se revisaron riesgos.
[ ] Se revisó compatibilidad.
[ ] Se definió cómo actualizar dependencias.
[ ] No hay librerías añadidas solo por moda.
24.5 Separación IA / determinismo
[ ] Las tareas cognitivas están identificadas.
[ ] Las tareas deterministas están identificadas.
[ ] La IA no valida sola tareas exactas.
[ ] Los cálculos se resuelven con lógica determinista.
[ ] Las rutas y archivos se verifican con scripts o funciones.
[ ] Las auditorías críticas tienen evidencia.
24.6 Arquitectura agéntica
[ ] Cada agente tiene responsabilidad clara.
[ ] Cada agente tiene límites.
[ ] Cada agente tiene entradas y salidas.
[ ] Cada agente tiene condición de cierre.
[ ] Los agentes no se pisan responsabilidades.
[ ] Producción y auditoría están separadas.
[ ] No hay agentes innecesarios.
24.7 Skills
[ ] Las skills tienen propósito claro.
[ ] Las skills tienen entradas y salidas.
[ ] Las skills indican cuándo usarse.
[ ] Las skills indican cuándo no usarse.
[ ] Las skills dejan evidencia si aplica.
[ ] Las skills no reemplazan scripts deterministas.
24.8 Reglas
[ ] Las reglas críticas están documentadas.
[ ] Las reglas tienen consecuencia.
[ ] Las reglas no están duplicadas.
[ ] Las reglas de seguridad están definidas.
[ ] Las reglas de memoria están definidas.
[ ] Las reglas de output están definidas.
24.9 Gates
[ ] Los gates mínimos están definidos.
[ ] Cada gate tiene criterio de PASS.
[ ] Cada gate tiene criterio de WARNING si aplica.
[ ] Cada gate tiene criterio de FAIL/BLOCKED.
[ ] Cada gate deja evidencia.
[ ] Los gates deterministas usan scripts o validaciones objetivas.
[ ] Los gates cognitivos tienen criterios claros.
[ ] Los gates críticos pueden bloquear avance.
24.10 Contexto y memoria
[ ] Cada agente recibe contexto mínimo suficiente.
[ ] Los subagentes devuelven resúmenes, no todo el historial.
[ ] Hay estrategia de compresión de contexto.
[ ] La memoria documental está clasificada.
[ ] El contexto histórico no contamina decisiones vigentes.
[ ] Hay control de fuentes contradictorias.
24.11 MCP, APIs e integraciones
[ ] Cada integración externa tiene propósito claro.
[ ] Se evaluó si bastaba solución local.
[ ] Los permisos están definidos.
[ ] El modo lectura/escritura está definido.
[ ] Hay manejo de errores.
[ ] Hay prueba de conexión si aplica.
[ ] Hay gate de seguridad para acciones externas.
24.12 Seguridad
[ ] Se aplica Deny-First para acciones sensibles.
[ ] Hay permisos mínimos.
[ ] Los secretos no están en código.
[ ] Los inputs externos se validan.
[ ] Las acciones irreversibles requieren aprobación.
[ ] Producción está separada de test si aplica.
[ ] Hay control sobre ejecución de comandos.
24.13 Testing y evidencia
[ ] Hay smoke test mínimo.
[ ] Hay pruebas para validadores.
[ ] Hay pruebas para gates.
[ ] Hay pruebas para integraciones críticas.
[ ] Hay evidencia de ejecución.
[ ] El cierre de fase exige evidencia.
[ ] No se declara éxito solo por afirmación de IA.
24.14 Output final
[ ] El output final está separado de artefactos internos.
[ ] El output está limpio.
[ ] El output usa fuentes correctas.
[ ] El output pasó validaciones.
[ ] El output está versionado si aplica.
[ ] Hay registro de cierre.
[ ] Hay revisión humana si el riesgo lo requiere.
24.15 Mantenimiento
[ ] Hay política de versionado.
[ ] Hay changelog o registro de cambios.
[ ] Las decisiones importantes usan ADR o equivalente.
[ ] Hay criterio para actualizar dependencias.
[ ] Hay criterio para retirar código muerto.
[ ] Hay documentación suficiente para continuar el sistema.
Estado final recomendado
Después de aplicar el checklist, el sistema puede quedar en uno de estos estados:

ARQUITECTURA_LISTA_PARA_IMPLEMENTAR
ARQUITECTURA_LISTA_CON_ADVERTENCIAS
ARQUITECTURA_INCOMPLETA
ARQUITECTURA_BLOQUEADA
Regla aplicable
Un sistema no está listo porque tenga muchas piezas.
Está listo cuando sus piezas tienen función, límites, validación y evidencia.
