<div align="center">
    <img src="https://cdn.shortpixel.ai/spai/q_lossy+w_671+to_auto+ret_img/codigonautas.com/wp-content/uploads/2024/09/Concepto-Refactorizacion-Codigo.jpg" alt="refator logo">
    <h1>Refactorización y/o Optimización</h1>
    <p>Implementación de <strong>Clean Code</strong></p>
</div>

Entrar en el mundo de la **Refactorización** y la **Optimización** es como pasar de ser un escritor de borradores a un editor de obras maestras. Aunque a menudo se confunden, tienen propósitos muy distintos.

Aquí te explico las diferencias, cuándo aplicar cada una y cómo hacerlo con elegancia.

---

## 1. Refactorización: "Limpiar la cocina mientras cocinas"

La refactorización es el proceso de reestructurar el código existente sin cambiar su comportamiento externo. El objetivo no es que el programa sea más rápido, sino que sea más **legible, mantenible y escalable**.

### ¿Por qué refactorizar?
* **Reducción de la Deuda Técnica:** Evitas que el código se vuelva un "plato de espagueti".
* **Facilidad de Extensión:** Es más fácil añadir funciones a un código limpio.
* **Detección de Bugs:** Al simplificar la lógica, los errores saltan a la vista.

### Técnicas Comunes
* **Extraer Método:** Si una función hace demasiadas cosas, divídela en piezas pequeñas.
* **Renombrado de Variables:** Cambiar `d` por `dias_para_vencimiento`.
* **Eliminación de Código Muerto:** Si no se usa, ¡fuera!



---

## 2. Optimización: "Ponerle un motor turbo al coche"

La optimización busca mejorar la eficiencia del programa, generalmente enfocándose en el **uso de memoria** o la **velocidad de ejecución**. Aquí sí cambiamos el "cómo" interno para obtener mejores resultados de rendimiento.

### ¿Cuándo optimizar?
> "La optimización prematura es la raíz de todos los males." — Donald Knuth.

Solo debes optimizar cuando:
1.  Has identificado un **cuello de botella** real mediante pruebas (profiling).
2.  El rendimiento actual afecta la experiencia del usuario o los costos del servidor.

### Áreas de Enfoque
* **Algoritmos:** Cambiar una búsqueda lineal $O(n)$ por una búsqueda binaria $O(\log n)$.
* **Acceso a Datos:** Reducir las consultas a la base de datos (usar caché o índices).
* **Concurrencia:** Aprovechar el procesamiento en paralelo.



---

## Comparativa Rápida

| Característica | Refactorización | Optimización |
| :--- | :--- | :--- |
| **Objetivo Principal** | Legibilidad y mantenibilidad. | Velocidad y eficiencia de recursos. |
| **¿Cambia la lógica?** | No, el resultado externo es el mismo. | No, pero cambia la implementación técnica. |
| **Público objetivo** | El desarrollador (humano). | El hardware / El usuario final. |
| **Riesgo** | Bajo (si hay tests). | Alto (puede introducir bugs complejos). |

---

## El Flujo de Trabajo Ideal

Para no perder la cabeza, lo ideal es seguir este orden:

1.  **Haz que funcione:** Escribe el código necesario para cumplir el requisito.
2.  **Hazlo bonito (Refactoriza):** Limpia el desorden, mejora los nombres y la estructura.
3.  **Hazlo rápido (Optimiza):** *Solo si es necesario*, mide el rendimiento y ajusta las partes lentas.

---

## Estructura actual del módulo

Este directorio ahora contiene dos versiones del ejercicio de consola:

- `Trabajo_final`: implementación original basada en scripts planos.
- `Trabajo_final_v2`: refactor autocontenido con mejor organización interna, trazabilidad y separación de responsabilidades.

## Objetivo de `Trabajo_final_v2`

`Trabajo_final_v2` no busca “corregir” automáticamente todos los defectos del sistema original. Su objetivo es conservar el comportamiento observable general, pero mejorar:

- legibilidad del código;
- organización por capas estilo MVC;
- centralización de persistencia;
- rastreabilidad mediante logging contextual;
- capacidad de prueba manual y automatizada sobre piezas estables.

## Cómo ejecutar

Versión original:

```bash
python3 Code-Optimization/Trabajo_final/main.py
```

Versión refactorizada:

```bash
cd Code-Optimization/Trabajo_final_v2 && python3 main.py
```

## Documentación relacionada

- README propio: [Trabajo_final_v2/README.md](Trabajo_final_v2/README.md)
- Arquitectura: [Trabajo_final_v2/docs/architecture.md](Trabajo_final_v2/docs/architecture.md)
- Pruebas manuales: [Trabajo_final_v2/docs/manual-testing.md](Trabajo_final_v2/docs/manual-testing.md)
- PRD: [Trabajo_final_v2/prds/trabajo_final_v2.md](Trabajo_final_v2/prds/trabajo_final_v2.md)
