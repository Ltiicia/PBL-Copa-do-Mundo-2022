'''/**************************** 
 Autor: Letícia Gonçalves Souza
 Componente Curricular: MI algoritmos  
 Concluido em:11/12/2022 
 Declaro que este código foi elaborado por mim de forma individual e não contém nenhum  
 trecho de código de colega ou de outro autor, tais como provindos de livros e apostilas,
 e páginas ou documentos eletrônicos da internet. Qualquer trecho de código de outra 
 autoria que não a minha está destacado com uma citação do autor e a fonte do código, e estou  
 ciente que estes trechos não serão considerados para fins de avaliação. 
 /*****************************'''


import json

def confronto1(X,eq1, eq2): #FUNÇÃO PARA INPUT DO CONFRONTO 1
    with open('confrontos.json', 'r') as json_file:
        confrontos = json.load(json_file)
    print(f'{eq1} x {eq2}')
    data = input(f'Data do confronto [dd/mm/aaaa]: ')
    local = input(f'Estadio do confronto: ')
    horario = input(f'Horario do confronto: ')
    gols_conf1_tm1 = input(f'Quantidade de gols de {eq1}: ')
    cartama_conf1_tm1 = input(f'Quantidade de cartões amarelos de {eq1}: ')
    cartver_conf1_tm1 = input(f'Quantidade de cartões vermelhos de {eq1}:')
    gols_conf1_tm2 = input(f'Quantidade de gols de {eq2}: ')
    cartama_conf1_tm2 = input(f'Quantidade de cartões amarelos de {eq2}: ')
    cartver_conf1_tm2 = input(f'Quantidade de cartões vermelhos de {eq2}:')
    confrontos[X][f"conf1_{X}"] = {'conf':f'{eq1} x {eq2}','hora': horario, 'data': data, 'local': local,'gols_conf1_tm1':int(gols_conf1_tm1), 'cartama_conf1_tm1': int(cartama_conf1_tm1), 'cartver_conf1_tm1': int(cartver_conf1_tm1), 'gols_conf1_tm2': int(gols_conf1_tm2), 'cartama_conf1_tm2': int(cartama_conf1_tm2), 'cartver_conf1_tm2':int(cartver_conf1_tm2)}
    with open('confrontos.json', 'w') as json_file:
        json.dump(confrontos, json_file, indent=4)

def confronto2(X,eq1, eq3): #FUNÇÃO PARA INPUT DO CONFRONTO 2
    with open('confrontos.json', 'r') as json_file:
        confrontos = json.load(json_file)
    print(f'{eq1} x {eq3}')
    data = input(f'Data do confronto [dd/mm/aaaa]: ')
    local = input(f'Estadio do confronto: ')
    horario = input(f'Horario do confronto: ')
    gols_conf2_tm1 = input(f'Quantidade de gols de {eq1}: ')
    cartama_conf2_tm1 = input(f'Quantidade de cartões amarelos de {eq1}: ')
    cartver_conf2_tm1 = input(f'Quantidade de cartões vermelhos de {eq1}:')
    gols_conf2_tm3 = input(f'Quantidade de gols de {eq3}: ')
    cartama_conf2_tm3 = input(f'Quantidade de cartões amarelos de {eq3}: ')
    cartver_conf2_tm3 = input(f'Quantidade de cartões vermelhos de {eq3}:')
    confrontos[X][f"conf2_{X}"] = {'conf':f'{eq1} x {eq3}','hora': horario, 'data': data, 'local': local,'gols_conf2_tm1':int(gols_conf2_tm1), 'cartama_conf2_tm1': int(cartama_conf2_tm1), f'cartver_conf2_tm1': int(cartver_conf2_tm1), 'gols_conf2_tm3': int(gols_conf2_tm3),'cartama_conf2_tm3': int(cartama_conf2_tm3), 'cartver_conf2_tm3': int(cartver_conf2_tm3)}
    with open('confrontos.json', 'w') as json_file:
        json.dump(confrontos, json_file, indent=4)

def confronto3(X,eq1, eq4): #FUNÇÃO PARA INPUT DO CONFRONTO 3
    with open('confrontos.json', 'r') as json_file:
        confrontos = json.load(json_file)
    print(f'{eq1} x {eq4}')
    data = input(f'Data do confronto [dd/mm/aaaa]: ')
    local = input(f'Estadio do confronto: ')
    horario = input(f'Horario do confronto: ')
    gols_conf3_tm1 = input(f'Quantidade de gols de {eq1}: ')
    cartama_conf3_tm1 = input(f'Quantidade de cartões amarelos de {eq1}: ')
    cartver_conf3_tm1 = input(f'Quantidade de cartões vermelhos de {eq1}:')
    gols_conf3_tm4 = input(f'Quantidade de gols de {eq4}: ')
    cartama_conf3_tm4 = input(f'Quantidade de cartões amarelos de {eq4}: ')
    cartver_conf3_tm4 = input(f'Quantidade de cartões vermelhos de {eq4}:')
    confrontos[X][f"conf3_{X}"] = {'conf':f'{eq1} x {eq4}','hora': horario, 'data': data, 'local': local,'gols_conf3_tm1':int(gols_conf3_tm1), 'cartama_conf3_tm1': int(cartama_conf3_tm1), 'cartver_conf3_tm1': int(cartver_conf3_tm1), 'gols_conf3_tm4': int(gols_conf3_tm4),'cartama_conf3_tm4': int(cartama_conf3_tm4), 'cartver_conf3_tm4': int(cartver_conf3_tm4)}
    with open('confrontos.json', 'w') as json_file:
        json.dump(confrontos, json_file, indent=4)

def confronto4(X,eq2, eq3): #FUNÇÃO PARA INPUT DO CONFRONTO 4
    with open('confrontos.json', 'r') as json_file:
        confrontos = json.load(json_file)
    print(f'{eq2} x {eq3}')
    data = input(f'Data do confronto [dd/mm/aaaa]: ')
    local = input(f'Estadio do confronto: ')
    horario = input(f'Horario do confronto: ')
    gols_conf4_tm2 = input(f'Quantidade de gols de {eq2}: ')
    cartama_conf4_tm2 = input(f'Quantidade de cartões amarelos de {eq2}: ')
    cartver_conf4_tm2 = input(f'Quantidade de cartões vermelhos de {eq2}:')
    gols_conf4_tm3 = input(f'Quantidade de gols de {eq3}: ')
    cartama_conf4_tm3 = input(f'Quantidade de cartões amarelos de {eq3}: ')
    cartver_conf4_tm3 = input(f'Quantidade de cartões vermelhos de {eq3}:')
    confrontos[X][f"conf4_{X}"] = {'conf':f'{eq2} x {eq3}','hora': horario, 'data': data, 'local': local,'gols_conf4_tm2':int(gols_conf4_tm2), 'cartama_conf4_tm2': int(cartama_conf4_tm2), f'cartver_conf4_tm2': int(cartver_conf4_tm2), 'gols_conf4_tm3': int(gols_conf4_tm3),'cartama_conf4_tm3': int(cartama_conf4_tm3), 'cartver_conf4_tm3' : int(cartver_conf4_tm3)}
    with open('confrontos.json', 'w') as json_file:
        json.dump(confrontos, json_file, indent=4)

def confronto5(X,eq2, eq4): #FUNÇÃO PARA INPUT DO CONFRONTO 5
    with open('confrontos.json', 'r') as json_file:
        confrontos = json.load(json_file)
    print(f'{eq2} x {eq4}')
    data = input(f'Data do confronto [dd/mm/aaaa]: ')
    local = input(f'Estadio do confronto: ')
    horario = input(f'Horario do confronto: ')
    gols_conf5_tm2 = input(f'Quantidade de gols de {eq2}: ')
    cartama_conf5_tm2 = input(f'Quantidade de cartões amarelos de {eq2}: ')
    cartver_conf5_tm2 = input(f'Quantidade de cartões vermelhos de {eq2}:')
    gols_conf5_tm4 = input(f'Quantidade de gols de {eq4}: ')
    cartama_conf5_tm4 = input(f'Quantidade de cartões amarelos de {eq4}: ')
    cartver_conf5_tm4 = input(f'Quantidade de cartões vermelhos de {eq4}:')
    confrontos[X][f"conf5_{X}"] = {'conf':f'{eq2} x {eq4}','hora': horario, 'data': data, 'local': local,'gols_conf5_tm2':int(gols_conf5_tm2), 'cartama_conf5_tm2': int(cartama_conf5_tm2), 'cartver_conf5_tm2': int(cartver_conf5_tm2), 'gols_conf5_tm4' : int(gols_conf5_tm4),'cartama_conf5_tm4' : int(cartama_conf5_tm4), 'cartver_conf5_tm4': int(cartver_conf5_tm4)}
    with open('confrontos.json', 'w') as json_file:
        json.dump(confrontos, json_file, indent=4)

