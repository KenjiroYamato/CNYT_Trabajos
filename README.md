# Tarea 1 Juan Pablo Camargo

### ¿como usar la libreria: lib_complax_cal?

ejemplo:

```python
import lib_complex_cal.funtions as cpx

if __name__ == "__main__":
    a=(1, 2)
    b=(3, 4)
    operacion = cpx.sumaCpx(a, b)  # <--Aqui
    print(operacion)
```

los numeros complejos se representan como tuplas, en formato `(a, b)`  
a = parte real  
b = parte imaginaria

este proyecto se realiza con fines educativos para la clase de Ciencia Naturales y Tecnologia en la [Escuela Colombiana de Ingenieria Julio Garavito](https://www.escuelaing.edu.co/es/)
