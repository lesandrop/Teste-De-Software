
#Entrada: Recebe o vetor vet com pelo menos 
#	um valor numérico
#Retorno: Vetor normalizado em que o menor
#	valor é 0, o maior valor é 50 e os demais
#	estão proporcionalmente redefinidos dentro
# 	desse intervalo.

def normalize(vet):

	new_vet = []
	vet_max = my_max(vet)
	vet_min = min(vet)

	if(vet_max - vet_min)==0:
		for n in range(len(vet)):
			new_vet.append(50)
		return new_vet
	
	for n in range(len(vet)):
		a = vet[n] - vet_min
		b = vet_max - vet_min
		c = a/b*50
		new_vet.append(c)

	return new_vet

if __name__ == "__main__":
	print(normalize([1,1,1,1]))
	print(normalize([0,1,1,100]))
	print(normalize([1,2,3,4]))
	print(normalize([0]))