def confronto6(X,eq3, eq4): #FUNÇÃO PARA INPUT DO CONFRONTO 6
    with open('confrontos.json', 'r') as json_file:
        confrontos = json.load(json_file)
    print(f'{eq3} x {eq4}')
    data = input(f'Data do confronto [dd/mm/aaaa]: ')
    local = input(f'Estadio do confronto: ')
    horario = input(f'Horario do confronto: ')
    gols_conf6_tm3 = input(f'Quantidade de gols de {eq3}: ')
    cartama_conf6_tm3 = input(f'Quantidade de cartões amarelos de {eq3}: ')
    cartver_conf6_tm3 = input(f'Quantidade de cartões vermelhos de {eq3}:')
    gols_conf6_tm4 = input(f'Quantidade de gols de {eq4}: ')
    cartama_conf6_tm4 = input(f'Quantidade de cartões amarelos de {eq4}: ')
    cartver_conf6_tm4 = input(f'Quantidade de cartões vermelhos de {eq4}:')
    confrontos[X][f"conf6_{X}"] = {'conf':f'{eq3} x {eq4}','hora': horario, 'data': data, 'local': local,'gols_conf6_tm3':int(gols_conf6_tm3), 'cartama_conf6_tm3': int(cartama_conf6_tm3), 'cartver_conf6_tm3': int(cartver_conf6_tm3), 'gols_conf6_tm4': int(gols_conf6_tm4),'cartama_conf6_tm4': int(cartama_conf6_tm4), 'cartver_conf6_tm4': int(cartver_conf6_tm4)}
    with open('confrontos.json', 'w') as json_file:
        json.dump(confrontos, json_file, indent=4)

def pontuação_gols(x,confrontos, conf, gols_tm1, gols_tm2, sele1, sele2): #FUNÇÃO PARA CALCULO DO VALOR DE PONTOS POR VITORIAS E GOLS
    sele1 = 0
    sele2 = 0
    if confrontos[x][conf][gols_tm1] > confrontos[x][conf][gols_tm2]:
        sele1 += 3
    elif confrontos[x][conf][gols_tm1] < confrontos[x][conf][gols_tm2]:
        sele2 += 3
    elif confrontos[x][conf][gols_tm1] == confrontos[x][conf][gols_tm2]:
        sele1 += 1
        sele2 += 1
    return sele1, sele2

def acumulo_pontos(sel1, sel2, sel3, sel4,x ): #FUNÇÃO COMPLEMENTAR PARA ACUMULO DE PONTOS
    sel1 = 0
    sel2 = 0
    sel3 = 0
    sel4 = 0
    gols_conf1 = pontuação_gols(x,confrontos, f"conf1_{x}","gols_conf1_tm1", "gols_conf1_tm2", sel1, sel2)
    sel1 +=  gols_conf1[0]
    sel2 +=  gols_conf1[1]

    gols_conf2 = pontuação_gols(x,confrontos, f"conf2_{x}", "gols_conf2_tm1", "gols_conf2_tm3", sel1, sel3)
    sel1 += gols_conf2[0]
    sel3 += gols_conf2[1]

    gols_conf3 = pontuação_gols(x,confrontos, f"conf3_{x}", "gols_conf3_tm1", "gols_conf3_tm4", sel1, sel4)
    sel1 += gols_conf3[0]
    sel4 += gols_conf3[1]

    gols_conf4 = pontuação_gols(x,confrontos, f"conf4_{x}", "gols_conf4_tm2", "gols_conf4_tm3", sel2, sel3)
    sel2 += gols_conf4[0]
    sel3 += gols_conf4[1]
        
    gols_conf5 = pontuação_gols(x,confrontos,f"conf5_{x}", "gols_conf5_tm2", "gols_conf5_tm4", sel2, sel4)
    sel2 += gols_conf5[0]
    sel4 += gols_conf5[1]

    gols_conf6 = pontuação_gols(x,confrontos, f"conf6_{x}", "gols_conf6_tm3", "gols_conf6_tm4", sel3, sel4)
    sel3 += gols_conf6[0]
    sel4 += gols_conf6[1]
    return sel1, sel2, sel3, sel4

def conf_print(eq1, eq2, eq3, eq4): # PRINT DOS CONFRONTOS A SEREM A CADASTRADOS
    print(f'QUAL CONFRONTO DESEJA CADASTRAR? \n[ 1 ]{eq1} X {eq2}\n[ 2 ]{eq1} X {eq3}\n[ 3 ]{eq1} X {eq4} \n[ 4 ]{eq2} X {eq3}\n[ 5 ]{eq2} X {eq4}\n[ 6 ]{eq3} X {eq4}')

def cad_grp(grupo,x): #FUNÇÃO PARA INPUT DOS GRUPOS 
        with open('grupos.json', 'r') as json_file:
            grupos = json.load(json_file)
        eq1 = input('NOME DA 1° EQUIPE: ')
        eq1 = verifica_sele('1°',eq1)
        grupo[f'eqp1_{x}'] = eq1
        eq2 = input('NOME DA 2° EQUIPE: ')
        eq2 = verifica_sele('2°',eq2)
        grupo[f'eqp2_{x}'] = eq2
        eq3 = input('NOME DA 3° EQUIPE: ')
        eq3 = verifica_sele('3°',eq3)
        grupo[f'eqp3_{x}'] = eq3
        eq4 = input('NOME DA 4° EQUIPE: ')
        eq4 = verifica_sele('4°',eq4)
        grupo[f'eqp4_{x}'] = eq4
        grupos[x] = grupo
        with open('grupos.json', 'w') as json_file:
            json.dump(grupos, json_file, indent=4)

def gols_por_sele(x): #FUNÇÃO PARA CALCULO DE GOLS POR SELEÇÃO
    gols_pro_tm1 = confrontos[x][f"conf1_{x}"]["gols_conf1_tm1"] + confrontos[x][f"conf2_{x}"]["gols_conf2_tm1"] + confrontos[x][f"conf3_{x}"]["gols_conf3_tm1"]
    gols_pro_tm2 = confrontos[x][f"conf1_{x}"]["gols_conf1_tm2"] + confrontos[x][f"conf4_{x}"]["gols_conf4_tm2"] + confrontos[x][f"conf5_{x}"]["gols_conf5_tm2"]
    gols_pro_tm3 = confrontos[x][f"conf2_{x}"]["gols_conf2_tm3"] + confrontos[x][f"conf4_{x}"]["gols_conf4_tm3"] + confrontos[x][f"conf6_{x}"]["gols_conf6_tm3"]
    gols_pro_tm4 = confrontos[x][f"conf3_{x}"]["gols_conf3_tm4"] + confrontos[x][f"conf5_{x}"]["gols_conf5_tm4"] + confrontos[x][f"conf6_{x}"]["gols_conf6_tm4"]
    return gols_pro_tm1, gols_pro_tm2, gols_pro_tm3, gols_pro_tm4

def saldo_gols(x): #FUNÇÃO PARA SALDO DE GOLS POR SELEÇÃO

    gols_pro_tm1 = confrontos[x][f"conf1_{x}"]["gols_conf1_tm1"] + confrontos[x][f"conf2_{x}"]["gols_conf2_tm1"] + confrontos[x][f"conf3_{x}"]["gols_conf3_tm1"]
    gols_pro_tm2 = confrontos[x][f"conf1_{x}"]["gols_conf1_tm2"] + confrontos[x][f"conf4_{x}"]["gols_conf4_tm2"] + confrontos[x][f"conf5_{x}"]["gols_conf5_tm2"]
    gols_pro_tm3 = confrontos[x][f"conf2_{x}"]["gols_conf2_tm3"] + confrontos[x][f"conf4_{x}"]["gols_conf4_tm3"] + confrontos[x][f"conf6_{x}"]["gols_conf6_tm3"]
    gols_pro_tm4 = confrontos[x][f"conf3_{x}"]["gols_conf3_tm4"] + confrontos[x][f"conf5_{x}"]["gols_conf5_tm4"] + confrontos[x][f"conf6_{x}"]["gols_conf6_tm4"]
    
    gols_contra_tm1 = confrontos[x][f"conf1_{x}"]["gols_conf1_tm2"] + confrontos[x][f"conf2_{x}"]["gols_conf2_tm3"] + confrontos[x][f"conf3_{x}"]["gols_conf3_tm4"]
    gols_contra_tm2 = confrontos[x][f"conf1_{x}"]["gols_conf1_tm1"] + confrontos[x][f"conf4_{x}"]["gols_conf4_tm3"] + confrontos[x][f"conf5_{x}"]["gols_conf5_tm4"]
    gols_contra_tm3 = confrontos[x][f"conf2_{x}"]["gols_conf2_tm1"] + confrontos[x][f"conf4_{x}"]["gols_conf4_tm2"] + confrontos[x][f"conf6_{x}"]["gols_conf6_tm4"]
    gols_contra_tm4 = confrontos[x][f"conf3_{x}"]["gols_conf3_tm1"] + confrontos[x][f"conf5_{x}"]["gols_conf5_tm2"] + confrontos[x][f"conf6_{x}"]["gols_conf6_tm3"]

    saldo_gols_tm1 = gols_pro_tm1 - gols_contra_tm1
    saldo_gols_tm2 = gols_pro_tm2 - gols_contra_tm2
    saldo_gols_tm3 = gols_pro_tm3 - gols_contra_tm3
    saldo_gols_tm4 = gols_pro_tm4 - gols_contra_tm4

    return saldo_gols_tm1, saldo_gols_tm2, saldo_gols_tm3, saldo_gols_tm4

