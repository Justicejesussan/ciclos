total_pagado = 0


for mes in range(1, 21):

    pago_mes = 10 * (2 ** (mes - 1))
    total_pagado += pago_mes

    print(f"Mes {mes}: {pago_mes} euros")
print(f"\nTotal pagado después de 20 meses: {total_pagado} euros")
