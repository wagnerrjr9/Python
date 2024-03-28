# Menu que vai aparecer sempre que chamarem a função opc_do_menu()
def opc_do_menu():
    print("1. Cadastrar Tarifas")
    print("2. Registrar Entrada de Veiculo")
    print("3. Registrar Saida de Veiculo")
    print("4. Gerar Relatório diario")
    print("5. Gerar Relatório por tipo de veiculo")
    print("6. Sair")
    opc = int(input("Digite uma opção entre 1 e 6: "))
    return opc
# Esse loop vai colocar como valor para opc oque vai retorna da função opc_do_menu e proseguir com o código
while True:
    #sempre que uma opção for terminada opc vai chamar novamente a função opc_do_menu e o usuario pode escolher outro opção/valor para opc e continuar o programa
    opc = opc_do_menu()
    
    if opc == 6:
        break
    if opc == 1:
        print("Coloque o valor fixo e adicional de cada veiculo.")
        carro_pequeno_3h = int(input("Valor fixo 3h carro pequeno: "))
        carro_pequeno_adicional = int(input("Valor horas adicional carro pequeno: "))
        carro_grande_3h = int(input("Valor fixo 3h carro grande: "))
        carro_grande_adicional = int(input("Valor horas adicional carro grande: "))
        moto_3h = int(input("Valor fixo 3h moto: "))
        moto_adicional = int(input("Valor horas adicional moto: "))
        
    elif opc == 2:
        print ("Coloque as infomaçoes do veiculo de entrada")
        tipo_veiculo = input("Digite o tipo de veículo (carro_pequeno, carro_grande, moto): ")
        placa =(input("Digite a placa do veiculo: "))
        from datetime import datetime
        data_hora_entrada_str = input("Digite a data e hora entrada veiculo nesse formato(AAAA-MM-DD HH:MM): ")
        data_hora_entrada = datetime.strptime(data_hora_entrada_str, "%Y-%m-%d %H:%M")
        print(f"Recibo de Entrada\nPlaca:{placa}\nTipo: {tipo_veiculo}\nData/Hora: {data_hora_entrada}")
       
    elif opc == 3:
        print ("Coloque as infomaçoes do veiculo de saida")
        tipo_veiculo = input("Digite o tipo de veículo (carro_pequeno, carro_grande, moto): ")
        placa =(input("Digite a placa do veiculo: "))
        from datetime import datetime
        data_hora_entrada_str = input("Digite a data e hora entrada veiculo nesse formato(AAAA-MM-DD HH:MM): ")
        data_hora_entrada = datetime.strptime(data_hora_entrada_str, "%Y-%m-%d %H:%M")
        data_hora_saida_str = input("Digite a data e hora de saida desse veiculo nesse formato(AAAA-MM-DD HH:MM): ")
        data_hora_saida = datetime.strptime(data_hora_saida_str, "%Y-%m-%d %H:%M")
        tempo_permanencia = data_hora_saida - data_hora_entrada
        horas = tempo_permanencia.seconds // 3600
        minutos = (tempo_permanencia.seconds % 3600) // 60
        if tipo_veiculo == "carro_pequeno":
            if tempo_permanencia <= 3:
                valor = carro_pequeno_3h
            else:
                horas_adicionais = tempo_permanencia - 3
                valor = carro_pequeno_3h + (horas_adicionais * carro_pequeno_adicional)
        elif tipo_veiculo == "carro_grande":
            if tempo_permanencia <= 3:
                valor = carro_grande_3h
            else:
                horas_adicionais = tempo_permanencia - 3
                valor = carro_grande_3h + (horas_adicionais * carro_grande_adicional)
        elif tipo_veiculo == "moto":
            if tempo_permanencia <= 3:
                valor = moto_3h
            else:
                horas_adicionais = tempo_permanencia - 3
                valor = moto_3h + (horas_adicionais * moto_adicional)
        else:
            print("Tipo de veículo inválido.")
        
    elif opc == 4:
        print("escreva as instruções para gerar o relatório")
        
    elif opc == 5:
        print("escreva as instruções para gerar o relatório por tipo")
    else:
        print("Número invalido")
        