def cartoes_ama(x): #FUNÇÃO PARA CARTÕES AMARELOS POR SELEÇÃO
    cartoes_tm1 = confrontos[x][f"conf1_{x}"]["cartama_conf1_tm1"] + confrontos[x][f"conf2_{x}"]["cartama_conf2_tm1"] + confrontos[x][f"conf3_{x}"]["cartama_conf3_tm1"]
    cartoes_tm2 = confrontos[x][f"conf1_{x}"]["cartama_conf1_tm2"] + confrontos[x][f"conf4_{x}"]["cartama_conf4_tm2"] + confrontos[x][f"conf5_{x}"]["cartama_conf5_tm2"]
    cartoes_tm3 = confrontos[x][f"conf2_{x}"]["cartama_conf2_tm3"] + confrontos[x][f"conf4_{x}"]["cartama_conf4_tm3"] + confrontos[x][f"conf6_{x}"]["cartama_conf6_tm3"]
    cartoes_tm4 = confrontos[x][f"conf3_{x}"]["cartama_conf3_tm4"] + confrontos[x][f"conf5_{x}"]["cartama_conf5_tm4"] + confrontos[x][f"conf6_{x}"]["cartama_conf6_tm4"]
    return cartoes_tm1, cartoes_tm2, cartoes_tm3, cartoes_tm4

def cartoes_ver(x): #FUNÇÃO PARA CARTÕES VERMELHOS POR SELEÇÃO
    cartoes_tm1 = confrontos[x][f"conf1_{x}"]["cartver_conf1_tm1"] + confrontos[x][f"conf2_{x}"]["cartver_conf2_tm1"] + confrontos[x][f"conf3_{x}"]["cartver_conf3_tm1"]
    cartoes_tm2 = confrontos[x][f"conf1_{x}"]["cartver_conf1_tm2"] + confrontos[x][f"conf4_{x}"]["cartver_conf4_tm2"] + confrontos[x][f"conf5_{x}"]["cartver_conf5_tm2"]
    cartoes_tm3 = confrontos[x][f"conf2_{x}"]["cartver_conf2_tm3"] + confrontos[x][f"conf4_{x}"]["cartver_conf4_tm3"] + confrontos[x][f"conf6_{x}"]["cartver_conf6_tm3"]
    cartoes_tm4 = confrontos[x][f"conf3_{x}"]["cartver_conf3_tm4"] + confrontos[x][f"conf5_{x}"]["cartver_conf5_tm4"] + confrontos[x][f"conf6_{x}"]["cartver_conf6_tm4"]
    return cartoes_tm1, cartoes_tm2, cartoes_tm3, cartoes_tm4

def lugar1_desempate(lugar1,sel1,sel2,sel3,sel4,x, saldogols_tm1, saldogols_tm2, saldogols_tm3, saldogols_tm4, cartama_tm1, cartama_tm2, cartama_tm3, cartama_tm4, cartver_tm1, cartver_tm2, cartver_tm3, cartver_tm4): #FUNÇÃO PARA DESEMPATE DO 1° LUGAR
    if sel1>sel2 and sel1>sel3 and sel1>sel4:
        lugar1 =  grupos[f'{x}'][f'eqp1_{x}']
    elif sel2>sel1 and sel2>sel3 and sel2>sel4:
        lugar1 =  grupos[f'{x}'][f'eqp2_{x}']
    elif sel3>sel1 and sel3>sel2 and sel3>sel4:
        lugar1 =  grupos[f'{x}'][f'eqp3_{x}']
    elif sel4>sel1 and sel4>sel2 and sel4>sel3:
        lugar1 =  grupos[f'{x}'][f'eqp4_{x}']
    else:
        if sel1 == sel2:
            if saldogols_tm1>saldogols_tm2:
                lugar1 = grupos[f'{x}'][f'eqp1_{x}']
            elif saldogols_tm1<saldogols_tm2:
                lugar1 = grupos[f'{x}'][f'eqp2_{x}']
            else: 
                if cartama_tm1>cartama_tm2:
                    lugar1 = grupos[f'{x}'][f'eqp2_{x}']
                elif cartama_tm1<cartama_tm2:
                    lugar1 = grupos[f'{x}'][f'eqp1_{x}']
                else:
                    if cartver_tm1>cartver_tm2:
                        lugar1 = grupos[f'{x}'][f'eqp2_{x}']
                    elif cartver_tm1<cartver_tm2:
                        lugar1 = grupos[f'{x}'][f'eqp1_{x}']
        elif sel1 == sel3:
            if saldogols_tm1>saldogols_tm3:
                lugar1 = grupos[f'{x}'][f'eqp1_{x}']
            elif saldogols_tm1<saldogols_tm3:
                lugar1 = grupos[f'{x}'][f'eqp3_{x}']  
            else: 
                if cartama_tm1>cartama_tm3:
                    lugar1 = grupos[f'{x}'][f'eqp3_{x}']
                elif cartama_tm1<cartama_tm3:
                    lugar1 = grupos[f'{x}'][f'eqp1_{x}']
                else:
                    if cartver_tm1>cartver_tm3:
                        lugar1 = grupos[f'{x}'][f'eqp3_{x}']
                    elif cartver_tm1<cartver_tm3:
                        lugar1 = grupos[f'{x}'][f'eqp1_{x}']
        elif sel1 == sel4:
            if saldogols_tm1>saldogols_tm4:
                lugar1 = grupos[f'{x}'][f'eqp1_{x}']
            elif saldogols_tm1<saldogols_tm4:
                lugar1 = grupos[f'{x}'][f'eqp4_{x}']
            else: 
                if cartama_tm1>cartama_tm4:
                    lugar1 = grupos[f'{x}'][f'eqp4_{x}']
                elif cartama_tm1<cartama_tm4:
                    lugar1 = grupos[f'{x}'][f'eqp1_{x}']
                else:
                    if cartver_tm1>cartver_tm4:
                        lugar1 = grupos[f'{x}'][f'eqp4_{x}']
                    elif cartver_tm1<cartver_tm4:
                        lugar1 = grupos[f'{x}'][f'eqp1_{x}'] 
        elif sel2 == sel3:
            if saldogols_tm2>saldogols_tm3:
                lugar1 = grupos[f'{x}'][f'eqp2_{x}']
            elif saldogols_tm2<saldogols_tm3:
                lugar1 = grupos[f'{x}'][f'eqp3_{x}']
            else: 
                if cartama_tm2>cartama_tm3:
                    lugar1 = grupos[f'{x}'][f'eqp3_{x}']
                elif cartama_tm2<cartama_tm3:
                    lugar1 = grupos[f'{x}'][f'eqp2_{x}']
                else:
                    if cartver_tm2>cartver_tm3:
                        lugar1 = grupos[f'{x}'][f'eqp3_{x}']
                    elif cartver_tm2<cartver_tm3:
                        lugar1 = grupos[f'{x}'][f'eqp2_{x}'] 
        elif sel2 == sel4:
            if saldogols_tm2>saldogols_tm4:
                lugar1 = grupos[f'{x}'][f'eqp2_{x}']
            elif saldogols_tm2<saldogols_tm4:
                lugar1 = grupos[f'{x}'][f'eqp4_{x}']
            else: 
                if cartama_tm2>cartama_tm4:
                    lugar1 = grupos[f'{x}'][f'eqp4_{x}']
                elif cartama_tm2<cartama_tm3:
                    lugar1 = grupos[f'{x}'][f'eqp2_{x}']
                else:
                    if cartver_tm2>cartver_tm4:
                        lugar1 = grupos[f'{x}'][f'eqp4_{x}']
                    elif cartver_tm2<cartver_tm4:
                        lugar1 = grupos[f'{x}'][f'eqp2_{x}']
        elif sel3 == sel4:
            if saldogols_tm3>saldogols_tm4:
                lugar1 = grupos[f'{x}'][f'eqp3_{x}']
            elif saldogols_tm3<saldogols_tm4:
                lugar1 = grupos[f'{x}'][f'eqp4_{x}']
            else: 
                if cartama_tm3>cartama_tm4:
                    lugar1 = grupos[f'{x}'][f'eqp4_{x}']
                elif cartama_tm3<cartama_tm4:
                    lugar1 = grupos[f'{x}'][f'eqp3_{x}']
                else:
                    if cartver_tm3>cartver_tm4:
                        lugar1 = grupos[f'{x}'][f'eqp4_{x}']
                    elif cartver_tm2<cartver_tm3:
                        lugar1 = grupos[f'{x}'][f'eqp3_{x}']
    return lugar1
