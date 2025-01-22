def somar_dois_numeros(num1, num2):
    return num1 + num2

def subtrair_dois_numeros(num1, num2):
    return num1 - num2

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2

def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Não é possível dividir por zero."
    
def area_do_triangulo(largura, comprimento):
    return (largura * comprimento) / 2

def area_do_triangulo_negativo(largura, comprimento):
    
    if largura < 0 or comprimento < 0:
        return "Largura e comprimento não podem ser negativos."
    else:
        return (largura * comprimento) / 2