km = float(input('Quantos KM o carro percorreu? '))
di = int(input('Quantos dias ele foi alugado? '))
prkm = km * 0.15
prdi = di * 60
prtol = prkm + prdi
print('O preço a pagar pelo total de Kilometros percorridos e dias usados é de: R${:.2f}'.format(prtol))