def lugar2_desempate(lugar2,sel1,sel2,sel3,sel4,x, saldogols_tm1, saldogols_tm2, saldogols_tm3, saldogols_tm4, cartama_tm1, cartama_tm2, cartama_tm3, cartama_tm4, cartver_tm1, cartver_tm2, cartver_tm3, cartver_tm4): #FUNÇÃO PARA DESEMPATE DO 2° LUGAR 

    if sel1>sel2 and sel1>sel3 and sel1<sel4 or sel1>sel2 and sel1<sel3 and sel1>sel4 or sel1<sel2 and sel1>sel3 and sel1>sel4:
        lugar2 = grupos[f'{x}'][f'eqp1_{x}']
    elif sel2>sel1 and sel2>sel3 and sel2<sel4 or sel2>sel1 and sel2<sel3 and sel2>sel4 or sel2<sel1 and sel2>sel3 and sel2>sel4:
        lugar2 = grupos[f'{x}'][f'eqp2_{x}']
    elif sel3>sel1 and sel3>sel2 and sel3<sel4 or sel3>sel1 and sel3<sel2 and sel3>sel4 or sel3<sel1 and sel3>sel2 and sel3>sel4:
        lugar2 = grupos[f'{x}'][f'eqp3_{x}']
    elif sel4>sel1 and sel4>sel2 and sel4<sel3 or sel4>sel1 and sel4<sel2 and sel4>sel3 or sel4<sel1 and sel4>sel2 and sel4>sel3:
        lugar2 = grupos[f'{x}'][f'eqp4_{x}']
    else:
        if sel1 == sel2:
            if saldogols_tm1>saldogols_tm2:
                lugar2 = grupos[f'{x}'][f'eqp2_{x}']
            elif saldogols_tm1<saldogols_tm2 and sel1>=sel2:
                lugar2 = grupos[f'{x}'][f'eqp1_{x}']
            else: 
                if cartama_tm1>cartama_tm2:
                    lugar2 = grupos[f'{x}'][f'eqp2_{x}']
                elif cartama_tm1<cartama_tm2:
                    lugar2 = grupos[f'{x}'][f'eqp1_{x}']
                else:
                    if cartver_tm1>cartver_tm2:
                        lugar2 = grupos[f'{x}'][f'eqp2_{x}']
                    elif cartver_tm1<cartver_tm2:
                        lugar2 = grupos[f'{x}'][f'eqp1_{x}']
        elif sel1 == sel3:
            if saldogols_tm1>saldogols_tm3:
                lugar2 = grupos[f'{x}'][f'eqp1_{x}']
            elif saldogols_tm1<saldogols_tm3:
                lugar2 = grupos[f'{x}'][f'eqp3_{x}']  
            else: 
                if cartama_tm1>cartama_tm3:
                    lugar2 = grupos[f'{x}'][f'eqp3_{x}']
                elif cartama_tm1<cartama_tm3:
                    lugar2 = grupos[f'{x}'][f'eqp1_{x}']
                else:
                    if cartver_tm1>cartver_tm3:
                        lugar2 = grupos[f'{x}'][f'eqp3_{x}']
                    elif cartver_tm1<cartver_tm3:
                        lugar2 = grupos[f'{x}'][f'eqp1_{x}']
        elif sel1 == sel4:
            if saldogols_tm1>saldogols_tm4:
                lugar2 = grupos[f'{x}'][f'eqp1_{x}']
            elif saldogols_tm1<saldogols_tm4:
                lugar2 = grupos[f'{x}'][f'eqp4_{x}']
            else: 
                if cartama_tm1>cartama_tm4:
                    lugar2 = grupos[f'{x}'][f'eqp4_{x}']
                elif cartama_tm1<cartama_tm4:
                    lugar2 = grupos[f'{x}'][f'eqp1_{x}']
                else:
                    if cartver_tm1>cartver_tm4:
                        lugar2 = grupos[f'{x}'][f'eqp4_{x}']
                    elif cartver_tm1<cartver_tm4:
                        lugar2 = grupos[f'{x}'][f'eqp1_{x}'] 
        elif sel2 == sel3:
            if saldogols_tm2>saldogols_tm3:
                lugar2 = grupos[f'{x}'][f'eqp2_{x}']
            elif saldogols_tm2<saldogols_tm3:
                lugar2 = grupos[f'{x}'][f'eqp3_{x}']
            else: 
                if cartama_tm2>cartama_tm3:
                    lugar2 = grupos[f'{x}'][f'eqp3_{x}']
                elif cartama_tm2<cartama_tm3:
                    lugar2 = grupos[f'{x}'][f'eqp2_{x}']
                else:
                    if cartver_tm2>cartver_tm3:
                        lugar2 = grupos[f'{x}'][f'eqp3_{x}']
                    elif cartver_tm2<cartver_tm3:
                        lugar2 = grupos[f'{x}'][f'eqp2_{x}'] 
        elif sel2 == sel4:
            if saldogols_tm2>saldogols_tm4:
                lugar2 = grupos[f'{x}'][f'eqp2_{x}']
            elif saldogols_tm2<saldogols_tm4:
                lugar2 = grupos[f'{x}'][f'eqp4_{x}']
            else: 
                if cartama_tm2>cartama_tm4:
                    lugar2 = grupos[f'{x}'][f'eqp4_{x}']
                elif cartama_tm2<cartama_tm3:
                    lugar2 = grupos[f'{x}'][f'eqp2_{x}']
                else:
                    if cartver_tm2>cartver_tm4:
                        lugar2 = grupos[f'{x}'][f'eqp4_{x}']
                    elif cartver_tm2<cartver_tm4:
                        lugar2 = grupos[f'{x}'][f'eqp2_{x}']
        elif sel3 == sel4:
            if saldogols_tm3>saldogols_tm4:
                lugar2 = grupos[f'{x}'][f'eqp3_{x}']
            elif saldogols_tm3<saldogols_tm4:
                lugar2 = grupos[f'{x}'][f'eqp4_{x}']
            else: 
                if cartama_tm3>cartama_tm4:
                    lugar2 = grupos[f'{x}'][f'eqp4_{x}']
                elif cartama_tm3<cartama_tm4:
                    lugar2 = grupos[f'{x}'][f'eqp3_{x}']
                else:
                    if cartver_tm3>cartver_tm4:
                        lugar2 = grupos[f'{x}'][f'eqp4_{x}']
                    elif cartver_tm2<cartver_tm3:
                        lugar2 = grupos[f'{x}'][f'eqp3_{x}']
    return lugar2

def exclui_grupo(x): #FUNÇÃO PARA EXCLUIR GRUPO
    with open('grupos.json', 'r') as json_file:
        grupos = json.load(json_file)
    grupos.pop(f'{x}')
    with open('grupos.json', 'w') as json_file:
        json.dump(grupos, json_file, indent=4)

def exclui_confro(x, eq1,eq2,eq3,eq4): # FUNÇÃO PARA EXCLUIR CONFRONTO
    with open('confrontos.json', 'r') as json_file:
        confrontos = json.load(json_file)
    print(f'QUAL CONFRONTO DESEJA EXCLUIR? \n[ 1 ]{eq1} X {eq2}\n[ 2 ]{eq1} X {eq3}\n[ 3 ]{eq1} X {eq4} \n[ 4 ]{eq2} X {eq3}\n[ 5 ]{eq2} X {eq4}\n[ 6 ]{eq3} X {eq4}')
    opc = input('QUAL SUA OPÇÃO?')
    if int(opc) == 1:
        confrontos[x].pop(f'conf1_{x}')
        with open('confrontos.json', 'w') as json_file:
            json.dump(confrontos, json_file, indent=4)
    elif int(opc) == 2:
        confrontos[x].pop(f'conf2_{x}')
        with open('confrontos.json', 'w') as json_file:
            json.dump(confrontos, json_file, indent=4)
    elif int(opc) == 3:
        confrontos[x].pop(f'conf3_{x}')
        with open('confrontos.json', 'w') as json_file:
            json.dump(confrontos, json_file, indent=4)
    elif int(opc) == 4:
        confrontos[x].pop(f'conf4_{x}')
        with open('confrontos.json', 'w') as json_file:
            json.dump(confrontos, json_file, indent=4)
    elif int(opc) == 5:
        confrontos[x].pop(f'conf5_{x}')
        with open('confrontos.json', 'w') as json_file:
            json.dump(confrontos, json_file, indent=4)
    elif int(opc) == 6:
        confrontos[x].pop(f'conf6_{x}')
        with open('confrontos.json', 'w') as json_file:
            json.dump(confrontos, json_file, indent=4)

def confro(x): #FUNÇÃO COMPLEMENTAR PARA CADASTRO DOS CONFRONTOS
    with open('grupos.json', 'r') as json_file:
        grupos = json.load(json_file)
    conf_print(grupos[x][f'eqp1_{x}'],grupos[x][f'eqp2_{x}'],grupos[x][f'eqp3_{x}'],grupos[x][f'eqp4_{x}'])
    opc = input('QUAL SUA OPÇÃO?')
    if int(opc) == 1:
        confronto1(x,grupos[x][f'eqp1_{x}'], grupos[x][f'eqp2_{x}'])
    elif int(opc) == 2:
        confronto2(x,grupos[x][f'eqp1_{x}'], grupos[x][f'eqp3_{x}'])
    elif int(opc) == 3:
        confronto3(x,grupos[x][f'eqp1_{x}'], grupos[x][f'eqp4_{x}'])
    elif int(opc) == 4:
        confronto4(x,grupos[x][f'eqp2_{x}'], grupos[x][f'eqp3_{x}'])
    elif int(opc) == 5:
        confronto5(x,grupos[x][f'eqp2_{x}'], grupos[x][f'eqp4_{x}'])
    elif int(opc) == 6:
        confronto6(x,grupos[x][f'eqp3_{x}'], grupos[x][f'eqp4_{x}'])

def verifica(x,y): #FUNÇÃO DE VERIFICAÇÃO DE INPUTS
    try:
        if type(x) != int:
            while x.isdigit() == False:
                print('Valor inválido')
                x = input('Qual sua opção? ')
        while int(x)<=0 or int(x)>y:
            print('Valor inválido')
            x = input('Qual sua opção? ')
    except:
        print('Valor inválido')
        x = int(input('Qual sua opção? '))   

