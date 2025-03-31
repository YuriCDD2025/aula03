Sport = int(input("Digite a quantidade de gol's do Sport na partida: "))
santa_cruz = int(input("Digite a quantidade de gol's do Santa na partida: "))
if Sport > santa_cruz:
    print(f"sport vence santa por {Sport}x{santa_cruz}")
elif Sport == santa_cruz:
    print(f"partida entre Sport e santa empata por {Sport}X{santa_cruz}")
else:
    print(f"Sport perde por {Sport}x{santa_cruz} ")