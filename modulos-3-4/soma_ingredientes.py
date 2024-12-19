preco_cenoura = 4.5
preco_oleo = 12
preco_acucar = 6
preco_ovos = 20 
preco_leite = 5
preco_fermento = 5

def soma_ingredientes (tem_cenoura,tem_oleo, tem_acucar, tem_ovos, tem_leite, tem_fermento):
    total_compra = 0 
    if tem_cenoura: 
        total_compra = total_compra + preco_cenoura
    if tem_acucar:
       total_compra = total_compra + preco_acucar
    if tem_oleo: 
        total_compra = total_compra + preco_oleo
    if tem_leite:
       total_compra = total_compra + preco_leite
    if tem_fermento:
       total_compra = total_compra + preco_fermento
    if tem_ovos:
       total_compra = total_compra + preco_ovos
    return total_compra

total = soma_ingredientes(True, True, True, True, True,True)

print(total)