def verifica_sele(x,eq): #FUNÇÃO PARA VERICAR REPETIÇÃO DE SELEÇÕES
    with open('grupos.json', 'r') as json_file:
        grupos = json.load(json_file)
    while eq == grupos['A']['eqp1_A'] or eq == grupos['A']['eqp2_A'] or eq == grupos['A']['eqp3_A'] or eq == grupos['A']['eqp4_A'] or eq == grupos['B']['eqp1_B'] or eq == grupos['B']['eqp2_B'] or eq == grupos['B']['eqp3_B'] or eq == grupos['B']['eqp4_B'] or eq == grupos['C']['eqp1_C'] or eq == grupos['C']['eqp2_C'] or eq == grupos['C']['eqp3_C'] or eq == grupos['C']['eqp4_C'] or eq == grupos['D']['eqp1_D'] or eq == grupos['D']['eqp2_D'] or eq == grupos['D']['eqp3_D'] or eq == grupos['D']['eqp4_D'] or eq == grupos['E']['eqp1_E'] or eq == grupos['E']['eqp2_E'] or eq == grupos['E']['eqp3_E'] or eq == grupos['E']['eqp4_E'] or eq == grupos['F']['eqp1_F'] or eq == grupos['F']['eqp2_F'] or eq == grupos['F']['eqp3_F'] or eq == grupos['F']['eqp4_F'] or eq == grupos['G']['eqp1_G'] or eq == grupos['G']['eqp2_G'] or eq == grupos['G']['eqp3_G'] or eq == grupos['G']['eqp4_G'] or eq == grupos['H']['eqp1_H'] or eq == grupos['H']['eqp2_H'] or eq == grupos['H']['eqp3_H'] or eq == grupos['H']['eqp4_H']:
        print('SELEÇÃO JA CADASTRADA, TENTE NOVAMENTE')
        eq = input(f'NOME DA {x} EQUIPE: ')
    return eq 

# VARIAVEIS DA PONTUAÇÃO DAS SELEÇÕES
seleção1 = seleção2 = seleção3 = seleção4 = seleção5 = seleção6 = seleção7 = seleção8 = seleção9 = seleção10 = seleção11 = seleção12  = seleção13  = seleção14  = seleção15  = seleção16  = seleção17 = seleção18 = 0
seleção19 = seleção20 = seleção21 = seleção22 = seleção23 = seleção24 = seleção25 = seleção26 = seleção27 = seleção28 = seleção29 = seleção30 = seleção31 = seleção32 = 0


#DICIONARIO DOS GRUPOS
grupoA, grupoB, grupoC, grupoD, grupoE, grupoF, grupoG, grupoH = {},{},{},{},{},{},{},{}

#VARIAVEIS DO 1° E 2° LUGAR DE CADA GRUPO 
lugar1_A = lugar1_B = lugar1_C = lugar1_D = lugar1_E = lugar1_F = lugar1_G = lugar1_H = '' 
lugar2_A = lugar2_B = lugar2_C = lugar2_D = lugar2_E = lugar2_F = lugar2_G = lugar2_H = ''

#DICIONARIO DO ARQUIVO GRUPOS 
grupos = {}
#DICIONARIO DO ARQUIVO CONFRONTOS
confrontos = {}

