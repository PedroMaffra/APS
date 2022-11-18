print ("Escolha o número do tipo de emissão de carbono que deseja calcular")
mod =['1-Pessoal','2-Casa','3-Combustível','4-Empresa','5-Crédito de carbono']
for nome in mod: print(nome)
c =int(input("Digite o número de sua escolha: "))

if (c>5) or (c<1):
      print ("valor inválido")
if (c==1):
   print ("Emissão por Respiração") 
   ida=int(input("Digite sua idade: "))
   if (ida<123):
     print (f"Você emitiu aproximadamente {int(ida*440)} kg de CO2 apenas respirando!")
   else: 
     print (f"Você quebrou o recorde do Guinness World Records Books, mas você emitiu aproximadamente {int(ida*440)} kg de CO2 apenas respirando!")
if (c==2):
          print ("Consumo elétrico de Sua casa") 
          con=float(input("Digite a quantidade de KWh/mês (média 100 KWh/mês) : "))
          print (f"Você vai emitir {float(con*320/100)} kg de CO2!")
     
elif (c==3):
  print ("Escolha o tipo de combustível que deseja")
  mod3 =['1-Gasolina','2-Diesel']
  for nome in mod3: print(nome)
  cl=int(input("Digite qual combustível: "))
  if (c==3 and cl==1): 
      gas=float(input("Digite a quantidade de litros: "))
      print (f"Você vai emitir {float(gas*0.82*0.75*3.7)} kg de CO2!")
  elif (c==3 and cl==2): 
          dis=float(input("Digite a quantidade de litros: "))
          print (f"Você vai emitir {float(dis*3.2)} kg de CO2!")
  else:
      print ("valor inválido")

elif (c==4):
  print ("Escolha o setor de sua empresa")
  mod4 =['1-Administração','2-Artes e Design','3-Ciências Exatas e Informática','4-Ciências Sociais e Humanas','5-Comunicação e Informação','6-Engenharias','7-Meio Ambiente','8-Saúde e Bem-estar']
  for nome in mod4: print(nome)
  emp=int(input("Digite o setor: "))
  if (c==4 and emp==1):
    fun1=int(input("Quantos funcionários sua empresa tem? "))
    gast1=float(input("Qual consumo de combustível da sua empresa? (em litros) "))
    ener1=float(input("Quanto é o consumo de energia elétrica em KWh/mês? "))
    print (f"Sua empresa vai emitir {float(gast1*3.2)+(ener1*320/100)+(fun1*3.667)} kg de CO2 no mês!")
  elif (c==4 and emp==2):
    fun2=int(input("Quantos funcionários sua empresa tem? "))
    gast2=float(input("Qual consumo de combustível da sua empresa? (em litros) "))
    ener2=float(input("Quanto é o consumo de energia elétrica em KWh/mês? "))
    print (f"Sua empresa vai emitir {float(gast2*3.2)+(ener2*320/100)+(fun2*3.667)} kg de CO2 no mês!")
  elif (c==4 and emp==3):
    fun3=int(input("Quantos funcionários sua empresa tem? "))
    gast3=float(input("Qual consumo de combustível da sua empresa? (em litros) "))
    ener3=float(input("Quanto é o consumo de energia elétrica em KWh/mês? "))
    print (f"Sua empresa vai emitir {float(gast3*3.2)+(ener3*320/100)+(fun3*3.667)} kg de CO2 no mês!")
  elif (c==4 and emp==4):
    fun4=int(input("Quantos funcionários sua empresa tem? "))
    gast4=float(input("Qual consumo de combustível da sua empresa? (em litros) "))
    ener4=float(input("Quanto é o consumo de energia elétrica em KWh/mês? "))
    print (f"Sua empresa vai emitir {float(gast4*3.2)+(ener4*320/100)+(fun4*3.667)} kg de CO2 no mês!")
  elif (c==4 and emp==5):
    fun5=int(input("Quantos funcionários sua empresa tem? "))
    gast5=float(input("Qual consumo de combustível da sua empresa? (em litros) "))
    ener5=float(input("Quanto é o consumo de energia elétrica em KWh/mês? "))
    print (f"Sua empresa vai emitir {float(gast5*3.2)+(ener5*320/100)+(fun5*3.667)} kg de CO2 no mês!")
  elif (c==4 and emp==6):
    fun6=int(input("Quantos funcionários sua empresa tem? "))
    gast6=float(input("Qual consumo de combustível da sua empresa? (em litros) "))
    ener6=float(input("Quanto é o consumo de energia elétrica em KWh/mês? "))
    print (f"Sua empresa vai emitir {float(gast6*3.2)+(ener6*320/100)+(fun6*3.667)} kg de CO2 no mês!")
  elif (c==4 and emp==7):
    fun7=int(input("Quantos funcionários sua empresa tem? "))
    gast7=float(input("Qual consumo de combustível da sua empresa? (em litros) "))
    ener7=float(input("Quanto é o consumo de energia elétrica em KWh/mês? "))
    print (f"Sua empresa vai emitir {float(gast7*3.2)+(ener7*320/100)+(fun7*3.667)} kg de CO2 no mês!")
  elif (c==4 and emp==8):
    fun8=int(input("Quantos funcionários sua empresa tem? "))
    gast8=float(input("Qual consumo de combustível da sua empresa? (em litros) "))
    ener8=float(input("Quanto é o consumo de energia elétrica em KWh/mês? "))
    print (f"Sua empresa vai emitir {float(gast8*3.2)+(ener8*320/100)+(fun8*3.667)} kg de CO2 no mês!")
  else:
      print ("valor inválido")
if (c==5):
    cre= float(input("Quantos kgs de CO2 foram deixados de poluir a atmosfera através da sua empresa? "))
    print (f"Sua empresa vai acumular {float(cre/1000)} em crédito de carbono")
    print (f"Esse valor pode ser precificado no mercado financeiro para venda entre {float(cre/1000*57)} e {float(cre/1000*99)} dólares em lucro dos excedentes dos créditos gerados.")
