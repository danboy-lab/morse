import winsound

def codificar():
	texto = input('Texto para morse -> ')
	texto = texto.lower()
	texto = texto.replace(" ", " / ")
	texto = texto.replace("a", " .-")
	texto = texto.replace("b", " -...")
	texto = texto.replace("c", " -.-.")
	texto = texto.replace("d", " -..")
	texto = texto.replace("e", " .")
	texto = texto.replace("f", " ..-.")
	texto = texto.replace("g", " --.")
	texto = texto.replace("h", " ....")
	texto = texto.replace("i", " ..")
	texto = texto.replace("j", " .---")
	texto = texto.replace("k", " -.-")
	texto = texto.replace("l", " .-..")
	texto = texto.replace("m", " --")
	texto = texto.replace("n", " -.")
	texto = texto.replace("o", " ---")
	texto = texto.replace("p", " .--.")
	texto = texto.replace("q", " --.-")
	texto = texto.replace("r", " .-.")
	texto = texto.replace("s", " ...")
	texto = texto.replace("t", " -")
	texto = texto.replace("u", " ..-")
	texto = texto.replace("v", " ...-")
	texto = texto.replace("w", ".--")
	texto = texto.replace("x", " -..-")
	texto = texto.replace("y", " -.--")
	texto = texto.replace("z", " --..")
	texto = texto.strip()
	print(texto)
	z = len(texto)
	c = 0
	while c < z:
		if texto[c] == ".":
			frequency = 2500  # Set Frequency To 2500 Hertz
			duration = 500  # Set Duration To 1000 ms == 1 second
			winsound.Beep(frequency, duration)
			c+=1
		elif texto[c] == "-":
			frequency = 2500  # Set Frequency To 2500 Hertz
			duration = 1000  # Set Duration To 1000 ms == 1 second
			winsound.Beep(frequency, duration)
			c+=1
		else:
			frequency = 32767  # Set Frequency To 2500 Hertz
			duration = 0  # Set Duration To 1000 ms == 1 second
			winsound.Beep(frequency, duration)
			c+=1
def decodificar():
	texto = input('Texto para morse -> ')
	texto = texto.lower()
	texto = texto.replace(" .- ", "a")
	texto = texto.replace(" -... ", "b")
	texto = texto.replace(" -.-. ", "c")
	texto = texto.replace(" -.. ", "d")
	texto = texto.replace(" . ", "e")
	texto = texto.replace(" ..-. ", "f")
	texto = texto.replace(" --. ", "g")
	texto = texto.replace(" .... ", "h")
	texto = texto.replace(" .. ", "i")
	texto = texto.replace(" .--- ", "j")
	texto = texto.replace(" -.- ", "k")
	texto = texto.replace(" .-.. ", "l")
	texto = texto.replace(" -- ", "m")
	texto = texto.replace(" -. ", "n")
	texto = texto.replace(" --- ", "o")
	texto = texto.replace(" .--. ", "p")
	texto = texto.replace(" --.- ", "q")
	texto = texto.replace(" .-. ", "r")
	texto = texto.replace(" ... ", "s")
	texto = texto.replace(" - ", "t")
	texto = texto.replace(" ..- ", "u")
	texto = texto.replace(" ...- ", "v")
	texto = texto.replace(" .-- ", "w")
	texto = texto.replace(" -..- ", "x")
	texto = texto.replace(" -.-- ", "y")
	texto = texto.replace(" --.. ", "z")
	texto = texto.replace(" / ", " ")
	texto = texto.strip()
	print(texto)

x = int(input('Deseja codificar ou decodificar?\nCodificar = 1\nDecodificar = 2\n~> '))

if x == 1:
	codificar()
elif x == 2:
	print("Em breve!")
else:
	while x != 1 or 2:
		x = int(input('Deseja codificar ou decodificar?\nCodificar = 1\nDecodificar = 2\n~> '))
		if x == 1:
			codificar()
		elif x == 2:
			decodificar()