#MENU PRINCIPAL
opção = 0
print('-=-='*20)
print('       BEM VINDO AO SEU CADASTRADOR OFICIAL DA COPA DO MUNDO!       ')
print('-=-='*20)
while int(opção) != 4:
    print('O QUE DESEJA FAZER? \n[ 1 ] CADASTRAR UM GRUPO \n[ 2 ] EDITAR UM GRUPO \n[ 3 ] EXIBIR OITAVAS DE FINAL \n[ 4 ] SAIR')
    opção = input('QUAL SUA OPÇÃO? ')
    verifica(opção, 4)
    #CADASTRAMENTO DOS GRUPOS
    if int(opção) == 1:
        print('-=-='*20)
        print('Qual grupo deseja cadastrar? \n[ 1 ]Grupo A  [ 2 ]Grupo B  [ 3 ]Grupo C  [ 4 ]Grupo D \n[ 5 ]Grupo E  [ 6 ]Grupo F  [ 7 ]Grupo G  [ 8 ]Grupo H')
        opc = input('QUAL SUA OPÇÃO? ')
        verifica(opc, 8)
        #CADASTRAMENTO DO GRUPO A
        if int(opc) == 1:
            print('-=-='*20)
            print('CADASTRAR: \n[ 1 ]EQUIPES \n[ 2 ]CONFRONTOS')
            opc = input('QUAL SUA OPÇÃO? ')
            verifica(opc, 2)

            if int(opc) == 1:
                print('-=-='*20)
                cad_grp(grupoA,'A')  

            elif int(opc) == 2:
               confro('A')
        #CADASTRAMENTO DO GRUPO B
        elif int(opc) == 2:
            print('-=-='*20)
            print('CADASTRAR: \n[ 1 ]EQUIPES \n[ 2 ]CONFRONTOS')
            opc = input('QUAL SUA OPÇÃO? ')
            verifica(opc, 2)
            if int(opc) == 1:
                print('-=-='*20)
                cad_grp(grupoB,'B')

            elif int(opc) == 2:
               confro('B')
        #CADASTRAMENTO DO GRUPO C        
        elif int(opc) == 3:
            print('-=-='*20)
            print('CADASTRAR: \n[ 1 ]EQUIPES \n[ 2 ]CONFRONTOS')
            opc = input('QUAL SUA OPÇÃO? ')
            verifica(opc, 2)
            if int(opc) == 1:
                print('-=-='*20)
                cad_grp(grupoC,'C')
            
            elif int(opc) == 2:
               confro('C')
        #CADASRTAMENTO DO GRUPO D        
        elif int(opc) == 4:
            print('-=-='*20)
            print('CADASTRAR: \n[ 1 ]EQUIPES \n[ 2 ]CONFRONTOS')
            opc = input('QUAL SUA OPÇÃO? ')
            verifica(opc, 2)
            if int(opc) == 1:
                print('-=-='*20)
                cad_grp(grupoD,'D')
            
            elif int(opc) == 2:
                confro('D')
        #CADASTRAMENTO DO GRUPO E
        elif int(opc) == 5:
            print('-=-='*20)
            with open('grupos.json', 'r') as json_file:
                    grupos = json.load(json_file)
            print('CADASTRAR: \n[ 1 ]EQUIPES \n[ 2 ]CONFRONTOS')
            opc = input('QUAL SUA OPÇÃO? ')
            verifica(opc, 2)
            if int(opc) == 1:
                print('-=-='*20)
                cad_grp(grupoE,'E')

            elif int(opc) == 2:
               confro('E')
        #CADASTRAMENTO DO GRUPO F        
        elif int(opc) == 6:
            print('-=-='*20)
            with open('grupos.json', 'r') as json_file:
                    grupos = json.load(json_file)
            print('CADASTRAR: \n[ 1 ]EQUIPES \n[ 2 ]CONFRONTOS')
            opc = input('QUAL SUA OPÇÃO? ')
            verifica(opc, 2)
            if int(opc) == 1:
                print('-=-='*20)
                cad_grp(grupoF,'F')

            elif int(opc) == 2:
               confro('F')
        #CADASTRAMENTO DO GRUPO G
        elif int(opc) == 7:
            print('-=-='*20)
            with open('grupos.json', 'r') as json_file:
                    grupos = json.load(json_file)
            print('CADASTRAR: \n[ 1 ]EQUIPES \n[ 2 ]CONFRONTOS')
            opc = input('QUAL SUA OPÇÃO? ')
            verifica(opc, 2)
            if int(opc) == 1:
                print('-=-='*20)
                cad_grp(grupoG,'G')

            elif int(opc) == 2:
                confro('G')
        #CADASTRAMENTO DO GRUPO H
        elif int(opc) == 8:
            print('-=-='*20)
            with open('grupos.json', 'r') as json_file:
                    grupos = json.load(json_file)
            print('CADASTRAR: \n[ 1 ]EQUIPES \n[ 2 ]CONFRONTOS')
            opc = input('QUAL SUA OPÇÃO? ')
            verifica(opc, 2)
            if int(opc) == 1:
                print('-=-='*20)
                cad_grp(grupoH,'H')

            elif int(opc) == 2:
                confro('H')
    #EDIÇÃO E EXCLUSÃO DOS ARQUIVOS
    elif int(opção) == 2:
        print('-=-='*20)
        print('O QUE QUER FAZER? \n[ 1 ]Editar \n[ 2 ]Excluir')
        opc = input('QUAL SUA OPÇÃO? ')
        verifica(opc, 2)
        #EDIÇAO  
        if int(opc) == 1:
            print('-=-='*20)
            print('O QUE DESEJA EDITAR?\n[ 1 ]Grupo\n[ 2 ]Confronto')
            opc = input('QUAL SUA OPÇÃO? ')
            verifica(opc, 2)
            #EDIÇÃO DOS GRUPOS
            if int(opc) == 1:
                print('-=-='*20)
                print('QUAL GRUPO DESEJA EDITAR? \n[ 1 ]Grupo A  [ 2 ]Grupo B  [ 3 ]Grupo C  [ 4 ]Grupo D \n[ 5 ]Grupo E  [ 6 ]Grupo F  [ 7 ]Grupo G  [ 8 ]Grupo H')
                opc = input('QUAL SUA OPÇÃO? ')
                verifica(opc, 2)
                if int(opc) == 1:
                    cad_grp(grupoA,'A')
                elif int(opc) == 2:
                    cad_grp(grupoA,'B')
                elif int(opc) == 3:
                    cad_grp(grupoA,'C')
                elif int(opc) == 4:
                    cad_grp(grupoA,'D')
                elif int(opc) == 5:
                    cad_grp(grupoA,'E')
                elif int(opc) == 6:
                    cad_grp(grupoA,'F')
                elif int(opc) == 7:
                    cad_grp(grupoA,'G')
                elif int(opc) == 8:
                    cad_grp(grupoA,'H')
            #EDIÇÃO DOS CONFRONTOS
            if int(opc) == 2:
                print('-=-='*20)
                print('DESEJA EDITAR OS CONFRONTOS DE QUAL GRUPO? \n[ 1 ]Grupo A  [ 2 ]Grupo B  [ 3 ]Grupo C  [ 4 ]Grupo D \n[ 5 ]Grupo E  [ 6 ]Grupo F  [ 7 ]Grupo G  [ 8 ]Grupo H')
                opc = input('QUAL SUA OPÇÃO? ')
                verifica(opc, 2)
                if int(opc) == 1:
                    confro('A')
                if int(opc) == 2:
                    confro('B')
                if int(opc) == 3:
                    confro('C')
                if int(opc) == 4:
                    confro('D')
                if int(opc) == 5:
                    confro('E')
                if int(opc) == 6:
                    confro('F')
                if int(opc) == 7:
                    confro('G')
                if int(opc) == 8:
                    confro('H')
        #EXCLUSÃO
        if int(opc) == 2:
            print('-=-='*20)
            print('O QUE DESEJA EXCLUIR?\n[ 1 ]Grupo\n[ 2 ]Confronto')
            opc = input('QUAL SUA OPÇÃO? ')
            verifica(opc, 2)
            #EXCLUSÃO DOS GRUPOS
            if int(opc) == 1:
                print('-=-='*20)
                print('QUAL GRUPO DESEJA EXCLUIR? \n[ 1 ]Grupo A  [ 2 ]Grupo B  [ 3 ]Grupo C  [ 4 ]Grupo D \n[ 5 ]Grupo E  [ 6 ]Grupo F  [ 7 ]Grupo G  [ 8 ]Grupo H')
                opc = input('QUAL SUA OPÇÃO? ')
                if int(opc) == 1:
                    exclui_grupo('A')
                elif int(opc) == 2:
                    exclui_grupo('B')
                elif int(opc) == 3:
                    exclui_grupo('C')
                elif int(opc) == 4:
                    exclui_grupo('D')
                elif int(opc) == 5:
                    exclui_grupo('E')
                elif int(opc) == 6:
                    exclui_grupo('F')
                elif int(opc) == 7:
                    exclui_grupo('G')
                elif int(opc) == 8:
                    exclui_grupo('H')
            #EXCLUSÃO DOS CONFRONTOS
            if int(opc) == 2:
                with open('grupos.json', 'r') as json_file:
                    grupos = json.load(json_file)
                print('-=-='*20)
                print('DESEJA EXCLUIR O CONFRONTO DE QUAL GRUPO? \n[ 1 ]Grupo A  [ 2 ]Grupo B  [ 3 ]Grupo C  [ 4 ]Grupo D \n[ 5 ]Grupo E  [ 6 ]Grupo F  [ 7 ]Grupo G  [ 8 ]Grupo H')
                opc = input('QUAL SUA OPÇÃO? ')
                verifica(opc, 2)
                if int(opc) == 1:
                    exclui_confro('A',grupos['A']['eqp1_A'],grupos['A']['eqp2_A'],grupos['A']['eqp3_A'],grupos['A']['eqp4_A'])
                if int(opc) == 2:
                    exclui_confro('B',grupos['B']['eqp1_B'],grupos['B']['eqp2_B'],grupos['A']['eqp3_B'],grupos['B']['eqp4_B'])
                if int(opc) == 3:
                    exclui_confro('C',grupos['C']['eqp1_C'],grupos['C']['eqp2_C'],grupos['C']['eqp3_C'],grupos['C']['eqp4_C'])
                if int(opc) == 4:
                    exclui_confro('D',grupos['D']['eqp1_D'],grupos['D']['eqp2_D'],grupos['D']['eqp3_D'],grupos['D']['eqp4_D'])
                if int(opc) == 5:
                    exclui_confro('E',grupos['E']['eqp1_E'],grupos['E']['eqp2_E'],grupos['E']['eqp3_E'],grupos['E']['eqp4_E'])
                if int(opc) == 6:
                    exclui_confro('F',grupos['F']['eqp1_F'],grupos['F']['eqp2_F'],grupos['F']['eqp3_F'],grupos['F']['eqp4_F'])
                if int(opc) == 7:
                    exclui_confro('G',grupos['G']['eqp1_G'],grupos['G']['eqp2_G'],grupos['G']['eqp3_G'],grupos['G']['eqp4_G'])
                if int(opc) == 8:
                    exclui_confro('H',grupos['H']['eqp1_H'],grupos['H']['eqp2_H'],grupos['H']['eqp3_H'],grupos['H']['eqp4_H'])
    #SAIDA DAS OITAVAS        
    elif int(opção) == 3:
        with open('confrontos.json', 'r') as json_file:
            confrontos = json.load(json_file)
        #VERIFICAÇÃO DE CADASTRO
        oitavas = False
        try:
            #CALCULO DA PONTUAÇÃO DAS SELEÇÕES 
            #GRUPO A
            pontos_A = acumulo_pontos(seleção1, seleção2, seleção3, seleção4,'A' )
            seleção1 = pontos_A[0]
            seleção2 = pontos_A[1]
            seleção3 = pontos_A[2]
            seleção4 = pontos_A[3]
            #GRUPO B
            pontos_B = acumulo_pontos(seleção5, seleção6, seleção7, seleção8,'B' )
            seleção5 = pontos_B[0]
            seleção6 = pontos_B[1]
            seleção7 = pontos_B[2]
            seleção8 = pontos_B[3]
            #GRUPO C
            pontos_C = acumulo_pontos(seleção9, seleção10, seleção11, seleção12,'C' )
            seleção9 = pontos_C[0]
            seleção10 = pontos_C[1]
            seleção11 = pontos_C[2]
            seleção12 = pontos_C[3]
            #GRUPO D
            pontos_D = acumulo_pontos(seleção13, seleção14, seleção15, seleção16,'D' )
            seleção13 = pontos_D[0]
            seleção14 = pontos_D[1]
            seleção15 = pontos_D[2]
            seleção16 = pontos_D[3]
            #GRUPO E
            pontos_E = acumulo_pontos(seleção17, seleção18, seleção19, seleção20,'E' )
            seleção17 = pontos_E[0]
            seleção18 = pontos_E[1]
            seleção19 = pontos_E[2]
            seleção20 = pontos_E[3]
            #GRUPO F
            pontos_F = acumulo_pontos(seleção21, seleção22, seleção23, seleção24,'F' )
            seleção21 = pontos_F[0]
            seleção22 = pontos_F[1]
            seleção23 = pontos_F[2]
            seleção24 = pontos_F[3]
            #GRUPO G
            pontos_G = acumulo_pontos(seleção25, seleção26, seleção27, seleção29,'G' )
            seleção25 = pontos_G[0]
            seleção26 = pontos_G[1]
            seleção27 = pontos_G[2]
            seleção28 = pontos_G[3]
            #GRUPO H
            pontos_H = acumulo_pontos(seleção29, seleção30, seleção31, seleção32,'H' )
            seleção29 = pontos_H[0]
            seleção30 = pontos_H[1]
            seleção31 = pontos_H[2]
            seleção32 = pontos_H[3]

            #CRITERIOS DE DESEMPATE
            #SALDO DE GOLS
            #GRUPO A
            saldogols_A = saldo_gols('A')
            saldogols_tm1_A = saldogols_A[0]
            saldogols_tm2_A = saldogols_A[1]
            saldogols_tm3_A = saldogols_A[2]
            saldogols_tm4_A = saldogols_A[3]
            
            #GRUPO B
            saldogols_B = saldo_gols('B')
            saldogols_tm1_B = saldogols_B[0]
            saldogols_tm2_B = saldogols_B[1]
            saldogols_tm3_B = saldogols_B[2]
            saldogols_tm4_B = saldogols_B[3]
            #GRUPO C
            saldogols_C = saldo_gols('C')
            saldogols_tm1_C = saldogols_C[0]
            saldogols_tm2_C = saldogols_C[1]
            saldogols_tm3_C = saldogols_C[2]
            saldogols_tm4_C = saldogols_C[3]
            #GRUPO D
            saldogols_D = saldo_gols('D')
            saldogols_tm1_D = saldogols_D[0]
            saldogols_tm2_D = saldogols_D[1]
            saldogols_tm3_D = saldogols_D[2]
            saldogols_tm4_D = saldogols_D[3]
            #GRUPO E
            saldogols_E = saldo_gols('E')
            saldogols_tm1_E = saldogols_E[0]
            saldogols_tm2_E = saldogols_E[1]
            saldogols_tm3_E = saldogols_E[2]
            saldogols_tm4_E = saldogols_E[3]
            #GRUPO F
            saldogols_F= saldo_gols('F')
            saldogols_tm1_F = saldogols_F[0]
            saldogols_tm2_F = saldogols_F[1]
            saldogols_tm3_F = saldogols_F[2]
            saldogols_tm4_F = saldogols_F[3]
            #GRUPO G
            saldogols_G = saldo_gols('G')
            saldogols_tm1_G = saldogols_G[0]
            saldogols_tm2_G = saldogols_G[1]
            saldogols_tm3_G = saldogols_G[2]
            saldogols_tm4_G = saldogols_G[3]
            #GRUPO H
            saldogols_H = saldo_gols('H')
            saldogols_tm1_H = saldogols_H[0]
            saldogols_tm2_H = saldogols_H[1]
            saldogols_tm3_H = saldogols_H[2]
            saldogols_tm4_H = saldogols_H[3]

            #CARTOES AMARELOS
            #GRUPO A
            cartama_A = cartoes_ama('A')
            cartama_tm1_A = cartama_A[0]
            cartama_tm2_A = cartama_A[1]
            cartama_tm3_A = cartama_A[2]
            cartama_tm4_A = cartama_A[3]
            #GRUPO B
            cartama_B= cartoes_ama('B')
            cartama_tm1_B = cartama_B[0]
            cartama_tm2_B = cartama_B[1]
            cartama_tm3_B = cartama_B[2]
            cartama_tm4_B = cartama_B[3]
            #GRUPO C
            cartama_C = cartoes_ama('C')
            cartama_tm1_C = cartama_C[0]
            cartama_tm2_C = cartama_C[1]
            cartama_tm3_C = cartama_C[2]
            cartama_tm4_C = cartama_C[3]
            #GRUPO D
            cartama_D = cartoes_ama('D')
            cartama_tm1_D = cartama_D[0]
            cartama_tm2_D = cartama_D[1]
            cartama_tm3_D = cartama_D[2]
            cartama_tm4_D = cartama_D[3]
            #GRUPO E
            cartama_E = cartoes_ama('E')
            cartama_tm1_E = cartama_E[0]
            cartama_tm2_E = cartama_E[1]
            cartama_tm3_E = cartama_E[2]
            cartama_tm4_E = cartama_E[3]
            #GRUPO F
            cartama_F = cartoes_ama('F')
            cartama_tm1_F = cartama_F[0]
            cartama_tm2_F = cartama_F[1]
            cartama_tm3_F = cartama_F[2]
            cartama_tm4_F = cartama_F[3]
            #GRUPO G
            cartama_G = cartoes_ama('G')
            cartama_tm1_G = cartama_G[0]
            cartama_tm2_G = cartama_G[1]
            cartama_tm3_G = cartama_G[2]
            cartama_tm4_G = cartama_G[3]
            #GRUPO H
            cartama_H = cartoes_ama('H')
            cartama_tm1_H = cartama_H[0]
            cartama_tm2_H = cartama_H[1]
            cartama_tm3_H = cartama_H[2]
            cartama_tm4_H = cartama_H[3]

            #CARTOES VERMELHOS
            #GRUPO A
            cartver_A = cartoes_ver('A')
            cartver_tm1_A = cartver_A[0]
            cartver_tm2_A = cartver_A[1]
            cartver_tm3_A = cartver_A[2]
            cartver_tm4_A = cartver_A[3]
            #GRUPO B
            cartver_B = cartoes_ver('B')
            cartver_tm1_B = cartver_B[0]
            cartver_tm2_B = cartver_B[1]
            cartver_tm3_B = cartver_B[2]
            cartver_tm4_B = cartver_B[3]
            #GRUPO C
            cartver_C = cartoes_ver('C')
            cartver_tm1_C = cartver_C[0]
            cartver_tm2_C = cartver_C[1]
            cartver_tm3_C = cartver_C[2]
            cartver_tm4_C = cartver_C[3]
            #GRUPO D
            cartver_D = cartoes_ver('D')
            cartver_tm1_D = cartver_D[0]
            cartver_tm2_D = cartver_D[1]
            cartver_tm3_D = cartver_D[2]
            cartver_tm4_D = cartver_D[3]
            #GRUPO E
            cartver_E = cartoes_ver('E')
            cartver_tm1_E = cartver_E[0]
            cartver_tm2_E = cartver_E[1]
            cartver_tm3_E = cartver_E[2]
            cartver_tm4_E = cartver_E[3]
            #GRUPO F
            cartver_F = cartoes_ver('F')
            cartver_tm1_F = cartver_F[0]
            cartver_tm2_F = cartver_F[1]
            cartver_tm3_F = cartver_F[2]
            cartver_tm4_F = cartver_F[3]
            #GRUPO G
            cartver_G = cartoes_ver('G')
            cartver_tm1_G = cartver_G[0]
            cartver_tm2_G = cartver_G[1]
            cartver_tm3_G = cartver_G[2]
            cartver_tm4_G = cartver_G[3]
            #GRUPO H
            cartver_H = cartoes_ver('H')
            cartver_tm1_H = cartver_H[0]
            cartver_tm2_H = cartver_H[1]
            cartver_tm3_H = cartver_H[2]
            cartver_tm4_H = cartver_H[3]

            #CALCULOS E VERIFICAÇÕES DO 1° E 2° LUGAR DE CADA GRUPO
            with open('grupos.json', 'r') as json_file:
                grupos = json.load(json_file)
            lugar1_A = lugar1_desempate(lugar1_A, seleção1, seleção2, seleção3, seleção4,'A', saldogols_tm1_A, saldogols_tm2_A, saldogols_tm3_A, saldogols_tm4_A, cartama_tm1_A, cartama_tm2_A, cartama_tm3_A, cartama_tm4_A, cartver_tm1_A, cartver_tm2_A, cartver_tm3_A, cartver_tm4_A)
            lugar2_A = lugar2_desempate(lugar2_A, seleção1, seleção2, seleção3, seleção4,'A', saldogols_tm1_A, saldogols_tm2_A, saldogols_tm3_A, saldogols_tm4_A, cartama_tm1_A, cartama_tm2_A, cartama_tm3_A, cartama_tm4_A, cartver_tm1_A, cartver_tm2_A, cartver_tm3_A, cartver_tm4_A)
            
            lugar1_B = lugar1_desempate(lugar1_B, seleção5, seleção6, seleção7, seleção8,'B', saldogols_tm1_B, saldogols_tm2_B, saldogols_tm3_B, saldogols_tm4_B, cartama_tm1_B, cartama_tm2_B, cartama_tm3_B, cartama_tm4_B, cartver_tm1_B, cartver_tm2_B, cartver_tm3_B, cartver_tm4_B)
            lugar2_B = lugar2_desempate(lugar2_B, seleção5, seleção6, seleção7, seleção8,'B', saldogols_tm1_B, saldogols_tm2_B, saldogols_tm3_B, saldogols_tm4_B, cartama_tm1_B, cartama_tm2_B, cartama_tm3_B, cartama_tm4_B, cartver_tm1_B, cartver_tm2_B, cartver_tm3_B, cartver_tm4_B)

            lugar1_C = lugar1_desempate(lugar1_C, seleção9, seleção10, seleção10, seleção12,'C', saldogols_tm1_C, saldogols_tm2_C, saldogols_tm3_C, saldogols_tm4_C, cartama_tm1_C, cartama_tm2_C, cartama_tm3_C, cartama_tm4_C, cartver_tm1_C, cartver_tm2_C, cartver_tm3_C, cartver_tm4_C)
            lugar2_C = lugar2_desempate(lugar2_C, seleção9, seleção10, seleção11, seleção12,'C', saldogols_tm1_C, saldogols_tm2_C, saldogols_tm3_C, saldogols_tm4_C, cartama_tm1_C, cartama_tm2_C, cartama_tm3_C, cartama_tm4_C, cartver_tm1_C, cartver_tm2_C, cartver_tm3_C, cartver_tm4_C)

            lugar1_D = lugar1_desempate(lugar1_D, seleção13, seleção14, seleção15, seleção16,'D', saldogols_tm1_D, saldogols_tm2_D, saldogols_tm3_D, saldogols_tm4_D, cartama_tm1_D, cartama_tm2_D, cartama_tm3_D, cartama_tm4_D, cartver_tm1_D, cartver_tm2_D, cartver_tm3_D, cartver_tm4_D)
            lugar2_D = lugar2_desempate(lugar2_D, seleção13, seleção14, seleção15, seleção16,'D', saldogols_tm1_D, saldogols_tm2_D, saldogols_tm3_D, saldogols_tm4_D, cartama_tm1_D, cartama_tm2_D, cartama_tm3_D, cartama_tm4_D, cartver_tm1_D, cartver_tm2_D, cartver_tm3_D, cartver_tm4_D)

            lugar1_E = lugar1_desempate(lugar1_E, seleção17, seleção18, seleção19, seleção20,'E', saldogols_tm1_E, saldogols_tm2_E, saldogols_tm3_E, saldogols_tm4_E, cartama_tm1_E, cartama_tm2_E, cartama_tm3_E, cartama_tm4_E, cartver_tm1_E, cartver_tm2_E, cartver_tm3_E, cartver_tm4_E)
            lugar2_E = lugar2_desempate(lugar2_E, seleção17, seleção18, seleção19, seleção20,'E', saldogols_tm1_E, saldogols_tm2_E, saldogols_tm3_E, saldogols_tm4_E, cartama_tm1_E, cartama_tm2_E, cartama_tm3_E, cartama_tm4_E, cartver_tm1_E, cartver_tm2_E, cartver_tm3_E, cartver_tm4_E)

            lugar1_F = lugar1_desempate(lugar1_F, seleção21, seleção22, seleção23, seleção24,'F', saldogols_tm1_F, saldogols_tm2_F, saldogols_tm3_F, saldogols_tm4_F, cartama_tm1_F, cartama_tm2_F, cartama_tm3_F, cartama_tm4_F, cartver_tm1_F, cartver_tm2_F, cartver_tm3_F, cartver_tm4_F)
            lugar2_F = lugar2_desempate(lugar2_F, seleção21, seleção22, seleção23, seleção24,'F', saldogols_tm1_F, saldogols_tm2_F, saldogols_tm3_F, saldogols_tm4_F, cartama_tm1_F, cartama_tm2_F, cartama_tm3_F, cartama_tm4_F, cartver_tm1_F, cartver_tm2_F, cartver_tm3_F, cartver_tm4_F)

            lugar1_G = lugar1_desempate(lugar1_G, seleção25, seleção26, seleção27, seleção28,'G', saldogols_tm1_G, saldogols_tm2_G, saldogols_tm3_G, saldogols_tm4_G, cartama_tm1_G, cartama_tm2_G, cartama_tm3_G, cartama_tm4_G, cartver_tm1_G, cartver_tm2_G, cartver_tm3_G, cartver_tm4_G)
            lugar2_G = lugar2_desempate(lugar2_G, seleção25, seleção2, seleção27, seleção28,'G', saldogols_tm1_G, saldogols_tm2_G, saldogols_tm3_G, saldogols_tm4_G, cartama_tm1_G, cartama_tm2_G, cartama_tm3_G, cartama_tm4_G, cartver_tm1_G, cartver_tm2_G, cartver_tm3_G, cartver_tm4_G)

            lugar1_H = lugar1_desempate(lugar1_H, seleção29, seleção30, seleção31, seleção32,'H', saldogols_tm1_H, saldogols_tm2_H, saldogols_tm3_H, saldogols_tm4_H, cartama_tm1_H, cartama_tm2_H, cartama_tm3_H, cartama_tm4_H, cartver_tm1_H, cartver_tm2_H, cartver_tm3_H, cartver_tm4_H)
            lugar2_H = lugar2_desempate(lugar2_H, seleção29, seleção30, seleção31, seleção32,'H', saldogols_tm1_H, saldogols_tm2_H, saldogols_tm3_H, saldogols_tm4_H, cartama_tm1_H, cartama_tm2_H, cartama_tm3_H, cartama_tm4_H, cartver_tm1_H, cartver_tm2_H, cartver_tm3_H, cartver_tm4_H)
            oitavas = True
        except:
            print('VOCÊ NÃO CADASTROU TODOS OS GRUPOS E CONFRONTOS')
        
        #SAIDA DAS OITAVAS
        if oitavas == True:
            print('-=-='*20)
            print('OITAVAS DE FINAL DA COPA DO MUNDO:')
            print()
            print(f'{lugar1_A} X {lugar2_B} -> SÁBADO, 03/12/2022 - 12:00 - Estádio Internacional Khalifa')
            print()
            print(f'{lugar1_B} X {lugar2_A} -> DOMINGO, 04/12/2022 - 16:00 - AL BAYT STADIUM')
            print()
            print(f'{lugar1_C} X {lugar2_D} -> SÁBADO, 03/12/2022 - 16:00 - AHMED BIN ALI STADIUM')
            print()
            print(f'{lugar1_D} X {lugar2_C} -> DOMINGO, 04/12/2022 - 12:00 - AL THUMAMA STADIUM')
            print()
            print(f'{lugar1_E} X {lugar2_F} -> SEGUNDA, 05/12/2022 - 12:00 - AL JANOUB STADIUM')
            print()
            print(f'{lugar1_F} X {lugar2_E} -> TERÇA, 06/12/2022 - 12:00 - ESTÁDIO DA CIDADE DA EDUCAÇÃO')
            print()
            print(f'{lugar1_G} X {lugar2_H} -> SEGUNDA, 05/12/2022 - 16:00 - STADIUM 974 - RAS ABU ABOUD')
            print()
            print(f'{lugar1_H} X {lugar2_G} -> TERÇA, 06/12/2022 - 16:00 - LUSAIL STADIUM')
            print('-=-='*20)
            print()
            #SAIDA DA MEDIA DE GOLS GERAL E POR GRUPO
            print('DESEJA VERIFICAR A MEDIA DE GOLS GERAL E MEDIA DE GOLS POR GRUPO? [S/N]: ')
            opc = input('QUAL SUA OPÇÃO?')
            if opc == 'S' or opc == 's':
                #GRUPO A
                gols_sele_A = gols_por_sele('A')
                gols_tm1_A = gols_sele_A[0]
                gols_tm2_A = gols_sele_A[1]
                gols_tm3_A = gols_sele_A[2]
                gols_tm4_A = gols_sele_A[3]
                #GRUPO B
                gols_sele_B = gols_por_sele('B')
                gols_tm1_B = gols_sele_B[0]
                gols_tm2_B = gols_sele_B[1]
                gols_tm3_B = gols_sele_B[2]
                gols_tm4_B = gols_sele_B[3]
                #GRUPO C
                gols_sele_C = gols_por_sele('C')
                gols_tm1_C = gols_sele_C[0]
                gols_tm2_C = gols_sele_C[1]
                gols_tm3_C = gols_sele_C[2]
                gols_tm4_C = gols_sele_C[3]
                #GRUPO D
                gols_sele_D = gols_por_sele('D')
                gols_tm1_D = gols_sele_D[0]
                gols_tm2_D = gols_sele_D[1]
                gols_tm3_D = gols_sele_D[2]
                gols_tm4_D = gols_sele_D[3]
                #GRUPO E
                gols_sele_E = gols_por_sele('E')
                gols_tm1_E = gols_sele_E[0]
                gols_tm2_E = gols_sele_E[1]
                gols_tm3_E = gols_sele_E[2]
                gols_tm4_E = gols_sele_E[3]
                #GRUPO F
                gols_sele_F = gols_por_sele('F')
                gols_tm1_F = gols_sele_F[0]
                gols_tm2_F = gols_sele_F[1]
                gols_tm3_F = gols_sele_F[2]
                gols_tm4_F = gols_sele_F[3]
                #GRUPO G
                gols_sele_G = gols_por_sele('G')
                gols_tm1_G = gols_sele_G[0]
                gols_tm2_G = gols_sele_G[1]
                gols_tm3_G = gols_sele_G[2]
                gols_tm4_G = gols_sele_G[3]
                #GRUPO G
                gols_sele_H = gols_por_sele('H')
                gols_tm1_H = gols_sele_H[0]
                gols_tm2_H = gols_sele_H[1]
                gols_tm3_H = gols_sele_H[2]
                gols_tm4_H = gols_sele_H[3]

                #CALCULO DA MEDIA TOTAL
                soma_tot = gols_tm1_A + gols_tm2_A + gols_tm3_A + gols_tm4_A + gols_tm1_B + gols_tm2_B + gols_tm3_B + gols_tm4_B + gols_tm1_C + gols_tm2_C + gols_tm3_C + gols_tm4_C + gols_tm1_D + gols_tm2_D + gols_tm3_D + gols_tm4_D + gols_tm1_E +gols_tm2_E + gols_tm3_E + gols_tm4_E + gols_tm1_F + gols_tm2_F + gols_tm3_F + gols_tm4_F + gols_tm1_G + gols_tm2_G + gols_tm3_G + gols_tm4_G + gols_tm1_H + gols_tm2_H + gols_tm3_H + gols_tm4_H 
                media_fase1 = soma_tot//32

                #CALCULO DA MEDIA POR GRUPO
                #GRUPO A
                soma_grupoA = gols_tm1_A + gols_tm2_A + gols_tm3_A + gols_tm4_A
                media_grupoA = soma_grupoA//4
                #GRUPO B
                soma_grupoB = gols_tm1_B + gols_tm2_B + gols_tm3_B + gols_tm4_B
                media_grupoB = soma_grupoB//4 
                #GRUPO C
                soma_grupoC = gols_tm1_C + gols_tm2_C + gols_tm3_C + gols_tm4_C
                media_grupoC = soma_grupoC//4 
                #GRUPO D
                soma_grupoD = gols_tm1_D + gols_tm2_D + gols_tm3_D + gols_tm4_D 
                media_grupoD = soma_grupoD//4
                #GRUPO E
                soma_grupoE = gols_tm1_E + gols_tm2_E + gols_tm3_E + gols_tm4_E
                media_grupoE = soma_grupoE//4
                #GRUPO F
                soma_grupoF = gols_tm1_F + gols_tm2_F + gols_tm3_F + gols_tm4_F
                media_grupoF = soma_grupoF//4
                #GRUPO G
                soma_grupoG = gols_tm1_G + gols_tm2_G + gols_tm3_G + gols_tm4_G
                media_grupoG = soma_grupoG//4
                #GRUPO H
                soma_grupoH = gols_tm1_H + gols_tm2_H + gols_tm3_H + gols_tm4_H
                media_grupoH = soma_grupoH//4

                print()
                print('-=-='*20)
                print(F'A MEDIA GERAL DE GOLS DA FASE 1 FOI DE: {media_fase1} GOLS POR PARTIDA')
                print()
                print(f'A MEDIA DE GOLS POR GRUPO FOI DE:\nGrupo A = {media_grupoA} \nGrupo B = {media_grupoB}\nGrupo C = {media_grupoC} \nGrupo D = {media_grupoD} \nGrupo E = {media_grupoE} \nGrupo F = {media_grupoF} \nGrupo G = {media_grupoG} \nGrupo H = {media_grupoH}')
                print()
    #FINAL DO PROGRAMA
    if int(opção) == 4:
        print('Encerrando...')








