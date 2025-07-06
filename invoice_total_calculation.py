"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA.
La función debe recibir la cantidad sin IVA y
el porcentaje de IVA a aplicar, y devolver el total de la factura.
Si se invoca la función sin pasarle el porcentaje de IVA,
deberá aplicar un 21%.
"""

def invoice_total_calculation(amount, iva_percentage):
    total_amount = 0
    if iva_percentage == "":
        iva_percentage = 0
    if iva_percentage :
            total_amount = amount + (amount * iva_percentage)
    else:
        total_amount = amount + (amount * 0.21)

    return total_amount



amount = float(input("Enter the amount $"))
iva = input("Enter the iva %")
#Calling the Function to test Functionality
print(f"The total amount is: {invoice_total_calculation(amount, iva)}")


