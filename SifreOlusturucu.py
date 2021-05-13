import time
import random
from datetime import datetime
def kaldir (kelime) :
	sesli = ['a' , 'e' , 'i' , 'o' , 'u']
	a = kelime[0]
	if a in sesli :
		for harf in kelime :
			if harf in sesli :
				kelime = kelime.replace(harf, "")
		kelime = a + kelime
		return kelime
	elif a not in sesli :
		for harf in kelime :
			if harf in sesli :
				kelime = kelime.replace(harf, "")
		return kelime
print(r"     _                          _       _               _____   _")
print(r"    / \     _   _   _   _   _  | |   __| |  _   ____   |_   _| (_)  _ __ ___  ")
print(r"   / _ \   | | | | | | | | | | | |  / _` | | | |_  /     | |   | | | '_ ` _ \ ")
print(r"  / ___ \  | |_| | | |_| | | | | | | (_| | | |  / /      | |   | | | | | | | |")
print(r" /_/   \_\ \___, | \___, | |_| |_|  \__,_| |_| /___|     |_|   |_| |_| |_| |_|")
print(r" 	    ___| |  ___| |	")
print(r"           |_____/ |_____/")       

print("\n\n[1]Bu araç Cyber1adam - Ayyıldız Tim tarafından yazılmıştır")
print("[2]Kullanım hakları yalnızca Ayyıldız Tim'e aittir")


print('''\n\nMaksimum performans için ;
(1) Türkçe karakter kullanmayın\n(Örnek : ı,ö,ü,ş)
(2) Sadece küçük karakterleri kullanın
(Örnek : a,b,c,d)
''')

while True :
	try :
		minimum = int(input('Oluşturulacak şifreler en az kaç haneli olsun : '))
		break
	except ValueError :
		print('Sayı dışında bir karakter girdiniz ')
while True :
	try :
		maksimum = int(input('Oluşturulacak şifreler en fazla kaç haneli olsun : '))
		while maksimum < minimum :
			print('Maksimum değer minimum değerden daha küçük olamaz ! ')
			maksimum = int(input('Oluşturulacak şifreler en fazla kaç haneli olsun : '))
		break
	except ValueError :
		print('Sayı dışında bir karakter girdiniz ')

ad = str(input('\nLütfen hedefin adını giriniz : ')).lower()
while ad == '' :
	print('\nHedefin adı gerekli bir bilgidir ! ')
	ad = str(input('\nLütfen hedefin adını giriniz : ')).lower() 
s_ad = kaldir(ad)

soyis = str(input('Lütfen hedefin soyadını giriniz : ')).lower()
while soyis == '' :
	print('\nHedefin soyadı gerekli bir bilgidir ! ')
	soyis = str(input('\nLütfen hedefin soyadını giriniz : ')).lower()
s_soyis = kaldir(soyis)

while True :
	try :
		pkodu = int(input('Lütfen hedefin yaşadığı şehrin plaka kodunu giriniz : '))
		if pkodu > 81 :
			print("Plaka kodu 81'den büyük olamaz ! ")
			continue
		if pkodu == 0 :
			print("Plaka kodu 0'a eşit olamaz ! ")
			continue
		break
	except ValueError :
		print('Sayı dışında bir karakter girdiniz ')
	
pkodu = str(pkodu)
t_pkodu = pkodu[::-1]

simdiki_yil = datetime.now().year
while True :
	try :
		dyili = int(input('Lütfen hedefin doğum yılını giriniz : '))
		if dyili > simdiki_yil :
			print('Doğum yılı mevcut yıldan daha büyük olamaz ! ')
			continue
		elif dyili < 1850 :
			print('Doğum yılı o kadar küçük olamaz ! ')
			continue
		break
	except ValueError :
		print('Sayı dışında bir karakter girdiniz ')
dyili = str(dyili)
t_dyili = dyili[::-1]

while True :
	try :
		dayi = int(input('Lütfen hedefin doğum ayını giriniz : '))
		if dayi > 12 :
			print("Doğum ayı 12'den büyük olamaz ! ")
			continue
		if dayi == 0 :
			print("Doğum ayı 0 olamaz ! ")
			continue
		break
	except ValueError :
		print('Sayı dışında bir karakter girdiniz ')
dayi = str(dayi)
if len(dayi) < 2 :
	dayi = '0' + dayi
while True :
	try :
		dgunu = int(input('Lütfen hedefin doğum gününü giriniz : '))
		sayili_dayi = int(dayi)
		if sayili_dayi == 2 :
			if dgunu > 29 :
				print('Şubat ayı en fazla 29 gün içerir ! ')
				continue
			elif dgunu == 0 :
				print("Doğum günü 0'a eşit olamaz ! ")
				continue
		elif sayili_dayi == 4 or sayili_dayi == 6 or sayili_dayi == 9 or sayili_dayi == 11 :
			if dgunu > 30 :
				print('Seçtiğiniz ay 30 gün içeriyor ! ')
				continue
			elif dgunu == 0 :
				print("Doğum günü 0'a eşit olamaz ! ")
				continue
		else :
			if dgunu > 31 :
				print('Seçtiğiniz ay 31 gün içeriyor ! ')
				continue
			elif dgunu == 0 :
				print("Doğum günü 0'a eşit olamaz ! ")
				continue
		break
	except ValueError :
		print('Sayı dışında bir karakter girdiniz ')
dgunu = str(dgunu)
if len(dgunu) < 2 :
	dgunu = '0' + dgunu
daygun = dayi + dgunu 
t_daygun = daygun[::-1]

dtarihi = dgunu + dayi + dyili
t_dtarihi = dtarihi [::-1]


son = []

sifreler = [ad + ad, 												ad + '_' + ad,
			ad + soyis,												ad + '_' + soyis,
			soyis + ad,												soyis + '_' + ad,
			soyis + soyis,											soyis + '_' + soyis,
			
			ad.upper() + ad,										ad.upper() + '_' + ad,
			ad.upper() + ad.upper(),								ad.upper() + '_' + ad.upper(),
			ad.upper() + ad.title(),								ad.upper() + '_' + ad.title(),
			ad.upper() + soyis,										ad.upper() + '_' + soyis,
			ad.upper() + soyis.upper(),								ad.upper() + '_' + soyis.upper(),
			ad.upper() + soyis.title(),								ad.upper() + '_' + soyis.title(),
			ad.title() + ad,										ad.title() + '_' + ad,
			ad.title() + ad.upper(),								ad.title() + '_' + ad.upper(),
			ad.title() + ad.title(),								ad.title() + '_' + ad.title(),
			ad.title() + soyis,										ad.title() + '_' + soyis,
			ad.title() + soyis.upper(),								ad.title() + '_' + soyis.upper(),
			ad.title() + soyis.title(),								ad.title() + '_' + soyis.title(),
			
			soyis.upper() + ad,										soyis.upper() + '_' + ad,
			soyis.upper() + ad.upper(),								soyis.upper() + '_' + ad.upper(),
			soyis.upper() + ad.title(),								soyis.upper() + '_' + ad.title(),
			soyis.upper() + soyis,									soyis.upper() + '_' + soyis,
			soyis.upper() + soyis.upper(),							soyis.upper() + '_' + soyis.upper(),
			soyis.upper() + soyis.title(),							soyis.upper() + '_' + soyis.title(),
			soyis.title() + ad,										soyis.title() + '_' + ad,
			soyis.title() + ad.upper(),								soyis.title() + '_' + ad.upper(),
			soyis.title() + ad.title(),								soyis.title() + '_' + ad.title(),
			soyis.title() + soyis,									soyis.title() + '_' + soyis,
			soyis.title() + soyis.upper(),							soyis.title() + '_' + soyis.upper(),
			soyis.title() + soyis.title(),							soyis.title() + '_' + soyis.title(),
			
			#######################################################################################################

			ad + pkodu,												ad + '_' + pkodu,										
			ad + pkodu + pkodu,   									ad + '_' + pkodu + pkodu, 
			ad + pkodu + t_pkodu,									ad + '_' + pkodu + t_pkodu,
			ad + t_pkodu,											ad + '_' + t_pkodu,
			ad + t_pkodu + pkodu,									ad + '_' + t_pkodu + pkodu,
			ad + t_pkodu + t_pkodu,									ad + '_' + t_pkodu + t_pkodu,

			soyis + pkodu,											soyis + '_' + pkodu,
			soyis + pkodu + pkodu,									soyis + '_' + pkodu + pkodu,
			soyis + pkodu + t_pkodu,								soyis + '_' + pkodu + t_pkodu,
			soyis + t_pkodu,										soyis + '_' + t_pkodu,
			soyis + t_pkodu + pkodu,								soyis + '_' + t_pkodu + pkodu,
			soyis + t_pkodu + t_pkodu,								soyis + '_' + t_pkodu + t_pkodu,

			ad + ad + pkodu,										ad + '_' + ad + pkodu, ad + '_' + ad + '_' + pkodu, ad + ad + '_' + pkodu,
			ad + soyis + pkodu, 									ad + '_' + soyis + pkodu, ad + '_' + soyis + '_' + pkodu, ad + soyis + '_' + pkodu,
			soyis + ad + pkodu,										soyis + '_' + ad + pkodu, soyis + '_' + ad + '_' + pkodu, soyis + ad + '_' + pkodu,
			soyis + soyis + pkodu,									soyis + '_' + soyis + pkodu, soyis + '_' + soyis + '_' + pkodu, soyis + soyis + '_' + pkodu,
			
			ad + ad + pkodu + pkodu,								ad + '_' + ad + pkodu + pkodu, ad + '_' + ad + '_' + pkodu + pkodu, ad + ad + '_' + pkodu + pkodu,
			ad + soyis + pkodu + pkodu,								ad + '_' + soyis + pkodu + pkodu, ad + '_' + soyis + '_' + pkodu + pkodu, ad + soyis + '_' + pkodu + pkodu,
			soyis + ad + pkodu + pkodu,								soyis + '_' + ad + pkodu + pkodu, soyis + '_' + ad + '_' + pkodu + pkodu, soyis + ad + '_' + pkodu + pkodu,
			soyis + soyis + pkodu + pkodu,							soyis + '_' + soyis + pkodu + pkodu, soyis + '_' + soyis + '_' + pkodu + pkodu, soyis + soyis + '_' + pkodu + pkodu,
			
			ad + ad + pkodu + t_pkodu,								ad + '_' + ad + pkodu + t_pkodu, ad + '_' + ad + '_' + pkodu + t_pkodu, ad + ad + '_' + pkodu + t_pkodu,
			ad + soyis + pkodu + t_pkodu,							ad + '_' + soyis + pkodu + t_pkodu, ad + '_' + soyis + '_' + pkodu + t_pkodu, ad + soyis + '_' + pkodu + t_pkodu,
			soyis + ad + pkodu + t_pkodu,							soyis + '_' + ad + pkodu + t_pkodu, soyis + '_' + ad + '_' + pkodu + t_pkodu, soyis + ad + '_' + pkodu + t_pkodu,
			soyis + soyis + pkodu + t_pkodu,						soyis + '_' + soyis + pkodu + t_pkodu, soyis + '_' + soyis + '_' + pkodu + t_pkodu, soyis + soyis + '_' + pkodu + t_pkodu,
			
			ad + ad + t_pkodu,										ad + '_' + ad + t_pkodu, ad + '_' + ad + '_' + t_pkodu, ad + ad + '_' + t_pkodu,
			ad + soyis + t_pkodu, 									ad + '_' + soyis + t_pkodu, ad + '_' + soyis + '_' + t_pkodu, ad + soyis + '_' + t_pkodu,
			soyis + ad + t_pkodu,									soyis + '_' + ad + t_pkodu, soyis + '_' + ad + '_' + t_pkodu, soyis + ad + '_' + t_pkodu,
			soyis + soyis + t_pkodu,								soyis + '_' + soyis + t_pkodu, soyis + '_' + soyis + '_' + t_pkodu, soyis + soyis + '_' + t_pkodu,

			ad + ad + t_pkodu + pkodu,								ad + '_' + ad + t_pkodu + pkodu, ad + '_' + ad + '_' + t_pkodu + pkodu, ad + ad + '_' + t_pkodu + pkodu,
			ad + soyis + t_pkodu + pkodu,							ad + '_' + soyis + t_pkodu + pkodu, ad + '_' + soyis + '_' + t_pkodu + pkodu, ad + soyis + '_' + t_pkodu + pkodu,
			soyis + ad + t_pkodu + pkodu,							soyis + '_' + ad + t_pkodu + pkodu, soyis + '_' + ad + '_' + t_pkodu + pkodu, soyis + ad + '_' + t_pkodu + pkodu,
			soyis + soyis + t_pkodu + pkodu,						soyis + '_' + soyis + t_pkodu + pkodu, soyis + '_' + soyis + '_' + t_pkodu + pkodu, soyis + soyis + '_' + t_pkodu + pkodu,

			ad + ad + t_pkodu + t_pkodu,							ad + '_' + ad + t_pkodu + t_pkodu, ad + '_' + ad + '_' + t_pkodu + t_pkodu, ad + ad + '_' + t_pkodu + t_pkodu,
			ad + soyis + t_pkodu + t_pkodu,							ad + '_' + soyis + t_pkodu + t_pkodu, ad + '_' + soyis + '_' + t_pkodu + t_pkodu, ad + soyis + '_' + t_pkodu + t_pkodu,
			soyis + ad + t_pkodu + t_pkodu,							soyis + '_' + ad + t_pkodu + t_pkodu, soyis + '_' + ad + '_' + t_pkodu + t_pkodu, soyis + ad + '_' + t_pkodu + t_pkodu,
			soyis + soyis + t_pkodu + t_pkodu,						soyis + '_' + soyis + t_pkodu + t_pkodu, soyis + '_' + soyis + '_' + t_pkodu + t_pkodu, soyis + soyis + '_' + t_pkodu + t_pkodu,
			
			#######################################################################################################################################################

			ad.upper() + pkodu,										ad.upper() + '_' + pkodu,										
			ad.upper() + pkodu + pkodu,   							ad.upper() + '_' + pkodu + pkodu, 
			ad.upper() + pkodu + t_pkodu,							ad.upper() + '_' + pkodu + t_pkodu,
			ad.upper() + t_pkodu,									ad.upper() + '_' + t_pkodu,
			ad.upper() + t_pkodu + pkodu,							ad.upper() + '_' + t_pkodu + pkodu,
			ad.upper() + t_pkodu + t_pkodu,							ad.upper() + '_' + t_pkodu + t_pkodu,
			soyis.upper() + pkodu,									soyis.upper() + '_' + pkodu,
			soyis.upper() + pkodu + pkodu,							soyis.upper() + '_' + pkodu + pkodu,
			soyis.upper() + pkodu + t_pkodu,						soyis.upper() + '_' + pkodu + t_pkodu,
			soyis.upper() + t_pkodu,								soyis.upper() + '_' + t_pkodu,
			soyis.upper() + t_pkodu + pkodu,						soyis.upper() + '_' + t_pkodu + pkodu,
			soyis.upper() + t_pkodu + t_pkodu,						soyis.upper() + '_' + t_pkodu + t_pkodu,

			ad.title() + pkodu,										ad.title() + '_' + pkodu,										
			ad.title() + pkodu + pkodu,   							ad.title() + '_' + pkodu + pkodu, 
			ad.title() + pkodu + t_pkodu,							ad.title() + '_' + pkodu + t_pkodu,
			ad.title() + t_pkodu,									ad.title() + '_' + t_pkodu,
			ad.title() + t_pkodu + pkodu,							ad.title() + '_' + t_pkodu + pkodu,
			ad.title() + t_pkodu + t_pkodu,							ad.title() + '_' + t_pkodu + t_pkodu,
			soyis.title() + pkodu,									soyis.title() + '_' + pkodu,
			soyis.title() + pkodu + pkodu,							soyis.title() + '_' + pkodu + pkodu,
			soyis.title() + pkodu + t_pkodu,						soyis.title() + '_' + pkodu + t_pkodu,
			soyis.title() + t_pkodu,								soyis.title() + '_' + t_pkodu,
			soyis.title() + t_pkodu + pkodu,						soyis.title() + '_' + t_pkodu + pkodu,
			soyis.title() + t_pkodu + t_pkodu,						soyis.title() + '_' + t_pkodu + t_pkodu,

			ad.upper() + ad + pkodu,								ad.upper() + '_' + ad + pkodu, ad.upper() + '_' + ad + '_' + pkodu, ad.upper() + ad + '_' + pkodu,
			ad.upper() + ad.upper() + pkodu,						ad.upper() + '_' + ad.upper() + pkodu, ad.upper() + '_' + ad.upper() + '_' + pkodu, ad.upper() + ad.upper() + '_' + pkodu,
			ad.upper() + ad.title() + pkodu,						ad.upper() + '_' + ad.title() + pkodu, ad.upper() + '_' + ad.title() + '_' + pkodu, ad.upper() + ad.title() + '_' + pkodu,
			ad.upper() + soyis + pkodu,								ad.upper() + '_' + soyis + pkodu, ad.upper() + '_' + soyis + '_' + pkodu, ad.upper() + soyis + '_' + pkodu,
			ad.upper() + soyis.upper() + pkodu,						ad.upper() + '_' + soyis.upper() + pkodu, ad.upper() + '_' + soyis.upper() + '_' + pkodu, ad.upper() + soyis.upper() + '_' + pkodu,
			ad.upper() + soyis.title() + pkodu,						ad.upper() + '_' + soyis.title() + pkodu, ad.upper() + '_' + soyis.title() + '_' + pkodu, ad.upper() + soyis.title() + '_' + pkodu,
			ad.title() + ad + pkodu,								ad.title() + '_' + ad + pkodu, ad.title() + '_' + ad + '_' + pkodu, ad.title() + ad + '_' + pkodu,
			ad.title() + ad.upper() + pkodu,						ad.title() + '_' + ad.upper() + pkodu, ad.title() + '_' + ad.upper() + '_' + pkodu, ad.title() + ad.upper() + '_' + pkodu,
			ad.title() + ad.title() + pkodu,						ad.title() + '_' + ad.title() + pkodu, ad.title() + '_' + ad.title() + '_' + pkodu, ad.title() + ad.title() + '_' + pkodu,
			ad.title() + soyis + pkodu,								ad.title() + '_' + soyis + pkodu, ad.title() + '_' + soyis + '_' + pkodu, ad.title() + soyis + '_' + pkodu,
			ad.title() + soyis.upper() + pkodu,						ad.title() + '_' + soyis.upper() + pkodu, ad.title() + '_' + soyis.upper() + '_' + pkodu, ad.title() + soyis.upper() + '_' + pkodu,
			ad.title() + soyis.title() + pkodu,						ad.title() + '_' + soyis.title() + pkodu, ad.title() + '_' + soyis.title() + '_' + pkodu, ad.title() + soyis.title() + '_' + pkodu,

			ad.upper() + ad + pkodu + pkodu,						ad.upper() + '_' + ad + pkodu + pkodu, ad.upper() + '_' + ad + '_' + pkodu + pkodu, ad.upper() + ad + '_' + pkodu + pkodu,
			ad.upper() + ad.upper() + pkodu + pkodu,				ad.upper() + '_' + ad.upper() + pkodu + pkodu, ad.upper() + '_' + ad.upper() + '_' + pkodu + pkodu, ad.upper() + ad.upper() + '_' + pkodu + pkodu,
			ad.upper() + ad.title() + pkodu + pkodu,				ad.upper() + '_' + ad.title() + pkodu + pkodu, ad.upper() + '_' + ad.title() + '_' + pkodu + pkodu, ad.upper() + ad.title() + '_' + pkodu + pkodu,
			ad.upper() + soyis + pkodu + pkodu,						ad.upper() + '_' + soyis + pkodu + pkodu, ad.upper() + '_' + soyis + '_' + pkodu + pkodu, ad.upper() + soyis + '_' + pkodu + pkodu,
			ad.upper() + soyis.upper() + pkodu + pkodu,				ad.upper() + '_' + soyis.upper() + pkodu + pkodu, ad.upper() + '_' + soyis.upper() + '_' + pkodu + pkodu, ad.upper() + soyis.upper() + '_' + pkodu + pkodu,
			ad.upper() + soyis.title() + pkodu + pkodu,				ad.upper() + '_' + soyis.title() + pkodu + pkodu, ad.upper() + '_' + soyis.title() + '_' + pkodu + pkodu, ad.upper() + soyis.title() + '_' + pkodu + pkodu,
			ad.title() + ad + pkodu + pkodu,						ad.title() + '_' + ad + pkodu + pkodu, ad.title() + '_' + ad + '_' + pkodu + pkodu, ad.title() + ad + '_' + pkodu + pkodu,
			ad.title() + ad.upper() + pkodu + pkodu,				ad.title() + '_' + ad.upper() + pkodu + pkodu, ad.title() + '_' + ad.upper() + '_' + pkodu + pkodu, ad.title() + ad.upper() + '_' + pkodu + pkodu,
			ad.title() + ad.title() + pkodu + pkodu,				ad.title() + '_' + ad.title() + pkodu + pkodu, ad.title() + '_' + ad.title() + '_' + pkodu + pkodu, ad.title() + ad.title() + '_' + pkodu + pkodu,
			ad.title() + soyis + pkodu + pkodu,						ad.title() + '_' + soyis + pkodu + pkodu, ad.title() + '_' + soyis + '_' + pkodu + pkodu, ad.title() + soyis + '_' + pkodu + pkodu,
			ad.title() + soyis.upper() + pkodu + pkodu,				ad.title() + '_' + soyis.upper() + pkodu + pkodu, ad.title() + '_' + soyis.upper() + '_' + pkodu + pkodu, ad.title() + soyis.upper() + '_' + pkodu + pkodu,
			ad.title() + soyis.title() + pkodu + pkodu,				ad.title() + '_' + soyis.title() + pkodu + pkodu, ad.title() + '_' + soyis.title() + '_' + pkodu + pkodu, ad.title() + soyis.title() + '_' + pkodu + pkodu,
			
			ad.upper() + ad + pkodu + t_pkodu,						ad.upper() + '_' + ad + pkodu + t_pkodu, ad.upper() + '_' + ad + '_' + pkodu + t_pkodu, ad.upper() + ad + '_' + pkodu + t_pkodu,
			ad.upper() + ad.upper() + pkodu + t_pkodu,  			ad.upper() + '_' + ad.upper() + pkodu + t_pkodu, ad.upper() + '_' + ad.upper() + '_' + pkodu + t_pkodu, ad.upper() + ad.upper() + '_' + pkodu + t_pkodu,
			ad.upper() + ad.title() + pkodu + t_pkodu,				ad.upper() + '_' + ad.title() + pkodu + t_pkodu, ad.upper() + '_' + ad.title() + '_' + pkodu + t_pkodu, ad.upper() + ad.title() + '_' + pkodu + t_pkodu,
			ad.upper() + soyis + pkodu + t_pkodu,					ad.upper() + '_' + soyis + pkodu + t_pkodu, ad.upper() + '_' + soyis + '_' + pkodu + t_pkodu, ad.upper() + soyis + '_' + pkodu + t_pkodu,
			ad.upper() + soyis.upper() + pkodu + t_pkodu,			ad.upper() + '_' + soyis.upper() + pkodu + t_pkodu, ad.upper() + '_' + soyis.upper() + '_' + pkodu + t_pkodu, ad.upper() + soyis.upper() + '_' + pkodu + t_pkodu,
			ad.upper() + soyis.title() + pkodu + t_pkodu,			ad.upper() + '_' + soyis.title() + pkodu + t_pkodu, ad.upper() + '_' + soyis.title() + '_' + pkodu + t_pkodu, ad.upper() + soyis.title() + '_' + pkodu + t_pkodu,
			ad.title() + ad + pkodu + t_pkodu,						ad.title() + '_' + ad + pkodu + t_pkodu, ad.title() + '_' + ad + '_' + pkodu + t_pkodu, ad.title() + ad + '_' + pkodu + t_pkodu,
			ad.title() + ad.upper() + pkodu + t_pkodu,				ad.title() + '_' + ad.upper() + pkodu + t_pkodu, ad.title() + '_' + ad.upper() + '_' + pkodu + t_pkodu, ad.title() + ad.upper() + '_' + pkodu + t_pkodu,
			ad.title() + ad.title() + pkodu + t_pkodu,				ad.title() + '_' + ad.title() + pkodu + t_pkodu, ad.title() + '_' + ad.title() + '_' + pkodu + t_pkodu, ad.title() + ad.title() + '_' + pkodu + t_pkodu,
			ad.title() + soyis + pkodu + t_pkodu,					ad.title() + '_' + soyis + pkodu + t_pkodu, ad.title() + '_' + soyis + '_' + pkodu + t_pkodu, ad.title() + soyis + '_' + pkodu + t_pkodu,
			ad.title() + soyis.upper() + pkodu + t_pkodu,			ad.title() + '_' + soyis.upper() + pkodu + t_pkodu, ad.title() + '_' + soyis.upper() + '_' + pkodu + t_pkodu, ad.title() + soyis.upper() + '_' + pkodu + t_pkodu,
			ad.title() + soyis.title() + pkodu + t_pkodu,			ad.title() + '_' + soyis.title() + pkodu + t_pkodu, ad.title() + '_' + soyis.title() + '_' + pkodu + t_pkodu, ad.title() + soyis.title() + '_' + pkodu + t_pkodu,
			
			ad.upper() + ad + t_pkodu,								ad.upper() + '_' + ad + t_pkodu, ad.upper() + '_' + ad + '_' + t_pkodu, ad.upper() + ad + '_' + t_pkodu,
			ad.upper() + ad.upper() + t_pkodu,						ad.upper() + '_' + ad.upper() + t_pkodu, ad.upper() + '_' + ad.upper() + '_' + t_pkodu, ad.upper() + ad.upper() + '_' + t_pkodu,
			ad.upper() + ad.title() + t_pkodu,						ad.upper() + '_' + ad.title() + t_pkodu, ad.upper() + '_' + ad.title() + '_' + t_pkodu, ad.upper() + ad.title() + '_' + t_pkodu,
			ad.upper() + soyis + t_pkodu,							ad.upper() + '_' + soyis + t_pkodu, ad.upper() + '_' + soyis + '_' + t_pkodu, ad.upper() + soyis + '_' + t_pkodu,
			ad.upper() + soyis.upper() + t_pkodu,					ad.upper() + '_' + soyis.upper() + t_pkodu, ad.upper() + '_' + soyis.upper() + '_' + t_pkodu, ad.upper() + soyis.upper() + '_' + t_pkodu,
			ad.upper() + soyis.title() + t_pkodu,					ad.upper() + '_' + soyis.title() + t_pkodu, ad.upper() + '_' + soyis.title() + '_' + t_pkodu, ad.upper() + soyis.title() + '_' + t_pkodu,
			ad.title() + ad + t_pkodu,								ad.title() + '_' + ad + t_pkodu, ad.title() + '_' + ad + '_' + t_pkodu, ad.title() + ad + '_' + t_pkodu,
			ad.title() + ad.upper() + t_pkodu,						ad.title() + '_' + ad.upper() + t_pkodu, ad.title() + '_' + ad.upper() + '_' + t_pkodu, ad.title() + ad.upper() + '_' + t_pkodu,
			ad.title() + ad.title() + t_pkodu,						ad.title() + '_' + ad.title() + t_pkodu, ad.title() + '_' + ad.title() + '_' + t_pkodu, ad.title() + ad.title() + '_' + t_pkodu,
			ad.title() + soyis + t_pkodu,							ad.title() + '_' + soyis + t_pkodu, ad.title() + '_' + soyis + '_' + t_pkodu, ad.title() + soyis + '_' + t_pkodu,
			ad.title() + soyis.upper() + t_pkodu,					ad.title() + '_' + soyis.upper() + t_pkodu, ad.title() + '_' + soyis.upper() + '_' + t_pkodu, ad.title() + soyis.upper() + '_' + t_pkodu,
			ad.title() + soyis.title() + t_pkodu,					ad.title() + '_' + soyis.title() + t_pkodu, ad.title() + '_' + soyis.title() + '_' + t_pkodu, ad.title() + soyis.title() + '_' + t_pkodu,
			
			ad.upper() + ad + t_pkodu + pkodu,						ad.upper() + '_' + ad + t_pkodu + pkodu, ad.upper() + '_' + ad + '_' + t_pkodu + pkodu, ad.upper() + ad + '_' + t_pkodu + pkodu,
			ad.upper() + ad.upper() + t_pkodu + pkodu,				ad.upper() + '_' + ad.upper() + t_pkodu + pkodu, ad.upper() + '_' + ad.upper() + '_' + t_pkodu + pkodu, ad.upper() + ad.upper() + '_' + t_pkodu + pkodu,
			ad.upper() + ad.title() + t_pkodu + pkodu,				ad.upper() + '_' + ad.title() + t_pkodu + pkodu, ad.upper() + '_' + ad.title() + '_' + t_pkodu + pkodu, ad.upper() + ad.title() + '_' + t_pkodu + pkodu,
			ad.upper() + soyis + t_pkodu + pkodu,					ad.upper() + '_' + soyis + t_pkodu + pkodu, ad.upper() + '_' + soyis + '_' + t_pkodu + pkodu, ad.upper() + soyis + '_' + t_pkodu + pkodu,
			ad.upper() + soyis.upper() + t_pkodu + pkodu,			ad.upper() + '_' + soyis.upper() + t_pkodu + pkodu, ad.upper() + '_' + soyis.upper() + '_' + t_pkodu + pkodu, ad.upper() + soyis.upper() + '_' + t_pkodu + pkodu,
			ad.upper() + soyis.title() + t_pkodu + pkodu,			ad.upper() + '_' + soyis.title() + t_pkodu + pkodu, ad.upper() + '_' + soyis.title() + '_' + t_pkodu + pkodu, ad.upper() + soyis.title() + '_' + t_pkodu + pkodu,
			ad.title() + ad + t_pkodu + pkodu,						ad.title() + '_' + ad + t_pkodu + pkodu, ad.title() + '_' + ad + '_' + t_pkodu + pkodu, ad.title() + ad + '_' + t_pkodu + pkodu,
			ad.title() + ad.upper() + t_pkodu + pkodu,				ad.title() + '_' + ad.upper() + t_pkodu + pkodu, ad.title() + '_' + ad.upper() + '_' + t_pkodu + pkodu, ad.title() + ad.upper() + '_' + t_pkodu + pkodu,
			ad.title() + ad.title() + t_pkodu + pkodu,				ad.title() + '_' + ad.title() + t_pkodu + pkodu, ad.title() + '_' + ad.title() + '_' + t_pkodu + pkodu, ad.title() + ad.title() + '_' + t_pkodu + pkodu,
			ad.title() + soyis + t_pkodu + pkodu,					ad.title() + '_' + soyis + t_pkodu + pkodu, ad.title() + '_' + soyis + '_' + t_pkodu + pkodu, ad.title() + soyis + '_' + t_pkodu + pkodu,
			ad.title() + soyis.upper() + t_pkodu + pkodu,			ad.title() + '_' + soyis.upper() + t_pkodu + pkodu, ad.title() + '_' + soyis.upper() + '_' + t_pkodu + pkodu, ad.title() + soyis.upper() + '_' + t_pkodu + pkodu,
			ad.title() + soyis.title() + t_pkodu + pkodu,			ad.title() + '_' + soyis.title() + t_pkodu + pkodu, ad.title() + '_' + soyis.title() + '_' + t_pkodu + pkodu, ad.title() + soyis.title() + '_' + t_pkodu + pkodu,
			
			ad.upper() + ad + t_pkodu + t_pkodu,					ad.upper() + '_' + ad + t_pkodu + t_pkodu, ad.upper() + '_' + ad + '_' + t_pkodu + t_pkodu, ad.upper() + ad + '_' + t_pkodu + t_pkodu,
			ad.upper() + ad.upper() + t_pkodu + t_pkodu,			ad.upper() + '_' + ad.upper() + t_pkodu + t_pkodu, ad.upper() + '_' + ad.upper() + '_' + t_pkodu + t_pkodu, ad.upper() + ad.upper() + '_' + t_pkodu + t_pkodu,
			ad.upper() + ad.title() + t_pkodu + t_pkodu,			ad.upper() + '_' + ad.title() + t_pkodu + t_pkodu, ad.upper() + '_' + ad.title() + '_' + t_pkodu + t_pkodu, ad.upper() + ad.title() + '_' + t_pkodu + t_pkodu,
			ad.upper() + soyis + t_pkodu + t_pkodu,					ad.upper() + '_' + soyis + t_pkodu + t_pkodu, ad.upper() + '_' + soyis + '_' + t_pkodu + t_pkodu, ad.upper() + soyis + '_' + t_pkodu + t_pkodu,
			ad.upper() + soyis.upper() + t_pkodu + t_pkodu,			ad.upper() + '_' + soyis.upper() + t_pkodu + t_pkodu, ad.upper() + '_' + soyis.upper() + '_' + t_pkodu + t_pkodu, ad.upper() + soyis.upper() + '_' + t_pkodu + t_pkodu,
			ad.upper() + soyis.title() + t_pkodu + t_pkodu,			ad.upper() + '_' + soyis.title() + t_pkodu + t_pkodu, ad.upper() + '_' + soyis.title() + '_' + t_pkodu + t_pkodu, ad.upper() + soyis.title() + '_' + t_pkodu + t_pkodu,
			ad.title() + ad + t_pkodu + t_pkodu,					ad.title() + '_' + ad + t_pkodu + t_pkodu, ad.title() + '_' + ad + '_' + t_pkodu + t_pkodu, ad.title() + ad + '_' + t_pkodu + t_pkodu,
			ad.title() + ad.upper() + t_pkodu + t_pkodu,			ad.title() + '_' + ad.upper() + t_pkodu + t_pkodu, ad.title() + '_' + ad.upper() + '_' + t_pkodu + t_pkodu, ad.title() + ad.upper() + '_' + t_pkodu + t_pkodu,
			ad.title() + ad.title() + t_pkodu + t_pkodu,			ad.title() + '_' + ad.title() + t_pkodu + t_pkodu, ad.title() + '_' + ad.title() + '_' + t_pkodu + t_pkodu, ad.title() + ad.title() + '_' + t_pkodu + t_pkodu,
			ad.title() + soyis + t_pkodu + t_pkodu,					ad.title() + '_' + soyis + t_pkodu + t_pkodu, ad.title() + '_' + soyis + '_' + t_pkodu + t_pkodu, ad.title() + soyis + '_' + t_pkodu + t_pkodu,
			ad.title() + soyis.upper() + t_pkodu + t_pkodu,			ad.title() + '_' + soyis.upper() + t_pkodu + t_pkodu, ad.title() + '_' + soyis.upper() + '_' + t_pkodu + t_pkodu, ad.title() + soyis.upper() + '_' + t_pkodu + t_pkodu,
			ad.title() + soyis.title() + t_pkodu + t_pkodu,			ad.title() + '_' + soyis.title() + t_pkodu + t_pkodu, ad.title() + '_' + soyis.title() + '_' + t_pkodu + t_pkodu, ad.title() + soyis.title() + '_' + t_pkodu + t_pkodu,
			
			soyis.upper() + ad + pkodu,								soyis.upper() + '_' + ad + pkodu, soyis.upper() + '_' + ad + '_' + pkodu, soyis.upper() + ad + '_' + pkodu,
			soyis.upper() + ad.upper() + pkodu,						soyis.upper() + '_' + ad.upper() + pkodu, soyis.upper() + '_' + ad.upper() + '_' + pkodu, soyis.upper() + ad.upper() + '_' + pkodu,
			soyis.upper() + ad.title() + pkodu,						soyis.upper() + '_' + ad.title() + pkodu, soyis.upper() + '_' + ad.title() + '_' + pkodu, soyis.upper() + ad.title() + '_' + pkodu,
			soyis.upper() + soyis + pkodu,							soyis.upper() + '_' + soyis + pkodu, soyis.upper() + '_' + soyis + '_' + pkodu, soyis.upper() + soyis + '_' + pkodu,
			soyis.upper() + soyis.upper() + pkodu,					soyis.upper() + '_' + soyis.upper() + pkodu, soyis.upper() + '_' + soyis.upper() + '_' + pkodu, soyis.upper() + soyis.upper() + '_' + pkodu,
			soyis.upper() + soyis.title() + pkodu,					soyis.upper() + '_' + soyis.title() + pkodu, soyis.upper() + '_' + soyis.title() + '_' + pkodu, soyis.upper() + soyis.title() + '_' + pkodu,
			soyis.title() + ad + pkodu,								soyis.title() + '_' + ad + pkodu, soyis.title() + '_' + ad + '_' + pkodu, soyis.title() + ad + '_' + pkodu,
			soyis.title() + ad.upper() + pkodu,						soyis.title() + '_' + ad.upper() + pkodu, soyis.title() + '_' + ad.upper() + '_' + pkodu, soyis.title() + ad.upper() + '_' + pkodu,
			soyis.title() + ad.title() + pkodu,						soyis.title() + '_' + ad.title() + pkodu, soyis.title() + '_' + ad.title() + '_' + pkodu, soyis.title() + ad.title() + '_' + pkodu,
			soyis.title() + soyis + pkodu,							soyis.title() + '_' + soyis + pkodu, soyis.title() + '_' + soyis + '_' + pkodu, soyis.title() + soyis + '_' + pkodu,
			soyis.title() + soyis.upper() + pkodu,					soyis.title() + '_' + soyis.upper() + pkodu, soyis.title() + '_' + soyis.upper() + '_' + pkodu, soyis.title() + soyis.upper() + '_' + pkodu,
			soyis.title() + soyis.title() + pkodu,					soyis.title() + '_' + soyis.title() + pkodu, soyis.title() + '_' + soyis.title() + '_' + pkodu, soyis.title() + soyis.title() + '_' + pkodu,
			
			soyis.upper() + ad + pkodu + pkodu,						soyis.upper() + '_' + ad + pkodu + pkodu, soyis.upper() + '_' + ad + '_' + pkodu + pkodu, soyis.upper() + ad + '_' + pkodu + pkodu,
			soyis.upper() + ad.upper() + pkodu + pkodu,				soyis.upper() + '_' + ad.upper() + pkodu + pkodu, soyis.upper() + '_' + ad.upper() + '_' + pkodu + pkodu, soyis.upper() + ad.upper() + '_' + pkodu + pkodu,
			soyis.upper() + ad.title() + pkodu + pkodu,				soyis.upper() + '_' + ad.title() + pkodu + pkodu, soyis.upper() + '_' + ad.title() + '_' + pkodu + pkodu, soyis.upper() + ad.title() + '_' + pkodu + pkodu,
			soyis.upper() + soyis + pkodu + pkodu,					soyis.upper() + '_' + soyis + pkodu + pkodu, soyis.upper() + '_' + soyis + '_' + pkodu + pkodu, soyis.upper() + soyis + '_' + pkodu + pkodu,
			soyis.upper() + soyis.upper() + pkodu + pkodu,			soyis.upper() + '_' + soyis.upper() + pkodu + pkodu, soyis.upper() + '_' + soyis.upper() + '_' + pkodu + pkodu, soyis.upper() + soyis.upper() + '_' + pkodu + pkodu,
			soyis.upper() + soyis.title() + pkodu + pkodu,			soyis.upper() + '_' + soyis.title() + pkodu + pkodu, soyis.upper() + '_' + soyis.title() + '_' + pkodu + pkodu, soyis.upper() + soyis.title() + '_' + pkodu + pkodu,
			soyis.title() + ad + pkodu + pkodu,						soyis.title() + '_' + ad + pkodu + pkodu, soyis.title() + '_' + ad + '_' + pkodu + pkodu, soyis.title() + ad + '_' + pkodu + pkodu,
			soyis.title() + ad.upper() + pkodu + pkodu,				soyis.title() + '_' + ad.upper() + pkodu + pkodu, soyis.title() + '_' + ad.upper() + '_' + pkodu + pkodu, soyis.title() + ad.upper() + '_' + pkodu + pkodu,
			soyis.title() + ad.title() + pkodu + pkodu,				soyis.title() + '_' + ad.title() + pkodu + pkodu, soyis.title() + '_' + ad.title() + '_' + pkodu + pkodu, soyis.title() + ad.title() + '_' + pkodu + pkodu,
			soyis.title() + soyis + pkodu + pkodu,					soyis.title() + '_' + soyis + pkodu + pkodu, soyis.title() + '_' + soyis + '_' + pkodu + pkodu, soyis.title() + soyis + '_' + pkodu + pkodu,
			soyis.title() + soyis.upper() + pkodu + pkodu,			soyis.title() + '_' + soyis.upper() + pkodu + pkodu, soyis.title() + '_' + soyis.upper() + '_' + pkodu + pkodu, soyis.title() + soyis.upper() + '_' + pkodu + pkodu,
			soyis.title() + soyis.title() + pkodu + pkodu,			soyis.title() + '_' + soyis.title() + pkodu + pkodu, soyis.title() + '_' + soyis.title() + '_' + pkodu + pkodu, soyis.title() + soyis.title() + '_' + pkodu + pkodu,
			
			soyis.upper() + ad + pkodu + t_pkodu,					soyis.upper() + '_' + ad + pkodu + t_pkodu, soyis.upper() + '_' + ad + '_' + pkodu + t_pkodu, soyis.upper() + ad + '_' + pkodu + t_pkodu,
			soyis.upper() + ad.upper() + pkodu + t_pkodu,  			soyis.upper() + '_' + ad.upper() + pkodu + t_pkodu, soyis.upper() + '_' + ad.upper() + '_' + pkodu + t_pkodu, soyis.upper() + ad.upper() + '_' + pkodu + t_pkodu,
			soyis.upper() + ad.title() + pkodu + t_pkodu,			soyis.upper() + '_' + ad.title() + pkodu + t_pkodu, soyis.upper() + '_' + ad.title() + '_' + pkodu + t_pkodu, soyis.upper() + ad.title() + '_' + pkodu + t_pkodu,
			soyis.upper() + soyis + pkodu + t_pkodu,				soyis.upper() + '_' + soyis + pkodu + t_pkodu, soyis.upper() + '_' + soyis + '_' + pkodu + t_pkodu, soyis.upper() + soyis + '_' + pkodu + t_pkodu,
			soyis.upper() + soyis.upper() + pkodu + t_pkodu,		soyis.upper() + '_' + soyis.upper() + pkodu + t_pkodu, soyis.upper() + '_' + soyis.upper() + '_' + pkodu + t_pkodu, soyis.upper() + soyis.upper() + '_' + pkodu + t_pkodu,
			soyis.upper() + soyis.title() + pkodu + t_pkodu,		soyis.upper() + '_' + soyis.title() + pkodu + t_pkodu, soyis.upper() + '_' + soyis.title() + '_' + pkodu + t_pkodu, soyis.upper() + soyis.title() + '_' + pkodu + t_pkodu,
			soyis.title() + ad + pkodu + t_pkodu,					soyis.title() + '_' + ad + pkodu + t_pkodu, soyis.title() + '_' + ad + '_' + pkodu + t_pkodu, soyis.title() + ad + '_' + pkodu + t_pkodu,
			soyis.title() + ad.upper() + pkodu + t_pkodu,			soyis.title() + '_' + ad.upper() + pkodu + t_pkodu, soyis.title() + '_' + ad.upper() + '_' + pkodu + t_pkodu, soyis.title() + ad.upper() + '_' + pkodu + t_pkodu,
			soyis.title() + ad.title() + pkodu + t_pkodu,			soyis.title() + '_' + ad.title() + pkodu + t_pkodu, soyis.title() + '_' + ad.title() + '_' + pkodu + t_pkodu, soyis.title() + ad.title() + '_' + pkodu + t_pkodu,
			soyis.title() + soyis + pkodu + t_pkodu,				soyis.title() + '_' + soyis + pkodu + t_pkodu, soyis.title() + '_' + soyis + '_' + pkodu + t_pkodu, soyis.title() + soyis + '_' + pkodu + t_pkodu,
			soyis.title() + soyis.upper() + pkodu + t_pkodu,		soyis.title() + '_' + soyis.upper() + pkodu + t_pkodu, soyis.title() + '_' + soyis.upper() + '_' + pkodu + t_pkodu, soyis.title() + soyis.upper() + '_' + pkodu + t_pkodu,
			soyis.title() + soyis.title() + pkodu + t_pkodu,		soyis.title() + '_' + soyis.title() + pkodu + t_pkodu, soyis.title() + '_' + soyis.title() + '_' + pkodu + t_pkodu, soyis.title() + soyis.title() + '_' + pkodu + t_pkodu,
			
			soyis.upper() + ad + t_pkodu,							soyis.upper() + '_' + ad + t_pkodu, soyis.upper() + '_' + ad + '_' + t_pkodu, soyis.upper() + ad + '_' + t_pkodu,
			soyis.upper() + ad.upper() + t_pkodu,					soyis.upper() + '_' + ad.upper() + t_pkodu, soyis.upper() + '_' + ad.upper() + '_' + t_pkodu, soyis.upper() + ad.upper() + '_' + t_pkodu,
			soyis.upper() + ad.title() + t_pkodu,					soyis.upper() + '_' + ad.title() + t_pkodu, soyis.upper() + '_' + ad.title() + '_' + t_pkodu, soyis.upper() + ad.title() + '_' + t_pkodu,
			soyis.upper() + soyis + t_pkodu,						soyis.upper() + '_' + soyis + t_pkodu, soyis.upper() + '_' + soyis + '_' + t_pkodu, soyis.upper() + soyis + '_' + t_pkodu,
			soyis.upper() + soyis.upper() + t_pkodu,				soyis.upper() + '_' + soyis.upper() + t_pkodu, soyis.upper() + '_' + soyis.upper() + '_' + t_pkodu, soyis.upper() + soyis.upper() + '_' + t_pkodu,
			soyis.upper() + soyis.title() + t_pkodu,				soyis.upper() + '_' + soyis.title() + t_pkodu, soyis.upper() + '_' + soyis.title() + '_' + t_pkodu, soyis.upper() + soyis.title() + '_' + t_pkodu,
			soyis.title() + ad + t_pkodu,							soyis.title() + '_' + ad + t_pkodu, soyis.title() + '_' + ad + '_' + t_pkodu, soyis.title() + ad + '_' + t_pkodu,
			soyis.title() + ad.upper() + t_pkodu,					soyis.title() + '_' + ad.upper() + t_pkodu, soyis.title() + '_' + ad.upper() + '_' + t_pkodu, soyis.title() + ad.upper() + '_' + t_pkodu,
			soyis.title() + ad.title() + t_pkodu,					soyis.title() + '_' + ad.title() + t_pkodu, soyis.title() + '_' + ad.title() + '_' + t_pkodu, soyis.title() + ad.title() + '_' + t_pkodu,
			soyis.title() + soyis + t_pkodu,						soyis.title() + '_' + soyis + t_pkodu, soyis.title() + '_' + soyis + '_' + t_pkodu, soyis.title() + soyis + '_' + t_pkodu,
			soyis.title() + soyis.upper() + t_pkodu,				soyis.title() + '_' + soyis.upper() + t_pkodu, soyis.title() + '_' + soyis.upper() + '_' + t_pkodu, soyis.title() + soyis.upper() + '_' + t_pkodu,
			soyis.title() + soyis.title() + t_pkodu,				soyis.title() + '_' + soyis.title() + t_pkodu, soyis.title() + '_' + soyis.title() + '_' + t_pkodu, soyis.title() + soyis.title() + '_' + t_pkodu,
			
			soyis.upper() + ad + t_pkodu + pkodu,					soyis.upper() + '_' + ad + t_pkodu + pkodu, soyis.upper() + '_' + ad + '_' + t_pkodu + pkodu, soyis.upper() + ad + '_' + t_pkodu + pkodu,
			soyis.upper() + ad.upper() + t_pkodu + pkodu,			soyis.upper() + '_' + ad.upper() + t_pkodu + pkodu, soyis.upper() + '_' + ad.upper() + '_' + t_pkodu + pkodu, soyis.upper() + ad.upper() + '_' + t_pkodu + pkodu,
			soyis.upper() + ad.title() + t_pkodu + pkodu,			soyis.upper() + '_' + ad.title() + t_pkodu + pkodu, soyis.upper() + '_' + ad.title() + '_' + t_pkodu + pkodu, soyis.upper() + ad.title() + '_' + t_pkodu + pkodu,
			soyis.upper() + soyis + t_pkodu + pkodu,				soyis.upper() + '_' + soyis + t_pkodu + pkodu, soyis.upper() + '_' + soyis + '_' + t_pkodu + pkodu, soyis.upper() + soyis + '_' + t_pkodu + pkodu,
			soyis.upper() + soyis.upper() + t_pkodu + pkodu,		soyis.upper() + '_' + soyis.upper() + t_pkodu + pkodu, soyis.upper() + '_' + soyis.upper() + '_' + t_pkodu + pkodu, soyis.upper() + soyis.upper() + '_' + t_pkodu + pkodu,
			soyis.upper() + soyis.title() + t_pkodu + pkodu,		soyis.upper() + '_' + soyis.title() + t_pkodu + pkodu, soyis.upper() + '_' + soyis.title() + '_' + t_pkodu + pkodu, soyis.upper() + soyis.title() + '_' + t_pkodu + pkodu,
			soyis.title() + ad + t_pkodu + pkodu,					soyis.title() + '_' + ad + t_pkodu + pkodu, soyis.title() + '_' + ad + '_' + t_pkodu + pkodu, soyis.title() + ad + '_' + t_pkodu + pkodu,
			soyis.title() + ad.upper() + t_pkodu + pkodu,			soyis.title() + '_' + ad.upper() + t_pkodu + pkodu, soyis.title() + '_' + ad.upper() + '_' + t_pkodu + pkodu, soyis.title() + ad.upper() + '_' + t_pkodu + pkodu,
			soyis.title() + ad.title() + t_pkodu + pkodu,			soyis.title() + '_' + ad.title() + t_pkodu + pkodu, soyis.title() + '_' + ad.title() + '_' + t_pkodu + pkodu, soyis.title() + ad.title() + '_' + t_pkodu + pkodu,
			soyis.title() + soyis + t_pkodu + pkodu,				soyis.title() + '_' + soyis + t_pkodu + pkodu, soyis.title() + '_' + soyis + '_' + t_pkodu + pkodu, soyis.title() + soyis + '_' + t_pkodu + pkodu,
			soyis.title() + soyis.upper() + t_pkodu + pkodu,		soyis.title() + '_' + soyis.upper() + t_pkodu + pkodu, soyis.title() + '_' + soyis.upper() + '_' + t_pkodu + pkodu, soyis.title() + soyis.upper() + '_' + t_pkodu + pkodu,
			soyis.title() + soyis.title() + t_pkodu + pkodu,		soyis.title() + '_' + soyis.title() + t_pkodu + pkodu, soyis.title() + '_' + soyis.title() + '_' + t_pkodu + pkodu, soyis.title() + soyis.title() + '_' + t_pkodu + pkodu,
			
			soyis.upper() + ad + t_pkodu + t_pkodu,					soyis.upper() + '_' + ad + t_pkodu + t_pkodu, soyis.upper() + '_' + ad + '_' + t_pkodu + t_pkodu, soyis.upper() + ad + '_' + t_pkodu + t_pkodu,
			soyis.upper() + ad.upper() + t_pkodu + t_pkodu,			soyis.upper() + '_' + ad.upper() + t_pkodu + t_pkodu, soyis.upper() + '_' + ad.upper() + '_' + t_pkodu + t_pkodu, soyis.upper() + ad.upper() + '_' + t_pkodu + t_pkodu,
			soyis.upper() + ad.title() + t_pkodu + t_pkodu,			soyis.upper() + '_' + ad.title() + t_pkodu + t_pkodu, soyis.upper() + '_' + ad.title() + '_' + t_pkodu + t_pkodu, soyis.upper() + ad.title() + '_' + t_pkodu + t_pkodu,
			soyis.upper() + soyis + t_pkodu + t_pkodu,				soyis.upper() + '_' + soyis + t_pkodu + t_pkodu, soyis.upper() + '_' + soyis + '_' + t_pkodu + t_pkodu, soyis.upper() + soyis + '_' + t_pkodu + t_pkodu,
			soyis.upper() + soyis.upper() + t_pkodu + t_pkodu,		soyis.upper() + '_' + soyis.upper() + t_pkodu + t_pkodu, soyis.upper() + '_' + soyis.upper() + '_' + t_pkodu + t_pkodu, soyis.upper() + soyis.upper() + '_' + t_pkodu + t_pkodu,
			soyis.upper() + soyis.title() + t_pkodu + t_pkodu,		soyis.upper() + '_' + soyis.title() + t_pkodu + t_pkodu, soyis.upper() + '_' + soyis.title() + '_' + t_pkodu + t_pkodu, soyis.upper() + soyis.title() + '_' + t_pkodu + t_pkodu,
			soyis.title() + ad + t_pkodu + t_pkodu,					soyis.title() + '_' + ad + t_pkodu + t_pkodu, soyis.title() + '_' + ad + '_' + t_pkodu + t_pkodu, soyis.title() + ad + '_' + t_pkodu + t_pkodu,
			soyis.title() + ad.upper() + t_pkodu + t_pkodu,			soyis.title() + '_' + ad.upper() + t_pkodu + t_pkodu, soyis.title() + '_' + ad.upper() + '_' + t_pkodu + t_pkodu, soyis.title() + ad.upper() + '_' + t_pkodu + t_pkodu,
			soyis.title() + ad.title() + t_pkodu + t_pkodu,			soyis.title() + '_' + ad.title() + t_pkodu + t_pkodu, soyis.title() + '_' + ad.title() + '_' + t_pkodu + t_pkodu, soyis.title() + ad.title() + '_' + t_pkodu + t_pkodu,
			soyis.title() + soyis + t_pkodu + t_pkodu,				soyis.title() + '_' + soyis + t_pkodu + t_pkodu, soyis.title() + '_' + soyis + '_' + t_pkodu + t_pkodu, soyis.title() + soyis + '_' + t_pkodu + t_pkodu,
			soyis.title() + soyis.upper() + t_pkodu + t_pkodu,		soyis.title() + '_' + soyis.upper() + t_pkodu + t_pkodu, soyis.title() + '_' + soyis.upper() + '_' + t_pkodu + t_pkodu, soyis.title() + soyis.upper() + '_' + t_pkodu + t_pkodu,
			soyis.title() + soyis.title() + t_pkodu + t_pkodu,		soyis.title() + '_' + soyis.title() + t_pkodu + t_pkodu, soyis.title() + '_' + soyis.title() + '_' + t_pkodu + t_pkodu, soyis.title() + soyis.title() + '_' + t_pkodu + t_pkodu,
			
			#########################################################################################################################################################################################

			ad + dyili,												ad + '_' + dyili,										
			ad + dyili + dyili,   									ad + '_' + dyili + dyili, 
			ad + dyili + t_dyili,									ad + '_' + dyili + t_dyili,
			ad + t_dyili,											ad + '_' + t_dyili,
			ad + t_dyili + dyili,									ad + '_' + t_dyili + dyili,
			ad + t_dyili + t_dyili,									ad + '_' + t_dyili + t_dyili,

			soyis + dyili,											soyis + '_' + dyili,
			soyis + dyili + dyili,									soyis + '_' + dyili + dyili,
			soyis + dyili + t_dyili,								soyis + '_' + dyili + t_dyili,
			soyis + t_dyili,										soyis + '_' + t_dyili,
			soyis + t_dyili + dyili,								soyis + '_' + t_dyili + dyili,
			soyis + t_dyili + t_dyili,								soyis + '_' + t_dyili + t_dyili,

			ad + ad + dyili,										ad + '_' + ad + dyili, ad + '_' + ad + '_' + dyili, ad + ad + '_' + dyili,
			ad + soyis + dyili, 									ad + '_' + soyis + dyili, ad + '_' + soyis + '_' + dyili, ad + soyis + '_' + dyili,
			soyis + ad + dyili,										soyis + '_' + ad + dyili, soyis + '_' + ad + '_' + dyili, soyis + ad + '_' + dyili,
			soyis + soyis + dyili,									soyis + '_' + soyis + dyili, soyis + '_' + soyis + '_' + dyili, soyis + soyis + '_' + dyili,
			
			ad + ad + dyili + dyili,								ad + '_' + ad + dyili + dyili, ad + '_' + ad + '_' + dyili + dyili, ad + ad + '_' + dyili + dyili,
			ad + soyis + dyili + dyili,								ad + '_' + soyis + dyili + dyili, ad + '_' + soyis + '_' + dyili + dyili, ad + soyis + '_' + dyili + dyili,
			soyis + ad + dyili + dyili,								soyis + '_' + ad + dyili + dyili, soyis + '_' + ad + '_' + dyili + dyili, soyis + ad + '_' + dyili + dyili,
			soyis + soyis + dyili + dyili,							soyis + '_' + soyis + dyili + dyili, soyis + '_' + soyis + '_' + dyili + dyili, soyis + soyis + '_' + dyili + dyili,
									
			ad + ad + dyili + t_dyili,								ad + '_' + ad + dyili + t_dyili, ad + '_' + ad + '_' + dyili + t_dyili, ad + ad + '_' + dyili + t_dyili,
			ad + soyis + dyili + t_dyili,							ad + '_' + soyis + dyili + t_dyili, ad + '_' + soyis + '_' + dyili + t_dyili, ad + soyis + '_' + dyili + t_dyili,
			soyis + ad + dyili + t_dyili,							soyis + '_' + ad + dyili + t_dyili, soyis + '_' + ad + '_' + dyili + t_dyili, soyis + ad + '_' + dyili + t_dyili,
			soyis + soyis + dyili + t_dyili,						soyis + '_' + soyis + dyili + t_dyili, soyis + '_' + soyis + '_' + dyili + t_dyili, soyis + soyis + '_' + dyili + t_dyili,
			
			ad + ad + t_dyili,										ad + '_' + ad + t_dyili, ad + '_' + ad + '_' + t_dyili, ad + ad + '_' + t_dyili,
			ad + soyis + t_dyili, 									ad + '_' + soyis + t_dyili, ad + '_' + soyis + '_' + t_dyili, ad + soyis + '_' + t_dyili,
			soyis + ad + t_dyili,									soyis + '_' + ad + t_dyili, soyis + '_' + ad + '_' + t_dyili, soyis + ad + '_' + t_dyili,
			soyis + soyis + t_dyili,								soyis + '_' + soyis + t_dyili, soyis + '_' + soyis + '_' + t_dyili, soyis + soyis + '_' + t_dyili,
			
			ad + ad + t_dyili + dyili,								ad + '_' + ad + t_dyili + dyili, ad + '_' + ad + '_' + t_dyili + dyili, ad + ad + '_' + t_dyili + dyili,
			ad + soyis + t_dyili + dyili,							ad + '_' + soyis + t_dyili + dyili, ad + '_' + soyis + '_' + t_dyili + dyili, ad + soyis + '_' + t_dyili + dyili,
			soyis + ad + t_dyili + dyili,							soyis + '_' + ad + t_dyili + dyili, soyis + '_' + ad + '_' + t_dyili + dyili, soyis + ad + '_' + t_dyili + dyili,
			soyis + soyis + t_dyili + dyili,						soyis + '_' + soyis + t_dyili + dyili, soyis + '_' + soyis + '_' + t_dyili + dyili, soyis + soyis + '_' + t_dyili + dyili,
			
			ad + ad + t_dyili + t_dyili,							ad + '_' + ad + t_dyili + t_dyili, ad + '_' + ad + '_' + t_dyili + t_dyili, ad + ad + '_' + t_dyili + t_dyili, 
			ad + soyis + t_dyili + t_dyili,							ad + '_' + soyis + t_dyili + t_dyili, ad + '_' + soyis + '_' + t_dyili + t_dyili, ad + soyis + '_' + t_dyili + t_dyili,
			soyis + ad + t_dyili + t_dyili,							soyis + '_' + ad + t_dyili + t_dyili, soyis + '_' + ad + '_' + t_dyili + t_dyili, soyis + ad + '_' + t_dyili + t_dyili,
			soyis + soyis + t_dyili + t_dyili,						soyis + '_' + soyis + t_dyili + t_dyili, soyis + '_' + soyis + '_' + t_dyili + t_dyili, soyis + soyis + '_' + t_dyili + t_dyili,
			
			ad + daygun,											ad + '_' + daygun,
			soyis + daygun,											soyis + '_' + daygun,
			
			ad + daygun + daygun,									ad + '_' + daygun + daygun,
			soyis + daygun + daygun,								soyis + '_' + daygun + daygun,

			ad + daygun + t_daygun,									ad + '_' + daygun + t_daygun,
			soyis + daygun + t_daygun,								soyis + '_' + daygun + t_daygun,

			ad + t_daygun,											ad + '_' + t_daygun,
			soyis + t_daygun,										soyis + '_' + t_daygun,
			
			ad + t_daygun + daygun,									ad + '_' + t_daygun + daygun,
			soyis + t_daygun + daygun,								soyis + '_' + t_daygun + daygun,

			ad + t_daygun + t_daygun,								ad + '_' + t_daygun + t_daygun,
			soyis + t_daygun + t_daygun,							soyis + '_' + t_daygun + t_daygun,

			ad + ad + daygun,										soyis + '_' + ad + daygun, soyis + '_' + ad + '_' + daygun, soyis + ad + '_' + daygun,
			ad + soyis + daygun,									soyis + '_' + soyis + daygun, soyis + '_' + soyis + '_' + daygun, soyis + soyis + '_' + daygun,
			soyis + ad + daygun,									soyis + '_' + ad + daygun, soyis + '_' + ad + '_' + daygun, soyis + ad + '_' + daygun,
			soyis + soyis + daygun,									soyis + '_' + soyis + daygun, soyis + '_' + soyis + '_' + daygun, soyis + soyis + '_' + daygun,

			ad + ad + t_daygun,										soyis + '_' + ad + t_daygun, soyis + '_' + ad + '_' + t_daygun, soyis + ad + '_' + t_daygun,
			ad + soyis + t_daygun,									soyis + '_' + soyis + t_daygun, soyis + '_' + soyis + '_' + t_daygun, soyis + soyis + '_' + t_daygun,
			soyis + ad + t_daygun,									soyis + '_' + ad + t_daygun, soyis + '_' + ad + '_' + t_daygun, soyis + ad + '_' + t_daygun,
			soyis + soyis + t_daygun,								soyis + '_' + soyis + t_daygun, soyis + '_' + soyis + '_' + t_daygun, soyis + soyis + '_' + t_daygun,
			
			ad + dtarihi,											ad + '_' + dtarihi,
			ad + t_dtarihi,											ad + '_' + t_dtarihi,
			soyis + dtarihi,										soyis + '_' + dtarihi,
			soyis + t_dtarihi,										soyis + '_' + t_dtarihi,

			ad + ad + dtarihi,										ad + '_' + ad + dtarihi, ad + '_' + ad + '_' + dtarihi, ad + ad + '_' + dtarihi,
			ad + soyis + dtarihi,									ad + '_' + soyis + dtarihi, ad + '_' + soyis + '_' + dtarihi, ad + soyis + '_' + dtarihi,
			ad + ad + t_dtarihi,									ad + '_' + ad + t_dtarihi, ad + '_' + ad + '_' + t_dtarihi, ad + ad + '_' + t_dtarihi,
			ad + soyis + t_dtarihi,									ad + '_' + soyis + t_dtarihi, ad + '_' + soyis + '_' + t_dtarihi, ad + soyis + '_' + t_dtarihi,

			soyis + ad + dtarihi,									soyis + '_' + ad + dtarihi, soyis + '_' + ad + '_' + dtarihi, soyis + ad + '_' + dtarihi,
			soyis + soyis + dtarihi,								soyis + '_' + soyis + dtarihi, soyis + '_' + soyis + '_' + dtarihi, soyis + soyis + '_' + dtarihi,
			soyis + ad + t_dtarihi,									soyis + '_' + ad + t_dtarihi, soyis + '_' + ad + '_' + t_dtarihi, soyis + ad + '_' + t_dtarihi,
			soyis + soyis + t_dtarihi,								soyis + '_' + soyis + t_dtarihi, soyis + '_' + soyis + '_' + t_dtarihi, soyis + soyis + '_' + t_dtarihi,

			#######################################################################################################################################################

			ad.upper() + dyili,										ad.upper() + '_' + dyili,										
			ad.upper() + dyili + dyili,   							ad.upper() + '_' + dyili + dyili, 
			ad.upper() + dyili + t_dyili,							ad.upper() + '_' + dyili + t_dyili,
			ad.upper() + t_dyili,									ad.upper() + '_' + t_dyili,
			ad.upper() + t_dyili + dyili,							ad.upper() + '_' + t_dyili + dyili,
			ad.upper() + t_dyili + t_dyili,							ad.upper() + '_' + t_dyili + t_dyili,

			soyis.upper() + dyili,									soyis.upper() + '_' + dyili,
			soyis.upper() + dyili + dyili,							soyis.upper() + '_' + dyili + dyili,
			soyis.upper() + dyili + t_dyili,						soyis.upper() + '_' + dyili + t_dyili,
			soyis.upper() + t_dyili,								soyis.upper() + '_' + t_dyili,
			soyis.upper() + t_dyili + dyili,						soyis.upper() + '_' + t_dyili + dyili,
			soyis.upper() + t_dyili + t_dyili,						soyis.upper() + '_' + t_dyili + t_dyili,

			ad.title() + dyili,										ad.title() + '_' + dyili,										
			ad.title() + dyili + dyili,   							ad.title() + '_' + dyili + dyili, 
			ad.title() + dyili + t_dyili,							ad.title() + '_' + dyili + t_dyili,
			ad.title() + t_dyili,									ad.title() + '_' + t_dyili,
			ad.title() + t_dyili + dyili,							ad.title() + '_' + t_dyili + dyili,
			ad.title() + t_dyili + t_dyili,							ad.title() + '_' + t_dyili + t_dyili,

			soyis.title() + dyili,									soyis.title() + '_' + dyili,
			soyis.title() + dyili + dyili,							soyis.title() + '_' + dyili + dyili,
			soyis.title() + dyili + t_dyili,						soyis.title() + '_' + dyili + t_dyili,
			soyis.title() + t_dyili,								soyis.title() + '_' + t_dyili,
			soyis.title() + t_dyili + dyili,						soyis.title() + '_' + t_dyili + dyili,
			soyis.title() + t_dyili + t_dyili,						soyis.title() + '_' + t_dyili + t_dyili,

			ad.upper() + ad + dyili,								ad.upper() + '_' + ad + dyili, ad.upper() + '_' + ad + '_' + dyili, ad.upper() + ad + '_' + dyili,
			ad.upper() + ad.upper() + dyili,						ad.upper() + '_' + ad.upper() + dyili, ad.upper() + '_' + ad.upper() + '_' + dyili, ad.upper() + ad.upper() + '_' + dyili,
			ad.upper() + ad.title() + dyili,						ad.upper() + '_' + ad.title() + dyili, ad.upper() + '_' + ad.title() + '_' + dyili, ad.upper() + ad.title() + '_' + dyili,
			ad.upper() + soyis + dyili,								ad.upper() + '_' + soyis + dyili, ad.upper() + '_' + soyis + '_' + dyili, ad.upper() + soyis + '_' + dyili,
			ad.upper() + soyis.upper() + dyili,						ad.upper() + '_' + soyis.upper() + dyili, ad.upper() + '_' + soyis.upper() + '_' + dyili, ad.upper() + soyis.upper() + '_' + dyili,
			ad.upper() + soyis.title() + dyili,						ad.upper() + '_' + soyis.title() + dyili, ad.upper() + '_' + soyis.title() + '_' + dyili, ad.upper() + soyis.title() + '_' + dyili,
			ad.title() + ad + dyili,								ad.title() + '_' + ad + dyili, ad.title() + '_' + ad + '_' + dyili, ad.title() + ad + '_' + dyili,
			ad.title() + ad.upper() + dyili,						ad.title() + '_' + ad.upper() + dyili, ad.title() + '_' + ad.upper() + '_' + dyili, ad.title() + ad.upper() + '_' + dyili,
			ad.title() + ad.title() + dyili,						ad.title() + '_' + ad.title() + dyili, ad.title() + '_' + ad.title() + '_' + dyili, ad.title() + ad.title() + '_' + dyili,
			ad.title() + soyis + dyili,								ad.title() + '_' + soyis + dyili, ad.title() + '_' + soyis + '_' + dyili, ad.title() + soyis + '_' + dyili,
			ad.title() + soyis.upper() + dyili,						ad.title() + '_' + soyis.upper() + dyili, ad.title() + '_' + soyis.upper() + '_' + dyili, ad.title() + soyis.upper() + '_' + dyili,
			ad.title() + soyis.title() + dyili,						ad.title() + '_' + soyis.title() + dyili, ad.title() + '_' + soyis.title() + '_' + dyili, ad.title() + soyis.title() + '_' + dyili,
			
			ad.upper() + ad + dyili + dyili,						ad.upper() + '_' + ad + dyili + dyili, ad.upper() + '_' + ad + '_' + dyili + dyili, ad.upper() + ad + '_' + dyili + dyili,
			ad.upper() + ad.upper() + dyili + dyili,				ad.upper() + '_' + ad.upper() + dyili + dyili, ad.upper() + '_' + ad.upper() + '_' + dyili + dyili, ad.upper() + ad.upper() + '_' + dyili + dyili,
			ad.upper() + ad.title() + dyili + dyili,				ad.upper() + '_' + ad.title() + dyili + dyili, ad.upper() + '_' + ad.title() + '_' + dyili + dyili, ad.upper() + ad.title() + '_' + dyili + dyili,
			ad.upper() + soyis + dyili + dyili,						ad.upper() + '_' + soyis + dyili + dyili, ad.upper() + '_' + soyis + '_' + dyili + dyili, ad.upper() + soyis + '_' + dyili + dyili,
			ad.upper() + soyis.upper() + dyili + dyili,				ad.upper() + '_' + soyis.upper() + dyili + dyili, ad.upper() + '_' + soyis.upper() + '_' + dyili + dyili, ad.upper() + soyis.upper() + '_' + dyili + dyili,
			ad.upper() + soyis.title() + dyili + dyili,				ad.upper() + '_' + soyis.title() + dyili + dyili, ad.upper() + '_' + soyis.title() + '_' + dyili + dyili, ad.upper() + soyis.title() + '_' + dyili + dyili,
			ad.title() + ad + dyili + dyili,						ad.title() + '_' + ad + dyili + dyili, ad.title() + '_' + ad + '_' + dyili + dyili, ad.title() + ad + '_' + dyili + dyili,
			ad.title() + ad.upper() + dyili + dyili,				ad.title() + '_' + ad.upper() + dyili + dyili, ad.title() + '_' + ad.upper() + '_' + dyili + dyili, ad.title() + ad.upper() + '_' + dyili + dyili,
			ad.title() + ad.title() + dyili + dyili,				ad.title() + '_' + ad.title() + dyili + dyili, ad.title() + '_' + ad.title() + '_' + dyili + dyili, ad.title() + ad.title() + '_' + dyili + dyili,
			ad.title() + soyis + dyili + dyili,						ad.title() + '_' + soyis + dyili + dyili, ad.title() + '_' + soyis + '_' + dyili + dyili, ad.title() + soyis + '_' + dyili + dyili,
			ad.title() + soyis.upper() + dyili + dyili,				ad.title() + '_' + soyis.upper() + dyili + dyili, ad.title() + '_' + soyis.upper() + '_' + dyili + dyili, ad.title() + soyis.upper() + '_' + dyili + dyili,
			ad.title() + soyis.title() + dyili + dyili,				ad.title() + '_' + soyis.title() + dyili + dyili, ad.title() + '_' + soyis.title() + '_' + dyili + dyili, ad.title() + soyis.title() + '_' + dyili + dyili,
			
			ad.upper() + ad + dyili + t_dyili,						ad.upper() + '_' + ad + dyili + t_dyili, ad.upper() + '_' + ad + '_' + dyili + t_dyili, ad.upper() + ad + '_' + dyili + t_dyili,
			ad.upper() + ad.upper() + dyili + t_dyili,  			ad.upper() + '_' + ad.upper() + dyili + t_dyili, ad.upper() + '_' + ad.upper() + '_' + dyili + t_dyili, ad.upper() + ad.upper() + '_' + dyili + t_dyili,
			ad.upper() + ad.title() + dyili + t_dyili,				ad.upper() + '_' + ad.title() + dyili + t_dyili, ad.upper() + '_' + ad.title() + '_' + dyili + t_dyili, ad.upper() + ad.title() + '_' + dyili + t_dyili,
			ad.upper() + soyis + dyili + t_dyili,					ad.upper() + '_' + soyis + dyili + t_dyili, ad.upper() + '_' + soyis + '_' + dyili + t_dyili, ad.upper() + soyis + '_' + dyili + t_dyili,
			ad.upper() + soyis.upper() + dyili + t_dyili,			ad.upper() + '_' + soyis.upper() + dyili + t_dyili, ad.upper() + '_' + soyis.upper() + '_' + dyili + t_dyili, ad.upper() + soyis.upper() + '_' + dyili + t_dyili,
			ad.upper() + soyis.title() + dyili + t_dyili,			ad.upper() + '_' + soyis.title() + dyili + t_dyili, ad.upper() + '_' + soyis.title() + '_' + dyili + t_dyili, ad.upper() + soyis.title() + '_' + dyili + t_dyili,
			ad.title() + ad + dyili + t_dyili,						ad.title() + '_' + ad + dyili + t_dyili, ad.title() + '_' + ad + '_' + dyili + t_dyili, ad.title() + ad + '_' + dyili + t_dyili,
			ad.title() + ad.upper() + dyili + t_dyili,				ad.title() + '_' + ad.upper() + dyili + t_dyili, ad.title() + '_' + ad.upper() + '_' + dyili + t_dyili, ad.title() + ad.upper() + '_' + dyili + t_dyili,
			ad.title() + ad.title() + dyili + t_dyili,				ad.title() + '_' + ad.title() + dyili + t_dyili, ad.title() + '_' + ad.title() + '_' + dyili + t_dyili, ad.title() + ad.title() + '_' + dyili + t_dyili,
			ad.title() + soyis + dyili + t_dyili,					ad.title() + '_' + soyis + dyili + t_dyili, ad.title() + '_' + soyis + '_' + dyili + t_dyili, ad.title() + soyis + '_' + dyili + t_dyili,
			ad.title() + soyis.upper() + dyili + t_dyili,			ad.title() + '_' + soyis.upper() + dyili + t_dyili, ad.title() + '_' + soyis.upper() + '_' + dyili + t_dyili, ad.title() + soyis.upper() + '_' + dyili + t_dyili,
			ad.title() + soyis.title() + dyili + t_dyili,			ad.title() + '_' + soyis.title() + dyili + t_dyili, ad.title() + '_' + soyis.title() + '_' + dyili + t_dyili, ad.title() + soyis.title() + '_' + dyili + t_dyili,
			
			ad.upper() + ad + t_dyili,								ad.upper() + '_' + ad + t_dyili, ad.upper() + '_' + ad + '_' + t_dyili, ad.upper() + ad + '_' + t_dyili,
			ad.upper() + ad.upper() + t_dyili,						ad.upper() + '_' + ad.upper() + t_dyili, ad.upper() + '_' + ad.upper() + '_' + t_dyili, ad.upper() + ad.upper() + '_' + t_dyili,
			ad.upper() + ad.title() + t_dyili,						ad.upper() + '_' + ad.title() + t_dyili, ad.upper() + '_' + ad.title() + '_' + t_dyili, ad.upper() + ad.title() + '_' + t_dyili,
			ad.upper() + soyis + t_dyili,							ad.upper() + '_' + soyis + t_dyili, ad.upper() + '_' + soyis + '_' + t_dyili, ad.upper() + soyis + '_' + t_dyili,
			ad.upper() + soyis.upper() + t_dyili,					ad.upper() + '_' + soyis.upper() + t_dyili, ad.upper() + '_' + soyis.upper() + '_' + t_dyili, ad.upper() + soyis.upper() + '_' + t_dyili,
			ad.upper() + soyis.title() + t_dyili,					ad.upper() + '_' + soyis.title() + t_dyili, ad.upper() + '_' + soyis.title() + '_' + t_dyili, ad.upper() + soyis.title() + '_' + t_dyili,
			ad.title() + ad + t_dyili,								ad.title() + '_' + ad + t_dyili, ad.title() + '_' + ad + '_' + t_dyili, ad.title() + ad + '_' + t_dyili,
			ad.title() + ad.upper() + t_dyili,						ad.title() + '_' + ad.upper() + t_dyili, ad.title() + '_' + ad.upper() + '_' + t_dyili, ad.title() + ad.upper() + '_' + t_dyili,
			ad.title() + ad.title() + t_dyili,						ad.title() + '_' + ad.title() + t_dyili, ad.title() + '_' + ad.title() + '_' + t_dyili, ad.title() + ad.title() + '_' + t_dyili,
			ad.title() + soyis + t_dyili,							ad.title() + '_' + soyis + t_dyili, ad.title() + '_' + soyis + '_' + t_dyili, ad.title() + soyis + '_' + t_dyili,
			ad.title() + soyis.upper() + t_dyili,					ad.title() + '_' + soyis.upper() + t_dyili, ad.title() + '_' + soyis.upper() + '_' + t_dyili, ad.title() + soyis.upper() + '_' + t_dyili,
			ad.title() + soyis.title() + t_dyili,					ad.title() + '_' + soyis.title() + t_dyili, ad.title() + '_' + soyis.title() + '_' + t_dyili, ad.title() + soyis.title() + '_' + t_dyili,

			ad.upper() + ad + t_dyili + dyili,						ad.upper() + '_' + ad + t_dyili + dyili, ad.upper() + '_' + ad + '_' + t_dyili + dyili, ad.upper() + ad + '_' + t_dyili + dyili,
			ad.upper() + ad.upper() + t_dyili + dyili,				ad.upper() + '_' + ad.upper() + t_dyili + dyili, ad.upper() + '_' + ad.upper() + '_' + t_dyili + dyili, ad.upper() + ad.upper() + '_' + t_dyili + dyili,
			ad.upper() + ad.title() + t_dyili + dyili,				ad.upper() + '_' + ad.title() + t_dyili + dyili, ad.upper() + '_' + ad.title() + '_' + t_dyili + dyili, ad.upper() + ad.title() + '_' + t_dyili + dyili,
			ad.upper() + soyis + t_dyili + dyili,					ad.upper() + '_' + soyis + t_dyili + dyili, ad.upper() + '_' + soyis + '_' + t_dyili + dyili, ad.upper() + soyis + '_' + t_dyili + dyili,
			ad.upper() + soyis.upper() + t_dyili + dyili,			ad.upper() + '_' + soyis.upper() + t_dyili + dyili, ad.upper() + '_' + soyis.upper() + '_' + t_dyili + dyili, ad.upper() + soyis.upper() + '_' + t_dyili + dyili,
			ad.upper() + soyis.title() + t_dyili + dyili,			ad.upper() + '_' + soyis.title() + t_dyili + dyili, ad.upper() + '_' + soyis.title() + '_' + t_dyili + dyili, ad.upper() + soyis.title() + '_' + t_dyili + dyili,
			ad.title() + ad + t_dyili + dyili,						ad.title() + '_' + ad + t_dyili + dyili, ad.title() + '_' + ad + '_' + t_dyili + dyili, ad.title() + ad + '_' + t_dyili + dyili,
			ad.title() + ad.upper() + t_dyili + dyili,				ad.title() + '_' + ad.upper() + t_dyili + dyili, ad.title() + '_' + ad.upper() + '_' + t_dyili + dyili, ad.title() + ad.upper() + '_' + t_dyili + dyili,
			ad.title() + ad.title() + t_dyili + dyili,				ad.title() + '_' + ad.title() + t_dyili + dyili, ad.title() + '_' + ad.title() + '_' + t_dyili + dyili, ad.title() + ad.title() + '_' + t_dyili + dyili,
			ad.title() + soyis + t_dyili + dyili,					ad.title() + '_' + soyis + t_dyili + dyili, ad.title() + '_' + soyis + '_' + t_dyili + dyili, ad.title() + soyis + '_' + t_dyili + dyili,
			ad.title() + soyis.upper() + t_dyili + dyili,			ad.title() + '_' + soyis.upper() + t_dyili + dyili, ad.title() + '_' + soyis.upper() + '_' + t_dyili + dyili, ad.title() + soyis.upper() + '_' + t_dyili + dyili,
			ad.title() + soyis.title() + t_dyili + dyili,			ad.title() + '_' + soyis.title() + t_dyili + dyili, ad.title() + '_' + soyis.title() + '_' + t_dyili + dyili, ad.title() + soyis.title() + '_' + t_dyili + dyili,

			ad.upper() + ad + t_dyili + t_dyili,					ad.upper() + '_' + ad + t_dyili + t_dyili, ad.upper() + '_' + ad + '_' + t_dyili + t_dyili, ad.upper() + ad + '_' + t_dyili + t_dyili,
			ad.upper() + ad.upper() + t_dyili + t_dyili,			ad.upper() + '_' + ad.upper() + t_dyili + t_dyili, ad.upper() + '_' + ad.upper() + '_' + t_dyili + t_dyili, ad.upper() + ad.upper() + '_' + t_dyili + t_dyili,
			ad.upper() + ad.title() + t_dyili + t_dyili,			ad.upper() + '_' + ad.title() + t_dyili + t_dyili, ad.upper() + '_' + ad.title() + '_' + t_dyili + t_dyili, ad.upper() + ad.title() + '_' + t_dyili + t_dyili,
			ad.upper() + soyis + t_dyili + t_dyili,					ad.upper() + '_' + soyis + t_dyili + t_dyili, ad.upper() + '_' + soyis + '_' + t_dyili + t_dyili, ad.upper() + soyis + '_' + t_dyili + t_dyili,
			ad.upper() + soyis.upper() + t_dyili + t_dyili,			ad.upper() + '_' + soyis.upper() + t_dyili + t_dyili, ad.upper() + '_' + soyis.upper() + '_' + t_dyili + t_dyili,ad.upper() + soyis.upper() + '_' + t_dyili + t_dyili,
			ad.upper() + soyis.title() + t_dyili + t_dyili,			ad.upper() + '_' + soyis.title() + t_dyili + t_dyili, ad.upper() + '_' + soyis.title() + '_' + t_dyili + t_dyili, ad.upper() + soyis.title() + '_' + t_dyili + t_dyili,
			ad.title() + ad + t_dyili + t_dyili,					ad.title() + '_' + ad + t_dyili + t_dyili, ad.title() + '_' + ad + '_' + t_dyili + t_dyili, t_dyili, ad.title() + ad + '_' + t_dyili + t_dyili,
			ad.title() + ad.upper() + t_dyili + t_dyili,			ad.title() + '_' + ad.upper() + t_dyili + t_dyili, ad.title() + '_' + ad.upper() + '_' + t_dyili + t_dyili, ad.title() + ad.upper() + '_' + t_dyili + t_dyili,
			ad.title() + ad.title() + t_dyili + t_dyili,			ad.title() + '_' + ad.title() + t_dyili + t_dyili, ad.title() + '_' + ad.title() + '_' + t_dyili + t_dyili, ad.title() + ad.title() + '_' + t_dyili + t_dyili,
			ad.title() + soyis + t_dyili + t_dyili,					ad.title() + '_' + soyis + t_dyili + t_dyili, ad.title() + '_' + soyis + '_' + t_dyili + t_dyili, ad.title() + soyis + '_' + t_dyili + t_dyili,
			ad.title() + soyis.upper() + t_dyili + t_dyili,			ad.title() + '_' + soyis.upper() + t_dyili + t_dyili, ad.title() + '_' + soyis.upper() + '_' + t_dyili + t_dyili, ad.title() + soyis.upper() + '_' + t_dyili + t_dyili,
			ad.title() + soyis.title() + t_dyili + t_dyili,			ad.title() + '_' + soyis.title() + t_dyili + t_dyili, ad.title() + '_' + soyis.title() + '_' + t_dyili + t_dyili, ad.title() + soyis.title() + '_' + t_dyili + t_dyili,

			soyis.upper() + ad + dyili,								soyis.upper() + '_' + ad + dyili, soyis.upper() + '_' + ad + '_' + dyili, soyis.upper() + ad + '_' + dyili,
			soyis.upper() + ad.upper() + dyili,						soyis.upper() + '_' + ad.upper() + dyili, soyis.upper() + '_' + ad.upper() + '_' + dyili, soyis.upper() + ad.upper() + '_' + dyili,
			soyis.upper() + ad.title() + dyili,						soyis.upper() + '_' + ad.title() + dyili, soyis.upper() + '_' + ad.title() + '_' + dyili, soyis.upper() + ad.title() + '_' + dyili,
			soyis.upper() + soyis + dyili,							soyis.upper() + '_' + soyis + dyili, soyis.upper() + '_' + soyis + '_' + dyili, soyis.upper() + soyis + '_' + dyili,
			soyis.upper() + soyis.upper() + dyili,					soyis.upper() + '_' + soyis.upper() + dyili, soyis.upper() + '_' + soyis.upper() + '_' + dyili, soyis.upper() + soyis.upper() + '_' + dyili,
			soyis.upper() + soyis.title() + dyili,					soyis.upper() + '_' + soyis.title() + dyili, soyis.upper() + '_' + soyis.title() + '_' + dyili, soyis.upper() + soyis.title() + '_' + dyili,
			soyis.title() + ad + dyili,								soyis.title() + '_' + ad + dyili, soyis.title() + '_' + ad + '_' + dyili, soyis.title() + ad + '_' + dyili,
			soyis.title() + ad.upper() + dyili,						soyis.title() + '_' + ad.upper() + dyili, soyis.title() + '_' + ad.upper() + '_' + dyili, soyis.title() + ad.upper() + '_' + dyili,
			soyis.title() + ad.title() + dyili,						soyis.title() + '_' + ad.title() + dyili, soyis.title() + '_' + ad.title() + '_' + dyili, soyis.title() + ad.title() + '_' + dyili,
			soyis.title() + soyis + dyili,							soyis.title() + '_' + soyis + dyili, soyis.title() + '_' + soyis + '_' + dyili, soyis.title() + soyis + '_' + dyili,
			soyis.title() + soyis.upper() + dyili,					soyis.title() + '_' + soyis.upper() + dyili, soyis.title() + '_' + soyis.upper() + '_' + dyili, soyis.title() + soyis.upper() + '_' + dyili,
			soyis.title() + soyis.title() + dyili,					soyis.title() + '_' + soyis.title() + dyili, soyis.title() + '_' + soyis.title() + '_' + dyili, soyis.title() + soyis.title() + '_' + dyili,

			soyis.upper() + ad + dyili + dyili,						soyis.upper() + '_' + ad + dyili + dyili, soyis.upper() + '_' + ad + '_' + dyili + dyili, soyis.upper() + ad + '_' + dyili + dyili,
			soyis.upper() + ad.upper() + dyili + dyili,				soyis.upper() + '_' + ad.upper() + dyili + dyili, soyis.upper() + '_' + ad.upper() + '_' + dyili + dyili, soyis.upper() + ad.upper() + '_' + dyili + dyili,
			soyis.upper() + ad.title() + dyili + dyili,				soyis.upper() + '_' + ad.title() + dyili + dyili, soyis.upper() + '_' + ad.title() + '_' + dyili + dyili, soyis.upper() + ad.title() + '_' + dyili + dyili,
			soyis.upper() + soyis + dyili + dyili,					soyis.upper() + '_' + soyis + dyili + dyili, soyis.upper() + '_' + soyis + '_' + dyili + dyili, soyis.upper() + soyis + '_' + dyili + dyili,
			soyis.upper() + soyis.upper() + dyili + dyili,			soyis.upper() + '_' + soyis.upper() + dyili + dyili, soyis.upper() + '_' + soyis.upper() + '_' + dyili + dyili, soyis.upper() + soyis.upper() + '_' + dyili + dyili,
			soyis.upper() + soyis.title() + dyili + dyili,			soyis.upper() + '_' + soyis.title() + dyili + dyili, soyis.upper() + '_' + soyis.title() + '_' + dyili + dyili, soyis.upper() + soyis.title() + '_' + dyili + dyili,
			soyis.title() + ad + dyili + dyili,						soyis.title() + '_' + ad + dyili + dyili, soyis.title() + '_' + ad + '_' + dyili + dyili, soyis.title() + ad + '_' + dyili + dyili,
			soyis.title() + ad.upper() + dyili + dyili,				soyis.title() + '_' + ad.upper() + dyili + dyili, soyis.title() + '_' + ad.upper() + '_' + dyili + dyili, soyis.title() + ad.upper() + '_' + dyili + dyili,
			soyis.title() + ad.title() + dyili + dyili,				soyis.title() + '_' + ad.title() + dyili + dyili, soyis.title() + '_' + ad.title() + '_' + dyili + dyili, soyis.title() + ad.title() + '_' + dyili + dyili,
			soyis.title() + soyis + dyili + dyili,					soyis.title() + '_' + soyis + dyili + dyili, soyis.title() + '_' + soyis + '_' + dyili + dyili, soyis.title() + soyis + '_' + dyili + dyili,
			soyis.title() + soyis.upper() + dyili + dyili,			soyis.title() + '_' + soyis.upper() + dyili + dyili, soyis.title() + '_' + soyis.upper() + '_' + dyili + dyili, soyis.title() + soyis.upper() + '_' + dyili + dyili,
			soyis.title() + soyis.title() + dyili + dyili,			soyis.title() + '_' + soyis.title() + dyili + dyili, soyis.title() + '_' + soyis.title() + '_' + dyili + dyili, soyis.title() + soyis.title() + '_' + dyili + dyili,

			soyis.upper() + ad + dyili + t_dyili,					soyis.upper() + '_' + ad + dyili + t_dyili, soyis.upper() + '_' + ad + '_' + dyili + t_dyili, soyis.upper() + ad + '_' + dyili + t_dyili,
			soyis.upper() + ad.upper() + dyili + t_dyili,  			soyis.upper() + '_' + ad.upper() + dyili + t_dyili, soyis.upper() + '_' + ad.upper() + '_' + dyili + t_dyili, soyis.upper() + ad.upper() + '_' + dyili + t_dyili,
			soyis.upper() + ad.title() + dyili + t_dyili,			soyis.upper() + '_' + ad.title() + dyili + t_dyili, soyis.upper() + '_' + ad.title() + '_' + dyili + t_dyili, soyis.upper() + ad.title() + '_' + dyili + t_dyili,
			soyis.upper() + soyis + dyili + t_dyili,				soyis.upper() + '_' + soyis + dyili + t_dyili, soyis.upper() + '_' + soyis + '_' + dyili + t_dyili, soyis.upper() + soyis + '_' + dyili + t_dyili,
			soyis.upper() + soyis.upper() + dyili + t_dyili,		soyis.upper() + '_' + soyis.upper() + dyili + t_dyili, soyis.upper() + '_' + soyis.upper() + '_' + dyili + t_dyili, soyis.upper() + soyis.upper() + '_' + dyili + t_dyili,
			soyis.upper() + soyis.title() + dyili + t_dyili,		soyis.upper() + '_' + soyis.title() + dyili + t_dyili, soyis.upper() + '_' + soyis.title() + '_' + dyili + t_dyili, soyis.upper() + soyis.title() + '_' + dyili + t_dyili,
			soyis.title() + ad + dyili + t_dyili,					soyis.title() + '_' + ad + dyili + t_dyili, soyis.title() + '_' + ad + '_' + dyili + t_dyili, soyis.title() + ad + '_' + dyili + t_dyili,
			soyis.title() + ad.upper() + dyili + t_dyili,			soyis.title() + '_' + ad.upper() + dyili + t_dyili, soyis.title() + '_' + ad.upper() + '_' + dyili + t_dyili, soyis.title() + ad.upper() + '_' + dyili + t_dyili,
			soyis.title() + ad.title() + dyili + t_dyili,			soyis.title() + '_' + ad.title() + dyili + t_dyili, soyis.title() + '_' + ad.title() + '_' + dyili + t_dyili, soyis.title() + ad.title() + '_' + dyili + t_dyili,
			soyis.title() + soyis + dyili + t_dyili,				soyis.title() + '_' + soyis + dyili + t_dyili, soyis.title() + '_' + soyis + '_' + dyili + t_dyili, soyis.title() + soyis + '_' + dyili + t_dyili,
			soyis.title() + soyis.upper() + dyili + t_dyili,		soyis.title() + '_' + soyis.upper() + dyili + t_dyili, soyis.title() + '_' + soyis.upper() + '_' + dyili + t_dyili, soyis.title() + soyis.upper() + '_' + dyili + t_dyili,
			soyis.title() + soyis.title() + dyili + t_dyili,		soyis.title() + '_' + soyis.title() + dyili + t_dyili, soyis.title() + '_' + soyis.title() + '_' + dyili + t_dyili, soyis.title() + soyis.title() + '_' + dyili + t_dyili,

			soyis.upper() + ad + t_dyili,							soyis.upper() + '_' + ad + t_dyili, soyis.upper() + '_' + ad + '_' + t_dyili, soyis.upper() + ad + '_' + t_dyili,
			soyis.upper() + ad.upper() + t_dyili,					soyis.upper() + '_' + ad.upper() + t_dyili, soyis.upper() + '_' + ad.upper() + '_' + t_dyili, soyis.upper() + ad.upper() + '_' + t_dyili,
			soyis.upper() + ad.title() + t_dyili,					soyis.upper() + '_' + ad.title() + t_dyili, soyis.upper() + '_' + ad.title() + '_' + t_dyili, soyis.upper() + ad.title() + '_' + t_dyili,
			soyis.upper() + soyis + t_dyili,						soyis.upper() + '_' + soyis + t_dyili, soyis.upper() + '_' + soyis + '_' + t_dyili, soyis.upper() + soyis + '_' + t_dyili,
			soyis.upper() + soyis.upper() + t_dyili,				soyis.upper() + '_' + soyis.upper() + t_dyili, soyis.upper() + '_' + soyis.upper() + '_' + t_dyili, soyis.upper() + soyis.upper() + '_' + t_dyili,
			soyis.upper() + soyis.title() + t_dyili,				soyis.upper() + '_' + soyis.title() + t_dyili, soyis.upper() + '_' + soyis.title() + '_' + t_dyili, soyis.upper() + soyis.title() + '_' + t_dyili,
			soyis.title() + ad + t_dyili,							soyis.title() + '_' + ad + t_dyili, soyis.title() + '_' + ad + '_' + t_dyili, soyis.title() + ad + '_' + t_dyili,
			soyis.title() + ad.upper() + t_dyili,					soyis.title() + '_' + ad.upper() + t_dyili, soyis.title() + '_' + ad.upper() + '_' + t_dyili, soyis.title() + ad.upper() + '_' + t_dyili,
			soyis.title() + ad.title() + t_dyili,					soyis.title() + '_' + ad.title() + t_dyili, soyis.title() + '_' + ad.title() + '_' + t_dyili, soyis.title() + ad.title() + '_' + t_dyili,
			soyis.title() + soyis + t_dyili,						soyis.title() + '_' + soyis + t_dyili, soyis.title() + '_' + soyis + '_' + t_dyili, soyis.title() + soyis + '_' + t_dyili,
			soyis.title() + soyis.upper() + t_dyili,				soyis.title() + '_' + soyis.upper() + t_dyili, soyis.title() + '_' + soyis.upper() + '_' + t_dyili, soyis.title() + soyis.upper() + '_' + t_dyili,
			soyis.title() + soyis.title() + t_dyili,				soyis.title() + '_' + soyis.title() + t_dyili, soyis.title() + '_' + soyis.title() + '_' + t_dyili, soyis.title() + soyis.title() + '_' + t_dyili,

			soyis.upper() + ad + t_dyili + dyili,					soyis.upper() + '_' + ad + t_dyili + dyili, soyis.upper() + '_' + ad + '_' + t_dyili + dyili, soyis.upper() + ad + '_' + t_dyili + dyili,
			soyis.upper() + ad.upper() + t_dyili + dyili,			soyis.upper() + '_' + ad.upper() + t_dyili + dyili, soyis.upper() + '_' + ad.upper() + '_' + t_dyili + dyili, soyis.upper() + ad.upper() + '_' + t_dyili + dyili,
			soyis.upper() + ad.title() + t_dyili + dyili,			soyis.upper() + '_' + ad.title() + t_dyili + dyili, soyis.upper() + '_' + ad.title() + '_' + t_dyili + dyili, soyis.upper() + ad.title() + '_' + t_dyili + dyili,
			soyis.upper() + soyis + t_dyili + dyili,				soyis.upper() + '_' + soyis + t_dyili + dyili, soyis.upper() + '_' + soyis + '_' + t_dyili + dyili, soyis.upper() + soyis + '_' + t_dyili + dyili,
			soyis.upper() + soyis.upper() + t_dyili + dyili,		soyis.upper() + '_' + soyis.upper() + t_dyili + dyili, soyis.upper() + '_' + soyis.upper() + '_' + t_dyili + dyili, soyis.upper() + soyis.upper() + '_' + t_dyili + dyili,
			soyis.upper() + soyis.title() + t_dyili + dyili,		soyis.upper() + '_' + soyis.title() + t_dyili + dyili, soyis.upper() + '_' + soyis.title() + '_' + t_dyili + dyili, soyis.upper() + soyis.title() + '_' + t_dyili + dyili,
			soyis.title() + ad + t_dyili + dyili,					soyis.title() + '_' + ad + t_dyili + dyili, soyis.title() + '_' + ad + '_' + t_dyili + dyili, soyis.title() + ad + '_' + t_dyili + dyili,
			soyis.title() + ad.upper() + t_dyili + dyili,			soyis.title() + '_' + ad.upper() + t_dyili + dyili, soyis.title() + '_' + ad.upper() + '_' + t_dyili + dyili, soyis.title() + ad.upper() + '_' + t_dyili + dyili,
			soyis.title() + ad.title() + t_dyili + dyili,			soyis.title() + '_' + ad.title() + t_dyili + dyili, soyis.title() + '_' + ad.title() + '_' + t_dyili + dyili, soyis.title() + ad.title() + '_' + t_dyili + dyili,
			soyis.title() + soyis + t_dyili + dyili,				soyis.title() + '_' + soyis + t_dyili + dyili, soyis.title() + '_' + soyis + '_' + t_dyili + dyili, soyis.title() + soyis + '_' + t_dyili + dyili,
			soyis.title() + soyis.upper() + t_dyili + dyili,		soyis.title() + '_' + soyis.upper() + t_dyili + dyili, soyis.title() + '_' + soyis.upper() + '_' + t_dyili + dyili, soyis.title() + soyis.upper() + '_' + t_dyili + dyili,
			soyis.title() + soyis.title() + t_dyili + dyili,		soyis.title() + '_' + soyis.title() + t_dyili + dyili, soyis.title() + '_' + soyis.title() + '_' + t_dyili + dyili, soyis.title() + soyis.title() + '_' + t_dyili + dyili,
			
			soyis.upper() + ad + t_dyili + t_dyili,					soyis.upper() + '_' + ad + t_dyili + t_dyili, soyis.upper() + '_' + ad + '_' + t_dyili + t_dyili, soyis.upper() + ad + '_' + t_dyili + t_dyili,
			soyis.upper() + ad.upper() + t_dyili + t_dyili,			soyis.upper() + '_' + ad.upper() + t_dyili + t_dyili, soyis.upper() + '_' + ad.upper() + '_' + t_dyili + t_dyili, soyis.upper() + ad.upper() + '_' + t_dyili + t_dyili,
			soyis.upper() + ad.title() + t_dyili + t_dyili,		    soyis.upper() + '_' + ad.title() + t_dyili + t_dyili, soyis.upper() + '_' + ad.title() + '_' + t_dyili + t_dyili, soyis.upper() + ad.title() + '_' + t_dyili + t_dyili,
			soyis.upper() + soyis + t_dyili + t_dyili,				soyis.upper() + '_' + soyis + t_dyili + t_dyili, soyis.upper() + '_' + soyis + '_' + t_dyili + t_dyili, soyis.upper() + soyis + '_' + t_dyili + t_dyili,
			soyis.upper() + soyis.upper() + t_dyili + t_dyili,		soyis.upper() + '_' + soyis.upper() + t_dyili + t_dyili, soyis.upper() + '_' + soyis.upper() + '_' + t_dyili + t_dyili, soyis.upper() + soyis.upper() + '_' + t_dyili + t_dyili,
			soyis.upper() + soyis.title() + t_dyili + t_dyili,		soyis.upper() + '_' + soyis.title() + t_dyili + t_dyili, soyis.upper() + '_' + soyis.title() + '_' + t_dyili + t_dyili, soyis.upper() + soyis.title() + '_' + t_dyili + t_dyili,
			soyis.title() + ad + t_dyili + t_dyili,					soyis.title() + '_' + ad + t_dyili + t_dyili, soyis.title() + '_' + ad + '_' + t_dyili + t_dyili, soyis.title() + ad + '_' + t_dyili + t_dyili,
			soyis.title() + ad.upper() + t_dyili + t_dyili,			soyis.title() + '_' + ad.upper() + t_dyili + t_dyili, soyis.title() + '_' + ad.upper() + '_' + t_dyili + t_dyili, soyis.title() + ad.upper() + '_' + t_dyili + t_dyili,
			soyis.title() + ad.title() + t_dyili + t_dyili,			soyis.title() + '_' + ad.title() + t_dyili + t_dyili, soyis.title() + '_' + ad.title() + '_' + t_dyili + t_dyili, soyis.title() + ad.title() + '_' + t_dyili + t_dyili,
			soyis.title() + soyis + t_dyili + t_dyili,				soyis.title() + '_' + soyis + t_dyili + t_dyili, soyis.title() + '_' + soyis + '_' + t_dyili + t_dyili, soyis.title() + soyis + '_' + t_dyili + t_dyili,
			soyis.title() + soyis.upper() + t_dyili + t_dyili,		soyis.title() + '_' + soyis.upper() + t_dyili + t_dyili, soyis.title() + '_' + soyis.upper() + '_' + t_dyili + t_dyili, soyis.title() + soyis.upper() + '_' + t_dyili + t_dyili,
			soyis.title() + soyis.title() + t_dyili + t_dyili,		soyis.title() + '_' + soyis.title() + t_dyili + t_dyili, soyis.title() + '_' + soyis.title() + '_' + t_dyili + t_dyili, soyis.title() + soyis.title() + '_' + t_dyili + t_dyili,
			
			ad.upper() + daygun,									ad.upper() + '_' + daygun,
			soyis.upper() + daygun,									soyis.upper() + '_' + daygun,
			ad.title() + daygun,									ad.title() + '_' + daygun,
			soyis.title() + daygun,									soyis.title() + '_' + daygun,
			
			ad.upper() + daygun + daygun,							ad.upper() + '_' + daygun + daygun,
			soyis.upper() + daygun + daygun,						soyis.upper() + '_' + daygun + daygun,
			ad.title() + daygun + daygun,							ad.title() + '_' + daygun + daygun,
			soyis.title() + daygun + daygun,						soyis.title() + '_' + daygun + daygun,

			ad.upper() + daygun + t_daygun,							ad.upper() + '_' + daygun + t_daygun,
			soyis.upper() + daygun + t_daygun,						soyis.upper() + '_' + daygun + t_daygun,
			ad.title() + daygun + t_daygun,							ad.title() + '_' + daygun + t_daygun,
			soyis.title() + daygun + t_daygun,						soyis.title() + '_' + daygun + t_daygun,

			ad.upper() + t_daygun,									ad.upper() + '_' + t_daygun,
			soyis.upper() + t_daygun,								soyis.upper() + '_' + t_daygun,
			ad.title() + t_daygun,									ad.title() + '_' + t_daygun,
			soyis.title() + t_daygun,								soyis.title() + '_' + t_daygun,
			
			ad.upper() + t_daygun + daygun,							ad.upper() + '_' + t_daygun + daygun,
			soyis.upper() + t_daygun + daygun,						soyis.upper() + '_' + t_daygun + daygun,
			ad.title() + t_daygun + daygun,							ad.title() + '_' + t_daygun + daygun,
			soyis.title() + t_daygun + daygun,						soyis.title() + '_' + t_daygun + daygun,

			ad.upper() + t_daygun + t_daygun,						ad.upper() + '_' + t_daygun + t_daygun,
			soyis.upper() + t_daygun + t_daygun,					soyis.upper() + '_' + t_daygun + t_daygun,
			ad.title() + t_daygun + t_daygun,						ad.title() + '_' + t_daygun + t_daygun,
			soyis.title() + t_daygun + t_daygun,					soyis.title() + '_' + t_daygun + t_daygun,

			ad.upper() + ad + daygun,								ad.upper() + '_' + ad + daygun, ad.upper() + '_' + ad + '_' + daygun, ad.upper() + ad + '_' + daygun,
			ad.upper() + ad.upper() + daygun,						ad.upper() + '_' + ad.upper() + daygun, ad.upper() + '_' + ad.upper() + '_' + daygun, ad.upper() + ad.upper() + '_' + daygun,
			ad.upper() + ad.title() + daygun,						ad.upper() + '_' + ad.title() + daygun, ad.upper() + '_' + ad.title() + '_' + daygun, ad.upper() + ad.title() + '_' + daygun,
			ad.upper() + soyis + daygun,							ad.upper() + '_' + soyis + daygun, ad.upper() + '_' + soyis + '_' + daygun, ad.upper() + soyis + '_' + daygun,
			ad.upper() + soyis.upper() + daygun,					ad.upper() + '_' + soyis.upper() + daygun, ad.upper() + '_' + soyis.upper() + '_' + daygun, ad.upper() + soyis.upper() + '_' + daygun,
			ad.upper() + soyis.title() + daygun,					ad.upper() + '_' + soyis.title() + daygun, ad.upper() + '_' + soyis.title() + '_' + daygun, ad.upper() + soyis.title() + '_' + daygun,
			ad.title() + ad + daygun,								ad.title() + '_' + ad + daygun, ad.title() + '_' + ad + '_' + daygun, ad.title() + ad + '_' + daygun,
			ad.title() + ad.upper() + daygun,						ad.title() + '_' + ad.upper() + daygun, ad.title() + '_' + ad.upper() + '_' + daygun, ad.title() + ad.upper() + '_' + daygun,
			ad.title() + ad.title() + daygun,						ad.title() + '_' + ad.title() + daygun, ad.title() + '_' + ad.title() + '_' + daygun, ad.title() + ad.title() + '_' + daygun,
			ad.title() + soyis + daygun,							ad.title() + '_' + soyis + daygun, ad.title() + '_' + soyis + '_' + daygun, ad.title() + soyis + '_' + daygun,
			ad.title() + soyis.upper() + daygun,					ad.title() + '_' + soyis.upper() + daygun, ad.title() + '_' + soyis.upper() + '_' + daygun, ad.title() + soyis.upper() + '_' + daygun,
			ad.title() + soyis.title() + daygun,					ad.title() + '_' + soyis.title() + daygun, ad.title() + '_' + soyis.title() + '_' + daygun, ad.title() + soyis.title() + '_' + daygun,
			
			ad.upper() + ad + daygun + daygun,						ad.upper() + '_' + ad + daygun + daygun, ad.upper() + '_' + ad + '_' + daygun + daygun, ad.upper() + ad + '_' + daygun + daygun,
			ad.upper() + ad.upper() + daygun + daygun,				ad.upper() + '_' + ad.upper() + daygun + daygun, ad.upper() + '_' + ad.upper() + '_' + daygun + daygun, ad.upper() + ad.upper() + '_' + daygun + daygun,
			ad.upper() + ad.title() + daygun + daygun,				ad.upper() + '_' + ad.title() + daygun + daygun, ad.upper() + '_' + ad.title() + '_' + daygun + daygun, ad.upper() + ad.title() + '_' + daygun + daygun,
			ad.upper() + soyis + daygun + daygun,					ad.upper() + '_' + soyis + daygun + daygun, ad.upper() + '_' + soyis + '_' + daygun + daygun, ad.upper() + soyis + '_' + daygun + daygun,
			ad.upper() + soyis.upper() + daygun + daygun,			ad.upper() + '_' + soyis.upper() + daygun + daygun, ad.upper() + '_' + soyis.upper() + '_' + daygun + daygun, ad.upper() + soyis.upper() + '_' + daygun + daygun,
			ad.upper() + soyis.title() + daygun + daygun,			ad.upper() + '_' + soyis.title() + daygun + daygun, ad.upper() + '_' + soyis.title() + '_' + daygun + daygun, ad.upper() + soyis.title() + '_' + daygun + daygun,
			ad.title() + ad + daygun + daygun,						ad.title() + '_' + ad + daygun + daygun, ad.title() + '_' + ad + '_' + daygun + daygun, ad.title() + ad + '_' + daygun + daygun,
			ad.title() + ad.upper() + daygun + daygun,				ad.title() + '_' + ad.upper() + daygun + daygun, ad.title() + '_' + ad.upper() + '_' + daygun + daygun, ad.title() + ad.upper() + '_' + daygun + daygun,
			ad.title() + ad.title() + daygun + daygun,				ad.title() + '_' + ad.title() + daygun + daygun, ad.title() + '_' + ad.title() + '_' + daygun + daygun, ad.title() + ad.title() + '_' + daygun + daygun,
			ad.title() + soyis + daygun + daygun,					ad.title() + '_' + soyis + daygun + daygun, ad.title() + '_' + soyis + '_' + daygun + daygun, ad.title() + soyis + '_' + daygun + daygun,
			ad.title() + soyis.upper() + daygun + daygun,			ad.title() + '_' + soyis.upper() + daygun + daygun, ad.title() + '_' + soyis.upper() + '_' + daygun + daygun, ad.title() + soyis.upper() + '_' + daygun + daygun,
			ad.title() + soyis.title() + daygun + daygun,			ad.title() + '_' + soyis.title() + daygun + daygun, ad.title() + '_' + soyis.title() + '_' + daygun + daygun, ad.title() + soyis.title() + '_' + daygun + daygun,
			
			ad.upper() + ad + daygun + t_daygun,					ad.upper() + '_' + ad + daygun + t_daygun, ad.upper() + '_' + ad + '_' + daygun + t_daygun, ad.upper() + ad + '_' + daygun + t_daygun,
			ad.upper() + ad.upper() + daygun + t_daygun,			ad.upper() + '_' + ad.upper() + daygun + t_daygun, ad.upper() + '_' + ad.upper() + '_' + daygun + t_daygun, ad.upper() + ad.upper() + '_' + daygun + t_daygun,
			ad.upper() + ad.title() + daygun + t_daygun,			ad.upper() + '_' + ad.title() + daygun + t_daygun, ad.upper() + '_' + ad.title() + '_' + daygun + t_daygun, ad.upper() + ad.title() + '_' + daygun + t_daygun,
			ad.upper() + soyis + daygun + t_daygun,					ad.upper() + '_' + soyis + daygun + t_daygun, ad.upper() + '_' + soyis + '_' + daygun + t_daygun, ad.upper() + soyis + '_' + daygun + t_daygun,
			ad.upper() + soyis.upper() + daygun + t_daygun,			ad.upper() + '_' + soyis.upper() + daygun + t_daygun, ad.upper() + '_' + soyis.upper() + '_' + daygun + t_daygun, ad.upper() + soyis.upper() + '_' + daygun + t_daygun,
			ad.upper() + soyis.title() + daygun + t_daygun,			ad.upper() + '_' + soyis.title() + daygun + t_daygun, ad.upper() + '_' + soyis.title() + '_' + daygun + t_daygun, ad.upper() + soyis.title() + '_' + daygun + t_daygun,
			ad.title() + ad + daygun + t_daygun,					ad.title() + '_' + ad + daygun + t_daygun, ad.title() + '_' + ad + '_' + daygun + t_daygun, ad.title() + ad + '_' + daygun + t_daygun,
			ad.title() + ad.upper() + daygun + t_daygun,			ad.title() + '_' + ad.upper() + daygun + t_daygun, ad.title() + '_' + ad.upper() + '_' + daygun + t_daygun, ad.title() + ad.upper() + '_' + daygun + t_daygun,
			ad.title() + ad.title() + daygun + t_daygun,			ad.title() + '_' + ad.title() + daygun + t_daygun, ad.title() + '_' + ad.title() + '_' + daygun + t_daygun, ad.title() + ad.title() + '_' + daygun + t_daygun,
			ad.title() + soyis + daygun + t_daygun,					ad.title() + '_' + soyis + daygun + t_daygun, ad.title() + '_' + soyis + '_' + daygun + t_daygun, ad.title() + soyis + '_' + daygun + t_daygun,
			ad.title() + soyis.upper() + daygun + t_daygun,			ad.title() + '_' + soyis.upper() + daygun + t_daygun, ad.title() + '_' + soyis.upper() + '_' + daygun + t_daygun, ad.title() + soyis.upper() + '_' + daygun + t_daygun,
			ad.title() + soyis.title() + daygun + t_daygun,			ad.title() + '_' + soyis.title() + daygun + t_daygun, ad.title() + '_' + soyis.title() + '_' + daygun + t_daygun, ad.title() + soyis.title() + '_' + daygun + t_daygun,
			
			ad.upper() + ad + t_daygun,								ad.upper() + '_' + ad + t_daygun, ad.upper() + '_' + ad + '_' + t_daygun, ad.upper() + ad + '_' + t_daygun,
			ad.upper() + ad.upper() + t_daygun,						ad.upper() + '_' + ad.upper() + t_daygun, ad.upper() + '_' + ad.upper() + '_' + t_daygun, ad.upper() + ad.upper() + '_' + t_daygun,
			ad.upper() + ad.title() + t_daygun,						ad.upper() + '_' + ad.title() + t_daygun, ad.upper() + '_' + ad.title() + '_' + t_daygun, ad.upper() + ad.title() + '_' + t_daygun,
			ad.upper() + soyis + t_daygun,							ad.upper() + '_' + soyis + t_daygun, ad.upper() + '_' + soyis + '_' + t_daygun, ad.upper() + soyis + '_' + t_daygun,
			ad.upper() + soyis.upper() + t_daygun,					ad.upper() + '_' + soyis.upper() + t_daygun, ad.upper() + '_' + soyis.upper() + '_' + t_daygun, ad.upper() + soyis.upper() + '_' + t_daygun,
			ad.upper() + soyis.title() + t_daygun,					ad.upper() + '_' + soyis.title() + t_daygun, ad.upper() + '_' + soyis.title() + '_' + t_daygun, ad.upper() + soyis.title() + '_' + t_daygun,
			ad.title() + ad + t_daygun,								ad.title() + '_' + ad + daygun, ad.title() + '_' + ad + '_' + t_daygun, ad.title() + ad + '_' + t_daygun,
			ad.title() + ad.upper() + t_daygun,						ad.title() + '_' + ad.upper() + daygun, ad.title() + '_' + ad.upper() + '_' + t_daygun, ad.title() + ad.upper() + '_' + t_daygun,
			ad.title() + ad.title() + t_daygun,						ad.title() + '_' + ad.title() + daygun, ad.title() + '_' + ad.title() + '_' + t_daygun, ad.title() + ad.title() + '_' + t_daygun,
			ad.title() + soyis + t_daygun,							ad.title() + '_' + soyis + daygun, ad.title() + '_' + soyis + '_' + t_daygun, ad.title() + soyis + '_' + t_daygun,
			ad.title() + soyis.upper() + t_daygun,					ad.title() + '_' + soyis.upper() + daygun, ad.title() + '_' + soyis.upper() + '_' + t_daygun, ad.title() + soyis.upper() + '_' + t_daygun,
			ad.title() + soyis.title() + t_daygun,					ad.title() + '_' + soyis.title() + daygun, ad.title() + '_' + soyis.title() + '_' + t_daygun, ad.title() + soyis.title() + '_' + t_daygun,

			ad.upper() + ad + t_daygun + daygun,					ad.upper() + '_' + ad + t_daygun + daygun, ad.upper() + '_' + ad + '_' + t_daygun + daygun, ad.upper() + ad + '_' + t_daygun + daygun,
			ad.upper() + ad.upper() + t_daygun + daygun,			ad.upper() + '_' + ad.upper() + t_daygun + daygun, ad.upper() + '_' + ad.upper() + '_' + t_daygun + daygun, ad.upper() + ad.upper() + '_' + t_daygun + daygun,
			ad.upper() + ad.title() + t_daygun + daygun,			ad.upper() + '_' + ad.title() + t_daygun + daygun, ad.upper() + '_' + ad.title() + '_' + t_daygun + daygun, ad.upper() + ad.title() + '_' + t_daygun + daygun,
			ad.upper() + soyis + t_daygun + daygun,					ad.upper() + '_' + soyis + t_daygun + daygun, ad.upper() + '_' + soyis + '_' + t_daygun + daygun, ad.upper() + soyis + '_' + t_daygun + daygun,
			ad.upper() + soyis.upper() + t_daygun + daygun,			ad.upper() + '_' + soyis.upper() + t_daygun + daygun, ad.upper() + '_' + soyis.upper() + '_' + t_daygun + daygun, ad.upper() + soyis.upper() + '_' + t_daygun + daygun,
			ad.upper() + soyis.title() + t_daygun + daygun,			ad.upper() + '_' + soyis.title() + t_daygun + daygun, ad.upper() + '_' + soyis.title() + '_' + t_daygun + daygun, ad.upper() + soyis.title() + '_' + t_daygun + daygun,
			ad.title() + ad + t_daygun + daygun,					ad.title() + '_' + ad + t_daygun + daygun, ad.title() + '_' + ad + '_' + t_daygun + daygun, ad.title() + ad + '_' + t_daygun + daygun,
			ad.title() + ad.upper() + t_daygun + daygun,			ad.title() + '_' + ad.upper() + t_daygun + daygun, ad.title() + '_' + ad.upper() + '_' + t_daygun + daygun, ad.title() + ad.upper() + '_' + t_daygun + daygun,
			ad.title() + ad.title() + t_daygun + daygun,			ad.title() + '_' + ad.title() + t_daygun + daygun, ad.title() + '_' + ad.title() + '_' + t_daygun + daygun, ad.title() + ad.title() + '_' + t_daygun + daygun,
			ad.title() + soyis + t_daygun + daygun,					ad.title() + '_' + soyis + t_daygun + daygun, ad.title() + '_' + soyis + '_' + t_daygun + daygun, ad.title() + soyis + '_' + t_daygun + daygun,
			ad.title() + soyis.upper() + t_daygun + daygun,			ad.title() + '_' + soyis.upper() + t_daygun + daygun, ad.title() + '_' + soyis.upper() + '_' + t_daygun + daygun, ad.title() + soyis.upper() + '_' + t_daygun + daygun,
			ad.title() + soyis.title() + t_daygun + daygun,			ad.title() + '_' + soyis.title() + t_daygun + daygun, ad.title() + '_' + soyis.title() + '_' + t_daygun + daygun, ad.title() + soyis.title() + '_' + t_daygun + daygun,

			ad.upper() + ad + t_daygun + t_daygun,					ad.upper() + '_' + ad + t_daygun + t_daygun, ad.upper() + '_' + ad + '_' + t_daygun + t_daygun, ad.upper() + ad + '_' + t_daygun + t_daygun,
			ad.upper() + ad.upper() + t_daygun + t_daygun,			ad.upper() + '_' + ad.upper() + t_daygun + t_daygun, ad.upper() + '_' + ad.upper() + '_' + t_daygun + t_daygun, ad.upper() + ad.upper() + '_' + t_daygun + t_daygun,
			ad.upper() + ad.title() + t_daygun + t_daygun,			ad.upper() + '_' + ad.title() + t_daygun + t_daygun, ad.upper() + '_' + ad.title() + '_' + t_daygun + t_daygun, ad.upper() + ad.title() + '_' + t_daygun + t_daygun,
			ad.upper() + soyis + t_daygun + t_daygun,				ad.upper() + '_' + soyis + t_daygun + t_daygun, ad.upper() + '_' + soyis + '_' + t_daygun + t_daygun, ad.upper() + soyis + '_' + t_daygun + t_daygun,
			ad.upper() + soyis.upper() + t_daygun + t_daygun,		ad.upper() + '_' + soyis.upper() + t_daygun + t_daygun, ad.upper() + '_' + soyis.upper() + '_' + t_daygun + t_daygun, ad.upper() + soyis.upper() + '_' + t_daygun + t_daygun,
			ad.upper() + soyis.title() + t_daygun + t_daygun,		ad.upper() + '_' + soyis.title() + t_daygun + t_daygun, ad.upper() + '_' + soyis.title() + '_' + t_daygun + t_daygun, ad.upper() + soyis.title() + '_' + t_daygun + t_daygun,
			ad.title() + ad + t_daygun + t_daygun,					ad.title() + '_' + ad + t_daygun + daygun, ad.title() + '_' + ad + '_' + t_daygun + t_daygun, ad.title() + ad + '_' + t_daygun + t_daygun,
			ad.title() + ad.upper() + t_daygun + t_daygun,			ad.title() + '_' + ad.upper() + t_daygun + daygun, ad.title() + '_' + ad.upper() + '_' + t_daygun + t_daygun, ad.title() + ad.upper() + '_' + t_daygun + t_daygun,
			ad.title() + ad.title() + t_daygun + t_daygun,			ad.title() + '_' + ad.title() + t_daygun + daygun, ad.title() + '_' + ad.title() + '_' + t_daygun + t_daygun, ad.title() + ad.title() + '_' + t_daygun + t_daygun,
			ad.title() + soyis + t_daygun + t_daygun,				ad.title() + '_' + soyis + t_daygun + daygun, ad.title() + '_' + soyis + '_' + t_daygun + t_daygun, ad.title() + soyis + '_' + t_daygun + t_daygun,
			ad.title() + soyis.upper() + t_daygun + t_daygun,		ad.title() + '_' + soyis.upper() + t_daygun + daygun, ad.title() + '_' + soyis.upper() + '_' + t_daygun + t_daygun, ad.title() + soyis.upper() + '_' + t_daygun + t_daygun,
			ad.title() + soyis.title() + t_daygun + t_daygun,		ad.title() + '_' + soyis.title() + t_daygun + daygun, ad.title() + '_' + soyis.title() + '_' + t_daygun + t_daygun, ad.title() + soyis.title() + '_' + t_daygun + t_daygun,

			soyis.upper() + ad + daygun,							soyis.upper() + '_' + ad + daygun, soyis.upper() + '_' + ad + '_' + daygun, soyis.upper() + ad + '_' + daygun,
			soyis.upper() + ad.upper() + daygun,					soyis.upper() + '_' + ad.upper() + daygun, soyis.upper() + '_' + ad.upper() + '_' + daygun, soyis.upper() + ad.upper() + '_' + daygun,
			soyis.upper() + ad.title() + daygun,					soyis.upper() + '_' + ad.title() + daygun, soyis.upper() + '_' + ad.title() + '_' + daygun, soyis.upper() + ad.title() + '_' + daygun,
			soyis.upper() + soyis + daygun,							soyis.upper() + '_' + soyis + daygun, soyis.upper() + '_' + soyis + '_' + daygun, soyis.upper() + soyis + '_' + daygun,
			soyis.upper() + soyis.upper() + daygun,					soyis.upper() + '_' + soyis.upper() + daygun, soyis.upper() + '_' + soyis.upper() + '_' + daygun, soyis.upper() + soyis.upper() + '_' + daygun,
			soyis.upper() + soyis.title() + daygun,					soyis.upper() + '_' + soyis.title() + daygun, soyis.upper() + '_' + soyis.title() + '_' + daygun, soyis.upper() + soyis.title() + '_' + daygun,
			soyis.title() + ad + daygun,							soyis.title() + '_' + ad + daygun, soyis.title() + '_' + ad + '_' + daygun, soyis.title() + ad + '_' + daygun,
			soyis.title() + ad.upper() + daygun,					soyis.title() + '_' + ad.upper() + daygun, soyis.title() + '_' + ad.upper() + '_' + daygun, soyis.title() + ad.upper() + '_' + daygun,
			soyis.title() + ad.title() + daygun,					soyis.title() + '_' + ad.title() + daygun, soyis.title() + '_' + ad.title() + '_' + daygun, soyis.title() + ad.title() + '_' + daygun,
			soyis.title() + soyis + daygun,							soyis.title() + '_' + soyis + daygun, soyis.title() + '_' + soyis + '_' + daygun, soyis.title() + soyis + '_' + daygun,
			soyis.title() + soyis.upper() + daygun,					soyis.title() + '_' + soyis.upper() + daygun, soyis.title() + '_' + soyis.upper() + '_' + daygun, soyis.title() + soyis.upper() + '_' + daygun,
			soyis.title() + soyis.title() + daygun,					soyis.title() + '_' + soyis.title() + daygun, soyis.title() + '_' + soyis.title() + '_' + daygun, soyis.title() + soyis.title() + '_' + daygun,
			
			soyis.upper() + ad + daygun + daygun,					soyis.upper() + '_' + ad + daygun + daygun, soyis.upper() + '_' + ad + '_' + daygun + daygun, soyis.upper() + ad + '_' + daygun + daygun,
			soyis.upper() + ad.upper() + daygun + daygun,			soyis.upper() + '_' + ad.upper() + daygun + daygun, soyis.upper() + '_' + ad.upper() + '_' + daygun + daygun, soyis.upper() + ad.upper() + '_' + daygun + daygun,
			soyis.upper() + ad.title() + daygun + daygun,			soyis.upper() + '_' + ad.title() + daygun + daygun, soyis.upper() + '_' + ad.title() + '_' + daygun + daygun, soyis.upper() + ad.title() + '_' + daygun + daygun,
			soyis.upper() + soyis + daygun + daygun,				soyis.upper() + '_' + soyis + daygun + daygun, soyis.upper() + '_' + soyis + '_' + daygun + daygun, soyis.upper() + soyis + '_' + daygun + daygun,
			soyis.upper() + soyis.upper() + daygun + daygun,		soyis.upper() + '_' + soyis.upper() + daygun + daygun, soyis.upper() + '_' + soyis.upper() + '_' + daygun + daygun, soyis.upper() + soyis.upper() + '_' + daygun + daygun,
			soyis.upper() + soyis.title() + daygun + daygun,		soyis.upper() + '_' + soyis.title() + daygun + daygun, soyis.upper() + '_' + soyis.title() + '_' + daygun + daygun, soyis.upper() + soyis.title() + '_' + daygun + daygun,
			soyis.title() + ad + daygun + daygun,					soyis.title() + '_' + ad + daygun + daygun, soyis.title() + '_' + ad + '_' + daygun + daygun, soyis.title() + ad + '_' + daygun + daygun,
			soyis.title() + ad.upper() + daygun + daygun,			soyis.title() + '_' + ad.upper() + daygun + daygun, soyis.title() + '_' + ad.upper() + '_' + daygun + daygun, soyis.title() + ad.upper() + '_' + daygun + daygun,
			soyis.title() + ad.title() + daygun + daygun,			soyis.title() + '_' + ad.title() + daygun + daygun, soyis.title() + '_' + ad.title() + '_' + daygun + daygun, soyis.title() + ad.title() + '_' + daygun + daygun,
			soyis.title() + soyis + daygun + daygun,				soyis.title() + '_' + soyis + daygun + daygun, soyis.title() + '_' + soyis + '_' + daygun + daygun, soyis.title() + soyis + '_' + daygun + daygun,
			soyis.title() + soyis.upper() + daygun + daygun,		soyis.title() + '_' + soyis.upper() + daygun + daygun, soyis.title() + '_' + soyis.upper() + '_' + daygun + daygun, soyis.title() + soyis.upper() + '_' + daygun + daygun,
			soyis.title() + soyis.title() + daygun + daygun,		soyis.title() + '_' + soyis.title() + daygun + daygun, soyis.title() + '_' + soyis.title() + '_' + daygun + daygun, soyis.title() + soyis.title() + '_' + daygun + daygun,
			
			soyis.upper() + ad + daygun + t_daygun,					soyis.upper() + '_' + ad + daygun + t_daygun, soyis.upper() + '_' + ad + '_' + daygun + t_daygun, soyis.upper() + ad + '_' + daygun + t_daygun,
			soyis.upper() + ad.upper() + daygun + t_daygun,			soyis.upper() + '_' + ad.upper() + daygun + t_daygun, soyis.upper() + '_' + ad.upper() + '_' + daygun + t_daygun, soyis.upper() + ad.upper() + '_' + daygun + t_daygun,
			soyis.upper() + ad.title() + daygun + t_daygun,			soyis.upper() + '_' + ad.title() + daygun + t_daygun, soyis.upper() + '_' + ad.title() + '_' + daygun + t_daygun, soyis.upper() + ad.title() + '_' + daygun + t_daygun,
			soyis.upper() + soyis + daygun + t_daygun,				soyis.upper() + '_' + soyis + daygun + t_daygun, soyis.upper() + '_' + soyis + '_' + daygun + t_daygun, soyis.upper() + soyis + '_' + daygun + t_daygun,
			soyis.upper() + soyis.upper() + daygun + t_daygun,		soyis.upper() + '_' + soyis.upper() + daygun + t_daygun, soyis.upper() + '_' + soyis.upper() + '_' + daygun + t_daygun, soyis.upper() + soyis.upper() + '_' + daygun + t_daygun,
			soyis.upper() + soyis.title() + daygun + t_daygun,		soyis.upper() + '_' + soyis.title() + daygun + t_daygun, soyis.upper() + '_' + soyis.title() + '_' + daygun + t_daygun, soyis.upper() + soyis.title() + '_' + daygun + t_daygun,
			soyis.title() + ad + daygun + t_daygun,					soyis.title() + '_' + ad + daygun + t_daygun, soyis.title() + '_' + ad + '_' + daygun + t_daygun, soyis.title() + ad + '_' + daygun + t_daygun,
			soyis.title() + ad.upper() + daygun + t_daygun,			soyis.title() + '_' + ad.upper() + daygun + t_daygun, soyis.title() + '_' + ad.upper() + '_' + daygun + t_daygun, soyis.title() + ad.upper() + '_' + daygun + t_daygun,
			soyis.title() + ad.title() + daygun + t_daygun,			soyis.title() + '_' + ad.title() + daygun + t_daygun, soyis.title() + '_' + ad.title() + '_' + daygun + t_daygun, soyis.title() + ad.title() + '_' + daygun + t_daygun,
			soyis.title() + soyis + daygun + t_daygun,				soyis.title() + '_' + soyis + daygun + t_daygun, soyis.title() + '_' + soyis + '_' + daygun + t_daygun, soyis.title() + soyis + '_' + daygun + t_daygun,
			soyis.title() + soyis.upper() + daygun + t_daygun,		soyis.title() + '_' + soyis.upper() + daygun + t_daygun, soyis.title() + '_' + soyis.upper() + '_' + daygun + t_daygun, soyis.title() + soyis.upper() + '_' + daygun + t_daygun,
			soyis.title() + soyis.title() + daygun + t_daygun,		soyis.title() + '_' + soyis.title() + daygun + t_daygun, soyis.title() + '_' + soyis.title() + '_' + daygun + t_daygun, soyis.title() + soyis.title() + '_' + daygun + t_daygun,
			
			soyis.upper() + ad + t_daygun,							soyis.upper() + '_' + ad + t_daygun, soyis.upper() + '_' + ad + '_' + t_daygun, soyis.upper() + ad + '_' + t_daygun,
			soyis.upper() + ad.upper() + t_daygun,					soyis.upper() + '_' + ad.upper() + t_daygun, soyis.upper() + '_' + ad.upper() + '_' + t_daygun, soyis.upper() + ad.upper() + '_' + t_daygun,
			soyis.upper() + ad.title() + t_daygun,					soyis.upper() + '_' + ad.title() + t_daygun, soyis.upper() + '_' + ad.title() + '_' + t_daygun, soyis.upper() + ad.title() + '_' + t_daygun,
			soyis.upper() + soyis + t_daygun,						soyis.upper() + '_' + soyis + t_daygun, soyis.upper() + '_' + soyis + '_' + t_daygun, soyis.upper() + soyis + '_' + t_daygun,
			soyis.upper() + soyis.upper() + t_daygun,				soyis.upper() + '_' + soyis.upper() + t_daygun, soyis.upper() + '_' + soyis.upper() + '_' + t_daygun, soyis.upper() + soyis.upper() + '_' + t_daygun,
			soyis.upper() + soyis.title() + t_daygun,				soyis.upper() + '_' + soyis.title() + t_daygun, soyis.upper() + '_' + soyis.title() + '_' + t_daygun, soyis.upper() + soyis.title() + '_' + t_daygun,
			soyis.title() + ad + t_daygun,							soyis.title() + '_' + ad + daygun, soyis.title() + '_' + ad + '_' + t_daygun, soyis.title() + ad + '_' + t_daygun,
			soyis.title() + ad.upper() + t_daygun,					soyis.title() + '_' + ad.upper() + daygun, soyis.title() + '_' + ad.upper() + '_' + t_daygun, soyis.title() + ad.upper() + '_' + t_daygun,
			soyis.title() + ad.title() + t_daygun,					soyis.title() + '_' + ad.title() + daygun, soyis.title() + '_' + ad.title() + '_' + t_daygun, soyis.title() + ad.title() + '_' + t_daygun,
			soyis.title() + soyis + t_daygun,						soyis.title() + '_' + soyis + daygun, soyis.title() + '_' + soyis + '_' + t_daygun, soyis.title() + soyis + '_' + t_daygun,
			soyis.title() + soyis.upper() + t_daygun,				soyis.title() + '_' + soyis.upper() + daygun, soyis.title() + '_' + soyis.upper() + '_' + t_daygun, soyis.title() + soyis.upper() + '_' + t_daygun,
			soyis.title() + soyis.title() + t_daygun,				soyis.title() + '_' + soyis.title() + daygun, soyis.title() + '_' + soyis.title() + '_' + t_daygun, soyis.title() + soyis.title() + '_' + t_daygun,

			soyis.upper() + ad + t_daygun + daygun,					soyis.upper() + '_' + ad + t_daygun + daygun, soyis.upper() + '_' + ad + '_' + t_daygun + daygun, soyis.upper() + ad + '_' + t_daygun + daygun,
			soyis.upper() + ad.upper() + t_daygun + daygun,			soyis.upper() + '_' + ad.upper() + t_daygun + daygun, soyis.upper() + '_' + ad.upper() + '_' + t_daygun + daygun, soyis.upper() + ad.upper() + '_' + t_daygun + daygun,
			soyis.upper() + ad.title() + t_daygun + daygun,			soyis.upper() + '_' + ad.title() + t_daygun + daygun, soyis.upper() + '_' + ad.title() + '_' + t_daygun + daygun, soyis.upper() + ad.title() + '_' + t_daygun + daygun,
			soyis.upper() + soyis + t_daygun + daygun,				soyis.upper() + '_' + soyis + t_daygun + daygun, soyis.upper() + '_' + soyis + '_' + t_daygun + daygun, soyis.upper() + soyis + '_' + t_daygun + daygun,
			soyis.upper() + soyis.upper() + t_daygun + daygun,		soyis.upper() + '_' + soyis.upper() + t_daygun + daygun, soyis.upper() + '_' + soyis.upper() + '_' + t_daygun + daygun, soyis.upper() + soyis.upper() + '_' + t_daygun + daygun,
			soyis.upper() + soyis.title() + t_daygun + daygun,		soyis.upper() + '_' + soyis.title() + t_daygun + daygun, soyis.upper() + '_' + soyis.title() + '_' + t_daygun + daygun, soyis.upper() + soyis.title() + '_' + t_daygun + daygun,
			soyis.title() + ad + t_daygun + daygun,					soyis.title() + '_' + ad + t_daygun + daygun, soyis.title() + '_' + ad + '_' + t_daygun + daygun, soyis.title() + ad + '_' + t_daygun + daygun,
			soyis.title() + ad.upper() + t_daygun + daygun,			soyis.title() + '_' + ad.upper() + t_daygun + daygun, soyis.title() + '_' + ad.upper() + '_' + t_daygun + daygun, soyis.title() + ad.upper() + '_' + t_daygun + daygun,
			soyis.title() + ad.title() + t_daygun + daygun,			soyis.title() + '_' + ad.title() + t_daygun + daygun, soyis.title() + '_' + ad.title() + '_' + t_daygun + daygun, soyis.title() + ad.title() + '_' + t_daygun + daygun,
			soyis.title() + soyis + t_daygun + daygun,				soyis.title() + '_' + soyis + t_daygun + daygun, soyis.title() + '_' + soyis + '_' + t_daygun + daygun, soyis.title() + soyis + '_' + t_daygun + daygun,
			soyis.title() + soyis.upper() + t_daygun + daygun,		soyis.title() + '_' + soyis.upper() + t_daygun + daygun, soyis.title() + '_' + soyis.upper() + '_' + t_daygun + daygun, soyis.title() + soyis.upper() + '_' + t_daygun + daygun,
			soyis.title() + soyis.title() + t_daygun + daygun,		soyis.title() + '_' + soyis.title() + t_daygun + daygun, soyis.title() + '_' + soyis.title() + '_' + t_daygun + daygun, soyis.title() + soyis.title() + '_' + t_daygun + daygun,

			soyis.upper() + ad + t_daygun + t_daygun,				soyis.upper() + '_' + ad + t_daygun + t_daygun, soyis.upper() + '_' + ad + '_' + t_daygun + t_daygun, soyis.upper() + ad + '_' + t_daygun + t_daygun,
			soyis.upper() + ad.upper() + t_daygun + t_daygun,		soyis.upper() + '_' + ad.upper() + t_daygun + t_daygun, soyis.upper() + '_' + ad.upper() + '_' + t_daygun + t_daygun, soyis.upper() + ad.upper() + '_' + t_daygun + t_daygun,
			soyis.upper() + ad.title() + t_daygun + t_daygun,		soyis.upper() + '_' + ad.title() + t_daygun + t_daygun, soyis.upper() + '_' + ad.title() + '_' + t_daygun + t_daygun, soyis.upper() + ad.title() + '_' + t_daygun + t_daygun,
			soyis.upper() + soyis + t_daygun + t_daygun,			soyis.upper() + '_' + soyis + t_daygun + t_daygun, soyis.upper() + '_' + soyis + '_' + t_daygun + t_daygun, soyis.upper() + soyis + '_' + t_daygun + t_daygun,
			soyis.upper() + soyis.upper() + t_daygun + t_daygun,	soyis.upper() + '_' + soyis.upper() + t_daygun + t_daygun, soyis.upper() + '_' + soyis.upper() + '_' + t_daygun + t_daygun, soyis.upper() + soyis.upper() + '_' + t_daygun + t_daygun,
			soyis.upper() + soyis.title() + t_daygun + t_daygun,	soyis.upper() + '_' + soyis.title() + t_daygun + t_daygun, soyis.upper() + '_' + soyis.title() + '_' + t_daygun + t_daygun, soyis.upper() + soyis.title() + '_' + t_daygun + t_daygun,
			soyis.title() + ad + t_daygun + t_daygun,				soyis.title() + '_' + ad + t_daygun + daygun, soyis.title() + '_' + ad + '_' + t_daygun + t_daygun, soyis.title() + ad + '_' + t_daygun + t_daygun,
			soyis.title() + ad.upper() + t_daygun + t_daygun,		soyis.title() + '_' + ad.upper() + t_daygun + daygun, soyis.title() + '_' + ad.upper() + '_' + t_daygun + t_daygun, soyis.title() + ad.upper() + '_' + t_daygun + t_daygun,
			soyis.title() + ad.title() + t_daygun + t_daygun,		soyis.title() + '_' + ad.title() + t_daygun + daygun, soyis.title() + '_' + ad.title() + '_' + t_daygun + t_daygun, soyis.title() + ad.title() + '_' + t_daygun + t_daygun,
			soyis.title() + soyis + t_daygun + t_daygun,			soyis.title() + '_' + soyis + t_daygun + daygun, soyis.title() + '_' + soyis + '_' + t_daygun + t_daygun, soyis.title() + soyis + '_' + t_daygun + t_daygun,
			soyis.title() + soyis.upper() + t_daygun + t_daygun,	soyis.title() + '_' + soyis.upper() + t_daygun + daygun, soyis.title() + '_' + soyis.upper() + '_' + t_daygun + t_daygun, soyis.title() + soyis.upper() + '_' + t_daygun + t_daygun,
			soyis.title() + soyis.title() + t_daygun + t_daygun,	soyis.title() + '_' + soyis.title() + t_daygun + daygun, soyis.title() + '_' + soyis.title() + '_' + t_daygun + t_daygun, soyis.title() + soyis.title() + '_' + t_daygun + t_daygun,

			ad.upper() + dtarihi,									ad.upper() + '_' + dtarihi,
			soyis.upper() + dtarihi,								soyis.upper() + '_' + dtarihi,
			ad.title() + dtarihi,									ad.title() + '_' + dtarihi,
			soyis.title() + dtarihi,								soyis.title() + '_' + dtarihi,
			
			ad.upper() + t_dtarihi,									ad.upper() + '_' + t_dtarihi,
			soyis.upper() + t_dtarihi,								soyis.upper() + '_' + t_dtarihi,
			ad.title() + t_dtarihi,									ad.title() + '_' + t_dtarihi,
			soyis.title() + t_dtarihi,								soyis.title() + '_' + t_dtarihi,
			
			ad.upper() + ad + dtarihi,								ad.upper() + '_' + ad + dtarihi, ad.upper() + '_' + ad + '_' + dtarihi, ad.upper() + ad + '_' + dtarihi,
			ad.upper() + ad.upper() + dtarihi,						ad.upper() + '_' + ad.upper() + dtarihi, ad.upper() + '_' + ad.upper() + '_' + dtarihi, ad.upper() + ad.upper() + '_' + dtarihi,
			ad.upper() + ad.title() + dtarihi,						ad.upper() + '_' + ad.title() + dtarihi, ad.upper() + '_' + ad.title() + '_' + dtarihi, ad.upper() + ad.title() + '_' + dtarihi,
			ad.upper() + soyis + dtarihi,							ad.upper() + '_' + soyis + dtarihi, ad.upper() + '_' + soyis + '_' + dtarihi, ad.upper() + soyis + '_' + dtarihi,
			ad.upper() + soyis.upper() + dtarihi,					ad.upper() + '_' + soyis.upper() + dtarihi, ad.upper() + '_' + soyis.upper() + '_' + dtarihi, ad.upper() + soyis.upper() + '_' + dtarihi,
			ad.upper() + soyis.title() + dtarihi,					ad.upper() + '_' + soyis.title() + dtarihi, ad.upper() + '_' + soyis.title() + '_' + dtarihi, ad.upper() + soyis.title() + '_' + dtarihi,
			ad.title() + ad + dtarihi,								ad.title() + '_' + ad + dtarihi, ad.title() + '_' + ad + '_' + dtarihi, ad.title() + ad + '_' + dtarihi,
			ad.title() + ad.upper() + dtarihi,						ad.title() + '_' + ad.upper() + dtarihi, ad.title() + '_' + ad.upper() + '_' + dtarihi, ad.title() + ad.upper() + '_' + dtarihi,
			ad.title() + ad.title() + dtarihi,						ad.title() + '_' + ad.title() + dtarihi, ad.title() + '_' + ad.title() + '_' + dtarihi, ad.title() + ad.title() + '_' + dtarihi,
			ad.title() + soyis + dtarihi,							ad.title() + '_' + soyis + dtarihi, ad.title() + '_' + soyis + '_' + dtarihi, ad.title() + soyis + '_' + dtarihi,
			ad.title() + soyis.upper() + dtarihi,					ad.title() + '_' + soyis.upper() + dtarihi, ad.title() + '_' + soyis.upper() + '_' + dtarihi, ad.title() + soyis.upper() + '_' + dtarihi,
			ad.title() + soyis.title() + dtarihi,					ad.title() + '_' + soyis.title() + dtarihi, ad.title() + '_' + soyis.title() + '_' + dtarihi, ad.title() + soyis.title() + '_' + dtarihi,
			
			ad.upper() + ad + t_dtarihi,							ad.upper() + '_' + ad + t_dtarihi, ad.upper() + '_' + ad + '_' + t_dtarihi, ad.upper() + ad + '_' + t_dtarihi,
			ad.upper() + ad.upper() + t_dtarihi,					ad.upper() + '_' + ad.upper() + t_dtarihi, ad.upper() + '_' + ad.upper() + '_' + t_dtarihi, ad.upper() + ad.upper() + '_' + t_dtarihi,
			ad.upper() + ad.title() + t_dtarihi,					ad.upper() + '_' + ad.title() + t_dtarihi, ad.upper() + '_' + ad.title() + '_' + t_dtarihi, ad.upper() + ad.title() + '_' + t_dtarihi,
			ad.upper() + soyis + t_dtarihi,							ad.upper() + '_' + soyis + t_dtarihi, ad.upper() + '_' + soyis + '_' + t_dtarihi, ad.upper() + soyis + '_' + t_dtarihi,
			ad.upper() + soyis.upper() + t_dtarihi,					ad.upper() + '_' + soyis.upper() + t_dtarihi, ad.upper() + '_' + soyis.upper() + '_' + t_dtarihi, ad.upper() + soyis.upper() + '_' + t_dtarihi,
			ad.upper() + soyis.title() + t_dtarihi,					ad.upper() + '_' + soyis.title() + t_dtarihi, ad.upper() + '_' + soyis.title() + '_' + t_dtarihi, ad.upper() + soyis.title() + '_' + t_dtarihi,
			ad.title() + ad + t_dtarihi,							ad.title() + '_' + ad + dtarihi, ad.title() + '_' + ad + '_' + t_dtarihi, ad.title() + ad + '_' + t_dtarihi,
			ad.title() + ad.upper() + t_dtarihi,					ad.title() + '_' + ad.upper() + dtarihi, ad.title() + '_' + ad.upper() + '_' + t_dtarihi, ad.title() + ad.upper() + '_' + t_dtarihi,
			ad.title() + ad.title() + t_dtarihi,					ad.title() + '_' + ad.title() + dtarihi, ad.title() + '_' + ad.title() + '_' + t_dtarihi, ad.title() + ad.title() + '_' + t_dtarihi,
			ad.title() + soyis + t_dtarihi,							ad.title() + '_' + soyis + dtarihi, ad.title() + '_' + soyis + '_' + t_dtarihi, ad.title() + soyis + '_' + t_dtarihi,
			ad.title() + soyis.upper() + t_dtarihi,					ad.title() + '_' + soyis.upper() + dtarihi, ad.title() + '_' + soyis.upper() + '_' + t_dtarihi, ad.title() + soyis.upper() + '_' + t_dtarihi,
			ad.title() + soyis.title() + t_dtarihi,					ad.title() + '_' + soyis.title() + dtarihi, ad.title() + '_' + soyis.title() + '_' + t_dtarihi, ad.title() + soyis.title() + '_' + t_dtarihi,

			soyis.upper() + ad + dtarihi,							soyis.upper() + '_' + ad + dtarihi, soyis.upper() + '_' + ad + '_' + dtarihi, soyis.upper() + ad + '_' + dtarihi,
			soyis.upper() + ad.upper() + dtarihi,					soyis.upper() + '_' + ad.upper() + dtarihi, soyis.upper() + '_' + ad.upper() + '_' + dtarihi, soyis.upper() + ad.upper() + '_' + dtarihi,
			soyis.upper() + ad.title() + dtarihi,					soyis.upper() + '_' + ad.title() + dtarihi, soyis.upper() + '_' + ad.title() + '_' + dtarihi, soyis.upper() + ad.title() + '_' + dtarihi,
			soyis.upper() + soyis + dtarihi,						soyis.upper() + '_' + soyis + dtarihi, soyis.upper() + '_' + soyis + '_' + dtarihi, soyis.upper() + soyis + '_' + dtarihi,
			soyis.upper() + soyis.upper() + dtarihi,				soyis.upper() + '_' + soyis.upper() + dtarihi, soyis.upper() + '_' + soyis.upper() + '_' + dtarihi, soyis.upper() + soyis.upper() + '_' + dtarihi,
			soyis.upper() + soyis.title() + dtarihi,				soyis.upper() + '_' + soyis.title() + dtarihi, soyis.upper() + '_' + soyis.title() + '_' + dtarihi, soyis.upper() + soyis.title() + '_' + dtarihi,
			soyis.title() + ad + dtarihi,							soyis.title() + '_' + ad + dtarihi, soyis.title() + '_' + ad + '_' + dtarihi, soyis.title() + ad + '_' + dtarihi,
			soyis.title() + ad.upper() + dtarihi,					soyis.title() + '_' + ad.upper() + dtarihi, soyis.title() + '_' + ad.upper() + '_' + dtarihi, soyis.title() + ad.upper() + '_' + dtarihi,
			soyis.title() + ad.title() + dtarihi,					soyis.title() + '_' + ad.title() + dtarihi, soyis.title() + '_' + ad.title() + '_' + dtarihi, soyis.title() + ad.title() + '_' + dtarihi,
			soyis.title() + soyis + dtarihi,						soyis.title() + '_' + soyis + dtarihi, soyis.title() + '_' + soyis + '_' + dtarihi, soyis.title() + soyis + '_' + dtarihi,
			soyis.title() + soyis.upper() + dtarihi,				soyis.title() + '_' + soyis.upper() + dtarihi, soyis.title() + '_' + soyis.upper() + '_' + dtarihi, soyis.title() + soyis.upper() + '_' + dtarihi,
			soyis.title() + soyis.title() + dtarihi,				soyis.title() + '_' + soyis.title() + dtarihi, soyis.title() + '_' + soyis.title() + '_' + dtarihi, soyis.title() + soyis.title() + '_' + dtarihi,
			
			soyis.upper() + ad + t_dtarihi,							soyis.upper() + '_' + ad + t_dtarihi, soyis.upper() + '_' + ad + '_' + t_dtarihi, soyis.upper() + ad + '_' + t_dtarihi,
			soyis.upper() + ad.upper() + t_dtarihi,					soyis.upper() + '_' + ad.upper() + t_dtarihi, soyis.upper() + '_' + ad.upper() + '_' + t_dtarihi, soyis.upper() + ad.upper() + '_' + t_dtarihi,
			soyis.upper() + ad.title() + t_dtarihi,					soyis.upper() + '_' + ad.title() + t_dtarihi, soyis.upper() + '_' + ad.title() + '_' + t_dtarihi, soyis.upper() + ad.title() + '_' + t_dtarihi,
			soyis.upper() + soyis + t_dtarihi,						soyis.upper() + '_' + soyis + t_dtarihi, soyis.upper() + '_' + soyis + '_' + t_dtarihi, soyis.upper() + soyis + '_' + t_dtarihi,
			soyis.upper() + soyis.upper() + t_dtarihi,				soyis.upper() + '_' + soyis.upper() + t_dtarihi, soyis.upper() + '_' + soyis.upper() + '_' + t_dtarihi, soyis.upper() + soyis.upper() + '_' + t_dtarihi,
			soyis.upper() + soyis.title() + t_dtarihi,				soyis.upper() + '_' + soyis.title() + t_dtarihi, soyis.upper() + '_' + soyis.title() + '_' + t_dtarihi, soyis.upper() + soyis.title() + '_' + t_dtarihi,
			soyis.title() + ad + t_dtarihi,							soyis.title() + '_' + ad + dtarihi, soyis.title() + '_' + ad + '_' + t_dtarihi, soyis.title() + ad + '_' + t_dtarihi,
			soyis.title() + ad.upper() + t_dtarihi,					soyis.title() + '_' + ad.upper() + dtarihi, soyis.title() + '_' + ad.upper() + '_' + t_dtarihi, soyis.title() + ad.upper() + '_' + t_dtarihi,
			soyis.title() + ad.title() + t_dtarihi,					soyis.title() + '_' + ad.title() + dtarihi, soyis.title() + '_' + ad.title() + '_' + t_dtarihi, soyis.title() + ad.title() + '_' + t_dtarihi,
			soyis.title() + soyis + t_dtarihi,						soyis.title() + '_' + soyis + dtarihi, soyis.title() + '_' + soyis + '_' + t_dtarihi, soyis.title() + soyis + '_' + t_dtarihi,
			soyis.title() + soyis.upper() + t_dtarihi,				soyis.title() + '_' + soyis.upper() + dtarihi, soyis.title() + '_' + soyis.upper() + '_' + t_dtarihi, soyis.title() + soyis.upper() + '_' + t_dtarihi,
			soyis.title() + soyis.title() + t_dtarihi,				soyis.title() + '_' + soyis.title() + dtarihi, soyis.title() + '_' + soyis.title() + '_' + t_dtarihi, soyis.title() + soyis.title() + '_' + t_dtarihi

			]

sessiz_sifreler = [s_ad + s_soyis,												s_ad + '_' + s_soyis,
			s_soyis + s_ad,												s_soyis + '_' + s_ad,
			
			s_ad.upper() + s_soyis,										s_ad.upper() + '_' + s_soyis,
			s_ad.upper() + s_soyis.upper(),								s_ad.upper() + '_' + s_soyis.upper(),
			s_ad.upper() + s_soyis.title(),								s_ad.upper() + '_' + s_soyis.title(),
			s_ad.title() + s_soyis,										s_ad.title() + '_' + s_soyis,
			s_ad.title() + s_soyis.upper(),								s_ad.title() + '_' + s_soyis.upper(),
			s_ad.title() + s_soyis.title(),								s_ad.title() + '_' + s_soyis.title(),
			
			s_soyis.upper() + s_ad,										s_soyis.upper() + '_' + s_ad,
			s_soyis.upper() + s_ad.upper(),								s_soyis.upper() + '_' + s_ad.upper(),
			s_soyis.upper() + s_ad.title(),								s_soyis.upper() + '_' + s_ad.title(),
			s_soyis.title() + s_ad,										s_soyis.title() + '_' + s_ad,
			s_soyis.title() + s_ad.upper(),								s_soyis.title() + '_' + s_ad.upper(),
			s_soyis.title() + s_ad.title(),								s_soyis.title() + '_' + s_ad.title(),
			
			#######################################################################################################

			s_ad + s_soyis + pkodu, 									s_ad + '_' + s_soyis + pkodu, s_ad + '_' + s_soyis + '_' + pkodu, s_ad + s_soyis + '_' + pkodu,
			s_soyis + s_ad + pkodu,										s_soyis + '_' + s_ad + pkodu, s_soyis + '_' + s_ad + '_' + pkodu, s_soyis + s_ad + '_' + pkodu,
			
			s_ad + s_soyis + pkodu + pkodu,								s_ad + '_' + s_soyis + pkodu + pkodu, s_ad + '_' + s_soyis + '_' + pkodu + pkodu, s_ad + s_soyis + '_' + pkodu + pkodu,
			s_soyis + s_ad + pkodu + pkodu,								s_soyis + '_' + s_ad + pkodu + pkodu, s_soyis + '_' + s_ad + '_' + pkodu + pkodu, s_soyis + s_ad + '_' + pkodu + pkodu,
			
			s_ad + s_soyis + pkodu + t_pkodu,							s_ad + '_' + s_soyis + pkodu + t_pkodu, s_ad + '_' + s_soyis + '_' + pkodu + t_pkodu, s_ad + s_soyis + '_' + pkodu + t_pkodu,
			s_soyis + s_ad + pkodu + t_pkodu,							s_soyis + '_' + s_ad + pkodu + t_pkodu, s_soyis + '_' + s_ad + '_' + pkodu + t_pkodu, s_soyis + s_ad + '_' + pkodu + t_pkodu,
			
			s_ad + s_soyis + t_pkodu, 									s_ad + '_' + s_soyis + t_pkodu, s_ad + '_' + s_soyis + '_' + t_pkodu, s_ad + s_soyis + '_' + t_pkodu,
			s_soyis + s_ad + t_pkodu,									s_soyis + '_' + s_ad + t_pkodu, s_soyis + '_' + s_ad + '_' + t_pkodu, s_soyis + s_ad + '_' + t_pkodu,
			
			s_ad + s_soyis + t_pkodu + pkodu,							s_ad + '_' + s_soyis + t_pkodu + pkodu, s_ad + '_' + s_soyis + '_' + t_pkodu + pkodu, s_ad + s_soyis + '_' + t_pkodu + pkodu,
			s_soyis + s_ad + t_pkodu + pkodu,							s_soyis + '_' + s_ad + t_pkodu + pkodu, s_soyis + '_' + s_ad + '_' + t_pkodu + pkodu, s_soyis + s_ad + '_' + t_pkodu + pkodu,
			
			s_ad + s_soyis + t_pkodu + t_pkodu,							s_ad + '_' + s_soyis + t_pkodu + t_pkodu, s_ad + '_' + s_soyis + '_' + t_pkodu + t_pkodu, s_ad + s_soyis + '_' + t_pkodu + t_pkodu,
			s_soyis + s_ad + t_pkodu + t_pkodu,							s_soyis + '_' + s_ad + t_pkodu + t_pkodu, s_soyis + '_' + s_ad + '_' + t_pkodu + t_pkodu, s_soyis + s_ad + '_' + t_pkodu + t_pkodu,
			
			#######################################################################################################################################################

			s_ad.upper() + s_soyis + pkodu,								s_ad.upper() + '_' + s_soyis + pkodu, s_ad.upper() + '_' + s_soyis + '_' + pkodu, s_ad.upper() + s_soyis + '_' + pkodu,
			s_ad.upper() + s_soyis.upper() + pkodu,						s_ad.upper() + '_' + s_soyis.upper() + pkodu, s_ad.upper() + '_' + s_soyis.upper() + '_' + pkodu, s_ad.upper() + s_soyis.upper() + '_' + pkodu,
			s_ad.upper() + s_soyis.title() + pkodu,						s_ad.upper() + '_' + s_soyis.title() + pkodu, s_ad.upper() + '_' + s_soyis.title() + '_' + pkodu, s_ad.upper() + s_soyis.title() + '_' + pkodu,
			s_ad.title() + s_soyis + pkodu,								s_ad.title() + '_' + s_soyis + pkodu, s_ad.title() + '_' + s_soyis + '_' + pkodu, s_ad.title() + s_soyis + '_' + pkodu,
			s_ad.title() + s_soyis.upper() + pkodu,						s_ad.title() + '_' + s_soyis.upper() + pkodu, s_ad.title() + '_' + s_soyis.upper() + '_' + pkodu, s_ad.title() + s_soyis.upper() + '_' + pkodu,
			s_ad.title() + s_soyis.title() + pkodu,						s_ad.title() + '_' + s_soyis.title() + pkodu, s_ad.title() + '_' + s_soyis.title() + '_' + pkodu, s_ad.title() + s_soyis.title() + '_' + pkodu,

			s_ad.upper() + s_soyis + pkodu + pkodu,						s_ad.upper() + '_' + s_soyis + pkodu + pkodu, s_ad.upper() + '_' + s_soyis + '_' + pkodu + pkodu, s_ad.upper() + s_soyis + '_' + pkodu + pkodu,
			s_ad.upper() + s_soyis.upper() + pkodu + pkodu,				s_ad.upper() + '_' + s_soyis.upper() + pkodu + pkodu, s_ad.upper() + '_' + s_soyis.upper() + '_' + pkodu + pkodu, s_ad.upper() + s_soyis.upper() + '_' + pkodu + pkodu,
			s_ad.upper() + s_soyis.title() + pkodu + pkodu,				s_ad.upper() + '_' + s_soyis.title() + pkodu + pkodu, s_ad.upper() + '_' + s_soyis.title() + '_' + pkodu + pkodu, s_ad.upper() + s_soyis.title() + '_' + pkodu + pkodu,
			s_ad.title() + s_soyis + pkodu + pkodu,						s_ad.title() + '_' + s_soyis + pkodu + pkodu, s_ad.title() + '_' + s_soyis + '_' + pkodu + pkodu, s_ad.title() + s_soyis + '_' + pkodu + pkodu,
			s_ad.title() + s_soyis.upper() + pkodu + pkodu,				s_ad.title() + '_' + s_soyis.upper() + pkodu + pkodu, s_ad.title() + '_' + s_soyis.upper() + '_' + pkodu + pkodu, s_ad.title() + s_soyis.upper() + '_' + pkodu + pkodu,
			s_ad.title() + s_soyis.title() + pkodu + pkodu,				s_ad.title() + '_' + s_soyis.title() + pkodu + pkodu, s_ad.title() + '_' + s_soyis.title() + '_' + pkodu + pkodu, s_ad.title() + s_soyis.title() + '_' + pkodu + pkodu,
			
			s_ad.upper() + s_soyis + pkodu + t_pkodu,					s_ad.upper() + '_' + s_soyis + pkodu + t_pkodu, s_ad.upper() + '_' + s_soyis + '_' + pkodu + t_pkodu, s_ad.upper() + s_soyis + '_' + pkodu + t_pkodu,
			s_ad.upper() + s_soyis.upper() + pkodu + t_pkodu,			s_ad.upper() + '_' + s_soyis.upper() + pkodu + t_pkodu, s_ad.upper() + '_' + s_soyis.upper() + '_' + pkodu + t_pkodu, s_ad.upper() + s_soyis.upper() + '_' + pkodu + t_pkodu,
			s_ad.upper() + s_soyis.title() + pkodu + t_pkodu,			s_ad.upper() + '_' + s_soyis.title() + pkodu + t_pkodu, s_ad.upper() + '_' + s_soyis.title() + '_' + pkodu + t_pkodu, s_ad.upper() + s_soyis.title() + '_' + pkodu + t_pkodu,
			s_ad.title() + s_soyis + pkodu + t_pkodu,					s_ad.title() + '_' + s_soyis + pkodu + t_pkodu, s_ad.title() + '_' + s_soyis + '_' + pkodu + t_pkodu, s_ad.title() + s_soyis + '_' + pkodu + t_pkodu,
			s_ad.title() + s_soyis.upper() + pkodu + t_pkodu,			s_ad.title() + '_' + s_soyis.upper() + pkodu + t_pkodu, s_ad.title() + '_' + s_soyis.upper() + '_' + pkodu + t_pkodu, s_ad.title() + s_soyis.upper() + '_' + pkodu + t_pkodu,
			s_ad.title() + s_soyis.title() + pkodu + t_pkodu,			s_ad.title() + '_' + s_soyis.title() + pkodu + t_pkodu, s_ad.title() + '_' + s_soyis.title() + '_' + pkodu + t_pkodu, s_ad.title() + s_soyis.title() + '_' + pkodu + t_pkodu,
			
			s_ad.upper() + s_soyis + t_pkodu,							s_ad.upper() + '_' + s_soyis + t_pkodu, s_ad.upper() + '_' + s_soyis + '_' + t_pkodu, s_ad.upper() + s_soyis + '_' + t_pkodu,
			s_ad.upper() + s_soyis.upper() + t_pkodu,					s_ad.upper() + '_' + s_soyis.upper() + t_pkodu, s_ad.upper() + '_' + s_soyis.upper() + '_' + t_pkodu, s_ad.upper() + s_soyis.upper() + '_' + t_pkodu,
			s_ad.upper() + s_soyis.title() + t_pkodu,					s_ad.upper() + '_' + s_soyis.title() + t_pkodu, s_ad.upper() + '_' + s_soyis.title() + '_' + t_pkodu, s_ad.upper() + s_soyis.title() + '_' + t_pkodu,
			s_ad.title() + s_soyis + t_pkodu,							s_ad.title() + '_' + s_soyis + t_pkodu, s_ad.title() + '_' + s_soyis + '_' + t_pkodu, s_ad.title() + s_soyis + '_' + t_pkodu,
			s_ad.title() + s_soyis.upper() + t_pkodu,					s_ad.title() + '_' + s_soyis.upper() + t_pkodu, s_ad.title() + '_' + s_soyis.upper() + '_' + t_pkodu, s_ad.title() + s_soyis.upper() + '_' + t_pkodu,
			s_ad.title() + s_soyis.title() + t_pkodu,					s_ad.title() + '_' + s_soyis.title() + t_pkodu, s_ad.title() + '_' + s_soyis.title() + '_' + t_pkodu, s_ad.title() + s_soyis.title() + '_' + t_pkodu,
			
			s_ad.upper() + s_soyis + t_pkodu + pkodu,					s_ad.upper() + '_' + s_soyis + t_pkodu + pkodu, s_ad.upper() + '_' + s_soyis + '_' + t_pkodu + pkodu, s_ad.upper() + s_soyis + '_' + t_pkodu + pkodu,
			s_ad.upper() + s_soyis.upper() + t_pkodu + pkodu,			s_ad.upper() + '_' + s_soyis.upper() + t_pkodu + pkodu, s_ad.upper() + '_' + s_soyis.upper() + '_' + t_pkodu + pkodu, s_ad.upper() + s_soyis.upper() + '_' + t_pkodu + pkodu,
			s_ad.upper() + s_soyis.title() + t_pkodu + pkodu,			s_ad.upper() + '_' + s_soyis.title() + t_pkodu + pkodu, s_ad.upper() + '_' + s_soyis.title() + '_' + t_pkodu + pkodu, s_ad.upper() + s_soyis.title() + '_' + t_pkodu + pkodu,
			s_ad.title() + s_soyis + t_pkodu + pkodu,					s_ad.title() + '_' + s_soyis + t_pkodu + pkodu, s_ad.title() + '_' + s_soyis + '_' + t_pkodu + pkodu, s_ad.title() + s_soyis + '_' + t_pkodu + pkodu,
			s_ad.title() + s_soyis.upper() + t_pkodu + pkodu,			s_ad.title() + '_' + s_soyis.upper() + t_pkodu + pkodu, s_ad.title() + '_' + s_soyis.upper() + '_' + t_pkodu + pkodu, s_ad.title() + s_soyis.upper() + '_' + t_pkodu + pkodu,
			s_ad.title() + s_soyis.title() + t_pkodu + pkodu,			s_ad.title() + '_' + s_soyis.title() + t_pkodu + pkodu, s_ad.title() + '_' + s_soyis.title() + '_' + t_pkodu + pkodu, s_ad.title() + s_soyis.title() + '_' + t_pkodu + pkodu,
			
			s_ad.upper() + s_soyis + t_pkodu + t_pkodu,					s_ad.upper() + '_' + s_soyis + t_pkodu + t_pkodu, s_ad.upper() + '_' + s_soyis + '_' + t_pkodu + t_pkodu, s_ad.upper() + s_soyis + '_' + t_pkodu + t_pkodu,
			s_ad.upper() + s_soyis.upper() + t_pkodu + t_pkodu,			s_ad.upper() + '_' + s_soyis.upper() + t_pkodu + t_pkodu, s_ad.upper() + '_' + s_soyis.upper() + '_' + t_pkodu + t_pkodu, s_ad.upper() + s_soyis.upper() + '_' + t_pkodu + t_pkodu,
			s_ad.upper() + s_soyis.title() + t_pkodu + t_pkodu,			s_ad.upper() + '_' + s_soyis.title() + t_pkodu + t_pkodu, s_ad.upper() + '_' + s_soyis.title() + '_' + t_pkodu + t_pkodu, s_ad.upper() + s_soyis.title() + '_' + t_pkodu + t_pkodu,
			s_ad.title() + s_soyis + t_pkodu + t_pkodu,					s_ad.title() + '_' + s_soyis + t_pkodu + t_pkodu, s_ad.title() + '_' + s_soyis + '_' + t_pkodu + t_pkodu, s_ad.title() + s_soyis + '_' + t_pkodu + t_pkodu,
			s_ad.title() + s_soyis.upper() + t_pkodu + t_pkodu,			s_ad.title() + '_' + s_soyis.upper() + t_pkodu + t_pkodu, s_ad.title() + '_' + s_soyis.upper() + '_' + t_pkodu + t_pkodu, s_ad.title() + s_soyis.upper() + '_' + t_pkodu + t_pkodu,
			s_ad.title() + s_soyis.title() + t_pkodu + t_pkodu,			s_ad.title() + '_' + s_soyis.title() + t_pkodu + t_pkodu, s_ad.title() + '_' + s_soyis.title() + '_' + t_pkodu + t_pkodu, s_ad.title() + s_soyis.title() + '_' + t_pkodu + t_pkodu,
			
			s_soyis.upper() + s_ad + pkodu,								s_soyis.upper() + '_' + s_ad + pkodu, s_soyis.upper() + '_' + s_ad + '_' + pkodu, s_soyis.upper() + s_ad + '_' + pkodu,
			s_soyis.upper() + s_ad.upper() + pkodu,						s_soyis.upper() + '_' + s_ad.upper() + pkodu, s_soyis.upper() + '_' + s_ad.upper() + '_' + pkodu, s_soyis.upper() + s_ad.upper() + '_' + pkodu,
			s_soyis.upper() + s_ad.title() + pkodu,						s_soyis.upper() + '_' + s_ad.title() + pkodu, s_soyis.upper() + '_' + s_ad.title() + '_' + pkodu, s_soyis.upper() + s_ad.title() + '_' + pkodu,
			s_soyis.title() + s_ad + pkodu,								s_soyis.title() + '_' + s_ad + pkodu, s_soyis.title() + '_' + s_ad + '_' + pkodu, s_soyis.title() + s_ad + '_' + pkodu,
			s_soyis.title() + s_ad.upper() + pkodu,						s_soyis.title() + '_' + s_ad.upper() + pkodu, s_soyis.title() + '_' + s_ad.upper() + '_' + pkodu, s_soyis.title() + s_ad.upper() + '_' + pkodu,
			s_soyis.title() + s_ad.title() + pkodu,						s_soyis.title() + '_' + s_ad.title() + pkodu, s_soyis.title() + '_' + s_ad.title() + '_' + pkodu, s_soyis.title() + s_ad.title() + '_' + pkodu,
			
			s_soyis.upper() + s_ad + pkodu + pkodu,						s_soyis.upper() + '_' + s_ad + pkodu + pkodu, s_soyis.upper() + '_' + s_ad + '_' + pkodu + pkodu, s_soyis.upper() + s_ad + '_' + pkodu + pkodu,
			s_soyis.upper() + s_ad.upper() + pkodu + pkodu,				s_soyis.upper() + '_' + s_ad.upper() + pkodu + pkodu, s_soyis.upper() + '_' + s_ad.upper() + '_' + pkodu + pkodu, s_soyis.upper() + s_ad.upper() + '_' + pkodu + pkodu,
			s_soyis.upper() + s_ad.title() + pkodu + pkodu,				s_soyis.upper() + '_' + s_ad.title() + pkodu + pkodu, s_soyis.upper() + '_' + s_ad.title() + '_' + pkodu + pkodu, s_soyis.upper() + s_ad.title() + '_' + pkodu + pkodu,
			s_soyis.title() + s_ad + pkodu + pkodu,						s_soyis.title() + '_' + s_ad + pkodu + pkodu, s_soyis.title() + '_' + s_ad + '_' + pkodu + pkodu, s_soyis.title() + s_ad + '_' + pkodu + pkodu,
			s_soyis.title() + s_ad.upper() + pkodu + pkodu,				s_soyis.title() + '_' + s_ad.upper() + pkodu + pkodu, s_soyis.title() + '_' + s_ad.upper() + '_' + pkodu + pkodu, s_soyis.title() + s_ad.upper() + '_' + pkodu + pkodu,
			s_soyis.title() + s_ad.title() + pkodu + pkodu,				s_soyis.title() + '_' + s_ad.title() + pkodu + pkodu, s_soyis.title() + '_' + s_ad.title() + '_' + pkodu + pkodu, s_soyis.title() + s_ad.title() + '_' + pkodu + pkodu,
			
			s_soyis.upper() + s_ad + pkodu + t_pkodu,					s_soyis.upper() + '_' + s_ad + pkodu + t_pkodu, s_soyis.upper() + '_' + s_ad + '_' + pkodu + t_pkodu, s_soyis.upper() + s_ad + '_' + pkodu + t_pkodu,
			s_soyis.upper() + s_ad.upper() + pkodu + t_pkodu,  			s_soyis.upper() + '_' + s_ad.upper() + pkodu + t_pkodu, s_soyis.upper() + '_' + s_ad.upper() + '_' + pkodu + t_pkodu, s_soyis.upper() + s_ad.upper() + '_' + pkodu + t_pkodu,
			s_soyis.upper() + s_ad.title() + pkodu + t_pkodu,			s_soyis.upper() + '_' + s_ad.title() + pkodu + t_pkodu, s_soyis.upper() + '_' + s_ad.title() + '_' + pkodu + t_pkodu, s_soyis.upper() + s_ad.title() + '_' + pkodu + t_pkodu,
			s_soyis.title() + s_ad + pkodu + t_pkodu,					s_soyis.title() + '_' + s_ad + pkodu + t_pkodu, s_soyis.title() + '_' + s_ad + '_' + pkodu + t_pkodu, s_soyis.title() + s_ad + '_' + pkodu + t_pkodu,
			s_soyis.title() + s_ad.upper() + pkodu + t_pkodu,			s_soyis.title() + '_' + s_ad.upper() + pkodu + t_pkodu, s_soyis.title() + '_' + s_ad.upper() + '_' + pkodu + t_pkodu, s_soyis.title() + s_ad.upper() + '_' + pkodu + t_pkodu,
			s_soyis.title() + s_ad.title() + pkodu + t_pkodu,			s_soyis.title() + '_' + s_ad.title() + pkodu + t_pkodu, s_soyis.title() + '_' + s_ad.title() + '_' + pkodu + t_pkodu, s_soyis.title() + s_ad.title() + '_' + pkodu + t_pkodu,
			
			
			s_soyis.upper() + s_ad + t_pkodu,							s_soyis.upper() + '_' + s_ad + t_pkodu, s_soyis.upper() + '_' + s_ad + '_' + t_pkodu, s_soyis.upper() + s_ad + '_' + t_pkodu,
			s_soyis.upper() + s_ad.upper() + t_pkodu,					s_soyis.upper() + '_' + s_ad.upper() + t_pkodu, s_soyis.upper() + '_' + s_ad.upper() + '_' + t_pkodu, s_soyis.upper() + s_ad.upper() + '_' + t_pkodu,
			s_soyis.upper() + s_ad.title() + t_pkodu,					s_soyis.upper() + '_' + s_ad.title() + t_pkodu, s_soyis.upper() + '_' + s_ad.title() + '_' + t_pkodu, s_soyis.upper() + s_ad.title() + '_' + t_pkodu,
			s_soyis.title() + s_ad + t_pkodu,							s_soyis.title() + '_' + s_ad + t_pkodu, s_soyis.title() + '_' + s_ad + '_' + t_pkodu, s_soyis.title() + s_ad + '_' + t_pkodu,
			s_soyis.title() + s_ad.upper() + t_pkodu,					s_soyis.title() + '_' + s_ad.upper() + t_pkodu, s_soyis.title() + '_' + s_ad.upper() + '_' + t_pkodu, s_soyis.title() + s_ad.upper() + '_' + t_pkodu,
			s_soyis.title() + s_ad.title() + t_pkodu,					s_soyis.title() + '_' + s_ad.title() + t_pkodu, s_soyis.title() + '_' + s_ad.title() + '_' + t_pkodu, s_soyis.title() + s_ad.title() + '_' + t_pkodu,
			
			s_soyis.upper() + s_ad + t_pkodu + pkodu,					s_soyis.upper() + '_' + s_ad + t_pkodu + pkodu, s_soyis.upper() + '_' + s_ad + '_' + t_pkodu + pkodu, s_soyis.upper() + s_ad + '_' + t_pkodu + pkodu,
			s_soyis.upper() + s_ad.upper() + t_pkodu + pkodu,			s_soyis.upper() + '_' + s_ad.upper() + t_pkodu + pkodu, s_soyis.upper() + '_' + s_ad.upper() + '_' + t_pkodu + pkodu, s_soyis.upper() + s_ad.upper() + '_' + t_pkodu + pkodu,
			s_soyis.upper() + s_ad.title() + t_pkodu + pkodu,			s_soyis.upper() + '_' + s_ad.title() + t_pkodu + pkodu, s_soyis.upper() + '_' + s_ad.title() + '_' + t_pkodu + pkodu, s_soyis.upper() + s_ad.title() + '_' + t_pkodu + pkodu,
			s_soyis.title() + s_ad + t_pkodu + pkodu,					s_soyis.title() + '_' + s_ad + t_pkodu + pkodu, s_soyis.title() + '_' + s_ad + '_' + t_pkodu + pkodu, s_soyis.title() + s_ad + '_' + t_pkodu + pkodu,
			s_soyis.title() + s_ad.upper() + t_pkodu + pkodu,			s_soyis.title() + '_' + s_ad.upper() + t_pkodu + pkodu, s_soyis.title() + '_' + s_ad.upper() + '_' + t_pkodu + pkodu, s_soyis.title() + s_ad.upper() + '_' + t_pkodu + pkodu,
			s_soyis.title() + s_ad.title() + t_pkodu + pkodu,			s_soyis.title() + '_' + s_ad.title() + t_pkodu + pkodu, s_soyis.title() + '_' + s_ad.title() + '_' + t_pkodu + pkodu, s_soyis.title() + s_ad.title() + '_' + t_pkodu + pkodu,
			
			s_soyis.upper() + s_ad + t_pkodu + t_pkodu,					s_soyis.upper() + '_' + s_ad + t_pkodu + t_pkodu, s_soyis.upper() + '_' + s_ad + '_' + t_pkodu + t_pkodu, s_soyis.upper() + s_ad + '_' + t_pkodu + t_pkodu,
			s_soyis.upper() + s_ad.upper() + t_pkodu + t_pkodu,			s_soyis.upper() + '_' + s_ad.upper() + t_pkodu + t_pkodu, s_soyis.upper() + '_' + s_ad.upper() + '_' + t_pkodu + t_pkodu, s_soyis.upper() + s_ad.upper() + '_' + t_pkodu + t_pkodu,
			s_soyis.upper() + s_ad.title() + t_pkodu + t_pkodu,			s_soyis.upper() + '_' + s_ad.title() + t_pkodu + t_pkodu, s_soyis.upper() + '_' + s_ad.title() + '_' + t_pkodu + t_pkodu, s_soyis.upper() + s_ad.title() + '_' + t_pkodu + t_pkodu,
			s_soyis.title() + s_ad + t_pkodu + t_pkodu,					s_soyis.title() + '_' + s_ad + t_pkodu + t_pkodu, s_soyis.title() + '_' + s_ad + '_' + t_pkodu + t_pkodu, s_soyis.title() + s_ad + '_' + t_pkodu + t_pkodu,
			s_soyis.title() + s_ad.upper() + t_pkodu + t_pkodu,			s_soyis.title() + '_' + s_ad.upper() + t_pkodu + t_pkodu, s_soyis.title() + '_' + s_ad.upper() + '_' + t_pkodu + t_pkodu, s_soyis.title() + s_ad.upper() + '_' + t_pkodu + t_pkodu,
			s_soyis.title() + s_ad.title() + t_pkodu + t_pkodu,			s_soyis.title() + '_' + s_ad.title() + t_pkodu + t_pkodu, s_soyis.title() + '_' + s_ad.title() + '_' + t_pkodu + t_pkodu, s_soyis.title() + s_ad.title() + '_' + t_pkodu + t_pkodu,
			
			#########################################################################################################################################################################################

			s_ad + s_soyis + dyili, 									s_ad + '_' + s_soyis + dyili, s_ad + '_' + s_soyis + '_' + dyili, s_ad + s_soyis + '_' + dyili,
			s_soyis + s_ad + dyili,										s_soyis + '_' + s_ad + dyili, s_soyis + '_' + s_ad + '_' + dyili, s_soyis + s_ad + '_' + dyili,
			
			s_ad + s_soyis + dyili + dyili,								s_ad + '_' + s_soyis + dyili + dyili, s_ad + '_' + s_soyis + '_' + dyili + dyili, s_ad + s_soyis + '_' + dyili + dyili,
			s_soyis + s_ad + dyili + dyili,								s_soyis + '_' + s_ad + dyili + dyili, s_soyis + '_' + s_ad + '_' + dyili + dyili, s_soyis + s_ad + '_' + dyili + dyili,
									
			s_ad + s_soyis + dyili + t_dyili,							s_ad + '_' + s_soyis + dyili + t_dyili, s_ad + '_' + s_soyis + '_' + dyili + t_dyili, s_ad + s_soyis + '_' + dyili + t_dyili,
			s_soyis + s_ad + dyili + t_dyili,							s_soyis + '_' + s_ad + dyili + t_dyili, s_soyis + '_' + s_ad + '_' + dyili + t_dyili, s_soyis + s_ad + '_' + dyili + t_dyili,
			
			s_ad + s_soyis + t_dyili, 									s_ad + '_' + s_soyis + t_dyili, s_ad + '_' + s_soyis + '_' + t_dyili, s_ad + s_soyis + '_' + t_dyili,
			s_soyis + s_ad + t_dyili,									s_soyis + '_' + s_ad + t_dyili, s_soyis + '_' + s_ad + '_' + t_dyili, s_soyis + s_ad + '_' + t_dyili,
			
			s_ad + s_soyis + t_dyili + dyili,							s_ad + '_' + s_soyis + t_dyili + dyili, s_ad + '_' + s_soyis + '_' + t_dyili + dyili, s_ad + s_soyis + '_' + t_dyili + dyili,
			s_soyis + s_ad + t_dyili + dyili,							s_soyis + '_' + s_ad + t_dyili + dyili, s_soyis + '_' + s_ad + '_' + t_dyili + dyili, s_soyis + s_ad + '_' + t_dyili + dyili,
			
			s_ad + s_soyis + t_dyili + t_dyili,							s_ad + '_' + s_soyis + t_dyili + t_dyili, s_ad + '_' + s_soyis + '_' + t_dyili + t_dyili, s_ad + s_soyis + '_' + t_dyili + t_dyili,
			s_soyis + s_ad + t_dyili + t_dyili,							s_soyis + '_' + s_ad + t_dyili + t_dyili, s_soyis + '_' + s_ad + '_' + t_dyili + t_dyili, s_soyis + s_ad + '_' + t_dyili + t_dyili,
			
			s_ad + s_soyis + daygun,									s_ad + '_' + s_soyis + daygun, s_ad + '_' + s_soyis + '_' + daygun, s_ad + s_soyis + '_' + daygun,
			s_soyis + s_ad + daygun,									s_soyis + '_' + s_ad + daygun, s_soyis + '_' + s_ad + '_' + daygun, s_soyis + s_ad + '_' + daygun,
			
			s_ad + s_soyis + t_daygun,									s_soyis + '_' + s_ad + t_daygun, s_soyis + '_' + s_ad + '_' + t_daygun, s_soyis + s_ad + '_' + t_daygun,
			s_soyis + s_ad + t_daygun,									s_soyis + '_' + s_ad + t_daygun, s_soyis + '_' + s_ad + '_' + t_daygun, s_soyis + s_ad + '_' + t_daygun,
			
			#######################################################################################################################################################

			s_ad.upper() + s_soyis + dyili,								s_ad.upper() + '_' + s_soyis + dyili, s_ad.upper() + '_' + s_soyis + '_' + dyili, s_ad.upper() + s_soyis + '_' + dyili,
			s_ad.upper() + s_soyis.upper() + dyili,						s_ad.upper() + '_' + s_soyis.upper() + dyili, s_ad.upper() + '_' + s_soyis.upper() + '_' + dyili, s_ad.upper() + s_soyis.upper() + '_' + dyili,
			s_ad.upper() + s_soyis.title() + dyili,						s_ad.upper() + '_' + s_soyis.title() + dyili, s_ad.upper() + '_' + s_soyis.title() + '_' + dyili, s_ad.upper() + s_soyis.title() + '_' + dyili,
			s_ad.title() + s_soyis + dyili,								s_ad.title() + '_' + s_soyis + dyili, s_ad.title() + '_' + s_soyis + '_' + dyili, s_ad.title() + s_soyis + '_' + dyili,
			s_ad.title() + s_soyis.upper() + dyili,						s_ad.title() + '_' + s_soyis.upper() + dyili, s_ad.title() + '_' + s_soyis.upper() + '_' + dyili, s_ad.title() + s_soyis.upper() + '_' + dyili,
			s_ad.title() + s_soyis.title() + dyili,						s_ad.title() + '_' + s_soyis.title() + dyili, s_ad.title() + '_' + s_soyis.title() + '_' + dyili, s_ad.title() + s_soyis.title() + '_' + dyili,
			
			s_ad.upper() + s_soyis + dyili + dyili,						s_ad.upper() + '_' + s_soyis + dyili + dyili, s_ad.upper() + '_' + s_soyis + '_' + dyili + dyili, s_ad.upper() + s_soyis + '_' + dyili + dyili,
			s_ad.upper() + s_soyis.upper() + dyili + dyili,				s_ad.upper() + '_' + s_soyis.upper() + dyili + dyili, s_ad.upper() + '_' + s_soyis.upper() + '_' + dyili + dyili, s_ad.upper() + s_soyis.upper() + '_' + dyili + dyili,
			s_ad.upper() + s_soyis.title() + dyili + dyili,				s_ad.upper() + '_' + s_soyis.title() + dyili + dyili, s_ad.upper() + '_' + s_soyis.title() + '_' + dyili + dyili, s_ad.upper() + s_soyis.title() + '_' + dyili + dyili,
			s_ad.title() + s_soyis + dyili + dyili,						s_ad.title() + '_' + s_soyis + dyili + dyili, s_ad.title() + '_' + s_soyis + '_' + dyili + dyili, s_ad.title() + s_soyis + '_' + dyili + dyili,
			s_ad.title() + s_soyis.upper() + dyili + dyili,				s_ad.title() + '_' + s_soyis.upper() + dyili + dyili, s_ad.title() + '_' + s_soyis.upper() + '_' + dyili + dyili, s_ad.title() + s_soyis.upper() + '_' + dyili + dyili,
			s_ad.title() + s_soyis.title() + dyili + dyili,				s_ad.title() + '_' + s_soyis.title() + dyili + dyili, s_ad.title() + '_' + s_soyis.title() + '_' + dyili + dyili, s_ad.title() + s_soyis.title() + '_' + dyili + dyili,
			
			s_ad.upper() + s_soyis + dyili + t_dyili,					s_ad.upper() + '_' + s_soyis + dyili + t_dyili, s_ad.upper() + '_' + s_soyis + '_' + dyili + t_dyili, s_ad.upper() + s_soyis + '_' + dyili + t_dyili,
			s_ad.upper() + s_soyis.upper() + dyili + t_dyili,			s_ad.upper() + '_' + s_soyis.upper() + dyili + t_dyili, s_ad.upper() + '_' + s_soyis.upper() + '_' + dyili + t_dyili, s_ad.upper() + s_soyis.upper() + '_' + dyili + t_dyili,
			s_ad.upper() + s_soyis.title() + dyili + t_dyili,			s_ad.upper() + '_' + s_soyis.title() + dyili + t_dyili, s_ad.upper() + '_' + s_soyis.title() + '_' + dyili + t_dyili, s_ad.upper() + s_soyis.title() + '_' + dyili + t_dyili,
			s_ad.title() + s_soyis + dyili + t_dyili,					s_ad.title() + '_' + s_soyis + dyili + t_dyili, s_ad.title() + '_' + s_soyis + '_' + dyili + t_dyili, s_ad.title() + s_soyis + '_' + dyili + t_dyili,
			s_ad.title() + s_soyis.upper() + dyili + t_dyili,			s_ad.title() + '_' + s_soyis.upper() + dyili + t_dyili, s_ad.title() + '_' + s_soyis.upper() + '_' + dyili + t_dyili, s_ad.title() + s_soyis.upper() + '_' + dyili + t_dyili,
			s_ad.title() + s_soyis.title() + dyili + t_dyili,			s_ad.title() + '_' + s_soyis.title() + dyili + t_dyili, s_ad.title() + '_' + s_soyis.title() + '_' + dyili + t_dyili, s_ad.title() + s_soyis.title() + '_' + dyili + t_dyili,
			
			s_ad.upper() + s_soyis + t_dyili,							s_ad.upper() + '_' + s_soyis + t_dyili, s_ad.upper() + '_' + s_soyis + '_' + t_dyili, s_ad.upper() + s_soyis + '_' + t_dyili,
			s_ad.upper() + s_soyis.upper() + t_dyili,					s_ad.upper() + '_' + s_soyis.upper() + t_dyili, s_ad.upper() + '_' + s_soyis.upper() + '_' + t_dyili, s_ad.upper() + s_soyis.upper() + '_' + t_dyili,
			s_ad.upper() + s_soyis.title() + t_dyili,					s_ad.upper() + '_' + s_soyis.title() + t_dyili, s_ad.upper() + '_' + s_soyis.title() + '_' + t_dyili, s_ad.upper() + s_soyis.title() + '_' + t_dyili,
			s_ad.title() + s_soyis + t_dyili,							s_ad.title() + '_' + s_soyis + t_dyili, s_ad.title() + '_' + s_soyis + '_' + t_dyili, s_ad.title() + s_soyis + '_' + t_dyili,
			s_ad.title() + s_soyis.upper() + t_dyili,					s_ad.title() + '_' + s_soyis.upper() + t_dyili, s_ad.title() + '_' + s_soyis.upper() + '_' + t_dyili, s_ad.title() + s_soyis.upper() + '_' + t_dyili,
			s_ad.title() + s_soyis.title() + t_dyili,					s_ad.title() + '_' + s_soyis.title() + t_dyili, s_ad.title() + '_' + s_soyis.title() + '_' + t_dyili, s_ad.title() + s_soyis.title() + '_' + t_dyili,

			s_ad.upper() + s_soyis + t_dyili + dyili,					s_ad.upper() + '_' + s_soyis + t_dyili + dyili, s_ad.upper() + '_' + s_soyis + '_' + t_dyili + dyili, s_ad.upper() + s_soyis + '_' + t_dyili + dyili,
			s_ad.upper() + s_soyis.upper() + t_dyili + dyili,			s_ad.upper() + '_' + s_soyis.upper() + t_dyili + dyili, s_ad.upper() + '_' + s_soyis.upper() + '_' + t_dyili + dyili, s_ad.upper() + s_soyis.upper() + '_' + t_dyili + dyili,
			s_ad.upper() + s_soyis.title() + t_dyili + dyili,			s_ad.upper() + '_' + s_soyis.title() + t_dyili + dyili, s_ad.upper() + '_' + s_soyis.title() + '_' + t_dyili + dyili, s_ad.upper() + s_soyis.title() + '_' + t_dyili + dyili,
			s_ad.title() + s_soyis + t_dyili + dyili,					s_ad.title() + '_' + s_soyis + t_dyili + dyili, s_ad.title() + '_' + s_soyis + '_' + t_dyili + dyili, s_ad.title() + s_soyis + '_' + t_dyili + dyili,
			s_ad.title() + s_soyis.upper() + t_dyili + dyili,			s_ad.title() + '_' + s_soyis.upper() + t_dyili + dyili, s_ad.title() + '_' + s_soyis.upper() + '_' + t_dyili + dyili, s_ad.title() + s_soyis.upper() + '_' + t_dyili + dyili,
			s_ad.title() + s_soyis.title() + t_dyili + dyili,			s_ad.title() + '_' + s_soyis.title() + t_dyili + dyili, s_ad.title() + '_' + s_soyis.title() + '_' + t_dyili + dyili, s_ad.title() + s_soyis.title() + '_' + t_dyili + dyili,

			s_ad.upper() + s_soyis + t_dyili + t_dyili,					s_ad.upper() + '_' + s_soyis + t_dyili + t_dyili, s_ad.upper() + '_' + s_soyis + '_' + t_dyili + t_dyili, s_ad.upper() + s_soyis + '_' + t_dyili + t_dyili,
			s_ad.upper() + s_soyis.upper() + t_dyili + t_dyili,			s_ad.upper() + '_' + s_soyis.upper() + t_dyili + t_dyili, s_ad.upper() + '_' + s_soyis.upper() + '_' + t_dyili + t_dyili,s_ad.upper() + s_soyis.upper() + '_' + t_dyili + t_dyili,
			s_ad.upper() + s_soyis.title() + t_dyili + t_dyili,			s_ad.upper() + '_' + s_soyis.title() + t_dyili + t_dyili, s_ad.upper() + '_' + s_soyis.title() + '_' + t_dyili + t_dyili, s_ad.upper() + s_soyis.title() + '_' + t_dyili + t_dyili,
			s_ad.title() + s_soyis + t_dyili + t_dyili,					s_ad.title() + '_' + s_soyis + t_dyili + t_dyili, s_ad.title() + '_' + s_soyis + '_' + t_dyili + t_dyili, s_ad.title() + s_soyis + '_' + t_dyili + t_dyili,
			s_ad.title() + s_soyis.upper() + t_dyili + t_dyili,			s_ad.title() + '_' + s_soyis.upper() + t_dyili + t_dyili, s_ad.title() + '_' + s_soyis.upper() + '_' + t_dyili + t_dyili, s_ad.title() + s_soyis.upper() + '_' + t_dyili + t_dyili,
			s_ad.title() + s_soyis.title() + t_dyili + t_dyili,			s_ad.title() + '_' + s_soyis.title() + t_dyili + t_dyili, s_ad.title() + '_' + s_soyis.title() + '_' + t_dyili + t_dyili, s_ad.title() + s_soyis.title() + '_' + t_dyili + t_dyili,

			s_soyis.upper() + s_ad + dyili,								s_soyis.upper() + '_' + s_ad + dyili, s_soyis.upper() + '_' + s_ad + '_' + dyili, s_soyis.upper() + s_ad + '_' + dyili,
			s_soyis.upper() + s_ad.upper() + dyili,						s_soyis.upper() + '_' + s_ad.upper() + dyili, s_soyis.upper() + '_' + s_ad.upper() + '_' + dyili, s_soyis.upper() + s_ad.upper() + '_' + dyili,
			s_soyis.upper() + s_ad.title() + dyili,						s_soyis.upper() + '_' + s_ad.title() + dyili, s_soyis.upper() + '_' + s_ad.title() + '_' + dyili, s_soyis.upper() + s_ad.title() + '_' + dyili,
			s_soyis.title() + s_ad + dyili,								s_soyis.title() + '_' + s_ad + dyili, s_soyis.title() + '_' + s_ad + '_' + dyili, s_soyis.title() + s_ad + '_' + dyili,
			s_soyis.title() + s_ad.upper() + dyili,						s_soyis.title() + '_' + s_ad.upper() + dyili, s_soyis.title() + '_' + s_ad.upper() + '_' + dyili, s_soyis.title() + s_ad.upper() + '_' + dyili,
			s_soyis.title() + s_ad.title() + dyili,						s_soyis.title() + '_' + s_ad.title() + dyili, s_soyis.title() + '_' + s_ad.title() + '_' + dyili, s_soyis.title() + s_ad.title() + '_' + dyili,
			
			s_soyis.upper() + s_ad + dyili + dyili,						s_soyis.upper() + '_' + s_ad + dyili + dyili, s_soyis.upper() + '_' + s_ad + '_' + dyili + dyili, s_soyis.upper() + s_ad + '_' + dyili + dyili,
			s_soyis.upper() + s_ad.upper() + dyili + dyili,				s_soyis.upper() + '_' + s_ad.upper() + dyili + dyili, s_soyis.upper() + '_' + s_ad.upper() + '_' + dyili + dyili, s_soyis.upper() + s_ad.upper() + '_' + dyili + dyili,
			s_soyis.upper() + s_ad.title() + dyili + dyili,				s_soyis.upper() + '_' + s_ad.title() + dyili + dyili, s_soyis.upper() + '_' + s_ad.title() + '_' + dyili + dyili, s_soyis.upper() + s_ad.title() + '_' + dyili + dyili,
			s_soyis.title() + s_ad + dyili + dyili,						s_soyis.title() + '_' + s_ad + dyili + dyili, s_soyis.title() + '_' + s_ad + '_' + dyili + dyili, s_soyis.title() + s_ad + '_' + dyili + dyili,
			s_soyis.title() + s_ad.upper() + dyili + dyili,				s_soyis.title() + '_' + s_ad.upper() + dyili + dyili, s_soyis.title() + '_' + s_ad.upper() + '_' + dyili + dyili, s_soyis.title() + s_ad.upper() + '_' + dyili + dyili,
			s_soyis.title() + s_ad.title() + dyili + dyili,				s_soyis.title() + '_' + s_ad.title() + dyili + dyili, s_soyis.title() + '_' + s_ad.title() + '_' + dyili + dyili, s_soyis.title() + s_ad.title() + '_' + dyili + dyili,
			
			s_soyis.upper() + s_ad + dyili + t_dyili,					s_soyis.upper() + '_' + s_ad + dyili + t_dyili, s_soyis.upper() + '_' + s_ad + '_' + dyili + t_dyili, s_soyis.upper() + s_ad + '_' + dyili + t_dyili,
			s_soyis.upper() + s_ad.upper() + dyili + t_dyili,  			s_soyis.upper() + '_' + s_ad.upper() + dyili + t_dyili, s_soyis.upper() + '_' + s_ad.upper() + '_' + dyili + t_dyili, s_soyis.upper() + s_ad.upper() + '_' + dyili + t_dyili,
			s_soyis.upper() + s_ad.title() + dyili + t_dyili,			s_soyis.upper() + '_' + s_ad.title() + dyili + t_dyili, s_soyis.upper() + '_' + s_ad.title() + '_' + dyili + t_dyili, s_soyis.upper() + s_ad.title() + '_' + dyili + t_dyili,
			s_soyis.title() + s_ad + dyili + t_dyili,					s_soyis.title() + '_' + s_ad + dyili + t_dyili, s_soyis.title() + '_' + s_ad + '_' + dyili + t_dyili, s_soyis.title() + s_ad + '_' + dyili + t_dyili,
			s_soyis.title() + s_ad.upper() + dyili + t_dyili,			s_soyis.title() + '_' + s_ad.upper() + dyili + t_dyili, s_soyis.title() + '_' + s_ad.upper() + '_' + dyili + t_dyili, s_soyis.title() + s_ad.upper() + '_' + dyili + t_dyili,
			s_soyis.title() + s_ad.title() + dyili + t_dyili,			s_soyis.title() + '_' + s_ad.title() + dyili + t_dyili, s_soyis.title() + '_' + s_ad.title() + '_' + dyili + t_dyili, s_soyis.title() + s_ad.title() + '_' + dyili + t_dyili,
			
			s_soyis.upper() + s_ad + t_dyili,							s_soyis.upper() + '_' + s_ad + t_dyili, s_soyis.upper() + '_' + s_ad + '_' + t_dyili, s_soyis.upper() + s_ad + '_' + t_dyili,
			s_soyis.upper() + s_ad.upper() + t_dyili,					s_soyis.upper() + '_' + s_ad.upper() + t_dyili, s_soyis.upper() + '_' + s_ad.upper() + '_' + t_dyili, s_soyis.upper() + s_ad.upper() + '_' + t_dyili,
			s_soyis.upper() + s_ad.title() + t_dyili,					s_soyis.upper() + '_' + s_ad.title() + t_dyili, s_soyis.upper() + '_' + s_ad.title() + '_' + t_dyili, s_soyis.upper() + s_ad.title() + '_' + t_dyili,
			s_soyis.title() + s_ad + t_dyili,							s_soyis.title() + '_' + s_ad + t_dyili, s_soyis.title() + '_' + s_ad + '_' + t_dyili, s_soyis.title() + s_ad + '_' + t_dyili,
			s_soyis.title() + s_ad.upper() + t_dyili,					s_soyis.title() + '_' + s_ad.upper() + t_dyili, s_soyis.title() + '_' + s_ad.upper() + '_' + t_dyili, s_soyis.title() + s_ad.upper() + '_' + t_dyili,
			s_soyis.title() + s_ad.title() + t_dyili,					s_soyis.title() + '_' + s_ad.title() + t_dyili, s_soyis.title() + '_' + s_ad.title() + '_' + t_dyili, s_soyis.title() + s_ad.title() + '_' + t_dyili,
			
			s_soyis.upper() + s_ad + t_dyili + dyili,					s_soyis.upper() + '_' + s_ad + t_dyili + dyili, s_soyis.upper() + '_' + s_ad + '_' + t_dyili + dyili, s_soyis.upper() + s_ad + '_' + t_dyili + dyili,
			s_soyis.upper() + s_ad.upper() + t_dyili + dyili,			s_soyis.upper() + '_' + s_ad.upper() + t_dyili + dyili, s_soyis.upper() + '_' + s_ad.upper() + '_' + t_dyili + dyili, s_soyis.upper() + s_ad.upper() + '_' + t_dyili + dyili,
			s_soyis.upper() + s_ad.title() + t_dyili + dyili,			s_soyis.upper() + '_' + s_ad.title() + t_dyili + dyili, s_soyis.upper() + '_' + s_ad.title() + '_' + t_dyili + dyili, s_soyis.upper() + s_ad.title() + '_' + t_dyili + dyili,
			s_soyis.title() + s_ad + t_dyili + dyili,					s_soyis.title() + '_' + s_ad + t_dyili + dyili, s_soyis.title() + '_' + s_ad + '_' + t_dyili + dyili, s_soyis.title() + s_ad + '_' + t_dyili + dyili,
			s_soyis.title() + s_ad.upper() + t_dyili + dyili,			s_soyis.title() + '_' + s_ad.upper() + t_dyili + dyili, s_soyis.title() + '_' + s_ad.upper() + '_' + t_dyili + dyili, s_soyis.title() + s_ad.upper() + '_' + t_dyili + dyili,
			s_soyis.title() + s_ad.title() + t_dyili + dyili,			s_soyis.title() + '_' + s_ad.title() + t_dyili + dyili, s_soyis.title() + '_' + s_ad.title() + '_' + t_dyili + dyili, s_soyis.title() + s_ad.title() + '_' + t_dyili + dyili,
			
			s_soyis.upper() + s_ad + t_dyili + t_dyili,					s_soyis.upper() + '_' + s_ad + t_dyili + t_dyili, s_soyis.upper() + '_' + s_ad + '_' + t_dyili + t_dyili, s_soyis.upper() + s_ad + '_' + t_dyili + t_dyili,
			s_soyis.upper() + s_ad.upper() + t_dyili + t_dyili,			s_soyis.upper() + '_' + s_ad.upper() + t_dyili + t_dyili, s_soyis.upper() + '_' + s_ad.upper() + '_' + t_dyili + t_dyili, s_soyis.upper() + s_ad.upper() + '_' + t_dyili + t_dyili,
			s_soyis.upper() + s_ad.title() + t_dyili + t_dyili,		    s_soyis.upper() + '_' + s_ad.title() + t_dyili + t_dyili, s_soyis.upper() + '_' + s_ad.title() + '_' + t_dyili + t_dyili, s_soyis.upper() + s_ad.title() + '_' + t_dyili + t_dyili,
			s_soyis.title() + s_ad + t_dyili + t_dyili,					s_soyis.title() + '_' + s_ad + t_dyili + t_dyili, s_soyis.title() + '_' + s_ad + '_' + t_dyili + t_dyili, s_soyis.title() + s_ad + '_' + t_dyili + t_dyili,
			s_soyis.title() + s_ad.upper() + t_dyili + t_dyili,			s_soyis.title() + '_' + s_ad.upper() + t_dyili + t_dyili, s_soyis.title() + '_' + s_ad.upper() + '_' + t_dyili + t_dyili, s_soyis.title() + s_ad.upper() + '_' + t_dyili + t_dyili,
			s_soyis.title() + s_ad.title() + t_dyili + t_dyili,			s_soyis.title() + '_' + s_ad.title() + t_dyili + t_dyili, s_soyis.title() + '_' + s_ad.title() + '_' + t_dyili + t_dyili, s_soyis.title() + s_ad.title() + '_' + t_dyili + t_dyili,
			
			s_ad.upper() + s_soyis + daygun,							s_ad.upper() + '_' + s_soyis + daygun, s_ad.upper() + '_' + s_soyis + '_' + daygun, s_ad.upper() + s_soyis + '_' + daygun,
			s_ad.upper() + s_soyis.upper() + daygun,					s_ad.upper() + '_' + s_soyis.upper() + daygun, s_ad.upper() + '_' + s_soyis.upper() + '_' + daygun, s_ad.upper() + s_soyis.upper() + '_' + daygun,
			s_ad.upper() + s_soyis.title() + daygun,					s_ad.upper() + '_' + s_soyis.title() + daygun, s_ad.upper() + '_' + s_soyis.title() + '_' + daygun, s_ad.upper() + s_soyis.title() + '_' + daygun,
			s_ad.title() + s_soyis + daygun,							s_ad.title() + '_' + s_soyis + daygun, s_ad.title() + '_' + s_soyis + '_' + daygun, s_ad.title() + s_soyis + '_' + daygun,
			s_ad.title() + s_soyis.upper() + daygun,					s_ad.title() + '_' + s_soyis.upper() + daygun, s_ad.title() + '_' + s_soyis.upper() + '_' + daygun, s_ad.title() + s_soyis.upper() + '_' + daygun,
			s_ad.title() + s_soyis.title() + daygun,					s_ad.title() + '_' + s_soyis.title() + daygun, s_ad.title() + '_' + s_soyis.title() + '_' + daygun, s_ad.title() + s_soyis.title() + '_' + daygun,
			
			s_ad.upper() + s_soyis + daygun + daygun,					s_ad.upper() + '_' + s_soyis + daygun + daygun, s_ad.upper() + '_' + s_soyis + '_' + daygun + daygun, s_ad.upper() + s_soyis + '_' + daygun + daygun,
			s_ad.upper() + s_soyis.upper() + daygun + daygun,			s_ad.upper() + '_' + s_soyis.upper() + daygun + daygun, s_ad.upper() + '_' + s_soyis.upper() + '_' + daygun + daygun, s_ad.upper() + s_soyis.upper() + '_' + daygun + daygun,
			s_ad.upper() + s_soyis.title() + daygun + daygun,			s_ad.upper() + '_' + s_soyis.title() + daygun + daygun, s_ad.upper() + '_' + s_soyis.title() + '_' + daygun + daygun, s_ad.upper() + s_soyis.title() + '_' + daygun + daygun,
			s_ad.title() + s_soyis + daygun + daygun,					s_ad.title() + '_' + s_soyis + daygun + daygun, s_ad.title() + '_' + s_soyis + '_' + daygun + daygun, s_ad.title() + s_soyis + '_' + daygun + daygun,
			s_ad.title() + s_soyis.upper() + daygun + daygun,			s_ad.title() + '_' + s_soyis.upper() + daygun + daygun, s_ad.title() + '_' + s_soyis.upper() + '_' + daygun + daygun, s_ad.title() + s_soyis.upper() + '_' + daygun + daygun,
			s_ad.title() + s_soyis.title() + daygun + daygun,			s_ad.title() + '_' + s_soyis.title() + daygun + daygun, s_ad.title() + '_' + s_soyis.title() + '_' + daygun + daygun, s_ad.title() + s_soyis.title() + '_' + daygun + daygun,
			
			s_ad.upper() + s_soyis + daygun + t_daygun,					s_ad.upper() + '_' + s_soyis + daygun + t_daygun, s_ad.upper() + '_' + s_soyis + '_' + daygun + t_daygun, s_ad.upper() + s_soyis + '_' + daygun + t_daygun,
			s_ad.upper() + s_soyis.upper() + daygun + t_daygun,			s_ad.upper() + '_' + s_soyis.upper() + daygun + t_daygun, s_ad.upper() + '_' + s_soyis.upper() + '_' + daygun + t_daygun, s_ad.upper() + s_soyis.upper() + '_' + daygun + t_daygun,
			s_ad.upper() + s_soyis.title() + daygun + t_daygun,			s_ad.upper() + '_' + s_soyis.title() + daygun + t_daygun, s_ad.upper() + '_' + s_soyis.title() + '_' + daygun + t_daygun, s_ad.upper() + s_soyis.title() + '_' + daygun + t_daygun,
			s_ad.title() + s_soyis + daygun + t_daygun,					s_ad.title() + '_' + s_soyis + daygun + t_daygun, s_ad.title() + '_' + s_soyis + '_' + daygun + t_daygun, s_ad.title() + s_soyis + '_' + daygun + t_daygun,
			s_ad.title() + s_soyis.upper() + daygun + t_daygun,			s_ad.title() + '_' + s_soyis.upper() + daygun + t_daygun, s_ad.title() + '_' + s_soyis.upper() + '_' + daygun + t_daygun, s_ad.title() + s_soyis.upper() + '_' + daygun + t_daygun,
			s_ad.title() + s_soyis.title() + daygun + t_daygun,			s_ad.title() + '_' + s_soyis.title() + daygun + t_daygun, s_ad.title() + '_' + s_soyis.title() + '_' + daygun + t_daygun, s_ad.title() + s_soyis.title() + '_' + daygun + t_daygun,
			
			s_ad.upper() + s_soyis + t_daygun,							s_ad.upper() + '_' + s_soyis + t_daygun, s_ad.upper() + '_' + s_soyis + '_' + t_daygun, s_ad.upper() + s_soyis + '_' + t_daygun,
			s_ad.upper() + s_soyis.upper() + t_daygun,					s_ad.upper() + '_' + s_soyis.upper() + t_daygun, s_ad.upper() + '_' + s_soyis.upper() + '_' + t_daygun, s_ad.upper() + s_soyis.upper() + '_' + t_daygun,
			s_ad.upper() + s_soyis.title() + t_daygun,					s_ad.upper() + '_' + s_soyis.title() + t_daygun, s_ad.upper() + '_' + s_soyis.title() + '_' + t_daygun, s_ad.upper() + s_soyis.title() + '_' + t_daygun,
			s_ad.title() + s_soyis + t_daygun,							s_ad.title() + '_' + s_soyis + daygun, s_ad.title() + '_' + s_soyis + '_' + t_daygun, s_ad.title() + s_soyis + '_' + t_daygun,
			s_ad.title() + s_soyis.upper() + t_daygun,					s_ad.title() + '_' + s_soyis.upper() + daygun, s_ad.title() + '_' + s_soyis.upper() + '_' + t_daygun, s_ad.title() + s_soyis.upper() + '_' + t_daygun,
			s_ad.title() + s_soyis.title() + t_daygun,					s_ad.title() + '_' + s_soyis.title() + daygun, s_ad.title() + '_' + s_soyis.title() + '_' + t_daygun, s_ad.title() + s_soyis.title() + '_' + t_daygun,

			s_ad.upper() + s_soyis + t_daygun + daygun,					s_ad.upper() + '_' + s_soyis + t_daygun + daygun, s_ad.upper() + '_' + s_soyis + '_' + t_daygun + daygun, s_ad.upper() + s_soyis + '_' + t_daygun + daygun,
			s_ad.upper() + s_soyis.upper() + t_daygun + daygun,			s_ad.upper() + '_' + s_soyis.upper() + t_daygun + daygun, s_ad.upper() + '_' + s_soyis.upper() + '_' + t_daygun + daygun, s_ad.upper() + s_soyis.upper() + '_' + t_daygun + daygun,
			s_ad.upper() + s_soyis.title() + t_daygun + daygun,			s_ad.upper() + '_' + s_soyis.title() + t_daygun + daygun, s_ad.upper() + '_' + s_soyis.title() + '_' + t_daygun + daygun, s_ad.upper() + s_soyis.title() + '_' + t_daygun + daygun,
			s_ad.title() + s_soyis + t_daygun + daygun,					s_ad.title() + '_' + s_soyis + t_daygun + daygun, s_ad.title() + '_' + s_soyis + '_' + t_daygun + daygun, s_ad.title() + s_soyis + '_' + t_daygun + daygun,
			s_ad.title() + s_soyis.upper() + t_daygun + daygun,			s_ad.title() + '_' + s_soyis.upper() + t_daygun + daygun, s_ad.title() + '_' + s_soyis.upper() + '_' + t_daygun + daygun, s_ad.title() + s_soyis.upper() + '_' + t_daygun + daygun,
			s_ad.title() + s_soyis.title() + t_daygun + daygun,			s_ad.title() + '_' + s_soyis.title() + t_daygun + daygun, s_ad.title() + '_' + s_soyis.title() + '_' + t_daygun + daygun, s_ad.title() + s_soyis.title() + '_' + t_daygun + daygun,

			s_ad.upper() + s_soyis + t_daygun + t_daygun,				s_ad.upper() + '_' + s_soyis + t_daygun + t_daygun, s_ad.upper() + '_' + s_soyis + '_' + t_daygun + t_daygun, s_ad.upper() + s_soyis + '_' + t_daygun + t_daygun,
			s_ad.upper() + s_soyis.upper() + t_daygun + t_daygun,		s_ad.upper() + '_' + s_soyis.upper() + t_daygun + t_daygun, s_ad.upper() + '_' + s_soyis.upper() + '_' + t_daygun + t_daygun, s_ad.upper() + s_soyis.upper() + '_' + t_daygun + t_daygun,
			s_ad.upper() + s_soyis.title() + t_daygun + t_daygun,		s_ad.upper() + '_' + s_soyis.title() + t_daygun + t_daygun, s_ad.upper() + '_' + s_soyis.title() + '_' + t_daygun + t_daygun, s_ad.upper() + s_soyis.title() + '_' + t_daygun + t_daygun,
			s_ad.title() + s_soyis + t_daygun + t_daygun,				s_ad.title() + '_' + s_soyis + t_daygun + daygun, s_ad.title() + '_' + s_soyis + '_' + t_daygun + t_daygun, s_ad.title() + s_soyis + '_' + t_daygun + t_daygun,
			s_ad.title() + s_soyis.upper() + t_daygun + t_daygun,		s_ad.title() + '_' + s_soyis.upper() + t_daygun + daygun, s_ad.title() + '_' + s_soyis.upper() + '_' + t_daygun + t_daygun, s_ad.title() + s_soyis.upper() + '_' + t_daygun + t_daygun,
			s_ad.title() + s_soyis.title() + t_daygun + t_daygun,		s_ad.title() + '_' + s_soyis.title() + t_daygun + daygun, s_ad.title() + '_' + s_soyis.title() + '_' + t_daygun + t_daygun, s_ad.title() + s_soyis.title() + '_' + t_daygun + t_daygun,

			s_soyis.upper() + s_ad + daygun,							s_soyis.upper() + '_' + s_ad + daygun, s_soyis.upper() + '_' + s_ad + '_' + daygun, s_soyis.upper() + s_ad + '_' + daygun,
			s_soyis.upper() + s_ad.upper() + daygun,					s_soyis.upper() + '_' + s_ad.upper() + daygun, s_soyis.upper() + '_' + s_ad.upper() + '_' + daygun, s_soyis.upper() + s_ad.upper() + '_' + daygun,
			s_soyis.upper() + s_ad.title() + daygun,					s_soyis.upper() + '_' + s_ad.title() + daygun, s_soyis.upper() + '_' + s_ad.title() + '_' + daygun, s_soyis.upper() + s_ad.title() + '_' + daygun,
			s_soyis.title() + s_ad + daygun,							s_soyis.title() + '_' + s_ad + daygun, s_soyis.title() + '_' + s_ad + '_' + daygun, s_soyis.title() + s_ad + '_' + daygun,
			s_soyis.title() + s_ad.upper() + daygun,					s_soyis.title() + '_' + s_ad.upper() + daygun, s_soyis.title() + '_' + s_ad.upper() + '_' + daygun, s_soyis.title() + s_ad.upper() + '_' + daygun,
			s_soyis.title() + s_ad.title() + daygun,					s_soyis.title() + '_' + s_ad.title() + daygun, s_soyis.title() + '_' + s_ad.title() + '_' + daygun, s_soyis.title() + s_ad.title() + '_' + daygun,
			
			s_soyis.upper() + s_ad + daygun + daygun,					s_soyis.upper() + '_' + s_ad + daygun + daygun, s_soyis.upper() + '_' + s_ad + '_' + daygun + daygun, s_soyis.upper() + s_ad + '_' + daygun + daygun,
			s_soyis.upper() + s_ad.upper() + daygun + daygun,			s_soyis.upper() + '_' + s_ad.upper() + daygun + daygun, s_soyis.upper() + '_' + s_ad.upper() + '_' + daygun + daygun, s_soyis.upper() + s_ad.upper() + '_' + daygun + daygun,
			s_soyis.upper() + s_ad.title() + daygun + daygun,			s_soyis.upper() + '_' + s_ad.title() + daygun + daygun, s_soyis.upper() + '_' + s_ad.title() + '_' + daygun + daygun, s_soyis.upper() + s_ad.title() + '_' + daygun + daygun,
			s_soyis.title() + s_ad + daygun + daygun,					s_soyis.title() + '_' + s_ad + daygun + daygun, s_soyis.title() + '_' + s_ad + '_' + daygun + daygun, s_soyis.title() + s_ad + '_' + daygun + daygun,
			s_soyis.title() + s_ad.upper() + daygun + daygun,			s_soyis.title() + '_' + s_ad.upper() + daygun + daygun, s_soyis.title() + '_' + s_ad.upper() + '_' + daygun + daygun, s_soyis.title() + s_ad.upper() + '_' + daygun + daygun,
			s_soyis.title() + s_ad.title() + daygun + daygun,			s_soyis.title() + '_' + s_ad.title() + daygun + daygun, s_soyis.title() + '_' + s_ad.title() + '_' + daygun + daygun, s_soyis.title() + s_ad.title() + '_' + daygun + daygun,
			
			s_soyis.upper() + s_ad + daygun + t_daygun,					s_soyis.upper() + '_' + s_ad + daygun + t_daygun, s_soyis.upper() + '_' + s_ad + '_' + daygun + t_daygun, s_soyis.upper() + s_ad + '_' + daygun + t_daygun,
			s_soyis.upper() + s_ad.upper() + daygun + t_daygun,			s_soyis.upper() + '_' + s_ad.upper() + daygun + t_daygun, s_soyis.upper() + '_' + s_ad.upper() + '_' + daygun + t_daygun, s_soyis.upper() + s_ad.upper() + '_' + daygun + t_daygun,
			s_soyis.upper() + s_ad.title() + daygun + t_daygun,			s_soyis.upper() + '_' + s_ad.title() + daygun + t_daygun, s_soyis.upper() + '_' + s_ad.title() + '_' + daygun + t_daygun, s_soyis.upper() + s_ad.title() + '_' + daygun + t_daygun,
			s_soyis.title() + s_ad + daygun + t_daygun,					s_soyis.title() + '_' + s_ad + daygun + t_daygun, s_soyis.title() + '_' + s_ad + '_' + daygun + t_daygun, s_soyis.title() + s_ad + '_' + daygun + t_daygun,
			s_soyis.title() + s_ad.upper() + daygun + t_daygun,			s_soyis.title() + '_' + s_ad.upper() + daygun + t_daygun, s_soyis.title() + '_' + s_ad.upper() + '_' + daygun + t_daygun, s_soyis.title() + s_ad.upper() + '_' + daygun + t_daygun,
			s_soyis.title() + s_ad.title() + daygun + t_daygun,			s_soyis.title() + '_' + s_ad.title() + daygun + t_daygun, s_soyis.title() + '_' + s_ad.title() + '_' + daygun + t_daygun, s_soyis.title() + s_ad.title() + '_' + daygun + t_daygun,
			
			s_soyis.upper() + s_ad + t_daygun,							s_soyis.upper() + '_' + s_ad + t_daygun, s_soyis.upper() + '_' + s_ad + '_' + t_daygun, s_soyis.upper() + s_ad + '_' + t_daygun,
			s_soyis.upper() + s_ad.upper() + t_daygun,					s_soyis.upper() + '_' + s_ad.upper() + t_daygun, s_soyis.upper() + '_' + s_ad.upper() + '_' + t_daygun, s_soyis.upper() + s_ad.upper() + '_' + t_daygun,
			s_soyis.upper() + s_ad.title() + t_daygun,					s_soyis.upper() + '_' + s_ad.title() + t_daygun, s_soyis.upper() + '_' + s_ad.title() + '_' + t_daygun, s_soyis.upper() + s_ad.title() + '_' + t_daygun,
			s_soyis.title() + s_ad + t_daygun,							s_soyis.title() + '_' + s_ad + daygun, s_soyis.title() + '_' + s_ad + '_' + t_daygun, s_soyis.title() + s_ad + '_' + t_daygun,
			s_soyis.title() + s_ad.upper() + t_daygun,					s_soyis.title() + '_' + s_ad.upper() + daygun, s_soyis.title() + '_' + s_ad.upper() + '_' + t_daygun, s_soyis.title() + s_ad.upper() + '_' + t_daygun,
			s_soyis.title() + s_ad.title() + t_daygun,					s_soyis.title() + '_' + s_ad.title() + daygun, s_soyis.title() + '_' + s_ad.title() + '_' + t_daygun, s_soyis.title() + s_ad.title() + '_' + t_daygun,
			
			s_soyis.upper() + s_ad + t_daygun + daygun,					s_soyis.upper() + '_' + s_ad + t_daygun + daygun, s_soyis.upper() + '_' + s_ad + '_' + t_daygun + daygun, s_soyis.upper() + s_ad + '_' + t_daygun + daygun,
			s_soyis.upper() + s_ad.upper() + t_daygun + daygun,			s_soyis.upper() + '_' + s_ad.upper() + t_daygun + daygun, s_soyis.upper() + '_' + s_ad.upper() + '_' + t_daygun + daygun, s_soyis.upper() + s_ad.upper() + '_' + t_daygun + daygun,
			s_soyis.upper() + s_ad.title() + t_daygun + daygun,			s_soyis.upper() + '_' + s_ad.title() + t_daygun + daygun, s_soyis.upper() + '_' + s_ad.title() + '_' + t_daygun + daygun, s_soyis.upper() + s_ad.title() + '_' + t_daygun + daygun,
			s_soyis.title() + s_ad + t_daygun + daygun,					s_soyis.title() + '_' + s_ad + t_daygun + daygun, s_soyis.title() + '_' + s_ad + '_' + t_daygun + daygun, s_soyis.title() + s_ad + '_' + t_daygun + daygun,
			s_soyis.title() + s_ad.upper() + t_daygun + daygun,			s_soyis.title() + '_' + s_ad.upper() + t_daygun + daygun, s_soyis.title() + '_' + s_ad.upper() + '_' + t_daygun + daygun, s_soyis.title() + s_ad.upper() + '_' + t_daygun + daygun,
			s_soyis.title() + s_ad.title() + t_daygun + daygun,			s_soyis.title() + '_' + s_ad.title() + t_daygun + daygun, s_soyis.title() + '_' + s_ad.title() + '_' + t_daygun + daygun, s_soyis.title() + s_ad.title() + '_' + t_daygun + daygun,
			
			s_soyis.upper() + s_ad + t_daygun + t_daygun,				s_soyis.upper() + '_' + s_ad + t_daygun + t_daygun, s_soyis.upper() + '_' + s_ad + '_' + t_daygun + t_daygun, s_soyis.upper() + s_ad + '_' + t_daygun + t_daygun,
			s_soyis.upper() + s_ad.upper() + t_daygun + t_daygun,		s_soyis.upper() + '_' + s_ad.upper() + t_daygun + t_daygun, s_soyis.upper() + '_' + s_ad.upper() + '_' + t_daygun + t_daygun, s_soyis.upper() + s_ad.upper() + '_' + t_daygun + t_daygun,
			s_soyis.upper() + s_ad.title() + t_daygun + t_daygun,		s_soyis.upper() + '_' + s_ad.title() + t_daygun + t_daygun, s_soyis.upper() + '_' + s_ad.title() + '_' + t_daygun + t_daygun, s_soyis.upper() + s_ad.title() + '_' + t_daygun + t_daygun,
			s_soyis.title() + s_ad + t_daygun + t_daygun,				s_soyis.title() + '_' + s_ad + t_daygun + daygun, s_soyis.title() + '_' + s_ad + '_' + t_daygun + t_daygun, s_soyis.title() + s_ad + '_' + t_daygun + t_daygun,
			s_soyis.title() + s_ad.upper() + t_daygun + t_daygun,		s_soyis.title() + '_' + s_ad.upper() + t_daygun + daygun, s_soyis.title() + '_' + s_ad.upper() + '_' + t_daygun + t_daygun, s_soyis.title() + s_ad.upper() + '_' + t_daygun + t_daygun,
			s_soyis.title() + s_ad.title() + t_daygun + t_daygun,		s_soyis.title() + '_' + s_ad.title() + t_daygun + daygun, s_soyis.title() + '_' + s_ad.title() + '_' + t_daygun + t_daygun, s_soyis.title() + s_ad.title() + '_' + t_daygun + t_daygun,
				
			s_ad.upper() + s_soyis + dtarihi,							s_ad.upper() + '_' + s_soyis + dtarihi, s_ad.upper() + '_' + s_soyis + '_' + dtarihi, s_ad.upper() + s_soyis + '_' + dtarihi,
			s_ad.upper() + s_soyis.upper() + dtarihi,					s_ad.upper() + '_' + s_soyis.upper() + dtarihi, s_ad.upper() + '_' + s_soyis.upper() + '_' + dtarihi, s_ad.upper() + s_soyis.upper() + '_' + dtarihi,
			s_ad.upper() + s_soyis.title() + dtarihi,					s_ad.upper() + '_' + s_soyis.title() + dtarihi, s_ad.upper() + '_' + s_soyis.title() + '_' + dtarihi, s_ad.upper() + s_soyis.title() + '_' + dtarihi,
			s_ad.title() + s_soyis + dtarihi,							s_ad.title() + '_' + s_soyis + dtarihi, s_ad.title() + '_' + s_soyis + '_' + dtarihi, s_ad.title() + s_soyis + '_' + dtarihi,
			s_ad.title() + s_soyis.upper() + dtarihi,					s_ad.title() + '_' + s_soyis.upper() + dtarihi, s_ad.title() + '_' + s_soyis.upper() + '_' + dtarihi, s_ad.title() + s_soyis.upper() + '_' + dtarihi,
			s_ad.title() + s_soyis.title() + dtarihi,					s_ad.title() + '_' + s_soyis.title() + dtarihi, s_ad.title() + '_' + s_soyis.title() + '_' + dtarihi, s_ad.title() + s_soyis.title() + '_' + dtarihi,
			
			s_ad.upper() + s_soyis + t_dtarihi,							s_ad.upper() + '_' + s_soyis + t_dtarihi, s_ad.upper() + '_' + s_soyis + '_' + t_dtarihi, s_ad.upper() + s_soyis + '_' + t_dtarihi,
			s_ad.upper() + s_soyis.upper() + t_dtarihi,					s_ad.upper() + '_' + s_soyis.upper() + t_dtarihi, s_ad.upper() + '_' + s_soyis.upper() + '_' + t_dtarihi, s_ad.upper() + s_soyis.upper() + '_' + t_dtarihi,
			s_ad.upper() + s_soyis.title() + t_dtarihi,					s_ad.upper() + '_' + s_soyis.title() + t_dtarihi, s_ad.upper() + '_' + s_soyis.title() + '_' + t_dtarihi, s_ad.upper() + s_soyis.title() + '_' + t_dtarihi,
			s_ad.title() + s_soyis + t_dtarihi,							s_ad.title() + '_' + s_soyis + dtarihi, s_ad.title() + '_' + s_soyis + '_' + t_dtarihi, s_ad.title() + s_soyis + '_' + t_dtarihi,
			s_ad.title() + s_soyis.upper() + t_dtarihi,					s_ad.title() + '_' + s_soyis.upper() + dtarihi, s_ad.title() + '_' + s_soyis.upper() + '_' + t_dtarihi, s_ad.title() + s_soyis.upper() + '_' + t_dtarihi,
			s_ad.title() + s_soyis.title() + t_dtarihi,					s_ad.title() + '_' + s_soyis.title() + dtarihi, s_ad.title() + '_' + s_soyis.title() + '_' + t_dtarihi, s_ad.title() + s_soyis.title() + '_' + t_dtarihi,

			#######################################################################################################

			s_ad + soyis,												s_ad + '_' + soyis,
			
			s_ad.upper() + soyis,										s_ad.upper() + '_' + soyis,
			s_ad.upper() + soyis.upper(),								s_ad.upper() + '_' + soyis.upper(),
			s_ad.upper() + soyis.title(),								s_ad.upper() + '_' + soyis.title(),
			s_ad.title() + soyis,										s_ad.title() + '_' + soyis,
			s_ad.title() + soyis.upper(),								s_ad.title() + '_' + soyis.upper(),
			s_ad.title() + soyis.title(),								s_ad.title() + '_' + soyis.title(),
			
			s_ad + pkodu,												s_ad + '_' + pkodu,										
			s_ad + pkodu + pkodu,   									s_ad + '_' + pkodu + pkodu, 
			s_ad + pkodu + t_pkodu,										s_ad + '_' + pkodu + t_pkodu,
			s_ad + t_pkodu,												s_ad + '_' + t_pkodu,
			s_ad + t_pkodu + pkodu,										s_ad + '_' + t_pkodu + pkodu,
			s_ad + t_pkodu + t_pkodu,									s_ad + '_' + t_pkodu + t_pkodu,

			soyis + pkodu,												soyis + '_' + pkodu,
			soyis + pkodu + pkodu,										soyis + '_' + pkodu + pkodu,
			soyis + pkodu + t_pkodu,									soyis + '_' + pkodu + t_pkodu,
			soyis + t_pkodu,											soyis + '_' + t_pkodu,
			soyis + t_pkodu + pkodu,									soyis + '_' + t_pkodu + pkodu,
			soyis + t_pkodu + t_pkodu,									soyis + '_' + t_pkodu + t_pkodu,

			s_ad + soyis + pkodu, 										s_ad + '_' + soyis + pkodu, s_ad + '_' + soyis + '_' + pkodu, s_ad + soyis + '_' + pkodu,
			s_ad + soyis + pkodu + pkodu,								s_ad + '_' + soyis + pkodu + pkodu, s_ad + '_' + soyis + '_' + pkodu + pkodu, s_ad + soyis + '_' + pkodu + pkodu,
			s_ad + soyis + pkodu + t_pkodu,								s_ad + '_' + soyis + pkodu + t_pkodu, s_ad + '_' + soyis + '_' + pkodu + t_pkodu, s_ad + soyis + '_' + pkodu + t_pkodu,
			s_ad + soyis + t_pkodu, 									s_ad + '_' + soyis + t_pkodu, s_ad + '_' + soyis + '_' + t_pkodu, s_ad + soyis + '_' + t_pkodu,
			s_ad + soyis + t_pkodu + pkodu,								s_ad + '_' + soyis + t_pkodu + pkodu, s_ad + '_' + soyis + '_' + t_pkodu + pkodu, s_ad + soyis + '_' + t_pkodu + pkodu,
			s_ad + soyis + t_pkodu + t_pkodu,							s_ad + '_' + soyis + t_pkodu + t_pkodu, s_ad + '_' + soyis + '_' + t_pkodu + t_pkodu, s_ad + soyis + '_' + t_pkodu + t_pkodu,
			
			#######################################################################################################################################################

			s_ad.upper() + pkodu,										s_ad.upper() + '_' + pkodu,										
			s_ad.upper() + pkodu + pkodu,   							s_ad.upper() + '_' + pkodu + pkodu, 
			s_ad.upper() + pkodu + t_pkodu,								s_ad.upper() + '_' + pkodu + t_pkodu,
			s_ad.upper() + t_pkodu,										s_ad.upper() + '_' + t_pkodu,
			s_ad.upper() + t_pkodu + pkodu,								s_ad.upper() + '_' + t_pkodu + pkodu,
			s_ad.upper() + t_pkodu + t_pkodu,							s_ad.upper() + '_' + t_pkodu + t_pkodu,
			
			s_ad.title() + pkodu,										s_ad.title() + '_' + pkodu,										
			s_ad.title() + pkodu + pkodu,   							s_ad.title() + '_' + pkodu + pkodu, 
			s_ad.title() + pkodu + t_pkodu,								s_ad.title() + '_' + pkodu + t_pkodu,
			s_ad.title() + t_pkodu,										s_ad.title() + '_' + t_pkodu,
			s_ad.title() + t_pkodu + pkodu,								s_ad.title() + '_' + t_pkodu + pkodu,
			s_ad.title() + t_pkodu + t_pkodu,							s_ad.title() + '_' + t_pkodu + t_pkodu,
			
			s_ad.upper() + soyis + pkodu,								s_ad.upper() + '_' + soyis + pkodu, s_ad.upper() + '_' + soyis + '_' + pkodu, s_ad.upper() + soyis + '_' + pkodu,
			s_ad.upper() + soyis.upper() + pkodu,						s_ad.upper() + '_' + soyis.upper() + pkodu, s_ad.upper() + '_' + soyis.upper() + '_' + pkodu, s_ad.upper() + soyis.upper() + '_' + pkodu,
			s_ad.upper() + soyis.title() + pkodu,						s_ad.upper() + '_' + soyis.title() + pkodu, s_ad.upper() + '_' + soyis.title() + '_' + pkodu, s_ad.upper() + soyis.title() + '_' + pkodu,
			s_ad.title() + soyis + pkodu,								s_ad.title() + '_' + soyis + pkodu, s_ad.title() + '_' + soyis + '_' + pkodu, s_ad.title() + soyis + '_' + pkodu,
			s_ad.title() + soyis.upper() + pkodu,						s_ad.title() + '_' + soyis.upper() + pkodu, s_ad.title() + '_' + soyis.upper() + '_' + pkodu, s_ad.title() + soyis.upper() + '_' + pkodu,
			s_ad.title() + soyis.title() + pkodu,						s_ad.title() + '_' + soyis.title() + pkodu, s_ad.title() + '_' + soyis.title() + '_' + pkodu, s_ad.title() + soyis.title() + '_' + pkodu,

			s_ad.upper() + soyis + pkodu + pkodu,						s_ad.upper() + '_' + soyis + pkodu + pkodu, s_ad.upper() + '_' + soyis + '_' + pkodu + pkodu, s_ad.upper() + soyis + '_' + pkodu + pkodu,
			s_ad.upper() + soyis.upper() + pkodu + pkodu,				s_ad.upper() + '_' + soyis.upper() + pkodu + pkodu, s_ad.upper() + '_' + soyis.upper() + '_' + pkodu + pkodu, s_ad.upper() + soyis.upper() + '_' + pkodu + pkodu,
			s_ad.upper() + soyis.title() + pkodu + pkodu,				s_ad.upper() + '_' + soyis.title() + pkodu + pkodu, s_ad.upper() + '_' + soyis.title() + '_' + pkodu + pkodu, s_ad.upper() + soyis.title() + '_' + pkodu + pkodu,
			s_ad.title() + soyis + pkodu + pkodu,						s_ad.title() + '_' + soyis + pkodu + pkodu, s_ad.title() + '_' + soyis + '_' + pkodu + pkodu, s_ad.title() + soyis + '_' + pkodu + pkodu,
			s_ad.title() + soyis.upper() + pkodu + pkodu,				s_ad.title() + '_' + soyis.upper() + pkodu + pkodu, s_ad.title() + '_' + soyis.upper() + '_' + pkodu + pkodu, s_ad.title() + soyis.upper() + '_' + pkodu + pkodu,
			s_ad.title() + soyis.title() + pkodu + pkodu,				s_ad.title() + '_' + soyis.title() + pkodu + pkodu, s_ad.title() + '_' + soyis.title() + '_' + pkodu + pkodu, s_ad.title() + soyis.title() + '_' + pkodu + pkodu,
			
			s_ad.upper() + soyis + pkodu + t_pkodu,						s_ad.upper() + '_' + soyis + pkodu + t_pkodu, s_ad.upper() + '_' + soyis + '_' + pkodu + t_pkodu, s_ad.upper() + soyis + '_' + pkodu + t_pkodu,
			s_ad.upper() + soyis.upper() + pkodu + t_pkodu,				s_ad.upper() + '_' + soyis.upper() + pkodu + t_pkodu, s_ad.upper() + '_' + soyis.upper() + '_' + pkodu + t_pkodu, s_ad.upper() + soyis.upper() + '_' + pkodu + t_pkodu,
			s_ad.upper() + soyis.title() + pkodu + t_pkodu,				s_ad.upper() + '_' + soyis.title() + pkodu + t_pkodu, s_ad.upper() + '_' + soyis.title() + '_' + pkodu + t_pkodu, s_ad.upper() + soyis.title() + '_' + pkodu + t_pkodu,
			s_ad.title() + soyis + pkodu + t_pkodu,						s_ad.title() + '_' + soyis + pkodu + t_pkodu, s_ad.title() + '_' + soyis + '_' + pkodu + t_pkodu, s_ad.title() + soyis + '_' + pkodu + t_pkodu,
			s_ad.title() + soyis.upper() + pkodu + t_pkodu,				s_ad.title() + '_' + soyis.upper() + pkodu + t_pkodu, s_ad.title() + '_' + soyis.upper() + '_' + pkodu + t_pkodu, s_ad.title() + soyis.upper() + '_' + pkodu + t_pkodu,
			s_ad.title() + soyis.title() + pkodu + t_pkodu,				s_ad.title() + '_' + soyis.title() + pkodu + t_pkodu, s_ad.title() + '_' + soyis.title() + '_' + pkodu + t_pkodu, s_ad.title() + soyis.title() + '_' + pkodu + t_pkodu,
			
			s_ad.upper() + soyis + t_pkodu,								s_ad.upper() + '_' + soyis + t_pkodu, s_ad.upper() + '_' + soyis + '_' + t_pkodu, s_ad.upper() + soyis + '_' + t_pkodu,
			s_ad.upper() + soyis.upper() + t_pkodu,						s_ad.upper() + '_' + soyis.upper() + t_pkodu, s_ad.upper() + '_' + soyis.upper() + '_' + t_pkodu, s_ad.upper() + soyis.upper() + '_' + t_pkodu,
			s_ad.upper() + soyis.title() + t_pkodu,						s_ad.upper() + '_' + soyis.title() + t_pkodu, s_ad.upper() + '_' + soyis.title() + '_' + t_pkodu, s_ad.upper() + soyis.title() + '_' + t_pkodu,
			s_ad.title() + soyis + t_pkodu,								s_ad.title() + '_' + soyis + t_pkodu, s_ad.title() + '_' + soyis + '_' + t_pkodu, s_ad.title() + soyis + '_' + t_pkodu,
			s_ad.title() + soyis.upper() + t_pkodu,						s_ad.title() + '_' + soyis.upper() + t_pkodu, s_ad.title() + '_' + soyis.upper() + '_' + t_pkodu, s_ad.title() + soyis.upper() + '_' + t_pkodu,
			s_ad.title() + soyis.title() + t_pkodu,						s_ad.title() + '_' + soyis.title() + t_pkodu, s_ad.title() + '_' + soyis.title() + '_' + t_pkodu, s_ad.title() + soyis.title() + '_' + t_pkodu,
			
			s_ad.upper() + soyis + t_pkodu + pkodu,						s_ad.upper() + '_' + soyis + t_pkodu + pkodu, s_ad.upper() + '_' + soyis + '_' + t_pkodu + pkodu, s_ad.upper() + soyis + '_' + t_pkodu + pkodu,
			s_ad.upper() + soyis.upper() + t_pkodu + pkodu,				s_ad.upper() + '_' + soyis.upper() + t_pkodu + pkodu, s_ad.upper() + '_' + soyis.upper() + '_' + t_pkodu + pkodu, s_ad.upper() + soyis.upper() + '_' + t_pkodu + pkodu,
			s_ad.upper() + soyis.title() + t_pkodu + pkodu,				s_ad.upper() + '_' + soyis.title() + t_pkodu + pkodu, s_ad.upper() + '_' + soyis.title() + '_' + t_pkodu + pkodu, s_ad.upper() + soyis.title() + '_' + t_pkodu + pkodu,
			s_ad.title() + soyis + t_pkodu + pkodu,						s_ad.title() + '_' + soyis + t_pkodu + pkodu, s_ad.title() + '_' + soyis + '_' + t_pkodu + pkodu, s_ad.title() + soyis + '_' + t_pkodu + pkodu,
			s_ad.title() + soyis.upper() + t_pkodu + pkodu,				s_ad.title() + '_' + soyis.upper() + t_pkodu + pkodu, s_ad.title() + '_' + soyis.upper() + '_' + t_pkodu + pkodu, s_ad.title() + soyis.upper() + '_' + t_pkodu + pkodu,
			s_ad.title() + soyis.title() + t_pkodu + pkodu,				s_ad.title() + '_' + soyis.title() + t_pkodu + pkodu, s_ad.title() + '_' + soyis.title() + '_' + t_pkodu + pkodu, s_ad.title() + soyis.title() + '_' + t_pkodu + pkodu,
			
			s_ad.upper() + soyis + t_pkodu + t_pkodu,					s_ad.upper() + '_' + soyis + t_pkodu + t_pkodu, s_ad.upper() + '_' + soyis + '_' + t_pkodu + t_pkodu, s_ad.upper() + soyis + '_' + t_pkodu + t_pkodu,
			s_ad.upper() + soyis.upper() + t_pkodu + t_pkodu,			s_ad.upper() + '_' + soyis.upper() + t_pkodu + t_pkodu, s_ad.upper() + '_' + soyis.upper() + '_' + t_pkodu + t_pkodu, s_ad.upper() + soyis.upper() + '_' + t_pkodu + t_pkodu,
			s_ad.upper() + soyis.title() + t_pkodu + t_pkodu,			s_ad.upper() + '_' + soyis.title() + t_pkodu + t_pkodu, s_ad.upper() + '_' + soyis.title() + '_' + t_pkodu + t_pkodu, s_ad.upper() + soyis.title() + '_' + t_pkodu + t_pkodu,
			s_ad.title() + soyis + t_pkodu + t_pkodu,					s_ad.title() + '_' + soyis + t_pkodu + t_pkodu, s_ad.title() + '_' + soyis + '_' + t_pkodu + t_pkodu, s_ad.title() + soyis + '_' + t_pkodu + t_pkodu,
			s_ad.title() + soyis.upper() + t_pkodu + t_pkodu,			s_ad.title() + '_' + soyis.upper() + t_pkodu + t_pkodu, s_ad.title() + '_' + soyis.upper() + '_' + t_pkodu + t_pkodu, s_ad.title() + soyis.upper() + '_' + t_pkodu + t_pkodu,
			s_ad.title() + soyis.title() + t_pkodu + t_pkodu,			s_ad.title() + '_' + soyis.title() + t_pkodu + t_pkodu, s_ad.title() + '_' + soyis.title() + '_' + t_pkodu + t_pkodu, s_ad.title() + soyis.title() + '_' + t_pkodu + t_pkodu,
			
			#########################################################################################################################################################################################

			s_ad + dyili,												s_ad + '_' + dyili,										
			s_ad + dyili + dyili,   									s_ad + '_' + dyili + dyili, 
			s_ad + dyili + t_dyili,										s_ad + '_' + dyili + t_dyili,
			s_ad + t_dyili,												s_ad + '_' + t_dyili,
			s_ad + t_dyili + dyili,										s_ad + '_' + t_dyili + dyili,
			s_ad + t_dyili + t_dyili,									s_ad + '_' + t_dyili + t_dyili,

			s_ad + soyis + dyili, 										s_ad + '_' + soyis + dyili, s_ad + '_' + soyis + '_' + dyili, s_ad + soyis + '_' + dyili,
			s_ad + soyis + dyili + dyili,								s_ad + '_' + soyis + dyili + dyili, s_ad + '_' + soyis + '_' + dyili + dyili, s_ad + soyis + '_' + dyili + dyili,
			s_ad + soyis + dyili + t_dyili,								s_ad + '_' + soyis + dyili + t_dyili, s_ad + '_' + soyis + '_' + dyili + t_dyili, s_ad + soyis + '_' + dyili + t_dyili,
			s_ad + soyis + t_dyili, 									s_ad + '_' + soyis + t_dyili, s_ad + '_' + soyis + '_' + t_dyili, s_ad + soyis + '_' + t_dyili,
			s_ad + soyis + t_dyili + dyili,								s_ad + '_' + soyis + t_dyili + dyili, s_ad + '_' + soyis + '_' + t_dyili + dyili, s_ad + soyis + '_' + t_dyili + dyili,
			s_ad + soyis + t_dyili + t_dyili,							s_ad + '_' + soyis + t_dyili + t_dyili, s_ad + '_' + soyis + '_' + t_dyili + t_dyili, s_ad + soyis + '_' + t_dyili + t_dyili,
			
			s_ad + daygun,												s_ad + '_' + daygun,
			s_ad + daygun + daygun,										s_ad + '_' + daygun + daygun,
			s_ad + daygun + t_daygun,									s_ad + '_' + daygun + t_daygun,
			s_ad + t_daygun,											s_ad + '_' + t_daygun,
			s_ad + t_daygun + daygun,									s_ad + '_' + t_daygun + daygun,
			s_ad + t_daygun + t_daygun,									s_ad + '_' + t_daygun + t_daygun,
			
			s_ad + soyis + daygun,										s_ad + '_' + soyis + daygun, s_ad + '_' + soyis + '_' + daygun, s_ad + soyis + '_' + daygun,
			s_ad + soyis + t_daygun,									soyis + '_' + s_ad + t_daygun, soyis + '_' + s_ad + '_' + t_daygun, soyis + s_ad + '_' + t_daygun,
			s_ad + dtarihi,												s_ad + '_' + dtarihi,
			s_ad + t_dtarihi,											s_ad + '_' + t_dtarihi,
			s_ad + soyis + dtarihi,										s_ad + '_' + soyis + dtarihi, s_ad + '_' + soyis + '_' + dtarihi, s_ad + soyis + '_' + dtarihi,
			s_ad + soyis + t_dtarihi,									s_ad + '_' + soyis + t_dtarihi, s_ad + '_' + soyis + '_' + t_dtarihi, s_ad + soyis + '_' + t_dtarihi,
			
			#######################################################################################################################################################

			s_ad.upper() + dyili,										s_ad.upper() + '_' + dyili,										
			s_ad.upper() + dyili + dyili,   							s_ad.upper() + '_' + dyili + dyili, 
			s_ad.upper() + dyili + t_dyili,								s_ad.upper() + '_' + dyili + t_dyili,
			s_ad.upper() + t_dyili,										s_ad.upper() + '_' + t_dyili,
			s_ad.upper() + t_dyili + dyili,								s_ad.upper() + '_' + t_dyili + dyili,
			s_ad.upper() + t_dyili + t_dyili,							s_ad.upper() + '_' + t_dyili + t_dyili,

			s_ad.title() + dyili,										s_ad.title() + '_' + dyili,										
			s_ad.title() + dyili + dyili,   							s_ad.title() + '_' + dyili + dyili, 
			s_ad.title() + dyili + t_dyili,								s_ad.title() + '_' + dyili + t_dyili,
			s_ad.title() + t_dyili,										s_ad.title() + '_' + t_dyili,
			s_ad.title() + t_dyili + dyili,								s_ad.title() + '_' + t_dyili + dyili,
			s_ad.title() + t_dyili + t_dyili,							s_ad.title() + '_' + t_dyili + t_dyili,

			s_ad.upper() + soyis + dyili,								s_ad.upper() + '_' + soyis + dyili, s_ad.upper() + '_' + soyis + '_' + dyili, s_ad.upper() + soyis + '_' + dyili,
			s_ad.upper() + soyis.upper() + dyili,						s_ad.upper() + '_' + soyis.upper() + dyili, s_ad.upper() + '_' + soyis.upper() + '_' + dyili, s_ad.upper() + soyis.upper() + '_' + dyili,
			s_ad.upper() + soyis.title() + dyili,						s_ad.upper() + '_' + soyis.title() + dyili, s_ad.upper() + '_' + soyis.title() + '_' + dyili, s_ad.upper() + soyis.title() + '_' + dyili,
			s_ad.title() + soyis + dyili,								s_ad.title() + '_' + soyis + dyili, s_ad.title() + '_' + soyis + '_' + dyili, s_ad.title() + soyis + '_' + dyili,
			s_ad.title() + soyis.upper() + dyili,						s_ad.title() + '_' + soyis.upper() + dyili, s_ad.title() + '_' + soyis.upper() + '_' + dyili, s_ad.title() + soyis.upper() + '_' + dyili,
			s_ad.title() + soyis.title() + dyili,						s_ad.title() + '_' + soyis.title() + dyili, s_ad.title() + '_' + soyis.title() + '_' + dyili, s_ad.title() + soyis.title() + '_' + dyili,
			
			s_ad.upper() + soyis + dyili + dyili,						s_ad.upper() + '_' + soyis + dyili + dyili, s_ad.upper() + '_' + soyis + '_' + dyili + dyili, s_ad.upper() + soyis + '_' + dyili + dyili,
			s_ad.upper() + soyis.upper() + dyili + dyili,				s_ad.upper() + '_' + soyis.upper() + dyili + dyili, s_ad.upper() + '_' + soyis.upper() + '_' + dyili + dyili, s_ad.upper() + soyis.upper() + '_' + dyili + dyili,
			s_ad.upper() + soyis.title() + dyili + dyili,				s_ad.upper() + '_' + soyis.title() + dyili + dyili, s_ad.upper() + '_' + soyis.title() + '_' + dyili + dyili, s_ad.upper() + soyis.title() + '_' + dyili + dyili,
			s_ad.title() + soyis + dyili + dyili,						s_ad.title() + '_' + soyis + dyili + dyili, s_ad.title() + '_' + soyis + '_' + dyili + dyili, s_ad.title() + soyis + '_' + dyili + dyili,
			s_ad.title() + soyis.upper() + dyili + dyili,				s_ad.title() + '_' + soyis.upper() + dyili + dyili, s_ad.title() + '_' + soyis.upper() + '_' + dyili + dyili, s_ad.title() + soyis.upper() + '_' + dyili + dyili,
			s_ad.title() + soyis.title() + dyili + dyili,				s_ad.title() + '_' + soyis.title() + dyili + dyili, s_ad.title() + '_' + soyis.title() + '_' + dyili + dyili, s_ad.title() + soyis.title() + '_' + dyili + dyili,
			
			s_ad.upper() + soyis + dyili + t_dyili,						s_ad.upper() + '_' + soyis + dyili + t_dyili, s_ad.upper() + '_' + soyis + '_' + dyili + t_dyili, s_ad.upper() + soyis + '_' + dyili + t_dyili,
			s_ad.upper() + soyis.upper() + dyili + t_dyili,				s_ad.upper() + '_' + soyis.upper() + dyili + t_dyili, s_ad.upper() + '_' + soyis.upper() + '_' + dyili + t_dyili, s_ad.upper() + soyis.upper() + '_' + dyili + t_dyili,
			s_ad.upper() + soyis.title() + dyili + t_dyili,				s_ad.upper() + '_' + soyis.title() + dyili + t_dyili, s_ad.upper() + '_' + soyis.title() + '_' + dyili + t_dyili, s_ad.upper() + soyis.title() + '_' + dyili + t_dyili,
			s_ad.title() + soyis + dyili + t_dyili,						s_ad.title() + '_' + soyis + dyili + t_dyili, s_ad.title() + '_' + soyis + '_' + dyili + t_dyili, s_ad.title() + soyis + '_' + dyili + t_dyili,
			s_ad.title() + soyis.upper() + dyili + t_dyili,				s_ad.title() + '_' + soyis.upper() + dyili + t_dyili, s_ad.title() + '_' + soyis.upper() + '_' + dyili + t_dyili, s_ad.title() + soyis.upper() + '_' + dyili + t_dyili,
			s_ad.title() + soyis.title() + dyili + t_dyili,				s_ad.title() + '_' + soyis.title() + dyili + t_dyili, s_ad.title() + '_' + soyis.title() + '_' + dyili + t_dyili, s_ad.title() + soyis.title() + '_' + dyili + t_dyili,
			
			s_ad.upper() + soyis + t_dyili,								s_ad.upper() + '_' + soyis + t_dyili, s_ad.upper() + '_' + soyis + '_' + t_dyili, s_ad.upper() + soyis + '_' + t_dyili,
			s_ad.upper() + soyis.upper() + t_dyili,						s_ad.upper() + '_' + soyis.upper() + t_dyili, s_ad.upper() + '_' + soyis.upper() + '_' + t_dyili, s_ad.upper() + soyis.upper() + '_' + t_dyili,
			s_ad.upper() + soyis.title() + t_dyili,						s_ad.upper() + '_' + soyis.title() + t_dyili, s_ad.upper() + '_' + soyis.title() + '_' + t_dyili, s_ad.upper() + soyis.title() + '_' + t_dyili,
			s_ad.title() + soyis + t_dyili,								s_ad.title() + '_' + soyis + t_dyili, s_ad.title() + '_' + soyis + '_' + t_dyili, s_ad.title() + soyis + '_' + t_dyili,
			s_ad.title() + soyis.upper() + t_dyili,						s_ad.title() + '_' + soyis.upper() + t_dyili, s_ad.title() + '_' + soyis.upper() + '_' + t_dyili, s_ad.title() + soyis.upper() + '_' + t_dyili,
			s_ad.title() + soyis.title() + t_dyili,						s_ad.title() + '_' + soyis.title() + t_dyili, s_ad.title() + '_' + soyis.title() + '_' + t_dyili, s_ad.title() + soyis.title() + '_' + t_dyili,

			s_ad.upper() + soyis + t_dyili + dyili,						s_ad.upper() + '_' + soyis + t_dyili + dyili, s_ad.upper() + '_' + soyis + '_' + t_dyili + dyili, s_ad.upper() + soyis + '_' + t_dyili + dyili,
			s_ad.upper() + soyis.upper() + t_dyili + dyili,				s_ad.upper() + '_' + soyis.upper() + t_dyili + dyili, s_ad.upper() + '_' + soyis.upper() + '_' + t_dyili + dyili, s_ad.upper() + soyis.upper() + '_' + t_dyili + dyili,
			s_ad.upper() + soyis.title() + t_dyili + dyili,				s_ad.upper() + '_' + soyis.title() + t_dyili + dyili, s_ad.upper() + '_' + soyis.title() + '_' + t_dyili + dyili, s_ad.upper() + soyis.title() + '_' + t_dyili + dyili,
			s_ad.title() + soyis + t_dyili + dyili,						s_ad.title() + '_' + soyis + t_dyili + dyili, s_ad.title() + '_' + soyis + '_' + t_dyili + dyili, s_ad.title() + soyis + '_' + t_dyili + dyili,
			s_ad.title() + soyis.upper() + t_dyili + dyili,				s_ad.title() + '_' + soyis.upper() + t_dyili + dyili, s_ad.title() + '_' + soyis.upper() + '_' + t_dyili + dyili, s_ad.title() + soyis.upper() + '_' + t_dyili + dyili,
			s_ad.title() + soyis.title() + t_dyili + dyili,				s_ad.title() + '_' + soyis.title() + t_dyili + dyili, s_ad.title() + '_' + soyis.title() + '_' + t_dyili + dyili, s_ad.title() + soyis.title() + '_' + t_dyili + dyili,

			s_ad.upper() + soyis + t_dyili + t_dyili,					s_ad.upper() + '_' + soyis + t_dyili + t_dyili, s_ad.upper() + '_' + soyis + '_' + t_dyili + t_dyili, s_ad.upper() + soyis + '_' + t_dyili + t_dyili,
			s_ad.upper() + soyis.upper() + t_dyili + t_dyili,			s_ad.upper() + '_' + soyis.upper() + t_dyili + t_dyili, s_ad.upper() + '_' + soyis.upper() + '_' + t_dyili + t_dyili,s_ad.upper() + soyis.upper() + '_' + t_dyili + t_dyili,
			s_ad.upper() + soyis.title() + t_dyili + t_dyili,			s_ad.upper() + '_' + soyis.title() + t_dyili + t_dyili, s_ad.upper() + '_' + soyis.title() + '_' + t_dyili + t_dyili, s_ad.upper() + soyis.title() + '_' + t_dyili + t_dyili,
			s_ad.title() + soyis + t_dyili + t_dyili,					s_ad.title() + '_' + soyis + t_dyili + t_dyili, s_ad.title() + '_' + soyis + '_' + t_dyili + t_dyili, s_ad.title() + soyis + '_' + t_dyili + t_dyili,
			s_ad.title() + soyis.upper() + t_dyili + t_dyili,			s_ad.title() + '_' + soyis.upper() + t_dyili + t_dyili, s_ad.title() + '_' + soyis.upper() + '_' + t_dyili + t_dyili, s_ad.title() + soyis.upper() + '_' + t_dyili + t_dyili,
			s_ad.title() + soyis.title() + t_dyili + t_dyili,			s_ad.title() + '_' + soyis.title() + t_dyili + t_dyili, s_ad.title() + '_' + soyis.title() + '_' + t_dyili + t_dyili, s_ad.title() + soyis.title() + '_' + t_dyili + t_dyili,
			
			s_ad.upper() + daygun,										s_ad.upper() + '_' + daygun,
			s_ad.title() + daygun,										s_ad.title() + '_' + daygun,
			
			s_ad.upper() + daygun + daygun,								s_ad.upper() + '_' + daygun + daygun,
			s_ad.title() + daygun + daygun,								s_ad.title() + '_' + daygun + daygun,
			
			s_ad.upper() + daygun + t_daygun,							s_ad.upper() + '_' + daygun + t_daygun,
			s_ad.title() + daygun + t_daygun,							s_ad.title() + '_' + daygun + t_daygun,
			
			s_ad.upper() + t_daygun,									s_ad.upper() + '_' + t_daygun,
			s_ad.title() + t_daygun,									s_ad.title() + '_' + t_daygun,
			
			s_ad.upper() + t_daygun + daygun,							s_ad.upper() + '_' + t_daygun + daygun,
			s_ad.title() + t_daygun + daygun,							s_ad.title() + '_' + t_daygun + daygun,
			
			s_ad.upper() + t_daygun + t_daygun,							s_ad.upper() + '_' + t_daygun + t_daygun,
			s_ad.title() + t_daygun + t_daygun,							s_ad.title() + '_' + t_daygun + t_daygun,
			
			s_ad.upper() + soyis + daygun,								s_ad.upper() + '_' + soyis + daygun, s_ad.upper() + '_' + soyis + '_' + daygun, s_ad.upper() + soyis + '_' + daygun,
			s_ad.upper() + soyis.upper() + daygun,						s_ad.upper() + '_' + soyis.upper() + daygun, s_ad.upper() + '_' + soyis.upper() + '_' + daygun, s_ad.upper() + soyis.upper() + '_' + daygun,
			s_ad.upper() + soyis.title() + daygun,						s_ad.upper() + '_' + soyis.title() + daygun, s_ad.upper() + '_' + soyis.title() + '_' + daygun, s_ad.upper() + soyis.title() + '_' + daygun,
			s_ad.title() + soyis + daygun,								s_ad.title() + '_' + soyis + daygun, s_ad.title() + '_' + soyis + '_' + daygun, s_ad.title() + soyis + '_' + daygun,
			s_ad.title() + soyis.upper() + daygun,						s_ad.title() + '_' + soyis.upper() + daygun, s_ad.title() + '_' + soyis.upper() + '_' + daygun, s_ad.title() + soyis.upper() + '_' + daygun,
			s_ad.title() + soyis.title() + daygun,						s_ad.title() + '_' + soyis.title() + daygun, s_ad.title() + '_' + soyis.title() + '_' + daygun, s_ad.title() + soyis.title() + '_' + daygun,
			
			s_ad.upper() + soyis + daygun + daygun,						s_ad.upper() + '_' + soyis + daygun + daygun, s_ad.upper() + '_' + soyis + '_' + daygun + daygun, s_ad.upper() + soyis + '_' + daygun + daygun,
			s_ad.upper() + soyis.upper() + daygun + daygun,				s_ad.upper() + '_' + soyis.upper() + daygun + daygun, s_ad.upper() + '_' + soyis.upper() + '_' + daygun + daygun, s_ad.upper() + soyis.upper() + '_' + daygun + daygun,
			s_ad.upper() + soyis.title() + daygun + daygun,				s_ad.upper() + '_' + soyis.title() + daygun + daygun, s_ad.upper() + '_' + soyis.title() + '_' + daygun + daygun, s_ad.upper() + soyis.title() + '_' + daygun + daygun,
			s_ad.title() + soyis + daygun + daygun,						s_ad.title() + '_' + soyis + daygun + daygun, s_ad.title() + '_' + soyis + '_' + daygun + daygun, s_ad.title() + soyis + '_' + daygun + daygun,
			s_ad.title() + soyis.upper() + daygun + daygun,				s_ad.title() + '_' + soyis.upper() + daygun + daygun, s_ad.title() + '_' + soyis.upper() + '_' + daygun + daygun, s_ad.title() + soyis.upper() + '_' + daygun + daygun,
			s_ad.title() + soyis.title() + daygun + daygun,				s_ad.title() + '_' + soyis.title() + daygun + daygun, s_ad.title() + '_' + soyis.title() + '_' + daygun + daygun, s_ad.title() + soyis.title() + '_' + daygun + daygun,
			
			s_ad.upper() + soyis + daygun + t_daygun,					s_ad.upper() + '_' + soyis + daygun + t_daygun, s_ad.upper() + '_' + soyis + '_' + daygun + t_daygun, s_ad.upper() + soyis + '_' + daygun + t_daygun,
			s_ad.upper() + soyis.upper() + daygun + t_daygun,			s_ad.upper() + '_' + soyis.upper() + daygun + t_daygun, s_ad.upper() + '_' + soyis.upper() + '_' + daygun + t_daygun, s_ad.upper() + soyis.upper() + '_' + daygun + t_daygun,
			s_ad.upper() + soyis.title() + daygun + t_daygun,			s_ad.upper() + '_' + soyis.title() + daygun + t_daygun, s_ad.upper() + '_' + soyis.title() + '_' + daygun + t_daygun, s_ad.upper() + soyis.title() + '_' + daygun + t_daygun,
			s_ad.title() + soyis + daygun + t_daygun,					s_ad.title() + '_' + soyis + daygun + t_daygun, s_ad.title() + '_' + soyis + '_' + daygun + t_daygun, s_ad.title() + soyis + '_' + daygun + t_daygun,
			s_ad.title() + soyis.upper() + daygun + t_daygun,			s_ad.title() + '_' + soyis.upper() + daygun + t_daygun, s_ad.title() + '_' + soyis.upper() + '_' + daygun + t_daygun, s_ad.title() + soyis.upper() + '_' + daygun + t_daygun,
			s_ad.title() + soyis.title() + daygun + t_daygun,			s_ad.title() + '_' + soyis.title() + daygun + t_daygun, s_ad.title() + '_' + soyis.title() + '_' + daygun + t_daygun, s_ad.title() + soyis.title() + '_' + daygun + t_daygun,
			
			s_ad.upper() + soyis + t_daygun,							s_ad.upper() + '_' + soyis + t_daygun, s_ad.upper() + '_' + soyis + '_' + t_daygun, s_ad.upper() + soyis + '_' + t_daygun,
			s_ad.upper() + soyis.upper() + t_daygun,					s_ad.upper() + '_' + soyis.upper() + t_daygun, s_ad.upper() + '_' + soyis.upper() + '_' + t_daygun, s_ad.upper() + soyis.upper() + '_' + t_daygun,
			s_ad.upper() + soyis.title() + t_daygun,					s_ad.upper() + '_' + soyis.title() + t_daygun, s_ad.upper() + '_' + soyis.title() + '_' + t_daygun, s_ad.upper() + soyis.title() + '_' + t_daygun,
			s_ad.title() + soyis + t_daygun,							s_ad.title() + '_' + soyis + daygun, s_ad.title() + '_' + soyis + '_' + t_daygun, s_ad.title() + soyis + '_' + t_daygun,
			s_ad.title() + soyis.upper() + t_daygun,					s_ad.title() + '_' + soyis.upper() + daygun, s_ad.title() + '_' + soyis.upper() + '_' + t_daygun, s_ad.title() + soyis.upper() + '_' + t_daygun,
			s_ad.title() + soyis.title() + t_daygun,					s_ad.title() + '_' + soyis.title() + daygun, s_ad.title() + '_' + soyis.title() + '_' + t_daygun, s_ad.title() + soyis.title() + '_' + t_daygun,

			s_ad.upper() + soyis + t_daygun + daygun,					s_ad.upper() + '_' + soyis + t_daygun + daygun, s_ad.upper() + '_' + soyis + '_' + t_daygun + daygun, s_ad.upper() + soyis + '_' + t_daygun + daygun,
			s_ad.upper() + soyis.upper() + t_daygun + daygun,			s_ad.upper() + '_' + soyis.upper() + t_daygun + daygun, s_ad.upper() + '_' + soyis.upper() + '_' + t_daygun + daygun, s_ad.upper() + soyis.upper() + '_' + t_daygun + daygun,
			s_ad.upper() + soyis.title() + t_daygun + daygun,			s_ad.upper() + '_' + soyis.title() + t_daygun + daygun, s_ad.upper() + '_' + soyis.title() + '_' + t_daygun + daygun, s_ad.upper() + soyis.title() + '_' + t_daygun + daygun,
			s_ad.title() + soyis + t_daygun + daygun,					s_ad.title() + '_' + soyis + t_daygun + daygun, s_ad.title() + '_' + soyis + '_' + t_daygun + daygun, s_ad.title() + soyis + '_' + t_daygun + daygun,
			s_ad.title() + soyis.upper() + t_daygun + daygun,			s_ad.title() + '_' + soyis.upper() + t_daygun + daygun, s_ad.title() + '_' + soyis.upper() + '_' + t_daygun + daygun, s_ad.title() + soyis.upper() + '_' + t_daygun + daygun,
			s_ad.title() + soyis.title() + t_daygun + daygun,			s_ad.title() + '_' + soyis.title() + t_daygun + daygun, s_ad.title() + '_' + soyis.title() + '_' + t_daygun + daygun, s_ad.title() + soyis.title() + '_' + t_daygun + daygun,

			s_ad.upper() + soyis + t_daygun + t_daygun,					s_ad.upper() + '_' + soyis + t_daygun + t_daygun, s_ad.upper() + '_' + soyis + '_' + t_daygun + t_daygun, s_ad.upper() + soyis + '_' + t_daygun + t_daygun,
			s_ad.upper() + soyis.upper() + t_daygun + t_daygun,			s_ad.upper() + '_' + soyis.upper() + t_daygun + t_daygun, s_ad.upper() + '_' + soyis.upper() + '_' + t_daygun + t_daygun, s_ad.upper() + soyis.upper() + '_' + t_daygun + t_daygun,
			s_ad.upper() + soyis.title() + t_daygun + t_daygun,			s_ad.upper() + '_' + soyis.title() + t_daygun + t_daygun, s_ad.upper() + '_' + soyis.title() + '_' + t_daygun + t_daygun, s_ad.upper() + soyis.title() + '_' + t_daygun + t_daygun,
			s_ad.title() + soyis + t_daygun + t_daygun,					s_ad.title() + '_' + soyis + t_daygun + daygun, s_ad.title() + '_' + soyis + '_' + t_daygun + t_daygun, s_ad.title() + soyis + '_' + t_daygun + t_daygun,
			s_ad.title() + soyis.upper() + t_daygun + t_daygun,			s_ad.title() + '_' + soyis.upper() + t_daygun + daygun, s_ad.title() + '_' + soyis.upper() + '_' + t_daygun + t_daygun, s_ad.title() + soyis.upper() + '_' + t_daygun + t_daygun,
			s_ad.title() + soyis.title() + t_daygun + t_daygun,			s_ad.title() + '_' + soyis.title() + t_daygun + daygun, s_ad.title() + '_' + soyis.title() + '_' + t_daygun + t_daygun, s_ad.title() + soyis.title() + '_' + t_daygun + t_daygun,
			
			s_ad.upper() + dtarihi,										s_ad.upper() + '_' + dtarihi,
			s_ad.title() + dtarihi,										s_ad.title() + '_' + dtarihi,
			s_ad.upper() + t_dtarihi,									s_ad.upper() + '_' + t_dtarihi,
			s_ad.title() + t_dtarihi,									s_ad.title() + '_' + t_dtarihi,
			
			s_ad.upper() + soyis + dtarihi,								s_ad.upper() + '_' + soyis + dtarihi, s_ad.upper() + '_' + soyis + '_' + dtarihi, s_ad.upper() + soyis + '_' + dtarihi,
			s_ad.upper() + soyis.upper() + dtarihi,						s_ad.upper() + '_' + soyis.upper() + dtarihi, s_ad.upper() + '_' + soyis.upper() + '_' + dtarihi, s_ad.upper() + soyis.upper() + '_' + dtarihi,
			s_ad.upper() + soyis.title() + dtarihi,						s_ad.upper() + '_' + soyis.title() + dtarihi, s_ad.upper() + '_' + soyis.title() + '_' + dtarihi, s_ad.upper() + soyis.title() + '_' + dtarihi,
			s_ad.title() + soyis + dtarihi,								s_ad.title() + '_' + soyis + dtarihi, s_ad.title() + '_' + soyis + '_' + dtarihi, s_ad.title() + soyis + '_' + dtarihi,
			s_ad.title() + soyis.upper() + dtarihi,						s_ad.title() + '_' + soyis.upper() + dtarihi, s_ad.title() + '_' + soyis.upper() + '_' + dtarihi, s_ad.title() + soyis.upper() + '_' + dtarihi,
			s_ad.title() + soyis.title() + dtarihi,						s_ad.title() + '_' + soyis.title() + dtarihi, s_ad.title() + '_' + soyis.title() + '_' + dtarihi, s_ad.title() + soyis.title() + '_' + dtarihi,
			
			s_ad.upper() + soyis + t_dtarihi,							s_ad.upper() + '_' + soyis + t_dtarihi, s_ad.upper() + '_' + soyis + '_' + t_dtarihi, s_ad.upper() + soyis + '_' + t_dtarihi,
			s_ad.upper() + soyis.upper() + t_dtarihi,					s_ad.upper() + '_' + soyis.upper() + t_dtarihi, s_ad.upper() + '_' + soyis.upper() + '_' + t_dtarihi, s_ad.upper() + soyis.upper() + '_' + t_dtarihi,
			s_ad.upper() + soyis.title() + t_dtarihi,					s_ad.upper() + '_' + soyis.title() + t_dtarihi, s_ad.upper() + '_' + soyis.title() + '_' + t_dtarihi, s_ad.upper() + soyis.title() + '_' + t_dtarihi,
			s_ad.title() + soyis + t_dtarihi,							s_ad.title() + '_' + soyis + dtarihi, s_ad.title() + '_' + soyis + '_' + t_dtarihi, s_ad.title() + soyis + '_' + t_dtarihi,
			s_ad.title() + soyis.upper() + t_dtarihi,					s_ad.title() + '_' + soyis.upper() + dtarihi, s_ad.title() + '_' + soyis.upper() + '_' + t_dtarihi, s_ad.title() + soyis.upper() + '_' + t_dtarihi,
			s_ad.title() + soyis.title() + t_dtarihi,					s_ad.title() + '_' + soyis.title() + dtarihi, s_ad.title() + '_' + soyis.title() + '_' + t_dtarihi, s_ad.title() + soyis.title() + '_' + t_dtarihi,
			
			#######################################################################################################

			s_soyis + ad,												s_soyis + '_' + ad,
			
			s_soyis.upper() + ad,										s_soyis.upper() + '_' + ad,
			s_soyis.upper() + ad.upper(),								s_soyis.upper() + '_' + ad.upper(),
			s_soyis.upper() + ad.title(),								s_soyis.upper() + '_' + ad.title(),
			s_soyis.title() + ad,										s_soyis.title() + '_' + ad,
			s_soyis.title() + ad.upper(),								s_soyis.title() + '_' + ad.upper(),
			s_soyis.title() + ad.title(),								s_soyis.title() + '_' + ad.title(),
			
			s_soyis + pkodu,											s_soyis + '_' + pkodu,
			s_soyis + pkodu + pkodu,									s_soyis + '_' + pkodu + pkodu,
			s_soyis + pkodu + t_pkodu,									s_soyis + '_' + pkodu + t_pkodu,
			s_soyis + t_pkodu,											s_soyis + '_' + t_pkodu,
			s_soyis + t_pkodu + pkodu,									s_soyis + '_' + t_pkodu + pkodu,
			s_soyis + t_pkodu + t_pkodu,								s_soyis + '_' + t_pkodu + t_pkodu,

			s_soyis + ad + pkodu,										s_soyis + '_' + ad + pkodu, s_soyis + '_' + ad + '_' + pkodu, s_soyis + ad + '_' + pkodu,
			s_soyis + ad + pkodu + pkodu,								s_soyis + '_' + ad + pkodu + pkodu, s_soyis + '_' + ad + '_' + pkodu + pkodu, s_soyis + ad + '_' + pkodu + pkodu,
			s_soyis + ad + pkodu + t_pkodu,								s_soyis + '_' + ad + pkodu + t_pkodu, s_soyis + '_' + ad + '_' + pkodu + t_pkodu, s_soyis + ad + '_' + pkodu + t_pkodu,
			s_soyis + ad + t_pkodu,										s_soyis + '_' + ad + t_pkodu, s_soyis + '_' + ad + '_' + t_pkodu, s_soyis + ad + '_' + t_pkodu,
			s_soyis + ad + t_pkodu + pkodu,								s_soyis + '_' + ad + t_pkodu + pkodu, s_soyis + '_' + ad + '_' + t_pkodu + pkodu, s_soyis + ad + '_' + t_pkodu + pkodu,
			s_soyis + ad + t_pkodu + t_pkodu,							s_soyis + '_' + ad + t_pkodu + t_pkodu, s_soyis + '_' + ad + '_' + t_pkodu + t_pkodu, s_soyis + ad + '_' + t_pkodu + t_pkodu,
			
			s_soyis.upper() + pkodu,									s_soyis.upper() + '_' + pkodu,
			s_soyis.upper() + pkodu + pkodu,							s_soyis.upper() + '_' + pkodu + pkodu,
			s_soyis.upper() + pkodu + t_pkodu,							s_soyis.upper() + '_' + pkodu + t_pkodu,
			s_soyis.upper() + t_pkodu,									s_soyis.upper() + '_' + t_pkodu,
			s_soyis.upper() + t_pkodu + pkodu,							s_soyis.upper() + '_' + t_pkodu + pkodu,
			s_soyis.upper() + t_pkodu + t_pkodu,						s_soyis.upper() + '_' + t_pkodu + t_pkodu,

			s_soyis.title() + pkodu,									s_soyis.title() + '_' + pkodu,
			s_soyis.title() + pkodu + pkodu,							s_soyis.title() + '_' + pkodu + pkodu,
			s_soyis.title() + pkodu + t_pkodu,							s_soyis.title() + '_' + pkodu + t_pkodu,
			s_soyis.title() + t_pkodu,									s_soyis.title() + '_' + t_pkodu,
			s_soyis.title() + t_pkodu + pkodu,							s_soyis.title() + '_' + t_pkodu + pkodu,
			s_soyis.title() + t_pkodu + t_pkodu,						s_soyis.title() + '_' + t_pkodu + t_pkodu,

			s_soyis.upper() + ad + pkodu,								s_soyis.upper() + '_' + ad + pkodu, s_soyis.upper() + '_' + ad + '_' + pkodu, s_soyis.upper() + ad + '_' + pkodu,
			s_soyis.upper() + ad.upper() + pkodu,						s_soyis.upper() + '_' + ad.upper() + pkodu, s_soyis.upper() + '_' + ad.upper() + '_' + pkodu, s_soyis.upper() + ad.upper() + '_' + pkodu,
			s_soyis.upper() + ad.title() + pkodu,						s_soyis.upper() + '_' + ad.title() + pkodu, s_soyis.upper() + '_' + ad.title() + '_' + pkodu, s_soyis.upper() + ad.title() + '_' + pkodu,
			s_soyis.title() + ad + pkodu,								s_soyis.title() + '_' + ad + pkodu, s_soyis.title() + '_' + ad + '_' + pkodu, s_soyis.title() + ad + '_' + pkodu,
			s_soyis.title() + ad.upper() + pkodu,						s_soyis.title() + '_' + ad.upper() + pkodu, s_soyis.title() + '_' + ad.upper() + '_' + pkodu, s_soyis.title() + ad.upper() + '_' + pkodu,
			s_soyis.title() + ad.title() + pkodu,						s_soyis.title() + '_' + ad.title() + pkodu, s_soyis.title() + '_' + ad.title() + '_' + pkodu, s_soyis.title() + ad.title() + '_' + pkodu,
			
			s_soyis.upper() + ad + pkodu + pkodu,						s_soyis.upper() + '_' + ad + pkodu + pkodu, s_soyis.upper() + '_' + ad + '_' + pkodu + pkodu, s_soyis.upper() + ad + '_' + pkodu + pkodu,
			s_soyis.upper() + ad.upper() + pkodu + pkodu,				s_soyis.upper() + '_' + ad.upper() + pkodu + pkodu, s_soyis.upper() + '_' + ad.upper() + '_' + pkodu + pkodu, s_soyis.upper() + ad.upper() + '_' + pkodu + pkodu,
			s_soyis.upper() + ad.title() + pkodu + pkodu,				s_soyis.upper() + '_' + ad.title() + pkodu + pkodu, s_soyis.upper() + '_' + ad.title() + '_' + pkodu + pkodu, s_soyis.upper() + ad.title() + '_' + pkodu + pkodu,
			s_soyis.title() + ad + pkodu + pkodu,						s_soyis.title() + '_' + ad + pkodu + pkodu, s_soyis.title() + '_' + ad + '_' + pkodu + pkodu, s_soyis.title() + ad + '_' + pkodu + pkodu,
			s_soyis.title() + ad.upper() + pkodu + pkodu,				s_soyis.title() + '_' + ad.upper() + pkodu + pkodu, s_soyis.title() + '_' + ad.upper() + '_' + pkodu + pkodu, s_soyis.title() + ad.upper() + '_' + pkodu + pkodu,
			s_soyis.title() + ad.title() + pkodu + pkodu,				s_soyis.title() + '_' + ad.title() + pkodu + pkodu, s_soyis.title() + '_' + ad.title() + '_' + pkodu + pkodu, s_soyis.title() + ad.title() + '_' + pkodu + pkodu,
			
			s_soyis.upper() + ad + pkodu + t_pkodu,						s_soyis.upper() + '_' + ad + pkodu + t_pkodu, s_soyis.upper() + '_' + ad + '_' + pkodu + t_pkodu, s_soyis.upper() + ad + '_' + pkodu + t_pkodu,
			s_soyis.upper() + ad.upper() + pkodu + t_pkodu,  			s_soyis.upper() + '_' + ad.upper() + pkodu + t_pkodu, s_soyis.upper() + '_' + ad.upper() + '_' + pkodu + t_pkodu, s_soyis.upper() + ad.upper() + '_' + pkodu + t_pkodu,
			s_soyis.upper() + ad.title() + pkodu + t_pkodu,				s_soyis.upper() + '_' + ad.title() + pkodu + t_pkodu, s_soyis.upper() + '_' + ad.title() + '_' + pkodu + t_pkodu, s_soyis.upper() + ad.title() + '_' + pkodu + t_pkodu,
			s_soyis.title() + ad + pkodu + t_pkodu,						s_soyis.title() + '_' + ad + pkodu + t_pkodu, s_soyis.title() + '_' + ad + '_' + pkodu + t_pkodu, s_soyis.title() + ad + '_' + pkodu + t_pkodu,
			s_soyis.title() + ad.upper() + pkodu + t_pkodu,				s_soyis.title() + '_' + ad.upper() + pkodu + t_pkodu, s_soyis.title() + '_' + ad.upper() + '_' + pkodu + t_pkodu, s_soyis.title() + ad.upper() + '_' + pkodu + t_pkodu,
			s_soyis.title() + ad.title() + pkodu + t_pkodu,				s_soyis.title() + '_' + ad.title() + pkodu + t_pkodu, s_soyis.title() + '_' + ad.title() + '_' + pkodu + t_pkodu, s_soyis.title() + ad.title() + '_' + pkodu + t_pkodu,
			
			s_soyis.upper() + ad + t_pkodu,								s_soyis.upper() + '_' + ad + t_pkodu, s_soyis.upper() + '_' + ad + '_' + t_pkodu, s_soyis.upper() + ad + '_' + t_pkodu,
			s_soyis.upper() + ad.upper() + t_pkodu,						s_soyis.upper() + '_' + ad.upper() + t_pkodu, s_soyis.upper() + '_' + ad.upper() + '_' + t_pkodu, s_soyis.upper() + ad.upper() + '_' + t_pkodu,
			s_soyis.upper() + ad.title() + t_pkodu,						s_soyis.upper() + '_' + ad.title() + t_pkodu, s_soyis.upper() + '_' + ad.title() + '_' + t_pkodu, s_soyis.upper() + ad.title() + '_' + t_pkodu,
			s_soyis.title() + ad + t_pkodu,								s_soyis.title() + '_' + ad + t_pkodu, s_soyis.title() + '_' + ad + '_' + t_pkodu, s_soyis.title() + ad + '_' + t_pkodu,
			s_soyis.title() + ad.upper() + t_pkodu,						s_soyis.title() + '_' + ad.upper() + t_pkodu, s_soyis.title() + '_' + ad.upper() + '_' + t_pkodu, s_soyis.title() + ad.upper() + '_' + t_pkodu,
			s_soyis.title() + ad.title() + t_pkodu,						s_soyis.title() + '_' + ad.title() + t_pkodu, s_soyis.title() + '_' + ad.title() + '_' + t_pkodu, s_soyis.title() + ad.title() + '_' + t_pkodu,
			
			s_soyis.upper() + ad + t_pkodu + pkodu,						s_soyis.upper() + '_' + ad + t_pkodu + pkodu, s_soyis.upper() + '_' + ad + '_' + t_pkodu + pkodu, s_soyis.upper() + ad + '_' + t_pkodu + pkodu,
			s_soyis.upper() + ad.upper() + t_pkodu + pkodu,				s_soyis.upper() + '_' + ad.upper() + t_pkodu + pkodu, s_soyis.upper() + '_' + ad.upper() + '_' + t_pkodu + pkodu, s_soyis.upper() + ad.upper() + '_' + t_pkodu + pkodu,
			s_soyis.upper() + ad.title() + t_pkodu + pkodu,				s_soyis.upper() + '_' + ad.title() + t_pkodu + pkodu, s_soyis.upper() + '_' + ad.title() + '_' + t_pkodu + pkodu, s_soyis.upper() + ad.title() + '_' + t_pkodu + pkodu,
			s_soyis.title() + ad + t_pkodu + pkodu,						s_soyis.title() + '_' + ad + t_pkodu + pkodu, s_soyis.title() + '_' + ad + '_' + t_pkodu + pkodu, s_soyis.title() + ad + '_' + t_pkodu + pkodu,
			s_soyis.title() + ad.upper() + t_pkodu + pkodu,				s_soyis.title() + '_' + ad.upper() + t_pkodu + pkodu, s_soyis.title() + '_' + ad.upper() + '_' + t_pkodu + pkodu, s_soyis.title() + ad.upper() + '_' + t_pkodu + pkodu,
			s_soyis.title() + ad.title() + t_pkodu + pkodu,				s_soyis.title() + '_' + ad.title() + t_pkodu + pkodu, s_soyis.title() + '_' + ad.title() + '_' + t_pkodu + pkodu, s_soyis.title() + ad.title() + '_' + t_pkodu + pkodu,
			
			s_soyis.upper() + ad + t_pkodu + t_pkodu,					s_soyis.upper() + '_' + ad + t_pkodu + t_pkodu, s_soyis.upper() + '_' + ad + '_' + t_pkodu + t_pkodu, s_soyis.upper() + ad + '_' + t_pkodu + t_pkodu,
			s_soyis.upper() + ad.upper() + t_pkodu + t_pkodu,			s_soyis.upper() + '_' + ad.upper() + t_pkodu + t_pkodu, s_soyis.upper() + '_' + ad.upper() + '_' + t_pkodu + t_pkodu, s_soyis.upper() + ad.upper() + '_' + t_pkodu + t_pkodu,
			s_soyis.upper() + ad.title() + t_pkodu + t_pkodu,			s_soyis.upper() + '_' + ad.title() + t_pkodu + t_pkodu, s_soyis.upper() + '_' + ad.title() + '_' + t_pkodu + t_pkodu, s_soyis.upper() + ad.title() + '_' + t_pkodu + t_pkodu,
			s_soyis.title() + ad + t_pkodu + t_pkodu,					s_soyis.title() + '_' + ad + t_pkodu + t_pkodu, s_soyis.title() + '_' + ad + '_' + t_pkodu + t_pkodu, s_soyis.title() + ad + '_' + t_pkodu + t_pkodu,
			s_soyis.title() + ad.upper() + t_pkodu + t_pkodu,			s_soyis.title() + '_' + ad.upper() + t_pkodu + t_pkodu, s_soyis.title() + '_' + ad.upper() + '_' + t_pkodu + t_pkodu, s_soyis.title() + ad.upper() + '_' + t_pkodu + t_pkodu,
			s_soyis.title() + ad.title() + t_pkodu + t_pkodu,			s_soyis.title() + '_' + ad.title() + t_pkodu + t_pkodu, s_soyis.title() + '_' + ad.title() + '_' + t_pkodu + t_pkodu, s_soyis.title() + ad.title() + '_' + t_pkodu + t_pkodu,
			
			#########################################################################################################################################################################################

			s_soyis + dyili,											s_soyis + '_' + dyili,
			s_soyis + dyili + dyili,									s_soyis + '_' + dyili + dyili,
			s_soyis + dyili + t_dyili,									s_soyis + '_' + dyili + t_dyili,
			s_soyis + t_dyili,											s_soyis + '_' + t_dyili,
			s_soyis + t_dyili + dyili,									s_soyis + '_' + t_dyili + dyili,
			s_soyis + t_dyili + t_dyili,								s_soyis + '_' + t_dyili + t_dyili,

			s_soyis + ad + dyili,										s_soyis + '_' + ad + dyili, s_soyis + '_' + ad + '_' + dyili, s_soyis + ad + '_' + dyili,
			s_soyis + ad + dyili + dyili,								s_soyis + '_' + ad + dyili + dyili, s_soyis + '_' + ad + '_' + dyili + dyili, s_soyis + ad + '_' + dyili + dyili,
			s_soyis + ad + dyili + t_dyili,								s_soyis + '_' + ad + dyili + t_dyili, s_soyis + '_' + ad + '_' + dyili + t_dyili, s_soyis + ad + '_' + dyili + t_dyili,
			s_soyis + ad + t_dyili,										s_soyis + '_' + ad + t_dyili, s_soyis + '_' + ad + '_' + t_dyili, s_soyis + ad + '_' + t_dyili,
			s_soyis + ad + t_dyili + dyili,								s_soyis + '_' + ad + t_dyili + dyili, s_soyis + '_' + ad + '_' + t_dyili + dyili, s_soyis + ad + '_' + t_dyili + dyili,
		    s_soyis + ad + t_dyili + t_dyili,							s_soyis + '_' + ad + t_dyili + t_dyili, s_soyis + '_' + ad + '_' + t_dyili + t_dyili, s_soyis + ad + '_' + t_dyili + t_dyili,
			s_soyis + daygun,											s_soyis + '_' + daygun,
			
			s_soyis + daygun + daygun,									s_soyis + '_' + daygun + daygun,
			s_soyis + daygun + t_daygun,								s_soyis + '_' + daygun + t_daygun,
			s_soyis + t_daygun,											s_soyis + '_' + t_daygun,
		    s_soyis + t_daygun + daygun,								s_soyis + '_' + t_daygun + daygun,
			s_soyis + t_daygun + t_daygun,								s_soyis + '_' + t_daygun + t_daygun,
			s_soyis + ad + daygun,										s_soyis + '_' + ad + daygun, s_soyis + '_' + ad + '_' + daygun, s_soyis + ad + '_' + daygun,
			s_soyis + ad + t_daygun,									s_soyis + '_' + ad + t_daygun, s_soyis + '_' + ad + '_' + t_daygun, s_soyis + ad + '_' + t_daygun,
			
			s_soyis + ad + dtarihi,										s_soyis + '_' + ad + dtarihi, s_soyis + '_' + ad + '_' + dtarihi, s_soyis + ad + '_' + dtarihi,
			s_soyis + ad + t_dtarihi,									s_soyis + '_' + ad + t_dtarihi, s_soyis + '_' + ad + '_' + t_dtarihi, s_soyis + ad + '_' + t_dtarihi,
			
			#######################################################################################################################################################

			s_soyis.upper() + dyili,									s_soyis.upper() + '_' + dyili,
			s_soyis.upper() + dyili + dyili,							s_soyis.upper() + '_' + dyili + dyili,
			s_soyis.upper() + dyili + t_dyili,							s_soyis.upper() + '_' + dyili + t_dyili,
			s_soyis.upper() + t_dyili,									s_soyis.upper() + '_' + t_dyili,
			s_soyis.upper() + t_dyili + dyili,							s_soyis.upper() + '_' + t_dyili + dyili,
			s_soyis.upper() + t_dyili + t_dyili,						s_soyis.upper() + '_' + t_dyili + t_dyili,

			s_soyis.title() + dyili,									s_soyis.title() + '_' + dyili,
			s_soyis.title() + dyili + dyili,							s_soyis.title() + '_' + dyili + dyili,
			s_soyis.title() + dyili + t_dyili,							s_soyis.title() + '_' + dyili + t_dyili,
			s_soyis.title() + t_dyili,									s_soyis.title() + '_' + t_dyili,
			s_soyis.title() + t_dyili + dyili,							s_soyis.title() + '_' + t_dyili + dyili,
			s_soyis.title() + t_dyili + t_dyili,						s_soyis.title() + '_' + t_dyili + t_dyili,

			s_soyis.upper() + ad + dyili,								s_soyis.upper() + '_' + ad + dyili, s_soyis.upper() + '_' + ad + '_' + dyili, s_soyis.upper() + ad + '_' + dyili,
			s_soyis.upper() + ad.upper() + dyili,						s_soyis.upper() + '_' + ad.upper() + dyili, s_soyis.upper() + '_' + ad.upper() + '_' + dyili, s_soyis.upper() + ad.upper() + '_' + dyili,
			s_soyis.upper() + ad.title() + dyili,						s_soyis.upper() + '_' + ad.title() + dyili, s_soyis.upper() + '_' + ad.title() + '_' + dyili, s_soyis.upper() + ad.title() + '_' + dyili,
			s_soyis.title() + ad + dyili,								s_soyis.title() + '_' + ad + dyili, s_soyis.title() + '_' + ad + '_' + dyili, s_soyis.title() + ad + '_' + dyili,
			s_soyis.title() + ad.upper() + dyili,						s_soyis.title() + '_' + ad.upper() + dyili, s_soyis.title() + '_' + ad.upper() + '_' + dyili, s_soyis.title() + ad.upper() + '_' + dyili,
			s_soyis.title() + ad.title() + dyili,						s_soyis.title() + '_' + ad.title() + dyili, s_soyis.title() + '_' + ad.title() + '_' + dyili, s_soyis.title() + ad.title() + '_' + dyili,
			
			s_soyis.upper() + ad + dyili + dyili,						s_soyis.upper() + '_' + ad + dyili + dyili, s_soyis.upper() + '_' + ad + '_' + dyili + dyili, s_soyis.upper() + ad + '_' + dyili + dyili,
			s_soyis.upper() + ad.upper() + dyili + dyili,				s_soyis.upper() + '_' + ad.upper() + dyili + dyili, s_soyis.upper() + '_' + ad.upper() + '_' + dyili + dyili, s_soyis.upper() + ad.upper() + '_' + dyili + dyili,
			s_soyis.upper() + ad.title() + dyili + dyili,				s_soyis.upper() + '_' + ad.title() + dyili + dyili, s_soyis.upper() + '_' + ad.title() + '_' + dyili + dyili, s_soyis.upper() + ad.title() + '_' + dyili + dyili,
			s_soyis.title() + ad + dyili + dyili,						s_soyis.title() + '_' + ad + dyili + dyili, s_soyis.title() + '_' + ad + '_' + dyili + dyili, s_soyis.title() + ad + '_' + dyili + dyili,
			s_soyis.title() + ad.upper() + dyili + dyili,				s_soyis.title() + '_' + ad.upper() + dyili + dyili, s_soyis.title() + '_' + ad.upper() + '_' + dyili + dyili, s_soyis.title() + ad.upper() + '_' + dyili + dyili,
			s_soyis.title() + ad.title() + dyili + dyili,				s_soyis.title() + '_' + ad.title() + dyili + dyili, s_soyis.title() + '_' + ad.title() + '_' + dyili + dyili, s_soyis.title() + ad.title() + '_' + dyili + dyili,
			
			s_soyis.upper() + ad + dyili + t_dyili,						s_soyis.upper() + '_' + ad + dyili + t_dyili, s_soyis.upper() + '_' + ad + '_' + dyili + t_dyili, s_soyis.upper() + ad + '_' + dyili + t_dyili,
			s_soyis.upper() + ad.upper() + dyili + t_dyili,  			s_soyis.upper() + '_' + ad.upper() + dyili + t_dyili, s_soyis.upper() + '_' + ad.upper() + '_' + dyili + t_dyili, s_soyis.upper() + ad.upper() + '_' + dyili + t_dyili,
			s_soyis.upper() + ad.title() + dyili + t_dyili,				s_soyis.upper() + '_' + ad.title() + dyili + t_dyili, s_soyis.upper() + '_' + ad.title() + '_' + dyili + t_dyili, s_soyis.upper() + ad.title() + '_' + dyili + t_dyili,
			s_soyis.title() + ad + dyili + t_dyili,						s_soyis.title() + '_' + ad + dyili + t_dyili, s_soyis.title() + '_' + ad + '_' + dyili + t_dyili, s_soyis.title() + ad + '_' + dyili + t_dyili,
			s_soyis.title() + ad.upper() + dyili + t_dyili,				s_soyis.title() + '_' + ad.upper() + dyili + t_dyili, s_soyis.title() + '_' + ad.upper() + '_' + dyili + t_dyili, s_soyis.title() + ad.upper() + '_' + dyili + t_dyili,
			s_soyis.title() + ad.title() + dyili + t_dyili,				s_soyis.title() + '_' + ad.title() + dyili + t_dyili, s_soyis.title() + '_' + ad.title() + '_' + dyili + t_dyili, s_soyis.title() + ad.title() + '_' + dyili + t_dyili,
			
			s_soyis.upper() + ad + t_dyili,								s_soyis.upper() + '_' + ad + t_dyili, s_soyis.upper() + '_' + ad + '_' + t_dyili, s_soyis.upper() + ad + '_' + t_dyili,
			s_soyis.upper() + ad.upper() + t_dyili,						s_soyis.upper() + '_' + ad.upper() + t_dyili, s_soyis.upper() + '_' + ad.upper() + '_' + t_dyili, s_soyis.upper() + ad.upper() + '_' + t_dyili,
			s_soyis.upper() + ad.title() + t_dyili,						s_soyis.upper() + '_' + ad.title() + t_dyili, s_soyis.upper() + '_' + ad.title() + '_' + t_dyili, s_soyis.upper() + ad.title() + '_' + t_dyili,
			s_soyis.title() + ad + t_dyili,								s_soyis.title() + '_' + ad + t_dyili, s_soyis.title() + '_' + ad + '_' + t_dyili, s_soyis.title() + ad + '_' + t_dyili,
			s_soyis.title() + ad.upper() + t_dyili,						s_soyis.title() + '_' + ad.upper() + t_dyili, s_soyis.title() + '_' + ad.upper() + '_' + t_dyili, s_soyis.title() + ad.upper() + '_' + t_dyili,
			s_soyis.title() + ad.title() + t_dyili,						s_soyis.title() + '_' + ad.title() + t_dyili, s_soyis.title() + '_' + ad.title() + '_' + t_dyili, s_soyis.title() + ad.title() + '_' + t_dyili,
			
			s_soyis.upper() + ad + t_dyili + dyili,						s_soyis.upper() + '_' + ad + t_dyili + dyili, s_soyis.upper() + '_' + ad + '_' + t_dyili + dyili, s_soyis.upper() + ad + '_' + t_dyili + dyili,
			s_soyis.upper() + ad.upper() + t_dyili + dyili,				s_soyis.upper() + '_' + ad.upper() + t_dyili + dyili, s_soyis.upper() + '_' + ad.upper() + '_' + t_dyili + dyili, s_soyis.upper() + ad.upper() + '_' + t_dyili + dyili,
			s_soyis.upper() + ad.title() + t_dyili + dyili,				s_soyis.upper() + '_' + ad.title() + t_dyili + dyili, s_soyis.upper() + '_' + ad.title() + '_' + t_dyili + dyili, s_soyis.upper() + ad.title() + '_' + t_dyili + dyili,
			s_soyis.title() + ad + t_dyili + dyili,						s_soyis.title() + '_' + ad + t_dyili + dyili, s_soyis.title() + '_' + ad + '_' + t_dyili + dyili, s_soyis.title() + ad + '_' + t_dyili + dyili,
			s_soyis.title() + ad.upper() + t_dyili + dyili,				s_soyis.title() + '_' + ad.upper() + t_dyili + dyili, s_soyis.title() + '_' + ad.upper() + '_' + t_dyili + dyili, s_soyis.title() + ad.upper() + '_' + t_dyili + dyili,
			s_soyis.title() + ad.title() + t_dyili + dyili,				s_soyis.title() + '_' + ad.title() + t_dyili + dyili, s_soyis.title() + '_' + ad.title() + '_' + t_dyili + dyili, s_soyis.title() + ad.title() + '_' + t_dyili + dyili,
			
			s_soyis.upper() + ad + t_dyili + t_dyili,					s_soyis.upper() + '_' + ad + t_dyili + t_dyili, s_soyis.upper() + '_' + ad + '_' + t_dyili + t_dyili, s_soyis.upper() + ad + '_' + t_dyili + t_dyili,
			s_soyis.upper() + ad.upper() + t_dyili + t_dyili,			s_soyis.upper() + '_' + ad.upper() + t_dyili + t_dyili, s_soyis.upper() + '_' + ad.upper() + '_' + t_dyili + t_dyili, s_soyis.upper() + ad.upper() + '_' + t_dyili + t_dyili,
			s_soyis.upper() + ad.title() + t_dyili + t_dyili,		    s_soyis.upper() + '_' + ad.title() + t_dyili + t_dyili, s_soyis.upper() + '_' + ad.title() + '_' + t_dyili + t_dyili, s_soyis.upper() + ad.title() + '_' + t_dyili + t_dyili,
			s_soyis.title() + ad + t_dyili + t_dyili,					s_soyis.title() + '_' + ad + t_dyili + t_dyili, s_soyis.title() + '_' + ad + '_' + t_dyili + t_dyili, s_soyis.title() + ad + '_' + t_dyili + t_dyili,
			s_soyis.title() + ad.upper() + t_dyili + t_dyili,			s_soyis.title() + '_' + ad.upper() + t_dyili + t_dyili, s_soyis.title() + '_' + ad.upper() + '_' + t_dyili + t_dyili, s_soyis.title() + ad.upper() + '_' + t_dyili + t_dyili,
			s_soyis.title() + ad.title() + t_dyili + t_dyili,			s_soyis.title() + '_' + ad.title() + t_dyili + t_dyili, s_soyis.title() + '_' + ad.title() + '_' + t_dyili + t_dyili, s_soyis.title() + ad.title() + '_' + t_dyili + t_dyili,
			
			s_soyis.upper() + daygun,									s_soyis.upper() + '_' + daygun,
			s_soyis.title() + daygun,									s_soyis.title() + '_' + daygun,
			s_soyis.upper() + daygun + daygun,							s_soyis.upper() + '_' + daygun + daygun,
			s_soyis.title() + daygun + daygun,							s_soyis.title() + '_' + daygun + daygun,

			s_soyis.upper() + daygun + t_daygun,						s_soyis.upper() + '_' + daygun + t_daygun,
			s_soyis.title() + daygun + t_daygun,						s_soyis.title() + '_' + daygun + t_daygun,
			s_soyis.upper() + t_daygun,									s_soyis.upper() + '_' + t_daygun,
			s_soyis.title() + t_daygun,									s_soyis.title() + '_' + t_daygun,
			
			s_soyis.upper() + t_daygun + daygun,						s_soyis.upper() + '_' + t_daygun + daygun,
			s_soyis.title() + t_daygun + daygun,						s_soyis.title() + '_' + t_daygun + daygun,
			s_soyis.upper() + t_daygun + t_daygun,						s_soyis.upper() + '_' + t_daygun + t_daygun,
			s_soyis.title() + t_daygun + t_daygun,						s_soyis.title() + '_' + t_daygun + t_daygun,

			s_soyis.upper() + ad + daygun,								s_soyis.upper() + '_' + ad + daygun, s_soyis.upper() + '_' + ad + '_' + daygun, s_soyis.upper() + ad + '_' + daygun,
			s_soyis.upper() + ad.upper() + daygun,						s_soyis.upper() + '_' + ad.upper() + daygun, s_soyis.upper() + '_' + ad.upper() + '_' + daygun, s_soyis.upper() + ad.upper() + '_' + daygun,
			s_soyis.upper() + ad.title() + daygun,						s_soyis.upper() + '_' + ad.title() + daygun, s_soyis.upper() + '_' + ad.title() + '_' + daygun, s_soyis.upper() + ad.title() + '_' + daygun,
			s_soyis.title() + ad + daygun,								s_soyis.title() + '_' + ad + daygun, s_soyis.title() + '_' + ad + '_' + daygun, s_soyis.title() + ad + '_' + daygun,
			s_soyis.title() + ad.upper() + daygun,						s_soyis.title() + '_' + ad.upper() + daygun, s_soyis.title() + '_' + ad.upper() + '_' + daygun, s_soyis.title() + ad.upper() + '_' + daygun,
			s_soyis.title() + ad.title() + daygun,						s_soyis.title() + '_' + ad.title() + daygun, s_soyis.title() + '_' + ad.title() + '_' + daygun, s_soyis.title() + ad.title() + '_' + daygun,
			
			s_soyis.upper() + ad + daygun + daygun,						s_soyis.upper() + '_' + ad + daygun + daygun, s_soyis.upper() + '_' + ad + '_' + daygun + daygun, s_soyis.upper() + ad + '_' + daygun + daygun,
			s_soyis.upper() + ad.upper() + daygun + daygun,				s_soyis.upper() + '_' + ad.upper() + daygun + daygun, s_soyis.upper() + '_' + ad.upper() + '_' + daygun + daygun, s_soyis.upper() + ad.upper() + '_' + daygun + daygun,
			s_soyis.upper() + ad.title() + daygun + daygun,				s_soyis.upper() + '_' + ad.title() + daygun + daygun, s_soyis.upper() + '_' + ad.title() + '_' + daygun + daygun, s_soyis.upper() + ad.title() + '_' + daygun + daygun,
			s_soyis.title() + ad + daygun + daygun,						s_soyis.title() + '_' + ad + daygun + daygun, s_soyis.title() + '_' + ad + '_' + daygun + daygun, s_soyis.title() + ad + '_' + daygun + daygun,
			s_soyis.title() + ad.upper() + daygun + daygun,				s_soyis.title() + '_' + ad.upper() + daygun + daygun, s_soyis.title() + '_' + ad.upper() + '_' + daygun + daygun, s_soyis.title() + ad.upper() + '_' + daygun + daygun,
			s_soyis.title() + ad.title() + daygun + daygun,				s_soyis.title() + '_' + ad.title() + daygun + daygun, s_soyis.title() + '_' + ad.title() + '_' + daygun + daygun, s_soyis.title() + ad.title() + '_' + daygun + daygun,
			
			s_soyis.upper() + ad + daygun + t_daygun,					s_soyis.upper() + '_' + ad + daygun + t_daygun, s_soyis.upper() + '_' + ad + '_' + daygun + t_daygun, s_soyis.upper() + ad + '_' + daygun + t_daygun,
			s_soyis.upper() + ad.upper() + daygun + t_daygun,			s_soyis.upper() + '_' + ad.upper() + daygun + t_daygun, s_soyis.upper() + '_' + ad.upper() + '_' + daygun + t_daygun, s_soyis.upper() + ad.upper() + '_' + daygun + t_daygun,
			s_soyis.upper() + ad.title() + daygun + t_daygun,			s_soyis.upper() + '_' + ad.title() + daygun + t_daygun, s_soyis.upper() + '_' + ad.title() + '_' + daygun + t_daygun, s_soyis.upper() + ad.title() + '_' + daygun + t_daygun,
			s_soyis.title() + ad + daygun + t_daygun,					s_soyis.title() + '_' + ad + daygun + t_daygun, s_soyis.title() + '_' + ad + '_' + daygun + t_daygun, s_soyis.title() + ad + '_' + daygun + t_daygun,
			s_soyis.title() + ad.upper() + daygun + t_daygun,			s_soyis.title() + '_' + ad.upper() + daygun + t_daygun, s_soyis.title() + '_' + ad.upper() + '_' + daygun + t_daygun, s_soyis.title() + ad.upper() + '_' + daygun + t_daygun,
			s_soyis.title() + ad.title() + daygun + t_daygun,			s_soyis.title() + '_' + ad.title() + daygun + t_daygun, s_soyis.title() + '_' + ad.title() + '_' + daygun + t_daygun, s_soyis.title() + ad.title() + '_' + daygun + t_daygun,
			
			s_soyis.upper() + ad + t_daygun,							s_soyis.upper() + '_' + ad + t_daygun, s_soyis.upper() + '_' + ad + '_' + t_daygun, s_soyis.upper() + ad + '_' + t_daygun,
			s_soyis.upper() + ad.upper() + t_daygun,					s_soyis.upper() + '_' + ad.upper() + t_daygun, s_soyis.upper() + '_' + ad.upper() + '_' + t_daygun, s_soyis.upper() + ad.upper() + '_' + t_daygun,
			s_soyis.upper() + ad.title() + t_daygun,					s_soyis.upper() + '_' + ad.title() + t_daygun, s_soyis.upper() + '_' + ad.title() + '_' + t_daygun, s_soyis.upper() + ad.title() + '_' + t_daygun,
			s_soyis.title() + ad + t_daygun,							s_soyis.title() + '_' + ad + daygun, s_soyis.title() + '_' + ad + '_' + t_daygun, s_soyis.title() + ad + '_' + t_daygun,
			s_soyis.title() + ad.upper() + t_daygun,					s_soyis.title() + '_' + ad.upper() + daygun, s_soyis.title() + '_' + ad.upper() + '_' + t_daygun, s_soyis.title() + ad.upper() + '_' + t_daygun,
			s_soyis.title() + ad.title() + t_daygun,					s_soyis.title() + '_' + ad.title() + daygun, s_soyis.title() + '_' + ad.title() + '_' + t_daygun, s_soyis.title() + ad.title() + '_' + t_daygun,
			
			s_soyis.upper() + ad + t_daygun + daygun,					s_soyis.upper() + '_' + ad + t_daygun + daygun, s_soyis.upper() + '_' + ad + '_' + t_daygun + daygun, s_soyis.upper() + ad + '_' + t_daygun + daygun,
			s_soyis.upper() + ad.upper() + t_daygun + daygun,			s_soyis.upper() + '_' + ad.upper() + t_daygun + daygun, s_soyis.upper() + '_' + ad.upper() + '_' + t_daygun + daygun, s_soyis.upper() + ad.upper() + '_' + t_daygun + daygun,
			s_soyis.upper() + ad.title() + t_daygun + daygun,			s_soyis.upper() + '_' + ad.title() + t_daygun + daygun, s_soyis.upper() + '_' + ad.title() + '_' + t_daygun + daygun, s_soyis.upper() + ad.title() + '_' + t_daygun + daygun,
			s_soyis.title() + ad + t_daygun + daygun,					s_soyis.title() + '_' + ad + t_daygun + daygun, s_soyis.title() + '_' + ad + '_' + t_daygun + daygun, s_soyis.title() + ad + '_' + t_daygun + daygun,
			s_soyis.title() + ad.upper() + t_daygun + daygun,			s_soyis.title() + '_' + ad.upper() + t_daygun + daygun, s_soyis.title() + '_' + ad.upper() + '_' + t_daygun + daygun, s_soyis.title() + ad.upper() + '_' + t_daygun + daygun,
			s_soyis.title() + ad.title() + t_daygun + daygun,			s_soyis.title() + '_' + ad.title() + t_daygun + daygun, s_soyis.title() + '_' + ad.title() + '_' + t_daygun + daygun, s_soyis.title() + ad.title() + '_' + t_daygun + daygun,
			
			s_soyis.upper() + ad + t_daygun + t_daygun,					s_soyis.upper() + '_' + ad + t_daygun + t_daygun, s_soyis.upper() + '_' + ad + '_' + t_daygun + t_daygun, s_soyis.upper() + ad + '_' + t_daygun + t_daygun,
			s_soyis.upper() + ad.upper() + t_daygun + t_daygun,			s_soyis.upper() + '_' + ad.upper() + t_daygun + t_daygun, s_soyis.upper() + '_' + ad.upper() + '_' + t_daygun + t_daygun, s_soyis.upper() + ad.upper() + '_' + t_daygun + t_daygun,
			s_soyis.upper() + ad.title() + t_daygun + t_daygun,			s_soyis.upper() + '_' + ad.title() + t_daygun + t_daygun, s_soyis.upper() + '_' + ad.title() + '_' + t_daygun + t_daygun, s_soyis.upper() + ad.title() + '_' + t_daygun + t_daygun,
			s_soyis.title() + ad + t_daygun + t_daygun,					s_soyis.title() + '_' + ad + t_daygun + daygun, s_soyis.title() + '_' + ad + '_' + t_daygun + t_daygun, s_soyis.title() + ad + '_' + t_daygun + t_daygun,
			s_soyis.title() + ad.upper() + t_daygun + t_daygun,			s_soyis.title() + '_' + ad.upper() + t_daygun + daygun, s_soyis.title() + '_' + ad.upper() + '_' + t_daygun + t_daygun, s_soyis.title() + ad.upper() + '_' + t_daygun + t_daygun,
			s_soyis.title() + ad.title() + t_daygun + t_daygun,			s_soyis.title() + '_' + ad.title() + t_daygun + daygun, s_soyis.title() + '_' + ad.title() + '_' + t_daygun + t_daygun, s_soyis.title() + ad.title() + '_' + t_daygun + t_daygun,
			
			s_soyis.upper() + dtarihi,									s_soyis.upper() + '_' + dtarihi,
			s_soyis.title() + dtarihi,									s_soyis.title() + '_' + dtarihi,
			s_soyis.upper() + t_dtarihi,								s_soyis.upper() + '_' + t_dtarihi,
			s_soyis.title() + t_dtarihi,								s_soyis.title() + '_' + t_dtarihi,
			
			s_soyis.upper() + s_soyis + dtarihi,						s_soyis.upper() + '_' + s_soyis + dtarihi, s_soyis.upper() + '_' + s_soyis + '_' + dtarihi, s_soyis.upper() + s_soyis + '_' + dtarihi,
			s_soyis.upper() + s_soyis.upper() + dtarihi,				s_soyis.upper() + '_' + s_soyis.upper() + dtarihi, s_soyis.upper() + '_' + s_soyis.upper() + '_' + dtarihi, s_soyis.upper() + s_soyis.upper() + '_' + dtarihi,
			s_soyis.upper() + s_soyis.title() + dtarihi,				s_soyis.upper() + '_' + s_soyis.title() + dtarihi, s_soyis.upper() + '_' + s_soyis.title() + '_' + dtarihi, s_soyis.upper() + s_soyis.title() + '_' + dtarihi,
			s_soyis.title() + s_soyis + dtarihi,						s_soyis.title() + '_' + s_soyis + dtarihi, s_soyis.title() + '_' + s_soyis + '_' + dtarihi, s_soyis.title() + s_soyis + '_' + dtarihi,
			s_soyis.title() + s_soyis.upper() + dtarihi,				s_soyis.title() + '_' + s_soyis.upper() + dtarihi, s_soyis.title() + '_' + s_soyis.upper() + '_' + dtarihi, s_soyis.title() + s_soyis.upper() + '_' + dtarihi,
			s_soyis.title() + s_soyis.title() + dtarihi,				s_soyis.title() + '_' + s_soyis.title() + dtarihi, s_soyis.title() + '_' + s_soyis.title() + '_' + dtarihi, s_soyis.title() + s_soyis.title() + '_' + dtarihi,
			
			s_soyis.upper() + s_soyis + t_dtarihi,						s_soyis.upper() + '_' + s_soyis + t_dtarihi, s_soyis.upper() + '_' + s_soyis + '_' + t_dtarihi, s_soyis.upper() + s_soyis + '_' + t_dtarihi,
			s_soyis.upper() + s_soyis.upper() + t_dtarihi,				s_soyis.upper() + '_' + s_soyis.upper() + t_dtarihi, s_soyis.upper() + '_' + s_soyis.upper() + '_' + t_dtarihi, s_soyis.upper() + s_soyis.upper() + '_' + t_dtarihi,
			s_soyis.upper() + s_soyis.title() + t_dtarihi,				s_soyis.upper() + '_' + s_soyis.title() + t_dtarihi, s_soyis.upper() + '_' + s_soyis.title() + '_' + t_dtarihi, s_soyis.upper() + s_soyis.title() + '_' + t_dtarihi,
			s_soyis.title() + s_soyis + t_dtarihi,						s_soyis.title() + '_' + s_soyis + dtarihi, s_soyis.title() + '_' + s_soyis + '_' + t_dtarihi, s_soyis.title() + s_soyis + '_' + t_dtarihi,
			s_soyis.title() + s_soyis.upper() + t_dtarihi,				s_soyis.title() + '_' + s_soyis.upper() + dtarihi, s_soyis.title() + '_' + s_soyis.upper() + '_' + t_dtarihi, s_soyis.title() + s_soyis.upper() + '_' + t_dtarihi,
			s_soyis.title() + s_soyis.title() + t_dtarihi,				s_soyis.title() + '_' + s_soyis.title() + dtarihi, s_soyis.title() + '_' + s_soyis.title() + '_' + t_dtarihi, s_soyis.title() + s_soyis.title() + '_' + t_dtarihi

			]
for sifre in sifreler :
	if sifre not in son and len(sifre) >= minimum and len(sifre) <= maksimum :
		son.append(sifre)
		a = sifre + '!'
		b = sifre + '.'
		if a not in son and len(a) >= minimum and len(a) <= maksimum :
			son.append(a)
			son.append(b)
	elif sifre not in son and len(sifre) < minimum :
		a = sifre + '!'
		b = sifre + '.'
		if a not in son and len(a) >= minimum and len(a) <= maksimum :
			son.append(a)
			son.append(b)
random.shuffle(son)
for sifre in sessiz_sifreler :
	if sifre not in son and len(sifre) >= minimum and len(sifre) <= maksimum :
		son.append(sifre)
		a = sifre + '!'
		b = sifre + '.'
		if a not in son and len(a) >= minimum and len(a) <= maksimum :
			son.append(a)
			son.append(b)
	elif sifre not in son and len(sifre) < minimum :
		a = sifre + '!'
		b = sifre + '.'
		if a not in son and len(a) >= minimum and len(a) <= maksimum :
			son.append(a)
			son.append(b)
random.shuffle(son)
print('''
[1] Galatsaray
[2] Fenerbahçe
[3] Beşiktaş
[4] Trabzonspor
[5] Hiçbiri
''')
while True :
	try :
		soru2 = int(input('\nHedefiniz yukardaki takımlardan hangisini tutuyor : '))
		if soru2 > 5 or soru2 < 1 :
			print('\nHatalı seçim yaptınız ! ')
			continue
		break
	except ValueError :
		print('Sayı dışında bir karakter girdiniz ')
		continue
soru2 = str(soru2)
if soru2 == '1' :
	takim = 'galatasaray'
	ktakim = 'gs'
	kurulus = '1905'
elif soru2 == '2' :
	takim = 'fenerbahce'
	ktakim = 'fb'
	kurulus = '1907'
elif soru2 == '3' :
	takim = 'besiktas'
	ktakim = 'bjk'
	kurulus = '1903'
elif soru2 == '4' :
	takim = 'trabzonspor'
	ktakim = 'ts'
	kurulus = '1967'
if soru2 != '5' :
	takim_sifreleri = [ ad + takim,
						soyis + takim,
						ad + ktakim,
						soyis + ktakim,
	
						ad + ad + takim,
						ad + soyis + takim,
						soyis + ad + takim,
						soyis + soyis + takim,

						ad + ad + ktakim,
						ad + soyis + ktakim,
						soyis + ad + ktakim,
						soyis + soyis + ktakim,
						
						ad.upper() + takim,
						soyis.upper() + takim,
						ad.upper() + ktakim,
						soyis.upper() + ktakim,

						ad.upper() + ad + takim,
						ad.upper() + soyis + takim,
						soyis.upper() + ad + takim,
						soyis.upper() + soyis + takim,

						ad.upper() + ad + ktakim,
						ad.upper() + soyis + ktakim,
						soyis.upper() + ad + ktakim,
						soyis.upper() + soyis + ktakim,

						ad + takim.upper(),
						soyis + takim.upper(),
						ad + ktakim.upper(),
						soyis + ktakim.upper(),
						
						ad + ad.upper() + takim,
						ad + soyis.upper() + takim,
						soyis + ad.upper() + takim,
						soyis + soyis.upper() + takim,

						ad + ad.upper() + ktakim,
						ad + soyis.upper() + ktakim,
						soyis + ad.upper() + ktakim,
						soyis + soyis.upper() + ktakim,
						
						ad + ad + takim.upper(),
						ad + soyis + takim.upper(),
						soyis + ad + takim.upper(),
						soyis + soyis + takim.upper(),

						ad + ad + ktakim.upper(),
						ad + soyis + ktakim.upper(),
						soyis + ad + ktakim.upper(),
						soyis + soyis + ktakim.upper(),
						
						ad.upper() + takim.upper(),
						soyis.upper() + takim.upper(),
						ad.upper() + ktakim.upper(),
						soyis.upper() + ktakim.upper(),
						
						ad.upper() + ad.upper() + takim,
						ad.upper() + soyis.upper() + takim,
						soyis.upper() + ad.upper() + takim,
						soyis.upper() + soyis.upper() + takim,

						ad.upper() + ad.upper() + ktakim,
						ad.upper() + soyis.upper() + ktakim,
						soyis.upper() + ad.upper() + ktakim,
						soyis.upper() + soyis.upper() + ktakim,

						ad.upper() + ad + takim.upper(),
						ad.upper() + soyis + takim.upper(),
						soyis.upper() + ad + takim.upper(),
						soyis.upper() + soyis + takim.upper(),

						ad.upper() + ad + ktakim.upper(),
						ad.upper() + soyis + ktakim.upper(),
						soyis.upper() + ad + ktakim.upper(),
						soyis.upper() + soyis + ktakim.upper(),

						ad + ad.upper() + takim.upper(),
						ad + soyis.upper() + takim.upper(),
						soyis + ad.upper() + takim.upper(),
						soyis + soyis.upper() + takim.upper(),

						ad + ad.upper() + ktakim.upper(),
						ad + soyis.upper() + ktakim.upper(),
						soyis + ad.upper() + ktakim.upper(),
						soyis + soyis.upper() + ktakim.upper(),

						ad.upper() + ad.upper() + takim.upper(),
						ad.upper() + soyis.upper() + takim.upper(),
						soyis.upper() + ad.upper() + takim.upper(),
						soyis.upper() + soyis.upper() + takim.upper(),

						ad.upper() + ad.upper() + ktakim.upper(),
						ad.upper() + soyis.upper() + ktakim.upper(),
						soyis.upper() + ad.upper() + ktakim.upper(),
						soyis.upper() + soyis.upper() + ktakim.upper(),

						ad.title() + takim,
						soyis.title() + takim,
						ad.title() + ktakim,
						soyis.title() + ktakim,

						ad.title() + ad + takim,
						ad.title() + soyis + takim,
						soyis.title() + ad + takim,
						soyis.title() + soyis + takim,

						ad.title() + ad + ktakim,
						ad.title() + soyis + ktakim,
						soyis.title() + ad + ktakim,
						soyis.title() + soyis + ktakim,

						ad + takim.title(),
						soyis + takim.title(),
						ad + ktakim.title(),
						soyis + ktakim.title(),

						ad + ad.title() + takim,
						ad + soyis.title() + takim,
						soyis + ad.title() + takim,
						soyis + soyis.title() + takim,

						ad + ad.title() + ktakim,
						ad + soyis.title() + ktakim,
						soyis + ad.title() + ktakim,
						soyis + soyis.title() + ktakim,

						ad + ad + takim.title(),
						ad + soyis + takim.title(),
						soyis + ad + takim.title(),
						soyis + soyis + takim.title(),

						ad + ad + ktakim.title(),
						ad + soyis + ktakim.title(),
						soyis + ad + ktakim.title(),
						soyis + soyis + ktakim.title(),

						ad.title() + takim.title(),
						soyis.title() + takim.title(),
						ad.title() + ktakim.title(),
						soyis.title() + ktakim.title(),

						ad.title() + ad.title() + takim,
						ad.title() + soyis.title() + takim,
						soyis.title() + ad.title() + takim,
						soyis.title() + soyis.title() + takim,

						ad.title() + ad.title() + ktakim,
						ad.title() + soyis.title() + ktakim,
						soyis.title() + ad.title() + ktakim,
						soyis.title() + soyis.title() + ktakim,

						ad.title() + ad + takim.title(),
						ad.title() + soyis + takim.title(),
						soyis.title() + ad + takim.title(),
						soyis.title() + soyis + takim.title(),

						ad.title() + ad + ktakim.title(),
						ad.title() + soyis + ktakim.title(),
						soyis.title() + ad + ktakim.title(),
						soyis.title() + soyis + ktakim.title(),

						ad + ad.title() + takim.title(),
						ad + soyis.title() + takim.title(),
						soyis + ad.title() + takim.title(),
						soyis + soyis.title() + takim.title(),

						ad + ad.title() + ktakim.title(),
						ad + soyis.title() + ktakim.title(),
						soyis + ad.title() + ktakim.title(),
						soyis + soyis.title() + ktakim.title(),

						ad.title() + ad.title() + takim.title(),
						ad.title() + soyis.title() + takim.title(),
						soyis.title() + ad.title() + takim.title(),
						soyis.title() + soyis.title() + takim.title(),

						ad.title() + ad.title() + ktakim.title(),
						ad.title() + soyis.title() + ktakim.title(),
						soyis.title() + ad.title() + ktakim.title(),
						soyis.title() + soyis.title() + ktakim.title(),

						ad.upper() + takim.title(),
						soyis.upper() + takim.title(),
						ad.upper() + ktakim.title(),
						soyis.upper() + ktakim.title(),
		
						ad.upper() + ad.title() + takim,
						ad.upper() + soyis.title() + takim,
						soyis.upper() + ad.title() + takim,
						soyis.upper() + soyis.title() + takim,

						ad.upper() + ad.title() + ktakim,
						ad.upper() + soyis.title() + ktakim,
						soyis.upper() + ad.title() + ktakim,
						soyis.upper() + soyis.title() + ktakim,

						ad.upper() + ad + takim.title(),
						ad.upper() + soyis + takim.title(),
						soyis.upper() + ad + takim.title(),
						soyis.upper() + soyis + takim.title(),

						ad.upper() + ad + ktakim.title(),
						ad.upper() + soyis + ktakim.title(),
						soyis.upper() + ad + ktakim.title(),
						soyis.upper() + soyis + ktakim.title(),

						ad + ad.upper() + takim.title(),
						ad + soyis.upper() + takim.title(),
						soyis + ad.upper() + takim.title(),
						soyis + soyis.upper() + takim.title(),
		
						ad + ad.upper() + ktakim.title(),
						ad + soyis.upper() + ktakim.title(),
						soyis + ad.upper() + ktakim.title(),
						soyis + soyis.upper() + ktakim.title(),

						ad.title() + takim.upper(),
						soyis.title() + takim.upper(),
						ad.title() + ktakim.upper(),
						soyis.title() + ktakim.upper(),
			
						ad.title() + ad.upper() + takim,
						ad.title() + soyis.upper() + takim,
						soyis.title() + ad.upper() + takim,
						soyis.title() + soyis.upper() + takim,

						ad.title() + ad.upper() + ktakim,
						ad.title() + soyis.upper() + ktakim,
						soyis.title() + ad.upper() + ktakim,
						soyis.title() + soyis.upper() + ktakim,

						ad.title() + ad + takim.upper(),
						ad.title() + soyis + takim.upper(),
						soyis.title() + ad + takim.upper(),
						soyis.title() + soyis + takim.upper(),

						ad.title() + ad + ktakim.upper(),
						ad.title() + soyis + ktakim.upper(),
						soyis.title() + ad + ktakim.upper(),
						soyis.title() + soyis + ktakim.upper(),

						ad + ad.title() + takim.upper(),
						ad + soyis.title() + takim.upper(),
						soyis + ad.title() + takim.upper(),
						soyis + soyis.title() + takim.upper(),

						ad + ad.title() + ktakim.upper(),
						ad + soyis.title() + ktakim.upper(),
						soyis + ad.title() + ktakim.upper(),
						soyis + soyis.title() + ktakim.upper(),

						ad.upper() + ad.upper() + takim.title(),
						ad.upper() + soyis.upper() + takim.title(),
						soyis.upper() + ad.upper() + takim.title(),
						soyis.upper() + soyis.upper() + takim.title(),

						ad.upper() + ad.upper() + ktakim.title(),
						ad.upper() + soyis.upper() + ktakim.title(),
						soyis.upper() + ad.upper() + ktakim.title(),
						soyis.upper() + soyis.upper() + ktakim.title(),

						ad.upper() + ad.title() + takim.upper(),
						ad.upper() + soyis.title() + takim.upper(),
						soyis.upper() + ad.title() + takim.upper(),
						soyis.upper() + soyis.title() + takim.upper(),
	
						ad.upper() + ad.title() + ktakim.upper(),
						ad.upper() + soyis.title() + ktakim.upper(),
						soyis.upper() + ad.title() + ktakim.upper(),
						soyis.upper() + soyis.title() + ktakim.upper(),

						ad.upper() + ad.title() + takim.title(),
						ad.upper() + soyis.title() + takim.title(),
						soyis.upper() + ad.title() + takim.title(),
						soyis.upper() + soyis.title() + takim.title(),
				
						ad.upper() + ad.title() + ktakim.title(),
						ad.upper() + soyis.title() + ktakim.title(),
						soyis.upper() + ad.title() + ktakim.title(),
						soyis.upper() + soyis.title() + ktakim.title(),

						ad.title() + ad.upper() + takim.title(),
						ad.title() + soyis.upper() + takim.title(),
						soyis.title() + ad.upper() + takim.title(),
						soyis.title() + soyis.upper() + takim.title(),

						ad.title() + ad.upper() + ktakim.title(),
						ad.title() + soyis.upper() + ktakim.title(),
						soyis.title() + ad.upper() + ktakim.title(),
						soyis.title() + soyis.upper() + ktakim.title(),

						ad.title() + ad.title() + takim.upper(),
						ad.title() + soyis.title() + takim.upper(),
						soyis.title() + ad.title() + takim.upper(),
						soyis.title() + soyis.title() + takim.upper(),

						ad.title() + ad.title() + ktakim.upper(),
						ad.title() + soyis.title() + ktakim.upper(),
						soyis.title() + ad.title() + ktakim.upper(),
						soyis.title() + soyis.title() + ktakim.upper(),

						ad + takim + kurulus,
						soyis + takim + kurulus,
						ad + ktakim + kurulus,
						soyis + ktakim + kurulus,

						ad + ad + takim + kurulus,
						ad + soyis + takim + kurulus,
						soyis + ad + takim + kurulus,
						soyis + soyis + takim + kurulus,

						ad + ad + ktakim + kurulus,
						ad + soyis + ktakim + kurulus,
						soyis + ad + ktakim + kurulus,
						soyis + soyis + ktakim + kurulus,

						ad.upper() + takim + kurulus,
						soyis.upper() + takim + kurulus,
						ad.upper() + ktakim + kurulus,
						soyis.upper() + ktakim + kurulus,

						ad.upper() + ad + takim + kurulus,
						ad.upper() + soyis + takim + kurulus,
						soyis.upper() + ad + takim + kurulus,
						soyis.upper() + soyis + takim + kurulus,

						ad.upper() + ad + ktakim + kurulus,
						ad.upper() + soyis + ktakim + kurulus,
						soyis.upper() + ad + ktakim + kurulus,
						soyis.upper() + soyis + ktakim + kurulus,

						ad + takim.upper() + kurulus,
						soyis + takim.upper() + kurulus,
						ad + ktakim.upper() + kurulus,
						soyis + ktakim.upper() + kurulus,

						ad + ad.upper() + takim + kurulus,
						ad + soyis.upper() + takim + kurulus,
						soyis + ad.upper() + takim + kurulus,
						soyis + soyis.upper() + takim + kurulus,

						ad + ad.upper() + ktakim + kurulus,
						ad + soyis.upper() + ktakim + kurulus,
						soyis + ad.upper() + ktakim + kurulus,
						soyis + soyis.upper() + ktakim + kurulus,

						ad + ad + takim.upper() + kurulus,
						ad + soyis + takim.upper() + kurulus,
						soyis + ad + takim.upper() + kurulus,
						soyis + soyis + takim.upper() + kurulus,

						ad + ad + ktakim.upper() + kurulus,
						ad + soyis + ktakim.upper() + kurulus,
						soyis + ad + ktakim.upper() + kurulus,
						soyis + soyis + ktakim.upper() + kurulus,

						ad.upper() + takim.upper() + kurulus,
						soyis.upper() + takim.upper() + kurulus,
						ad.upper() + ktakim.upper() + kurulus,
						soyis.upper() + ktakim.upper() + kurulus,

						ad.upper() + ad.upper() + takim + kurulus,
						ad.upper() + soyis.upper() + takim + kurulus,
						soyis.upper() + ad.upper() + takim + kurulus,
						soyis.upper() + soyis.upper() + takim + kurulus,

						ad.upper() + ad.upper() + ktakim + kurulus,
						ad.upper() + soyis.upper() + ktakim + kurulus,
						soyis.upper() + ad.upper() + ktakim + kurulus,
						soyis.upper() + soyis.upper() + ktakim + kurulus,

						ad.upper() + ad + takim.upper() + kurulus,
						ad.upper() + soyis + takim.upper() + kurulus,
						soyis.upper() + ad + takim.upper() + kurulus,
						soyis.upper() + soyis + takim.upper() + kurulus,

						ad.upper() + ad + ktakim.upper() + kurulus,
						ad.upper() + soyis + ktakim.upper() + kurulus,
						soyis.upper() + ad + ktakim.upper() + kurulus,
						soyis.upper() + soyis + ktakim.upper() + kurulus,

						ad + ad.upper() + takim.upper() + kurulus,
						ad + soyis.upper() + takim.upper() + kurulus,
						soyis + ad.upper() + takim.upper() + kurulus,
						soyis + soyis.upper() + takim.upper() + kurulus,

						ad + ad.upper() + ktakim.upper() + kurulus,
						ad + soyis.upper() + ktakim.upper() + kurulus,
						soyis + ad.upper() + ktakim.upper() + kurulus,
						soyis + soyis.upper() + ktakim.upper() + kurulus,

						ad.upper() + ad.upper() + takim.upper() + kurulus,
						ad.upper() + soyis.upper() + takim.upper() + kurulus,
						soyis.upper() + ad.upper() + takim.upper() + kurulus,
						soyis.upper() + soyis.upper() + takim.upper() + kurulus,

						ad.upper() + ad.upper() + ktakim.upper() + kurulus,
						ad.upper() + soyis.upper() + ktakim.upper() + kurulus,
						soyis.upper() + ad.upper() + ktakim.upper() + kurulus,
						soyis.upper() + soyis.upper() + ktakim.upper() + kurulus,
						
						ad.title() + takim + kurulus,
						soyis.title() + takim + kurulus,
						ad.title() + ktakim + kurulus,
						soyis.title() + ktakim + kurulus,
						
						ad.title() + ad + takim + kurulus,
						ad.title() + soyis + takim + kurulus,
						soyis.title() + ad + takim + kurulus,
						soyis.title() + soyis + takim + kurulus,

						ad.title() + ad + ktakim + kurulus,
						ad.title() + soyis + ktakim + kurulus,
						soyis.title() + ad + ktakim + kurulus,
						soyis.title() + soyis + ktakim + kurulus,

						ad + takim.title() + kurulus,
						soyis + takim.title() + kurulus,
						ad + ktakim.title() + kurulus,
						soyis + ktakim.title() + kurulus,

						ad + ad.title() + takim + kurulus,
						ad + soyis.title() + takim + kurulus,
						soyis + ad.title() + takim + kurulus,
						soyis + soyis.title() + takim + kurulus,
						
						ad + ad.title() + ktakim + kurulus,
						ad + soyis.title() + ktakim + kurulus,
						soyis + ad.title() + ktakim + kurulus,
						soyis + soyis.title() + ktakim + kurulus,
						
						ad + ad + takim.title() + kurulus,
						ad + soyis + takim.title() + kurulus,
						soyis + ad + takim.title() + kurulus,
						soyis + soyis + takim.title() + kurulus,

						ad + ad + ktakim.title() + kurulus,
						ad + soyis + ktakim.title() + kurulus,
						soyis + ad + ktakim.title() + kurulus,
						soyis + soyis + ktakim.title() + kurulus,

						ad.title() + takim.title() + kurulus,
						soyis.title() + takim.title() + kurulus,
						ad.title() + ktakim.title() + kurulus,
						soyis.title() + ktakim.title() + kurulus,

						ad.title() + ad.title() + takim + kurulus,
						ad.title() + soyis.title() + takim + kurulus,
						soyis.title() + ad.title() + takim + kurulus,
						soyis.title() + soyis.title() + takim + kurulus,

						ad.title() + ad.title() + ktakim + kurulus,
						ad.title() + soyis.title() + ktakim + kurulus,
						soyis.title() + ad.title() + ktakim + kurulus,
						soyis.title() + soyis.title() + ktakim + kurulus,
	
						ad.title() + ad + takim.title() + kurulus,
						ad.title() + soyis + takim.title() + kurulus,
						soyis.title() + ad + takim.title() + kurulus,
						soyis.title() + soyis + takim.title() + kurulus,

						ad.title() + ad + ktakim.title() + kurulus,
						ad.title() + soyis + ktakim.title() + kurulus,
						soyis.title() + ad + ktakim.title() + kurulus,
						soyis.title() + soyis + ktakim.title() + kurulus,

						ad + ad.title() + takim.title() + kurulus,
						ad + soyis.title() + takim.title() + kurulus,
						soyis + ad.title() + takim.title() + kurulus,
						soyis + soyis.title() + takim.title() + kurulus,

						ad + ad.title() + ktakim.title() + kurulus,
						ad + soyis.title() + ktakim.title() + kurulus,
						soyis + ad.title() + ktakim.title() + kurulus,
						soyis + soyis.title() + ktakim.title() + kurulus,

						ad.title() + ad.title() + takim.title() + kurulus,
						ad.title() + soyis.title() + takim.title() + kurulus,
						soyis.title() + ad.title() + takim.title() + kurulus,
						soyis.title() + soyis.title() + takim.title() + kurulus,

						ad.title() + ad.title() + ktakim.title() + kurulus,
						ad.title() + soyis.title() + ktakim.title() + kurulus,
						soyis.title() + ad.title() + ktakim.title() + kurulus,
						soyis.title() + soyis.title() + ktakim.title() + kurulus,

						ad.upper() + takim.title() + kurulus,
						soyis.upper() + takim.title() + kurulus,
						ad.upper() + ktakim.title() + kurulus,
						soyis.upper() + ktakim.title() + kurulus,
						
						ad.upper() + ad.title() + takim + kurulus,
						ad.upper() + soyis.title() + takim + kurulus,
						soyis.upper() + ad.title() + takim + kurulus,
						soyis.upper() + soyis.title() + takim + kurulus,
	
						ad.upper() + ad.title() + ktakim + kurulus,
						ad.upper() + soyis.title() + ktakim + kurulus,
						soyis.upper() + ad.title() + ktakim + kurulus,
						soyis.upper() + soyis.title() + ktakim + kurulus,

						ad.upper() + ad + takim.title() + kurulus,
						ad.upper() + soyis + takim.title() + kurulus,
						soyis.upper() + ad + takim.title() + kurulus,
						soyis.upper() + soyis + takim.title() + kurulus,
	
						ad.upper() + ad + ktakim.title() + kurulus,
						ad.upper() + soyis + ktakim.title() + kurulus,
						soyis.upper() + ad + ktakim.title() + kurulus,
						soyis.upper() + soyis + ktakim.title() + kurulus,
						
						
						ad + ad.upper() + takim.title() + kurulus,
						ad + soyis.upper() + takim.title() + kurulus,
						soyis + ad.upper() + takim.title() + kurulus,
						soyis + soyis.upper() + takim.title() + kurulus,
			
						ad + ad.upper() + ktakim.title() + kurulus,
						ad + soyis.upper() + ktakim.title() + kurulus,
						soyis + ad.upper() + ktakim.title() + kurulus,
						soyis + soyis.upper() + ktakim.title() + kurulus,
				
						ad.title() + takim.upper() + kurulus,
						soyis.title() + takim.upper() + kurulus,
						ad.title() + ktakim.upper() + kurulus,
						soyis.title() + ktakim.upper() + kurulus,
					
						ad.title() + ad.upper() + takim + kurulus,
						ad.title() + soyis.upper() + takim + kurulus,
						soyis.title() + ad.upper() + takim + kurulus,
						soyis.title() + soyis.upper() + takim + kurulus,
						
						ad.title() + ad.upper() + ktakim + kurulus,
						ad.title() + soyis.upper() + ktakim + kurulus,
						soyis.title() + ad.upper() + ktakim + kurulus,
						soyis.title() + soyis.upper() + ktakim + kurulus,
				
						ad.title() + ad + takim.upper() + kurulus,
						ad.title() + soyis + takim.upper() + kurulus,
						soyis.title() + ad + takim.upper() + kurulus,
						soyis.title() + soyis + takim.upper() + kurulus,
				
						ad.title() + ad + ktakim.upper() + kurulus,
						ad.title() + soyis + ktakim.upper() + kurulus,
						soyis.title() + ad + ktakim.upper() + kurulus,
						soyis.title() + soyis + ktakim.upper() + kurulus,
					
						ad + ad.title() + takim.upper() + kurulus,
						ad + soyis.title() + takim.upper() + kurulus,
						soyis + ad.title() + takim.upper() + kurulus,
						soyis + soyis.title() + takim.upper() + kurulus,
						
						ad + ad.title() + ktakim.upper() + kurulus,
						ad + soyis.title() + ktakim.upper() + kurulus,
						soyis + ad.title() + ktakim.upper() + kurulus,
						soyis + soyis.title() + ktakim.upper() + kurulus,
						
						ad.upper() + ad.upper() + takim.title() + kurulus,
						ad.upper() + soyis.upper() + takim.title() + kurulus,
						soyis.upper() + ad.upper() + takim.title() + kurulus,
						soyis.upper() + soyis.upper() + takim.title() + kurulus,
						
						ad.upper() + ad.upper() + ktakim.title() + kurulus,
						ad.upper() + soyis.upper() + ktakim.title() + kurulus,
						soyis.upper() + ad.upper() + ktakim.title() + kurulus,
						soyis.upper() + soyis.upper() + ktakim.title() + kurulus,
						
						ad.upper() + ad.title() + takim.upper() + kurulus,
						ad.upper() + soyis.title() + takim.upper() + kurulus,
						soyis.upper() + ad.title() + takim.upper() + kurulus,
						soyis.upper() + soyis.title() + takim.upper() + kurulus,
					
						ad.upper() + ad.title() + ktakim.upper() + kurulus,
						ad.upper() + soyis.title() + ktakim.upper() + kurulus,
						soyis.upper() + ad.title() + ktakim.upper() + kurulus,
						soyis.upper() + soyis.title() + ktakim.upper() + kurulus,
						
						ad.upper() + ad.title() + takim.title() + kurulus,
						ad.upper() + soyis.title() + takim.title() + kurulus,
						soyis.upper() + ad.title() + takim.title() + kurulus,
						soyis.upper() + soyis.title() + takim.title() + kurulus,
						
						ad.upper() + ad.title() + ktakim.title() + kurulus,
						ad.upper() + soyis.title() + ktakim.title() + kurulus,
						soyis.upper() + ad.title() + ktakim.title() + kurulus,
						soyis.upper() + soyis.title() + ktakim.title() + kurulus,
						
						ad.title() + ad.upper() + takim.title() + kurulus,
						ad.title() + soyis.upper() + takim.title() + kurulus,
						soyis.title() + ad.upper() + takim.title() + kurulus,
						soyis.title() + soyis.upper() + takim.title() + kurulus,

						ad.title() + ad.upper() + ktakim.title() + kurulus,
						ad.title() + soyis.upper() + ktakim.title() + kurulus,
						soyis.title() + ad.upper() + ktakim.title() + kurulus,
						soyis.title() + soyis.upper() + ktakim.title() + kurulus,
							
						ad.title() + ad.title() + takim.upper() + kurulus,
						ad.title() + soyis.title() + takim.upper() + kurulus,
						soyis.title() + ad.title() + takim.upper() + kurulus,
						soyis.title() + soyis.title() + takim.upper() + kurulus,
						
						ad.title() + ad.title() + ktakim.upper() + kurulus,
						ad.title() + soyis.title() + ktakim.upper() + kurulus,
						soyis.title() + ad.title() + ktakim.upper() + kurulus,
						soyis.title() + soyis.title() + ktakim.upper() + kurulus,
						
						ad.title() + ad.title() + takim.title() + kurulus,
						ad.title() + soyis.title() + takim.title() + kurulus,
						soyis.title() + ad.title() + takim.title() + kurulus,
						soyis.title() + soyis.title() + takim.title() + kurulus,
						
						ad + takim + dyili,
						soyis + takim + dyili,
						ad + ktakim + dyili,
						soyis + ktakim + dyili,
					
						ad + ad + takim + dyili,
						ad + soyis + takim + dyili,
						soyis + ad + takim + dyili,
						soyis + soyis + takim + dyili,
						
						ad + ad + ktakim + dyili,
						ad + soyis + ktakim + dyili,
						soyis + ad + ktakim + dyili,
						soyis + soyis + ktakim + dyili,
						
						ad.upper() + takim + dyili,
						soyis.upper() + takim + dyili,
						ad.upper() + ktakim + dyili,
						soyis.upper() + ktakim + dyili,
						
						ad.upper() + ad + takim + dyili,
						ad.upper() + soyis + takim + dyili,
						soyis.upper() + ad + takim + dyili,
						soyis.upper() + soyis + takim + dyili,
						
						ad.upper() + ad + ktakim + dyili,
						ad.upper() + soyis + ktakim + dyili,
						soyis.upper() + ad + ktakim + dyili,
						soyis.upper() + soyis + ktakim + dyili,
						
						ad + takim.upper() + dyili,
						soyis + takim.upper() + dyili,
						ad + ktakim.upper() + dyili,
						soyis + ktakim.upper() + dyili,
						
						ad + ad.upper() + takim + dyili,
						ad + soyis.upper() + takim + dyili,
						soyis + ad.upper() + takim + dyili,
						soyis + soyis.upper() + takim + dyili,
						
						ad + ad.upper() + ktakim + dyili,
						ad + soyis.upper() + ktakim + dyili,
						soyis + ad.upper() + ktakim + dyili,
						soyis + soyis.upper() + ktakim + dyili,
						
						ad + ad + takim.upper() + dyili,
						ad + soyis + takim.upper() + dyili,
						soyis + ad + takim.upper() + dyili,
						soyis + soyis + takim.upper() + dyili,
						
						ad + ad + ktakim.upper() + dyili,
						ad + soyis + ktakim.upper() + dyili,
						soyis + ad + ktakim.upper() + dyili,
						soyis + soyis + ktakim.upper() + dyili,
						
						ad.upper() + takim.upper() + dyili,
						soyis.upper() + takim.upper() + dyili,
						ad.upper() + ktakim.upper() + dyili,
						soyis.upper() + ktakim.upper() + dyili,
						
						ad.upper() + ad.upper() + takim + dyili,
						ad.upper() + soyis.upper() + takim + dyili,
						soyis.upper() + ad.upper() + takim + dyili,
						soyis.upper() + soyis.upper() + takim + dyili,
					
						ad.upper() + ad.upper() + ktakim + dyili,
						ad.upper() + soyis.upper() + ktakim + dyili,
						soyis.upper() + ad.upper() + ktakim + dyili,
						soyis.upper() + soyis.upper() + ktakim + dyili,
						
						ad.upper() + ad + takim.upper() + dyili,
						ad.upper() + soyis + takim.upper() + dyili,
						soyis.upper() + ad + takim.upper() + dyili,
						soyis.upper() + soyis + takim.upper() + dyili,
						
						ad.upper() + ad + ktakim.upper() + dyili,
						ad.upper() + soyis + ktakim.upper() + dyili,
						soyis.upper() + ad + ktakim.upper() + dyili,
						soyis.upper() + soyis + ktakim.upper() + dyili,
						
						ad + ad.upper() + takim.upper() + dyili,
						ad + soyis.upper() + takim.upper() + dyili,
						soyis + ad.upper() + takim.upper() + dyili,
						soyis + soyis.upper() + takim.upper() + dyili,
						
						ad + ad.upper() + ktakim.upper() + dyili,
						ad + soyis.upper() + ktakim.upper() + dyili,
						soyis + ad.upper() + ktakim.upper() + dyili,
						soyis + soyis.upper() + ktakim.upper() + dyili,
						
						ad.upper() + ad.upper() + takim.upper() + dyili,
						ad.upper() + soyis.upper() + takim.upper() + dyili,
						soyis.upper() + ad.upper() + takim.upper() + dyili,
						soyis.upper() + soyis.upper() + takim.upper() + dyili,
						
						ad.upper() + ad.upper() + ktakim.upper() + dyili,
						ad.upper() + soyis.upper() + ktakim.upper() + dyili,
						soyis.upper() + ad.upper() + ktakim.upper() + dyili,
						soyis.upper() + soyis.upper() + ktakim.upper() + dyili,
						
						ad.title() + takim + dyili,
						soyis.title() + takim + dyili,
						ad.title() + ktakim + dyili,
						soyis.title() + ktakim + dyili,
						
						ad.title() + ad + takim + dyili,
						ad.title() + soyis + takim + dyili,
						soyis.title() + ad + takim + dyili,
						soyis.title() + soyis + takim + dyili,
						
						ad.title() + ad + ktakim + dyili,
						ad.title() + soyis + ktakim + dyili,
						soyis.title() + ad + ktakim + dyili,
						soyis.title() + soyis + ktakim + dyili,
						
						ad + takim.title() + dyili,
						soyis + takim.title() + dyili,
						ad + ktakim.title() + dyili,
						soyis + ktakim.title() + dyili,
						
						ad + ad.title() + takim + dyili,
						ad + soyis.title() + takim + dyili,
						soyis + ad.title() + takim + dyili,
						soyis + soyis.title() + takim + dyili,
						
						ad + ad.title() + ktakim + dyili,
						ad + soyis.title() + ktakim + dyili,
						soyis + ad.title() + ktakim + dyili,
						soyis + soyis.title() + ktakim + dyili,
						
						ad + ad + takim.title() + dyili,
						ad + soyis + takim.title() + dyili,
						soyis + ad + takim.title() + dyili,
						soyis + soyis + takim.title() + dyili,
						
						ad + ad + ktakim.title() + dyili,
						ad + soyis + ktakim.title() + dyili,
						soyis + ad + ktakim.title() + dyili,
						soyis + soyis + ktakim.title() + dyili,
						
						ad.title() + takim.title() + dyili,
						soyis.title() + takim.title() + dyili,
						ad.title() + ktakim.title() + dyili,
						soyis.title() + ktakim.title() + dyili,
						
						ad.title() + ad.title() + takim + dyili,
						ad.title() + soyis.title() + takim + dyili,
						soyis.title() + ad.title() + takim + dyili,
						soyis.title() + soyis.title() + takim + dyili,
						
						ad.title() + ad.title() + ktakim + dyili,
						ad.title() + soyis.title() + ktakim + dyili,
						soyis.title() + ad.title() + ktakim + dyili,
						soyis.title() + soyis.title() + ktakim + dyili,
						
						ad.title() + ad + takim.title() + dyili,
						ad.title() + soyis + takim.title() + dyili,
						soyis.title() + ad + takim.title() + dyili,
						soyis.title() + soyis + takim.title() + dyili,
						
						ad.title() + ad + ktakim.title() + dyili,
						ad.title() + soyis + ktakim.title() + dyili,
						soyis.title() + ad + ktakim.title() + dyili,
						soyis.title() + soyis + ktakim.title() + dyili,
						
						ad + ad.title() + takim.title() + dyili,
						ad + soyis.title() + takim.title() + dyili,
						soyis + ad.title() + takim.title() + dyili,
						soyis + soyis.title() + takim.title() + dyili,
						
						ad + ad.title() + ktakim.title() + dyili,
						ad + soyis.title() + ktakim.title() + dyili,
						soyis + ad.title() + ktakim.title() + dyili,
						soyis + soyis.title() + ktakim.title() + dyili,
						
						ad.title() + ad.title() + takim.title() + dyili,
						ad.title() + soyis.title() + takim.title() + dyili,
						soyis.title() + ad.title() + takim.title() + dyili,
						soyis.title() + soyis.title() + takim.title() + dyili,
						
						ad.title() + ad.title() + ktakim.title() + dyili,
						ad.title() + soyis.title() + ktakim.title() + dyili,
						soyis.title() + ad.title() + ktakim.title() + dyili,
						soyis.title() + soyis.title() + ktakim.title() + dyili,
						
						ad.upper() + takim.title() + dyili,
						soyis.upper() + takim.title() + dyili,
						ad.upper() + ktakim.title() + dyili,
						soyis.upper() + ktakim.title() + dyili,
					
						ad.upper() + ad.title() + takim + dyili,
						ad.upper() + soyis.title() + takim + dyili,
						soyis.upper() + ad.title() + takim + dyili,
						soyis.upper() + soyis.title() + takim + dyili,
						
						ad.upper() + ad.title() + ktakim + dyili,
						ad.upper() + soyis.title() + ktakim + dyili,
						soyis.upper() + ad.title() + ktakim + dyili,
						soyis.upper() + soyis.title() + ktakim + dyili,
						
						ad.upper() + ad + takim.title() + dyili,
						ad.upper() + soyis + takim.title() + dyili,
						soyis.upper() + ad + takim.title() + dyili,
						soyis.upper() + soyis + takim.title() + dyili,
						
						ad.upper() + ad + ktakim.title() + dyili,
						ad.upper() + soyis + ktakim.title() + dyili,
						soyis.upper() + ad + ktakim.title() + dyili,
						soyis.upper() + soyis + ktakim.title() + dyili,
						
						ad + ad.upper() + takim.title() + dyili,
						ad + soyis.upper() + takim.title() + dyili,
						soyis + ad.upper() + takim.title() + dyili,
						soyis + soyis.upper() + takim.title() + dyili,
						
						ad + ad.upper() + ktakim.title() + dyili,
						ad + soyis.upper() + ktakim.title() + dyili,
						soyis + ad.upper() + ktakim.title() + dyili,
						soyis + soyis.upper() + ktakim.title() + dyili,
						
						ad.title() + takim.upper() + dyili,
						soyis.title() + takim.upper() + dyili,
						ad.title() + ktakim.upper() + dyili,
						soyis.title() + ktakim.upper() + dyili,
						
						ad.title() + ad.upper() + takim + dyili,
						ad.title() + soyis.upper() + takim + dyili,
						soyis.title() + ad.upper() + takim + dyili,
						soyis.title() + soyis.upper() + takim + dyili,
						
						ad.title() + ad.upper() + ktakim + dyili,
						ad.title() + soyis.upper() + ktakim + dyili,
						soyis.title() + ad.upper() + ktakim + dyili,
						soyis.title() + soyis.upper() + ktakim + dyili,
						
						ad.title() + ad + takim.upper() + dyili,
						ad.title() + soyis + takim.upper() + dyili,
						soyis.title() + ad + takim.upper() + dyili,
						soyis.title() + soyis + takim.upper() + dyili,
						
						ad.title() + ad + ktakim.upper() + dyili,
						ad.title() + soyis + ktakim.upper() + dyili,
						soyis.title() + ad + ktakim.upper() + dyili,
						soyis.title() + soyis + ktakim.upper() + dyili,
						
						ad + ad.title() + takim.upper() + dyili,
						ad + soyis.title() + takim.upper() + dyili,
						soyis + ad.title() + takim.upper() + dyili,
						soyis + soyis.title() + takim.upper() + dyili,
						
						ad + ad.title() + ktakim.upper() + dyili,
						ad + soyis.title() + ktakim.upper() + dyili,
						soyis + ad.title() + ktakim.upper() + dyili,
						soyis + soyis.title() + ktakim.upper() + dyili,
						
						ad.upper() + ad.upper() + takim.title() + dyili,
						ad.upper() + soyis.upper() + takim.title() + dyili,
						soyis.upper() + ad.upper() + takim.title() + dyili,
						soyis.upper() + soyis.upper() + takim.title() + dyili,
						
						ad.upper() + ad.upper() + ktakim.title() + dyili,
						ad.upper() + soyis.upper() + ktakim.title() + dyili,
						soyis.upper() + ad.upper() + ktakim.title() + dyili,
						soyis.upper() + soyis.upper() + ktakim.title() + dyili,
						
						ad.upper() + ad.title() + takim.upper() + dyili,
						ad.upper() + soyis.title() + takim.upper() + dyili,
						soyis.upper() + ad.title() + takim.upper() + dyili,
						soyis.upper() + soyis.title() + takim.upper() + dyili,
						
						ad.upper() + ad.title() + ktakim.upper() + dyili,
						ad.upper() + soyis.title() + ktakim.upper() + dyili,
						soyis.upper() + ad.title() + ktakim.upper() + dyili,
						soyis.upper() + soyis.title() + ktakim.upper() + dyili,
						
						ad.upper() + ad.title() + takim.title() + dyili,
						ad.upper() + soyis.title() + takim.title() + dyili,
						soyis.upper() + ad.title() + takim.title() + dyili,
						soyis.upper() + soyis.title() + takim.title() + dyili,
						
						ad.upper() + ad.title() + ktakim.title() + dyili,
						ad.upper() + soyis.title() + ktakim.title() + dyili,
						soyis.upper() + ad.title() + ktakim.title() + dyili,
						soyis.upper() + soyis.title() + ktakim.title() + dyili,
						
						ad.title() + ad.upper() + takim.title() + dyili,
						ad.title() + soyis.upper() + takim.title() + dyili,
						soyis.title() + ad.upper() + takim.title() + dyili,
						soyis.title() + soyis.upper() + takim.title() + dyili,
						
						ad.title() + ad.upper() + ktakim.title() + dyili,
						ad.title() + soyis.upper() + ktakim.title() + dyili,
						soyis.title() + ad.upper() + ktakim.title() + dyili,
						soyis.title() + soyis.upper() + ktakim.title() + dyili,
						
						ad.title() + ad.title() + takim.upper() + dyili,
						ad.title() + soyis.title() + takim.upper() + dyili,
						soyis.title() + ad.title() + takim.upper() + dyili,
						soyis.title() + soyis.title() + takim.upper() + dyili,
						
						ad.title() + ad.title() + ktakim.upper() + dyili,
						ad.title() + soyis.title() + ktakim.upper() + dyili,
						soyis.title() + ad.title() + ktakim.upper() + dyili,
						soyis.title() + soyis.title() + ktakim.upper() + dyili,
						
						ad + takim + pkodu,
						soyis + takim + pkodu,
						ad + ktakim + pkodu,
						soyis + ktakim + pkodu,
					
						ad + ad + takim + pkodu,
						ad + soyis + takim + pkodu,
						soyis + ad + takim + pkodu,
						soyis + soyis + takim + pkodu,
						
						ad + ad + ktakim + pkodu,
						ad + soyis + ktakim + pkodu,
						soyis + ad + ktakim + pkodu,
						soyis + soyis + ktakim + pkodu,
						
						ad.upper() + takim + pkodu,
						soyis.upper() + takim + pkodu,
						ad.upper() + ktakim + pkodu,
						soyis.upper() + ktakim + pkodu,
						
						ad.upper() + ad + takim + pkodu,
						ad.upper() + soyis + takim + pkodu,
						
						soyis.upper() + ad + takim + pkodu,
						soyis.upper() + soyis + takim + pkodu,
						
						ad.upper() + ad + ktakim + pkodu,
						ad.upper() + soyis + ktakim + pkodu,
						soyis.upper() + ad + ktakim + pkodu,
						soyis.upper() + soyis + ktakim + pkodu,
						
						ad + takim.upper() + pkodu,
						soyis + takim.upper() + pkodu,
						ad + ktakim.upper() + pkodu,
						soyis + ktakim.upper() + pkodu,
						
						ad + ad.upper() + takim + pkodu,
						ad + soyis.upper() + takim + pkodu,
						soyis + ad.upper() + takim + pkodu,
						soyis + soyis.upper() + takim + pkodu,
						
						ad + ad.upper() + ktakim + pkodu,
						ad + soyis.upper() + ktakim + pkodu,
						soyis + ad.upper() + ktakim + pkodu,
						soyis + soyis.upper() + ktakim + pkodu,
						
						ad + ad + takim.upper() + pkodu,
						ad + soyis + takim.upper() + pkodu,
						soyis + ad + takim.upper() + pkodu,
						soyis + soyis + takim.upper() + pkodu,
						
						ad + ad + ktakim.upper() + pkodu,
						ad + soyis + ktakim.upper() + pkodu,
						soyis + ad + ktakim.upper() + pkodu,
						soyis + soyis + ktakim.upper() + pkodu,
						
						ad.upper() + takim.upper() + pkodu,
						soyis.upper() + takim.upper() + pkodu,
						ad.upper() + ktakim.upper() + pkodu,
						soyis.upper() + ktakim.upper() + pkodu,
						
						ad.upper() + ad.upper() + takim + pkodu,
						ad.upper() + soyis.upper() + takim + pkodu,
						soyis.upper() + ad.upper() + takim + pkodu,
						soyis.upper() + soyis.upper() + takim + pkodu,
						
						ad.upper() + ad.upper() + ktakim + pkodu,
						ad.upper() + soyis.upper() + ktakim + pkodu,
						soyis.upper() + ad.upper() + ktakim + pkodu,
						soyis.upper() + soyis.upper() + ktakim + pkodu,
						
						ad.upper() + ad + takim.upper() + pkodu,
						ad.upper() + soyis + takim.upper() + pkodu,
						soyis.upper() + ad + takim.upper() + pkodu,
						soyis.upper() + soyis + takim.upper() + pkodu,
						
						ad.upper() + ad + ktakim.upper() + pkodu,
						ad.upper() + soyis + ktakim.upper() + pkodu,
						soyis.upper() + ad + ktakim.upper() + pkodu,
						soyis.upper() + soyis + ktakim.upper() + pkodu,
						
						ad + ad.upper() + takim.upper() + pkodu,
						ad + soyis.upper() + takim.upper() + pkodu,
						soyis + ad.upper() + takim.upper() + pkodu,
						soyis + soyis.upper() + takim.upper() + pkodu,
						
						ad + ad.upper() + ktakim.upper() + pkodu,
						ad + soyis.upper() + ktakim.upper() + pkodu,
						soyis + ad.upper() + ktakim.upper() + pkodu,
						soyis + soyis.upper() + ktakim.upper() + pkodu,
						
						ad.upper() + ad.upper() + takim.upper() + pkodu,
						ad.upper() + soyis.upper() + takim.upper() + pkodu,
						soyis.upper() + ad.upper() + takim.upper() + pkodu,
						soyis.upper() + soyis.upper() + takim.upper() + pkodu,
					
						ad.upper() + ad.upper() + ktakim.upper() + pkodu,
						ad.upper() + soyis.upper() + ktakim.upper() + pkodu,
						soyis.upper() + ad.upper() + ktakim.upper() + pkodu,
						soyis.upper() + soyis.upper() + ktakim.upper() + pkodu,
						
						ad.title() + takim + pkodu,
						soyis.title() + takim + pkodu,
						ad.title() + ktakim + pkodu,
						soyis.title() + ktakim + pkodu,
						
						ad.title() + ad + takim + pkodu,
						ad.title() + soyis + takim + pkodu,
						soyis.title() + ad + takim + pkodu,
						soyis.title() + soyis + takim + pkodu,
						
						ad.title() + ad + ktakim + pkodu,
						ad.title() + soyis + ktakim + pkodu,
						soyis.title() + ad + ktakim + pkodu,
						soyis.title() + soyis + ktakim + pkodu,
						
						ad + takim.title() + pkodu,
						soyis + takim.title() + pkodu,
						ad + ktakim.title() + pkodu,
						soyis + ktakim.title() + pkodu,
						
						ad + ad.title() + takim + pkodu,
						ad + soyis.title() + takim + pkodu,
						soyis + ad.title() + takim + pkodu,
						soyis + soyis.title() + takim + pkodu,
						
						ad + ad.title() + ktakim + pkodu,
						ad + soyis.title() + ktakim + pkodu,
						soyis + ad.title() + ktakim + pkodu,
						soyis + soyis.title() + ktakim + pkodu,
						
						ad + ad + takim.title() + pkodu,
						ad + soyis + takim.title() + pkodu,
						soyis + ad + takim.title() + pkodu,
						soyis + soyis + takim.title() + pkodu,
						
						ad + ad + ktakim.title() + pkodu,
						ad + soyis + ktakim.title() + pkodu,
						soyis + ad + ktakim.title() + pkodu,
						soyis + soyis + ktakim.title() + pkodu,
						
						ad.title() + takim.title() + pkodu,
						soyis.title() + takim.title() + pkodu,
						ad.title() + ktakim.title() + pkodu,
						soyis.title() + ktakim.title() + pkodu,
						
						ad.title() + ad.title() + takim + pkodu,
						ad.title() + soyis.title() + takim + pkodu,
						soyis.title() + ad.title() + takim + pkodu,
						soyis.title() + soyis.title() + takim + pkodu,

						ad.title() + ad.title() + ktakim + pkodu,
						ad.title() + soyis.title() + ktakim + pkodu,
						soyis.title() + ad.title() + ktakim + pkodu,
						soyis.title() + soyis.title() + ktakim + pkodu,
						
						ad.title() + ad + takim.title() + pkodu,
						ad.title() + soyis + takim.title() + pkodu,
						soyis.title() + ad + takim.title() + pkodu,
						soyis.title() + soyis + takim.title() + pkodu,
						
						ad.title() + ad + ktakim.title() + pkodu,
						ad.title() + soyis + ktakim.title() + pkodu,
						soyis.title() + ad + ktakim.title() + pkodu,
						soyis.title() + soyis + ktakim.title() + pkodu,
						
						ad + ad.title() + takim.title() + pkodu,
						ad + soyis.title() + takim.title() + pkodu,
						soyis + ad.title() + takim.title() + pkodu,
						soyis + soyis.title() + takim.title() + pkodu,
						
						ad + ad.title() + ktakim.title() + pkodu,
						ad + soyis.title() + ktakim.title() + pkodu,
						soyis + ad.title() + ktakim.title() + pkodu,
						soyis + soyis.title() + ktakim.title() + pkodu,
						
						ad.title() + ad.title() + takim.title() + pkodu,
						ad.title() + soyis.title() + takim.title() + pkodu,
						soyis.title() + ad.title() + takim.title() + pkodu,
						soyis.title() + soyis.title() + takim.title() + pkodu,
						
						ad.title() + ad.title() + ktakim.title() + pkodu,
						ad.title() + soyis.title() + ktakim.title() + pkodu,
						soyis.title() + ad.title() + ktakim.title() + pkodu,
						soyis.title() + soyis.title() + ktakim.title() + pkodu,
						
						ad.upper() + takim.title() + pkodu,
						soyis.upper() + takim.title() + pkodu,
						ad.upper() + ktakim.title() + pkodu,
						soyis.upper() + ktakim.title() + pkodu,
						
						ad.upper() + ad.title() + takim + pkodu,
						ad.upper() + soyis.title() + takim + pkodu,
						soyis.upper() + ad.title() + takim + pkodu,
						soyis.upper() + soyis.title() + takim + pkodu,
						
						ad.upper() + ad.title() + ktakim + pkodu,
						ad.upper() + soyis.title() + ktakim + pkodu,
						soyis.upper() + ad.title() + ktakim + pkodu,
						soyis.upper() + soyis.title() + ktakim + pkodu,
						
						ad.upper() + ad + takim.title() + pkodu,
						ad.upper() + soyis + takim.title() + pkodu,
						soyis.upper() + ad + takim.title() + pkodu,
						soyis.upper() + soyis + takim.title() + pkodu,
						
						ad.upper() + ad + ktakim.title() + pkodu,
						ad.upper() + soyis + ktakim.title() + pkodu,
						soyis.upper() + ad + ktakim.title() + pkodu,
						soyis.upper() + soyis + ktakim.title() + pkodu,
						
						ad + ad.upper() + takim.title() + pkodu,
						ad + soyis.upper() + takim.title() + pkodu,
						soyis + ad.upper() + takim.title() + pkodu,
						soyis + soyis.upper() + takim.title() + pkodu,
						
						ad + ad.upper() + ktakim.title() + pkodu,
						ad + soyis.upper() + ktakim.title() + pkodu,
						soyis + ad.upper() + ktakim.title() + pkodu,
						soyis + soyis.upper() + ktakim.title() + pkodu,
						
						ad.title() + takim.upper() + pkodu,
						soyis.title() + takim.upper() + pkodu,
						ad.title() + ktakim.upper() + pkodu,
						soyis.title() + ktakim.upper() + pkodu,
						
						ad.title() + ad.upper() + takim + pkodu,
						ad.title() + soyis.upper() + takim + pkodu,
						soyis.title() + ad.upper() + takim + pkodu,
						soyis.title() + soyis.upper() + takim + pkodu,
						
						ad.title() + ad.upper() + ktakim + pkodu,
						ad.title() + soyis.upper() + ktakim + pkodu,
						soyis.title() + ad.upper() + ktakim + pkodu,
						soyis.title() + soyis.upper() + ktakim + pkodu,
						
						ad.title() + ad + takim.upper() + pkodu,
						ad.title() + soyis + takim.upper() + pkodu,
						soyis.title() + ad + takim.upper() + pkodu,
						soyis.title() + soyis + takim.upper() + pkodu,
						
						ad.title() + ad + ktakim.upper() + pkodu,
						ad.title() + soyis + ktakim.upper() + pkodu,
						soyis.title() + ad + ktakim.upper() + pkodu,
						soyis.title() + soyis + ktakim.upper() + pkodu,
						
						ad + ad.title() + takim.upper() + pkodu,
						ad + soyis.title() + takim.upper() + pkodu,
						soyis + ad.title() + takim.upper() + pkodu,
						soyis + soyis.title() + takim.upper() + pkodu,
						
						ad + ad.title() + ktakim.upper() + pkodu,
						ad + soyis.title() + ktakim.upper() + pkodu,
						soyis + ad.title() + ktakim.upper() + pkodu,
						soyis + soyis.title() + ktakim.upper() + pkodu,
						
						ad.upper() + ad.upper() + takim.title() + pkodu,
						ad.upper() + soyis.upper() + takim.title() + pkodu,
						soyis.upper() + ad.upper() + takim.title() + pkodu,
						soyis.upper() + soyis.upper() + takim.title() + pkodu,
						
						ad.upper() + ad.upper() + ktakim.title() + pkodu,
						ad.upper() + soyis.upper() + ktakim.title() + pkodu,
						soyis.upper() + ad.upper() + ktakim.title() + pkodu,
						soyis.upper() + soyis.upper() + ktakim.title() + pkodu,
						
						ad.upper() + ad.title() + takim.upper() + pkodu,
						ad.upper() + soyis.title() + takim.upper() + pkodu,
						soyis.upper() + ad.title() + takim.upper() + pkodu,
						soyis.upper() + soyis.title() + takim.upper() + pkodu,
						
						ad.upper() + ad.title() + ktakim.upper() + pkodu,
						ad.upper() + soyis.title() + ktakim.upper() + pkodu,
						soyis.upper() + ad.title() + ktakim.upper() + pkodu,
						soyis.upper() + soyis.title() + ktakim.upper() + pkodu,
						
						ad.upper() + ad.title() + takim.title() + pkodu,
						ad.upper() + soyis.title() + takim.title() + pkodu,
						soyis.upper() + ad.title() + takim.title() + pkodu,
						soyis.upper() + soyis.title() + takim.title() + pkodu,
						
						ad.upper() + ad.title() + ktakim.title() + pkodu,
						ad.upper() + soyis.title() + ktakim.title() + pkodu,
						soyis.upper() + ad.title() + ktakim.title() + pkodu,
						soyis.upper() + soyis.title() + ktakim.title() + pkodu,
						
						ad.title() + ad.upper() + takim.title() + pkodu,
						ad.title() + soyis.upper() + takim.title() + pkodu,
						soyis.title() + ad.upper() + takim.title() + pkodu,
						soyis.title() + soyis.upper() + takim.title() + pkodu,
						
						ad.title() + ad.upper() + ktakim.title() + pkodu,
						ad.title() + soyis.upper() + ktakim.title() + pkodu,
						soyis.title() + ad.upper() + ktakim.title() + pkodu,
						soyis.title() + soyis.upper() + ktakim.title() + pkodu,
						
						ad.title() + ad.title() + takim.upper() + pkodu,
						ad.title() + soyis.title() + takim.upper() + pkodu,
						soyis.title() + ad.title() + takim.upper() + pkodu,
						soyis.title() + soyis.title() + takim.upper() + pkodu,
						
						ad.title() + ad.title() + ktakim.upper() + pkodu,
						ad.title() + soyis.title() + ktakim.upper() + pkodu,
						soyis.title() + ad.title() + ktakim.upper() + pkodu,
						soyis.title() + soyis.title() + ktakim.upper() + pkodu,
						
						ad + takim + t_pkodu,
						soyis + takim + t_pkodu,
						ad + ktakim + t_pkodu,
						soyis + ktakim + t_pkodu,
						
						ad + ad + takim + t_pkodu,
						ad + soyis + takim + t_pkodu,
						soyis + ad + takim + t_pkodu,
						soyis + soyis + takim + t_pkodu,
						
						ad + ad + ktakim + t_pkodu,
						ad + soyis + ktakim + t_pkodu,
						soyis + ad + ktakim + t_pkodu,
						soyis + soyis + ktakim + t_pkodu,
						
						ad.upper() + takim + t_pkodu,
						soyis.upper() + takim + t_pkodu,
						ad.upper() + ktakim + t_pkodu,
						soyis.upper() + ktakim + t_pkodu,
						
						ad.upper() + ad + takim + t_pkodu,
						ad.upper() + soyis + takim + t_pkodu,
						soyis.upper() + ad + takim + t_pkodu,
						soyis.upper() + soyis + takim + t_pkodu,
						
						ad.upper() + ad + ktakim + t_pkodu,
						ad.upper() + soyis + ktakim + t_pkodu,
						soyis.upper() + ad + ktakim + t_pkodu,
						soyis.upper() + soyis + ktakim + t_pkodu,
						
						ad + takim.upper() + t_pkodu,
						soyis + takim.upper() + t_pkodu,
						ad + ktakim.upper() + t_pkodu,
						soyis + ktakim.upper() + t_pkodu,
						
						ad + ad.upper() + takim + t_pkodu,
						ad + soyis.upper() + takim + t_pkodu,
						soyis + ad.upper() + takim + t_pkodu,
						soyis + soyis.upper() + takim + t_pkodu,
						
						ad + ad.upper() + ktakim + t_pkodu,
						ad + soyis.upper() + ktakim + t_pkodu,
						soyis + ad.upper() + ktakim + t_pkodu,
						soyis + soyis.upper() + ktakim + t_pkodu,
						
						ad + ad + takim.upper() + t_pkodu,
						ad + soyis + takim.upper() + t_pkodu,
						soyis + ad + takim.upper() + t_pkodu,
						soyis + soyis + takim.upper() + t_pkodu,
						
						ad + ad + ktakim.upper() + t_pkodu,
						ad + soyis + ktakim.upper() + t_pkodu,
						soyis + ad + ktakim.upper() + t_pkodu,
						soyis + soyis + ktakim.upper() + t_pkodu,
						
						ad.upper() + takim.upper() + t_pkodu,
						soyis.upper() + takim.upper() + t_pkodu,
						ad.upper() + ktakim.upper() + t_pkodu,
						soyis.upper() + ktakim.upper() + t_pkodu,
						
						ad.upper() + ad.upper() + takim + t_pkodu,
						ad.upper() + soyis.upper() + takim + t_pkodu,
						soyis.upper() + ad.upper() + takim + t_pkodu,
						soyis.upper() + soyis.upper() + takim + t_pkodu,
						
						ad.upper() + ad.upper() + ktakim + t_pkodu,
						ad.upper() + soyis.upper() + ktakim + t_pkodu,
						soyis.upper() + ad.upper() + ktakim + t_pkodu,
						soyis.upper() + soyis.upper() + ktakim + t_pkodu,
						
						ad.upper() + ad + takim.upper() + t_pkodu,
						ad.upper() + soyis + takim.upper() + t_pkodu,
						soyis.upper() + ad + takim.upper() + t_pkodu,
						soyis.upper() + soyis + takim.upper() + t_pkodu,
						
						ad.upper() + ad + ktakim.upper() + t_pkodu,
						ad.upper() + soyis + ktakim.upper() + t_pkodu,
						soyis.upper() + ad + ktakim.upper() + t_pkodu,
						soyis.upper() + soyis + ktakim.upper() + t_pkodu,
						
						ad + ad.upper() + takim.upper() + t_pkodu,
						ad + soyis.upper() + takim.upper() + t_pkodu,
						soyis + ad.upper() + takim.upper() + t_pkodu,
						soyis + soyis.upper() + takim.upper() + t_pkodu,
						
						ad + ad.upper() + ktakim.upper() + t_pkodu,
						ad + soyis.upper() + ktakim.upper() + t_pkodu,
						soyis + ad.upper() + ktakim.upper() + t_pkodu,
						soyis + soyis.upper() + ktakim.upper() + t_pkodu,
						
						ad.upper() + ad.upper() + takim.upper() + t_pkodu,
						ad.upper() + soyis.upper() + takim.upper() + t_pkodu,
						soyis.upper() + ad.upper() + takim.upper() + t_pkodu,
						soyis.upper() + soyis.upper() + takim.upper() + t_pkodu,

						ad.upper() + ad.upper() + ktakim.upper() + t_pkodu,
						ad.upper() + soyis.upper() + ktakim.upper() + t_pkodu,
						soyis.upper() + ad.upper() + ktakim.upper() + t_pkodu,
						soyis.upper() + soyis.upper() + ktakim.upper() + t_pkodu,
						
						ad.title() + takim + t_pkodu,
						soyis.title() + takim + t_pkodu,
						ad.title() + ktakim + t_pkodu,
						soyis.title() + ktakim + t_pkodu,
						
						ad.title() + ad + takim + t_pkodu,
						ad.title() + soyis + takim + t_pkodu,
						soyis.title() + ad + takim + t_pkodu,
						soyis.title() + soyis + takim + t_pkodu,

						ad.title() + ad + ktakim + t_pkodu,
						ad.title() + soyis + ktakim + t_pkodu,
						soyis.title() + ad + ktakim + t_pkodu,
						soyis.title() + soyis + ktakim + t_pkodu,

						ad + takim.title() + t_pkodu,
						soyis + takim.title() + t_pkodu,
						ad + ktakim.title() + t_pkodu,
						soyis + ktakim.title() + t_pkodu,
						
						ad + ad.title() + takim + t_pkodu,
						ad + soyis.title() + takim + t_pkodu,
						soyis + ad.title() + takim + t_pkodu,
						soyis + soyis.title() + takim + t_pkodu,

						ad + ad.title() + ktakim + t_pkodu,
						ad + soyis.title() + ktakim + t_pkodu,
						soyis + ad.title() + ktakim + t_pkodu,
						soyis + soyis.title() + ktakim + t_pkodu,

						ad + ad + takim.title() + t_pkodu,
						ad + soyis + takim.title() + t_pkodu,
						soyis + ad + takim.title() + t_pkodu,
						soyis + soyis + takim.title() + t_pkodu,

						ad + ad + ktakim.title() + t_pkodu,
						ad + soyis + ktakim.title() + t_pkodu,
						soyis + ad + ktakim.title() + t_pkodu,
						soyis + soyis + ktakim.title() + t_pkodu,

						ad.title() + takim.title() + t_pkodu,
						soyis.title() + takim.title() + t_pkodu,
						ad.title() + ktakim.title() + t_pkodu,
						soyis.title() + ktakim.title() + t_pkodu,

						ad.title() + ad.title() + takim + t_pkodu,
						ad.title() + soyis.title() + takim + t_pkodu,
						soyis.title() + ad.title() + takim + t_pkodu,
						soyis.title() + soyis.title() + takim + t_pkodu,

						ad.title() + ad.title() + ktakim + t_pkodu,
						ad.title() + soyis.title() + ktakim + t_pkodu,
						soyis.title() + ad.title() + ktakim + t_pkodu,
						soyis.title() + soyis.title() + ktakim + t_pkodu,

						ad.title() + ad + takim.title() + t_pkodu,
						ad.title() + soyis + takim.title() + t_pkodu,
						soyis.title() + ad + takim.title() + t_pkodu,
						soyis.title() + soyis + takim.title() + t_pkodu,

						ad.title() + ad + ktakim.title() + t_pkodu,
						ad.title() + soyis + ktakim.title() + t_pkodu,
						soyis.title() + ad + ktakim.title() + t_pkodu,
						soyis.title() + soyis + ktakim.title() + t_pkodu,

						ad + ad.title() + takim.title() + t_pkodu,
						ad + soyis.title() + takim.title() + t_pkodu,
						soyis + ad.title() + takim.title() + t_pkodu,
						soyis + soyis.title() + takim.title() + t_pkodu,

						ad + ad.title() + ktakim.title() + t_pkodu,
						ad + soyis.title() + ktakim.title() + t_pkodu,
						soyis + ad.title() + ktakim.title() + t_pkodu,
						soyis + soyis.title() + ktakim.title() + t_pkodu,

						ad.title() + ad.title() + takim.title() + t_pkodu,
						ad.title() + soyis.title() + takim.title() + t_pkodu,
						soyis.title() + ad.title() + takim.title() + t_pkodu,
						soyis.title() + soyis.title() + takim.title() + t_pkodu,

						ad.title() + ad.title() + ktakim.title() + t_pkodu,
						ad.title() + soyis.title() + ktakim.title() + t_pkodu,
						soyis.title() + ad.title() + ktakim.title() + t_pkodu,
						soyis.title() + soyis.title() + ktakim.title() + t_pkodu,

						ad.upper() + takim.title() + t_pkodu,
						soyis.upper() + takim.title() + t_pkodu,
						ad.upper() + ktakim.title() + t_pkodu,
						soyis.upper() + ktakim.title() + t_pkodu,

						ad.upper() + ad.title() + takim + t_pkodu,
						ad.upper() + soyis.title() + takim + t_pkodu,
						soyis.upper() + ad.title() + takim + t_pkodu,
						soyis.upper() + soyis.title() + takim + t_pkodu,

						ad.upper() + ad.title() + ktakim + t_pkodu,
						ad.upper() + soyis.title() + ktakim + t_pkodu,
						soyis.upper() + ad.title() + ktakim + t_pkodu,
						soyis.upper() + soyis.title() + ktakim + t_pkodu,

						ad.upper() + ad + takim.title() + t_pkodu,
						ad.upper() + soyis + takim.title() + t_pkodu,
						soyis.upper() + ad + takim.title() + t_pkodu,
						soyis.upper() + soyis + takim.title() + t_pkodu,

						ad.upper() + ad + ktakim.title() + t_pkodu,
						ad.upper() + soyis + ktakim.title() + t_pkodu,
						soyis.upper() + ad + ktakim.title() + t_pkodu,
						soyis.upper() + soyis + ktakim.title() + t_pkodu,
						
						ad + ad.upper() + takim.title() + t_pkodu,
						ad + soyis.upper() + takim.title() + t_pkodu,
						soyis + ad.upper() + takim.title() + t_pkodu,
						soyis + soyis.upper() + takim.title() + t_pkodu,
	
						ad + ad.upper() + ktakim.title() + t_pkodu,
						ad + soyis.upper() + ktakim.title() + t_pkodu,
						soyis + ad.upper() + ktakim.title() + t_pkodu,
						soyis + soyis.upper() + ktakim.title() + t_pkodu,

						ad.title() + takim.upper() + t_pkodu,
						soyis.title() + takim.upper() + t_pkodu,
						ad.title() + ktakim.upper() + t_pkodu,
						soyis.title() + ktakim.upper() + t_pkodu,

						ad.title() + ad.upper() + takim + t_pkodu,
						ad.title() + soyis.upper() + takim + t_pkodu,
						soyis.title() + ad.upper() + takim + t_pkodu,
						soyis.title() + soyis.upper() + takim + t_pkodu,

						ad.title() + ad.upper() + ktakim + t_pkodu,
						ad.title() + soyis.upper() + ktakim + t_pkodu,
						soyis.title() + ad.upper() + ktakim + t_pkodu,
						soyis.title() + soyis.upper() + ktakim + t_pkodu,

						ad.title() + ad + takim.upper() + t_pkodu,
						ad.title() + soyis + takim.upper() + t_pkodu,
						soyis.title() + ad + takim.upper() + t_pkodu,
						soyis.title() + soyis + takim.upper() + t_pkodu,

						ad.title() + ad + ktakim.upper() + t_pkodu,
						ad.title() + soyis + ktakim.upper() + t_pkodu,
						soyis.title() + ad + ktakim.upper() + t_pkodu,
						soyis.title() + soyis + ktakim.upper() + t_pkodu,

						ad + ad.title() + takim.upper() + t_pkodu,
						ad + soyis.title() + takim.upper() + t_pkodu,
						soyis + ad.title() + takim.upper() + t_pkodu,
						soyis + soyis.title() + takim.upper() + t_pkodu,

						ad + ad.title() + ktakim.upper() + t_pkodu,
						ad + soyis.title() + ktakim.upper() + t_pkodu,
						soyis + ad.title() + ktakim.upper() + t_pkodu,
						soyis + soyis.title() + ktakim.upper() + t_pkodu,

						ad.upper() + ad.upper() + takim.title() + t_pkodu,
						ad.upper() + soyis.upper() + takim.title() + t_pkodu,
						soyis.upper() + ad.upper() + takim.title() + t_pkodu,
						soyis.upper() + soyis.upper() + takim.title() + t_pkodu,

						ad.upper() + ad.upper() + ktakim.title() + t_pkodu,
						ad.upper() + soyis.upper() + ktakim.title() + t_pkodu,
						soyis.upper() + ad.upper() + ktakim.title() + t_pkodu,
						soyis.upper() + soyis.upper() + ktakim.title() + t_pkodu,

						ad.upper() + ad.title() + takim.upper() + t_pkodu,
						ad.upper() + soyis.title() + takim.upper() + t_pkodu,
						soyis.upper() + ad.title() + takim.upper() + t_pkodu,
						soyis.upper() + soyis.title() + takim.upper() + t_pkodu,

						ad.upper() + ad.title() + ktakim.upper() + t_pkodu,
						ad.upper() + soyis.title() + ktakim.upper() + t_pkodu,
						soyis.upper() + ad.title() + ktakim.upper() + t_pkodu,
						soyis.upper() + soyis.title() + ktakim.upper() + t_pkodu,
	
						ad.upper() + ad.title() + takim.title() + t_pkodu,
						ad.upper() + soyis.title() + takim.title() + t_pkodu,
						soyis.upper() + ad.title() + takim.title() + t_pkodu,
						soyis.upper() + soyis.title() + takim.title() + t_pkodu,

						ad.upper() + ad.title() + ktakim.title() + t_pkodu,
						ad.upper() + soyis.title() + ktakim.title() + t_pkodu,
						soyis.upper() + ad.title() + ktakim.title() + t_pkodu,
						soyis.upper() + soyis.title() + ktakim.title() + t_pkodu,

						ad.title() + ad.upper() + takim.title() + t_pkodu,
						ad.title() + soyis.upper() + takim.title() + t_pkodu,
						soyis.title() + ad.upper() + takim.title() + t_pkodu,
						soyis.title() + soyis.upper() + takim.title() + t_pkodu,

						ad.title() + ad.upper() + ktakim.title() + t_pkodu,
						ad.title() + soyis.upper() + ktakim.title() + t_pkodu,
						soyis.title() + ad.upper() + ktakim.title() + t_pkodu,
						soyis.title() + soyis.upper() + ktakim.title() + t_pkodu,

						ad.title() + ad.title() + takim.upper() + t_pkodu,
						ad.title() + soyis.title() + takim.upper() + t_pkodu,
						soyis.title() + ad.title() + takim.upper() + t_pkodu,
						soyis.title() + soyis.title() + takim.upper() + t_pkodu,
	
						ad.title() + ad.title() + ktakim.upper() + t_pkodu,
						ad.title() + soyis.title() + ktakim.upper() + t_pkodu,
						soyis.title() + ad.title() + ktakim.upper() + t_pkodu,
						soyis.title() + soyis.title() + ktakim.upper() + t_pkodu
						
						]
	sessiz_takim_sifreleri = [
	




								]					
if soru2 != '5' :
	for sifre in takim_sifreleri :
		if sifre not in son and len(sifre) >= minimum and len(sifre) <= maksimum :
			son.append(sifre)
			a = sifre + '!'
			if a not in son and len(a) >= minimum and len(a) <= maksimum :
				son.append(a)
			b = sifre + '.'
			if b not in son and len(b) >= minimum and len(b) <= maksimum :
				son.append(b)
		elif sifre not in son and len(sifre) < minimum :
			c = sifre + '!' 
			d = sifre + '.'
			if len(c) >= minimum and len(c) <= maksimum : 
				son.append(c)
				son.append(d)
				random.shuffle(son)
	for sifre in sessiz_takim_sifreleri :
		if sifre not in son and len(sifre) >= minimum and len(sifre) <= maksimum :
			son.append(sifre)
			a = sifre + '!'
			if a not in son and len(a) >= minimum and len(a) <= maksimum :
				son.append(a)
			b = sifre + '.'
			if b not in son and len(b) >= minimum and len(b) <= maksimum :
				son.append(b)
		elif sifre not in son and len(sifre) < minimum :
			c = sifre + '!' 
			d = sifre + '.'
			if len(c) >= minimum and len(c) <= maksimum : 
				son.append(c)
				son.append(d)
				random.shuffle(son)
elif soru2 == '5' :
	pass
soru = input('Hedefin kendisine çok yakıştırdığı ya da \ninsanların ona çok taktığı bir lakap var mı (e - h) : ')
while soru != 'e' and soru != 'E' and soru != 'h' and soru != 'H' :
	print('\nHatalı seçim yaptınız ! ')
	soru = input('\nHedefin kendisine çok yakıştırdığı ya da \ninsanların ona çok taktığı bir lakap var mı (e - h) : ')
if soru == 'e' or soru == 'E' :
	lakap = input('Lütfen hedefin lakabını giriniz : ')
	lakapli_sifreler = [lakap + ad, 									lakap + '_' + ad,
			
			lakap.upper() + ad,											lakap.upper() + '_' + ad,
			lakap.upper() + ad.upper(),									lakap.upper() + '_' + ad.upper(),
			lakap.upper() + ad.title(),									lakap.upper() + '_' + ad.title(),
			lakap.title() + ad,											lakap.title() + '_' + ad,
			lakap.title() + ad.upper(),									lakap.title() + '_' + ad.upper(),
			lakap.title() + ad.title(),									lakap.title() + '_' + ad.title(),
			
			#######################################################################################################

			lakap + pkodu,												lakap + '_' + pkodu,										
			lakap + pkodu + pkodu,   									lakap + '_' + pkodu + pkodu, 
			lakap + pkodu + t_pkodu,									lakap + '_' + pkodu + t_pkodu,
			lakap + t_pkodu,											lakap + '_' + t_pkodu,
			lakap + t_pkodu + pkodu,									lakap + '_' + t_pkodu + pkodu,
			lakap + t_pkodu + t_pkodu,									lakap + '_' + t_pkodu + t_pkodu,

			lakap + ad + pkodu,											lakap + '_' + ad + pkodu, lakap + '_' + ad + '_' + pkodu, lakap + ad + '_' + pkodu,
			lakap + ad + pkodu + pkodu,									lakap + '_' + ad + pkodu + pkodu, lakap + '_' + ad + '_' + pkodu + pkodu, lakap + ad + '_' + pkodu + pkodu,
			lakap + ad + pkodu + t_pkodu,								lakap + '_' + ad + pkodu + t_pkodu, lakap + '_' + ad + '_' + pkodu + t_pkodu, lakap + ad + '_' + pkodu + t_pkodu,
			lakap + ad + t_pkodu,										lakap + '_' + ad + t_pkodu, lakap + '_' + ad + '_' + t_pkodu, lakap + ad + '_' + t_pkodu,
			lakap + ad + t_pkodu + pkodu,								lakap + '_' + ad + t_pkodu + pkodu, lakap + '_' + ad + '_' + t_pkodu + pkodu, lakap + ad + '_' + t_pkodu + pkodu,
			lakap + ad + t_pkodu + t_pkodu,								lakap + '_' + ad + t_pkodu + t_pkodu, lakap + '_' + ad + '_' + t_pkodu + t_pkodu, lakap + ad + '_' + t_pkodu + t_pkodu,
			
			#######################################################################################################################################################

			lakap.upper() + pkodu,										lakap.upper() + '_' + pkodu,										
			lakap.upper() + pkodu + pkodu,   							lakap.upper() + '_' + pkodu + pkodu, 
			lakap.upper() + pkodu + t_pkodu,							lakap.upper() + '_' + pkodu + t_pkodu,
			lakap.upper() + t_pkodu,									lakap.upper() + '_' + t_pkodu,
			lakap.upper() + t_pkodu + pkodu,							lakap.upper() + '_' + t_pkodu + pkodu,
			lakap.upper() + t_pkodu + t_pkodu,							lakap.upper() + '_' + t_pkodu + t_pkodu,
			
			lakap.title() + pkodu,										lakap.title() + '_' + pkodu,										
			lakap.title() + pkodu + pkodu,   							lakap.title() + '_' + pkodu + pkodu, 
			lakap.title() + pkodu + t_pkodu,							lakap.title() + '_' + pkodu + t_pkodu,
			lakap.title() + t_pkodu,									lakap.title() + '_' + t_pkodu,
			lakap.title() + t_pkodu + pkodu,							lakap.title() + '_' + t_pkodu + pkodu,
			lakap.title() + t_pkodu + t_pkodu,							lakap.title() + '_' + t_pkodu + t_pkodu,
			
			lakap.upper() + ad + pkodu,									lakap.upper() + '_' + ad + pkodu, lakap.upper() + '_' + ad + '_' + pkodu, lakap.upper() + ad + '_' + pkodu,
			lakap.upper() + ad.upper() + pkodu,							lakap.upper() + '_' + ad.upper() + pkodu, lakap.upper() + '_' + ad.upper() + '_' + pkodu, lakap.upper() + ad.upper() + '_' + pkodu,
			lakap.upper() + ad.title() + pkodu,							lakap.upper() + '_' + ad.title() + pkodu, lakap.upper() + '_' + ad.title() + '_' + pkodu, lakap.upper() + ad.title() + '_' + pkodu,
			lakap.title() + ad + pkodu,									lakap.title() + '_' + ad + pkodu, lakap.title() + '_' + ad + '_' + pkodu, lakap.title() + ad + '_' + pkodu,
			lakap.title() + ad.upper() + pkodu,							lakap.title() + '_' + ad.upper() + pkodu, lakap.title() + '_' + ad.upper() + '_' + pkodu, lakap.title() + ad.upper() + '_' + pkodu,
			lakap.title() + ad.title() + pkodu,							lakap.title() + '_' + ad.title() + pkodu, lakap.title() + '_' + ad.title() + '_' + pkodu, lakap.title() + ad.title() + '_' + pkodu,
			
			lakap.upper() + ad + pkodu + pkodu,							lakap.upper() + '_' + ad + pkodu + pkodu, lakap.upper() + '_' + ad + '_' + pkodu + pkodu, lakap.upper() + ad + '_' + pkodu + pkodu,
			lakap.upper() + ad.upper() + pkodu + pkodu,					lakap.upper() + '_' + ad.upper() + pkodu + pkodu, lakap.upper() + '_' + ad.upper() + '_' + pkodu + pkodu, lakap.upper() + ad.upper() + '_' + pkodu + pkodu,
			lakap.upper() + ad.title() + pkodu + pkodu,					lakap.upper() + '_' + ad.title() + pkodu + pkodu, lakap.upper() + '_' + ad.title() + '_' + pkodu + pkodu, lakap.upper() + ad.title() + '_' + pkodu + pkodu,
			lakap.title() + ad + pkodu + pkodu,							lakap.title() + '_' + ad + pkodu + pkodu, lakap.title() + '_' + ad + '_' + pkodu + pkodu, lakap.title() + ad + '_' + pkodu + pkodu,
			lakap.title() + ad.upper() + pkodu + pkodu,					lakap.title() + '_' + ad.upper() + pkodu + pkodu, lakap.title() + '_' + ad.upper() + '_' + pkodu + pkodu, lakap.title() + ad.upper() + '_' + pkodu + pkodu,
			lakap.title() + ad.title() + pkodu + pkodu,					lakap.title() + '_' + ad.title() + pkodu + pkodu, lakap.title() + '_' + ad.title() + '_' + pkodu + pkodu, lakap.title() + ad.title() + '_' + pkodu + pkodu,
			
			lakap.upper() + ad + pkodu + t_pkodu,						lakap.upper() + '_' + ad + pkodu + t_pkodu, lakap.upper() + '_' + ad + '_' + pkodu + t_pkodu, lakap.upper() + ad + '_' + pkodu + t_pkodu,
			lakap.upper() + ad.upper() + pkodu + t_pkodu,  				lakap.upper() + '_' + ad.upper() + pkodu + t_pkodu, lakap.upper() + '_' + ad.upper() + '_' + pkodu + t_pkodu, lakap.upper() + ad.upper() + '_' + pkodu + t_pkodu,
			lakap.upper() + ad.title() + pkodu + t_pkodu,				lakap.upper() + '_' + ad.title() + pkodu + t_pkodu, lakap.upper() + '_' + ad.title() + '_' + pkodu + t_pkodu, lakap.upper() + ad.title() + '_' + pkodu + t_pkodu,
			lakap.title() + ad + pkodu + t_pkodu,						lakap.title() + '_' + ad + pkodu + t_pkodu, lakap.title() + '_' + ad + '_' + pkodu + t_pkodu, lakap.title() + ad + '_' + pkodu + t_pkodu,
			lakap.title() + ad.upper() + pkodu + t_pkodu,				lakap.title() + '_' + ad.upper() + pkodu + t_pkodu, lakap.title() + '_' + ad.upper() + '_' + pkodu + t_pkodu, lakap.title() + ad.upper() + '_' + pkodu + t_pkodu,
			lakap.title() + ad.title() + pkodu + t_pkodu,				lakap.title() + '_' + ad.title() + pkodu + t_pkodu, lakap.title() + '_' + ad.title() + '_' + pkodu + t_pkodu, lakap.title() + ad.title() + '_' + pkodu + t_pkodu,
			
			lakap.upper() + ad + t_pkodu,								lakap.upper() + '_' + ad + t_pkodu, lakap.upper() + '_' + ad + '_' + t_pkodu, lakap.upper() + ad + '_' + t_pkodu,
			lakap.upper() + ad.upper() + t_pkodu,						lakap.upper() + '_' + ad.upper() + t_pkodu, lakap.upper() + '_' + ad.upper() + '_' + t_pkodu, lakap.upper() + ad.upper() + '_' + t_pkodu,
			lakap.upper() + ad.title() + t_pkodu,						lakap.upper() + '_' + ad.title() + t_pkodu, lakap.upper() + '_' + ad.title() + '_' + t_pkodu, lakap.upper() + ad.title() + '_' + t_pkodu,
			lakap.title() + ad + t_pkodu,								lakap.title() + '_' + ad + t_pkodu, lakap.title() + '_' + ad + '_' + t_pkodu, lakap.title() + ad + '_' + t_pkodu,
			lakap.title() + ad.upper() + t_pkodu,						lakap.title() + '_' + ad.upper() + t_pkodu, lakap.title() + '_' + ad.upper() + '_' + t_pkodu, lakap.title() + ad.upper() + '_' + t_pkodu,
			lakap.title() + ad.title() + t_pkodu,						lakap.title() + '_' + ad.title() + t_pkodu, lakap.title() + '_' + ad.title() + '_' + t_pkodu, lakap.title() + ad.title() + '_' + t_pkodu,
			
			lakap.upper() + ad + t_pkodu + pkodu,						lakap.upper() + '_' + ad + t_pkodu + pkodu, lakap.upper() + '_' + ad + '_' + t_pkodu + pkodu, lakap.upper() + ad + '_' + t_pkodu + pkodu,
			lakap.upper() + ad.upper() + t_pkodu + pkodu,				lakap.upper() + '_' + ad.upper() + t_pkodu + pkodu, lakap.upper() + '_' + ad.upper() + '_' + t_pkodu + pkodu, lakap.upper() + ad.upper() + '_' + t_pkodu + pkodu,
			lakap.upper() + ad.title() + t_pkodu + pkodu,				lakap.upper() + '_' + ad.title() + t_pkodu + pkodu, lakap.upper() + '_' + ad.title() + '_' + t_pkodu + pkodu, lakap.upper() + ad.title() + '_' + t_pkodu + pkodu,
			lakap.title() + ad + t_pkodu + pkodu,						lakap.title() + '_' + ad + t_pkodu + pkodu, lakap.title() + '_' + ad + '_' + t_pkodu + pkodu, lakap.title() + ad + '_' + t_pkodu + pkodu,
			lakap.title() + ad.upper() + t_pkodu + pkodu,				lakap.title() + '_' + ad.upper() + t_pkodu + pkodu, lakap.title() + '_' + ad.upper() + '_' + t_pkodu + pkodu, lakap.title() + ad.upper() + '_' + t_pkodu + pkodu,
			lakap.title() + ad.title() + t_pkodu + pkodu,				lakap.title() + '_' + ad.title() + t_pkodu + pkodu, lakap.title() + '_' + ad.title() + '_' + t_pkodu + pkodu, lakap.title() + ad.title() + '_' + t_pkodu + pkodu,
			
			lakap.upper() + ad + t_pkodu + t_pkodu,						lakap.upper() + '_' + ad + t_pkodu + t_pkodu, lakap.upper() + '_' + ad + '_' + t_pkodu + t_pkodu, lakap.upper() + ad + '_' + t_pkodu + t_pkodu,
			lakap.upper() + ad.upper() + t_pkodu + t_pkodu,				lakap.upper() + '_' + ad.upper() + t_pkodu + t_pkodu, lakap.upper() + '_' + ad.upper() + '_' + t_pkodu + t_pkodu, lakap.upper() + ad.upper() + '_' + t_pkodu + t_pkodu,
			lakap.upper() + ad.title() + t_pkodu + t_pkodu,				lakap.upper() + '_' + ad.title() + t_pkodu + t_pkodu, lakap.upper() + '_' + ad.title() + '_' + t_pkodu + t_pkodu, lakap.upper() + ad.title() + '_' + t_pkodu + t_pkodu,
			lakap.title() + ad + t_pkodu + t_pkodu,						lakap.title() + '_' + ad + t_pkodu + t_pkodu, lakap.title() + '_' + ad + '_' + t_pkodu + t_pkodu, lakap.title() + ad + '_' + t_pkodu + t_pkodu,
			lakap.title() + ad.upper() + t_pkodu + t_pkodu,				lakap.title() + '_' + ad.upper() + t_pkodu + t_pkodu, lakap.title() + '_' + ad.upper() + '_' + t_pkodu + t_pkodu, lakap.title() + ad.upper() + '_' + t_pkodu + t_pkodu,
			lakap.title() + ad.title() + t_pkodu + t_pkodu,				lakap.title() + '_' + ad.title() + t_pkodu + t_pkodu, lakap.title() + '_' + ad.title() + '_' + t_pkodu + t_pkodu, lakap.title() + ad.title() + '_' + t_pkodu + t_pkodu,
			
			#########################################################################################################################################################################################

			lakap + dyili,												lakap + '_' + dyili,										
			lakap + dyili + dyili,   									lakap + '_' + dyili + dyili, 
			lakap + dyili + t_dyili,									lakap + '_' + dyili + t_dyili,
			lakap + t_dyili,											lakap + '_' + t_dyili,
			lakap + t_dyili + dyili,									lakap + '_' + t_dyili + dyili,
			lakap + t_dyili + t_dyili,									lakap + '_' + t_dyili + t_dyili,

			lakap + ad + dyili,											lakap + '_' + ad + dyili, lakap + '_' + ad + '_' + dyili, lakap + ad + '_' + dyili,
			lakap + ad + dyili + dyili,									lakap + '_' + ad + dyili + dyili, lakap + '_' + ad + '_' + dyili + dyili, lakap + ad + '_' + dyili + dyili,
			lakap + ad + dyili + t_dyili,								lakap + '_' + ad + dyili + t_dyili, lakap + '_' + ad + '_' + dyili + t_dyili, lakap + ad + '_' + dyili + t_dyili,
			lakap + ad + t_dyili,										lakap + '_' + ad + t_dyili, lakap + '_' + ad + '_' + t_dyili, lakap + ad + '_' + t_dyili,
			lakap + ad + t_dyili + dyili,								lakap + '_' + ad + t_dyili + dyili, lakap + '_' + ad + '_' + t_dyili + dyili, lakap + ad + '_' + t_dyili + dyili,
			lakap + ad + t_dyili + t_dyili,								lakap + '_' + ad + t_dyili + t_dyili, lakap + '_' + ad + '_' + t_dyili + t_dyili, lakap + ad + '_' + t_dyili + t_dyili, 
			lakap + daygun,												lakap + '_' + daygun,
			lakap + daygun + daygun,									lakap + '_' + daygun + daygun,
			lakap + daygun + t_daygun,									lakap + '_' + daygun + t_daygun,
			lakap + t_daygun,											lakap + '_' + t_daygun,
			lakap + t_daygun + daygun,									lakap + '_' + t_daygun + daygun,
			lakap + t_daygun + t_daygun,								lakap + '_' + t_daygun + t_daygun,
			lakap + ad + daygun,										lakap + '_' + ad + daygun, lakap + '_' + ad + '_' + daygun, lakap + ad + '_' + daygun,
			lakap + ad + t_daygun,										lakap + '_' + ad + t_daygun, lakap + '_' + ad + '_' + t_daygun, lakap + ad + '_' + t_daygun,
			lakap + dtarihi,											lakap + '_' + dtarihi,
			lakap + t_dtarihi,											lakap + '_' + t_dtarihi,
			lakap + ad + dtarihi,										lakap + '_' + ad + dtarihi, lakap + '_' + ad + '_' + dtarihi, lakap + ad + '_' + dtarihi,
			lakap + ad + t_dtarihi,										lakap + '_' + ad + t_dtarihi, lakap + '_' + ad + '_' + t_dtarihi, lakap + ad + '_' + t_dtarihi,
			
			#######################################################################################################################################################

			lakap.upper() + dyili,										lakap.upper() + '_' + dyili,										
			lakap.upper() + dyili + dyili,   							lakap.upper() + '_' + dyili + dyili, 
			lakap.upper() + dyili + t_dyili,							lakap.upper() + '_' + dyili + t_dyili,
			lakap.upper() + t_dyili,									lakap.upper() + '_' + t_dyili,
			lakap.upper() + t_dyili + dyili,							lakap.upper() + '_' + t_dyili + dyili,
			lakap.upper() + t_dyili + t_dyili,							lakap.upper() + '_' + t_dyili + t_dyili,

			lakap.title() + dyili,										lakap.title() + '_' + dyili,										
			lakap.title() + dyili + dyili,   							lakap.title() + '_' + dyili + dyili, 
			lakap.title() + dyili + t_dyili,							lakap.title() + '_' + dyili + t_dyili,
			lakap.title() + t_dyili,									lakap.title() + '_' + t_dyili,
			lakap.title() + t_dyili + dyili,							lakap.title() + '_' + t_dyili + dyili,
			lakap.title() + t_dyili + t_dyili,							lakap.title() + '_' + t_dyili + t_dyili,

			lakap.upper() + ad + dyili,									lakap.upper() + '_' + ad + dyili, lakap.upper() + '_' + ad + '_' + dyili, lakap.upper() + ad + '_' + dyili,
			lakap.upper() + ad.upper() + dyili,							lakap.upper() + '_' + ad.upper() + dyili, lakap.upper() + '_' + ad.upper() + '_' + dyili, lakap.upper() + ad.upper() + '_' + dyili,
			lakap.upper() + ad.title() + dyili,							lakap.upper() + '_' + ad.title() + dyili, lakap.upper() + '_' + ad.title() + '_' + dyili, lakap.upper() + ad.title() + '_' + dyili,
			lakap.title() + ad + dyili,									lakap.title() + '_' + ad + dyili, lakap.title() + '_' + ad + '_' + dyili, lakap.title() + ad + '_' + dyili,
			lakap.title() + ad.upper() + dyili,							lakap.title() + '_' + ad.upper() + dyili, lakap.title() + '_' + ad.upper() + '_' + dyili, lakap.title() + ad.upper() + '_' + dyili,
			lakap.title() + ad.title() + dyili,							lakap.title() + '_' + ad.title() + dyili, lakap.title() + '_' + ad.title() + '_' + dyili, lakap.title() + ad.title() + '_' + dyili,
			
			lakap.upper() + ad + dyili + dyili,							lakap.upper() + '_' + ad + dyili + dyili, lakap.upper() + '_' + ad + '_' + dyili + dyili, lakap.upper() + ad + '_' + dyili + dyili,
			lakap.upper() + ad.upper() + dyili + dyili,					lakap.upper() + '_' + ad.upper() + dyili + dyili, lakap.upper() + '_' + ad.upper() + '_' + dyili + dyili, lakap.upper() + ad.upper() + '_' + dyili + dyili,
			lakap.upper() + ad.title() + dyili + dyili,					lakap.upper() + '_' + ad.title() + dyili + dyili, lakap.upper() + '_' + ad.title() + '_' + dyili + dyili, lakap.upper() + ad.title() + '_' + dyili + dyili,
			lakap.title() + ad + dyili + dyili,							lakap.title() + '_' + ad + dyili + dyili, lakap.title() + '_' + ad + '_' + dyili + dyili, lakap.title() + ad + '_' + dyili + dyili,
			lakap.title() + ad.upper() + dyili + dyili,					lakap.title() + '_' + ad.upper() + dyili + dyili, lakap.title() + '_' + ad.upper() + '_' + dyili + dyili, lakap.title() + ad.upper() + '_' + dyili + dyili,
			lakap.title() + ad.title() + dyili + dyili,					lakap.title() + '_' + ad.title() + dyili + dyili, lakap.title() + '_' + ad.title() + '_' + dyili + dyili, lakap.title() + ad.title() + '_' + dyili + dyili,
			
			lakap.upper() + ad + dyili + t_dyili,						lakap.upper() + '_' + ad + dyili + t_dyili, lakap.upper() + '_' + ad + '_' + dyili + t_dyili, lakap.upper() + ad + '_' + dyili + t_dyili,
			lakap.upper() + ad.upper() + dyili + t_dyili,  				lakap.upper() + '_' + ad.upper() + dyili + t_dyili, lakap.upper() + '_' + ad.upper() + '_' + dyili + t_dyili, lakap.upper() + ad.upper() + '_' + dyili + t_dyili,
			lakap.upper() + ad.title() + dyili + t_dyili,				lakap.upper() + '_' + ad.title() + dyili + t_dyili, lakap.upper() + '_' + ad.title() + '_' + dyili + t_dyili, lakap.upper() + ad.title() + '_' + dyili + t_dyili,
			lakap.title() + ad + dyili + t_dyili,						lakap.title() + '_' + ad + dyili + t_dyili, lakap.title() + '_' + ad + '_' + dyili + t_dyili, lakap.title() + ad + '_' + dyili + t_dyili,
			lakap.title() + ad.upper() + dyili + t_dyili,				lakap.title() + '_' + ad.upper() + dyili + t_dyili, lakap.title() + '_' + ad.upper() + '_' + dyili + t_dyili, lakap.title() + ad.upper() + '_' + dyili + t_dyili,
			lakap.title() + ad.title() + dyili + t_dyili,				lakap.title() + '_' + ad.title() + dyili + t_dyili, lakap.title() + '_' + ad.title() + '_' + dyili + t_dyili, lakap.title() + ad.title() + '_' + dyili + t_dyili,
			
			lakap.upper() + ad + t_dyili,								lakap.upper() + '_' + ad + t_dyili, lakap.upper() + '_' + ad + '_' + t_dyili, lakap.upper() + ad + '_' + t_dyili,
			lakap.upper() + ad.upper() + t_dyili,						lakap.upper() + '_' + ad.upper() + t_dyili, lakap.upper() + '_' + ad.upper() + '_' + t_dyili, lakap.upper() + ad.upper() + '_' + t_dyili,
			lakap.upper() + ad.title() + t_dyili,						lakap.upper() + '_' + ad.title() + t_dyili, lakap.upper() + '_' + ad.title() + '_' + t_dyili, lakap.upper() + ad.title() + '_' + t_dyili,
			lakap.title() + ad + t_dyili,								lakap.title() + '_' + ad + t_dyili, lakap.title() + '_' + ad + '_' + t_dyili, lakap.title() + ad + '_' + t_dyili,
			lakap.title() + ad.upper() + t_dyili,						lakap.title() + '_' + ad.upper() + t_dyili, lakap.title() + '_' + ad.upper() + '_' + t_dyili, lakap.title() + ad.upper() + '_' + t_dyili,
			lakap.title() + ad.title() + t_dyili,						lakap.title() + '_' + ad.title() + t_dyili, lakap.title() + '_' + ad.title() + '_' + t_dyili, lakap.title() + ad.title() + '_' + t_dyili,
			
			lakap.upper() + ad + t_dyili + dyili,						lakap.upper() + '_' + ad + t_dyili + dyili, lakap.upper() + '_' + ad + '_' + t_dyili + dyili, lakap.upper() + ad + '_' + t_dyili + dyili,
			lakap.upper() + ad.upper() + t_dyili + dyili,				lakap.upper() + '_' + ad.upper() + t_dyili + dyili, lakap.upper() + '_' + ad.upper() + '_' + t_dyili + dyili, lakap.upper() + ad.upper() + '_' + t_dyili + dyili,
			lakap.upper() + ad.title() + t_dyili + dyili,				lakap.upper() + '_' + ad.title() + t_dyili + dyili, lakap.upper() + '_' + ad.title() + '_' + t_dyili + dyili, lakap.upper() + ad.title() + '_' + t_dyili + dyili,
			lakap.title() + ad + t_dyili + dyili,						lakap.title() + '_' + ad + t_dyili + dyili, lakap.title() + '_' + ad + '_' + t_dyili + dyili, lakap.title() + ad + '_' + t_dyili + dyili,
			lakap.title() + ad.upper() + t_dyili + dyili,				lakap.title() + '_' + ad.upper() + t_dyili + dyili, lakap.title() + '_' + ad.upper() + '_' + t_dyili + dyili, lakap.title() + ad.upper() + '_' + t_dyili + dyili,
			lakap.title() + ad.title() + t_dyili + dyili,				lakap.title() + '_' + ad.title() + t_dyili + dyili, lakap.title() + '_' + ad.title() + '_' + t_dyili + dyili, lakap.title() + ad.title() + '_' + t_dyili + dyili,
			
			lakap.upper() + ad + t_dyili + t_dyili,						lakap.upper() + '_' + ad + t_dyili + t_dyili, lakap.upper() + '_' + ad + '_' + t_dyili + t_dyili, lakap.upper() + ad + '_' + t_dyili + t_dyili,
			lakap.upper() + ad.upper() + t_dyili + t_dyili,				lakap.upper() + '_' + ad.upper() + t_dyili + t_dyili, lakap.upper() + '_' + ad.upper() + '_' + t_dyili + t_dyili, lakap.upper() + ad.upper() + '_' + t_dyili + t_dyili,
			lakap.upper() + ad.title() + t_dyili + t_dyili,				lakap.upper() + '_' + ad.title() + t_dyili + t_dyili, lakap.upper() + '_' + ad.title() + '_' + t_dyili + t_dyili, lakap.upper() + ad.title() + '_' + t_dyili + t_dyili,
			lakap.title() + ad + t_dyili + t_dyili,						lakap.title() + '_' + ad + t_dyili + t_dyili, lakap.title() + '_' + ad + '_' + t_dyili + t_dyili, t_dyili, lakap.title() + ad + '_' + t_dyili + t_dyili,
			lakap.title() + ad.upper() + t_dyili + t_dyili,				lakap.title() + '_' + ad.upper() + t_dyili + t_dyili, lakap.title() + '_' + ad.upper() + '_' + t_dyili + t_dyili, lakap.title() + ad.upper() + '_' + t_dyili + t_dyili,
			lakap.title() + ad.title() + t_dyili + t_dyili,				lakap.title() + '_' + ad.title() + t_dyili + t_dyili, lakap.title() + '_' + ad.title() + '_' + t_dyili + t_dyili, lakap.title() + ad.title() + '_' + t_dyili + t_dyili,
			
			lakap.upper() + daygun,										lakap.upper() + '_' + daygun,
			lakap.title() + daygun,										lakap.title() + '_' + daygun,
			
			lakap.upper() + daygun + daygun,							lakap.upper() + '_' + daygun + daygun,
			lakap.title() + daygun + daygun,							lakap.title() + '_' + daygun + daygun,
			
			lakap.upper() + daygun + t_daygun,							lakap.upper() + '_' + daygun + t_daygun,
			lakap.title() + daygun + t_daygun,							lakap.title() + '_' + daygun + t_daygun,
			
			lakap.upper() + t_daygun,									lakap.upper() + '_' + t_daygun,
			lakap.title() + t_daygun,									lakap.title() + '_' + t_daygun,
			
			lakap.upper() + t_daygun + daygun,							lakap.upper() + '_' + t_daygun + daygun,
			lakap.title() + t_daygun + daygun,							lakap.title() + '_' + t_daygun + daygun,
			
			lakap.upper() + t_daygun + t_daygun,						lakap.upper() + '_' + t_daygun + t_daygun,
			lakap.title() + t_daygun + t_daygun,						lakap.title() + '_' + t_daygun + t_daygun,
			
			lakap.upper() + ad + daygun,								lakap.upper() + '_' + ad + daygun, lakap.upper() + '_' + ad + '_' + daygun, lakap.upper() + ad + '_' + daygun,
			lakap.upper() + ad.upper() + daygun,						lakap.upper() + '_' + ad.upper() + daygun, lakap.upper() + '_' + ad.upper() + '_' + daygun, lakap.upper() + ad.upper() + '_' + daygun,
			lakap.upper() + ad.title() + daygun,						lakap.upper() + '_' + ad.title() + daygun, lakap.upper() + '_' + ad.title() + '_' + daygun, lakap.upper() + ad.title() + '_' + daygun,
			lakap.title() + ad + daygun,								lakap.title() + '_' + ad + daygun, lakap.title() + '_' + ad + '_' + daygun, lakap.title() + ad + '_' + daygun,
			lakap.title() + ad.upper() + daygun,						lakap.title() + '_' + ad.upper() + daygun, lakap.title() + '_' + ad.upper() + '_' + daygun, lakap.title() + ad.upper() + '_' + daygun,
			lakap.title() + ad.title() + daygun,						lakap.title() + '_' + ad.title() + daygun, lakap.title() + '_' + ad.title() + '_' + daygun, lakap.title() + ad.title() + '_' + daygun,
			
			lakap.upper() + ad + daygun + daygun,						lakap.upper() + '_' + ad + daygun + daygun, lakap.upper() + '_' + ad + '_' + daygun + daygun, lakap.upper() + ad + '_' + daygun + daygun,
			lakap.upper() + ad.upper() + daygun + daygun,				lakap.upper() + '_' + ad.upper() + daygun + daygun, lakap.upper() + '_' + ad.upper() + '_' + daygun + daygun, lakap.upper() + ad.upper() + '_' + daygun + daygun,
			lakap.upper() + ad.title() + daygun + daygun,				lakap.upper() + '_' + ad.title() + daygun + daygun, lakap.upper() + '_' + ad.title() + '_' + daygun + daygun, lakap.upper() + ad.title() + '_' + daygun + daygun,
			lakap.title() + ad + daygun + daygun,						lakap.title() + '_' + ad + daygun + daygun, lakap.title() + '_' + ad + '_' + daygun + daygun, lakap.title() + ad + '_' + daygun + daygun,
			lakap.title() + ad.upper() + daygun + daygun,				lakap.title() + '_' + ad.upper() + daygun + daygun, lakap.title() + '_' + ad.upper() + '_' + daygun + daygun, lakap.title() + ad.upper() + '_' + daygun + daygun,
			lakap.title() + ad.title() + daygun + daygun,				lakap.title() + '_' + ad.title() + daygun + daygun, lakap.title() + '_' + ad.title() + '_' + daygun + daygun, lakap.title() + ad.title() + '_' + daygun + daygun,
				
			lakap.upper() + ad + daygun + t_daygun,						lakap.upper() + '_' + ad + daygun + t_daygun, lakap.upper() + '_' + ad + '_' + daygun + t_daygun, lakap.upper() + ad + '_' + daygun + t_daygun,
			lakap.upper() + ad.upper() + daygun + t_daygun,				lakap.upper() + '_' + ad.upper() + daygun + t_daygun, lakap.upper() + '_' + ad.upper() + '_' + daygun + t_daygun, lakap.upper() + ad.upper() + '_' + daygun + t_daygun,
			lakap.upper() + ad.title() + daygun + t_daygun,				lakap.upper() + '_' + ad.title() + daygun + t_daygun, lakap.upper() + '_' + ad.title() + '_' + daygun + t_daygun, lakap.upper() + ad.title() + '_' + daygun + t_daygun,
			lakap.title() + ad + daygun + t_daygun,						lakap.title() + '_' + ad + daygun + t_daygun, lakap.title() + '_' + ad + '_' + daygun + t_daygun, lakap.title() + ad + '_' + daygun + t_daygun,
			lakap.title() + ad.upper() + daygun + t_daygun,				lakap.title() + '_' + ad.upper() + daygun + t_daygun, lakap.title() + '_' + ad.upper() + '_' + daygun + t_daygun, lakap.title() + ad.upper() + '_' + daygun + t_daygun,
			lakap.title() + ad.title() + daygun + t_daygun,				lakap.title() + '_' + ad.title() + daygun + t_daygun, lakap.title() + '_' + ad.title() + '_' + daygun + t_daygun, lakap.title() + ad.title() + '_' + daygun + t_daygun,
			
			lakap.upper() + ad + t_daygun,								lakap.upper() + '_' + ad + t_daygun, lakap.upper() + '_' + ad + '_' + t_daygun, lakap.upper() + ad + '_' + t_daygun,
			lakap.upper() + ad.upper() + t_daygun,						lakap.upper() + '_' + ad.upper() + t_daygun, lakap.upper() + '_' + ad.upper() + '_' + t_daygun, lakap.upper() + ad.upper() + '_' + t_daygun,
			lakap.upper() + ad.title() + t_daygun,						lakap.upper() + '_' + ad.title() + t_daygun, lakap.upper() + '_' + ad.title() + '_' + t_daygun, lakap.upper() + ad.title() + '_' + t_daygun,
			lakap.title() + ad + t_daygun,								lakap.title() + '_' + ad + daygun, lakap.title() + '_' + ad + '_' + t_daygun, lakap.title() + ad + '_' + t_daygun,
			lakap.title() + ad.upper() + t_daygun,						lakap.title() + '_' + ad.upper() + daygun, lakap.title() + '_' + ad.upper() + '_' + t_daygun, lakap.title() + ad.upper() + '_' + t_daygun,
			lakap.title() + ad.title() + t_daygun,						lakap.title() + '_' + ad.title() + daygun, lakap.title() + '_' + ad.title() + '_' + t_daygun, lakap.title() + ad.title() + '_' + t_daygun,
			
			lakap.upper() + ad + t_daygun + daygun,						lakap.upper() + '_' + ad + t_daygun + daygun, lakap.upper() + '_' + ad + '_' + t_daygun + daygun, lakap.upper() + ad + '_' + t_daygun + daygun,
			lakap.upper() + ad.upper() + t_daygun + daygun,				lakap.upper() + '_' + ad.upper() + t_daygun + daygun, lakap.upper() + '_' + ad.upper() + '_' + t_daygun + daygun, lakap.upper() + ad.upper() + '_' + t_daygun + daygun,
			lakap.upper() + ad.title() + t_daygun + daygun,				lakap.upper() + '_' + ad.title() + t_daygun + daygun, lakap.upper() + '_' + ad.title() + '_' + t_daygun + daygun, lakap.upper() + ad.title() + '_' + t_daygun + daygun,
			lakap.title() + ad + t_daygun + daygun,						lakap.title() + '_' + ad + t_daygun + daygun, lakap.title() + '_' + ad + '_' + t_daygun + daygun, lakap.title() + ad + '_' + t_daygun + daygun,
			lakap.title() + ad.upper() + t_daygun + daygun,				lakap.title() + '_' + ad.upper() + t_daygun + daygun, lakap.title() + '_' + ad.upper() + '_' + t_daygun + daygun, lakap.title() + ad.upper() + '_' + t_daygun + daygun,
			lakap.title() + ad.title() + t_daygun + daygun,				lakap.title() + '_' + ad.title() + t_daygun + daygun, lakap.title() + '_' + ad.title() + '_' + t_daygun + daygun, lakap.title() + ad.title() + '_' + t_daygun + daygun,
			
			lakap.upper() + ad + t_daygun + t_daygun,					lakap.upper() + '_' + ad + t_daygun + t_daygun, lakap.upper() + '_' + ad + '_' + t_daygun + t_daygun, lakap.upper() + ad + '_' + t_daygun + t_daygun,
			lakap.upper() + ad.upper() + t_daygun + t_daygun,			lakap.upper() + '_' + ad.upper() + t_daygun + t_daygun, lakap.upper() + '_' + ad.upper() + '_' + t_daygun + t_daygun, lakap.upper() + ad.upper() + '_' + t_daygun + t_daygun,
			lakap.upper() + ad.title() + t_daygun + t_daygun,			lakap.upper() + '_' + ad.title() + t_daygun + t_daygun, lakap.upper() + '_' + ad.title() + '_' + t_daygun + t_daygun, lakap.upper() + ad.title() + '_' + t_daygun + t_daygun,
			lakap.title() + ad + t_daygun + t_daygun,					lakap.title() + '_' + ad + t_daygun + daygun, lakap.title() + '_' + ad + '_' + t_daygun + t_daygun, lakap.title() + ad + '_' + t_daygun + t_daygun,
			lakap.title() + ad.upper() + t_daygun + t_daygun,			lakap.title() + '_' + ad.upper() + t_daygun + daygun, lakap.title() + '_' + ad.upper() + '_' + t_daygun + t_daygun, lakap.title() + ad.upper() + '_' + t_daygun + t_daygun,
			lakap.title() + ad.title() + t_daygun + t_daygun,			lakap.title() + '_' + ad.title() + t_daygun + daygun, lakap.title() + '_' + ad.title() + '_' + t_daygun + t_daygun, lakap.title() + ad.title() + '_' + t_daygun + t_daygun,
			
			lakap.upper() + dtarihi,									lakap.upper() + '_' + dtarihi,
			lakap.title() + dtarihi,									lakap.title() + '_' + dtarihi,
			
			lakap.upper() + t_dtarihi,									lakap.upper() + '_' + t_dtarihi,
			lakap.title() + t_dtarihi,									lakap.title() + '_' + t_dtarihi,
			
			lakap.upper() + ad + dtarihi,								lakap.upper() + '_' + ad + dtarihi, lakap.upper() + '_' + ad + '_' + dtarihi, lakap.upper() + ad + '_' + dtarihi,
			lakap.upper() + ad.upper() + dtarihi,						lakap.upper() + '_' + ad.upper() + dtarihi, lakap.upper() + '_' + ad.upper() + '_' + dtarihi, lakap.upper() + ad.upper() + '_' + dtarihi,
			lakap.upper() + ad.title() + dtarihi,						lakap.upper() + '_' + ad.title() + dtarihi, lakap.upper() + '_' + ad.title() + '_' + dtarihi, lakap.upper() + ad.title() + '_' + dtarihi,
			lakap.title() + ad + dtarihi,								lakap.title() + '_' + ad + dtarihi, lakap.title() + '_' + ad + '_' + dtarihi, lakap.title() + ad + '_' + dtarihi,
			lakap.title() + ad.upper() + dtarihi,						lakap.title() + '_' + ad.upper() + dtarihi, lakap.title() + '_' + ad.upper() + '_' + dtarihi, lakap.title() + ad.upper() + '_' + dtarihi,
			lakap.title() + ad.title() + dtarihi,						lakap.title() + '_' + ad.title() + dtarihi, lakap.title() + '_' + ad.title() + '_' + dtarihi, lakap.title() + ad.title() + '_' + dtarihi,
			
			lakap.upper() + ad + t_dtarihi,								lakap.upper() + '_' + ad + t_dtarihi, lakap.upper() + '_' + ad + '_' + t_dtarihi, lakap.upper() + ad + '_' + t_dtarihi,
			lakap.upper() + ad.upper() + t_dtarihi,						lakap.upper() + '_' + ad.upper() + t_dtarihi, lakap.upper() + '_' + ad.upper() + '_' + t_dtarihi, lakap.upper() + ad.upper() + '_' + t_dtarihi,
			lakap.upper() + ad.title() + t_dtarihi,						lakap.upper() + '_' + ad.title() + t_dtarihi, lakap.upper() + '_' + ad.title() + '_' + t_dtarihi, lakap.upper() + ad.title() + '_' + t_dtarihi,
			lakap.title() + ad + t_dtarihi,								lakap.title() + '_' + ad + dtarihi, lakap.title() + '_' + ad + '_' + t_dtarihi, lakap.title() + ad + '_' + t_dtarihi,
			lakap.title() + ad.upper() + t_dtarihi,						lakap.title() + '_' + ad.upper() + dtarihi, lakap.title() + '_' + ad.upper() + '_' + t_dtarihi, lakap.title() + ad.upper() + '_' + t_dtarihi,
			lakap.title() + ad.title() + t_dtarihi,						lakap.title() + '_' + ad.title() + dtarihi, lakap.title() + '_' + ad.title() + '_' + t_dtarihi, lakap.title() + ad.title() + '_' + t_dtarihi,
			
			lakap + soyis,												lakap + '_' + soyis,
			soyis + lakap,												soyis + '_' + lakap,
			
			lakap.upper() + soyis,										lakap.upper() + '_' + soyis,
			lakap.upper() + soyis.upper(),								lakap.upper() + '_' + soyis.upper(),
			lakap.upper() + soyis.title(),								lakap.upper() + '_' + soyis.title(),
			lakap.title() + soyis,										lakap.title() + '_' + soyis,
			lakap.title() + soyis.upper(),								lakap.title() + '_' + soyis.upper(),
			lakap.title() + soyis.title(),								lakap.title() + '_' + soyis.title(),
			
			soyis.upper() + lakap,										soyis.upper() + '_' + lakap,
			soyis.upper() + lakap.upper(),								soyis.upper() + '_' + lakap.upper(),
			soyis.upper() + lakap.title(),								soyis.upper() + '_' + lakap.title(),
			soyis.title() + lakap,										soyis.title() + '_' + lakap,
			soyis.title() + lakap.upper(),								soyis.title() + '_' + lakap.upper(),
			soyis.title() + lakap.title(),								soyis.title() + '_' + lakap.title(),
			
			#######################################################################################################
			
			lakap + soyis + pkodu, 										lakap + '_' + soyis + pkodu, lakap + '_' + soyis + '_' + pkodu, lakap + soyis + '_' + pkodu,
			soyis + lakap + pkodu,										soyis + '_' + lakap + pkodu, soyis + '_' + lakap + '_' + pkodu, soyis + lakap + '_' + pkodu,
			
			lakap + soyis + pkodu + pkodu,								lakap + '_' + soyis + pkodu + pkodu, lakap + '_' + soyis + '_' + pkodu + pkodu, lakap + soyis + '_' + pkodu + pkodu,
			soyis + lakap + pkodu + pkodu,								soyis + '_' + lakap + pkodu + pkodu, soyis + '_' + lakap + '_' + pkodu + pkodu, soyis + lakap + '_' + pkodu + pkodu,
			
			lakap + soyis + pkodu + t_pkodu,							lakap + '_' + soyis + pkodu + t_pkodu, lakap + '_' + soyis + '_' + pkodu + t_pkodu, lakap + soyis + '_' + pkodu + t_pkodu,
			soyis + lakap + pkodu + t_pkodu,							soyis + '_' + lakap + pkodu + t_pkodu, soyis + '_' + lakap + '_' + pkodu + t_pkodu, soyis + lakap + '_' + pkodu + t_pkodu,
			
			lakap + soyis + t_pkodu, 									lakap + '_' + soyis + t_pkodu, lakap + '_' + soyis + '_' + t_pkodu, lakap + soyis + '_' + t_pkodu,
			soyis + lakap + t_pkodu,									soyis + '_' + lakap + t_pkodu, soyis + '_' + lakap + '_' + t_pkodu, soyis + lakap + '_' + t_pkodu,
			
			lakap + soyis + t_pkodu + pkodu,							lakap + '_' + soyis + t_pkodu + pkodu, lakap + '_' + soyis + '_' + t_pkodu + pkodu, lakap + soyis + '_' + t_pkodu + pkodu,
			soyis + lakap + t_pkodu + pkodu,							soyis + '_' + lakap + t_pkodu + pkodu, soyis + '_' + lakap + '_' + t_pkodu + pkodu, soyis + lakap + '_' + t_pkodu + pkodu,
			
			lakap + soyis + t_pkodu + t_pkodu,							lakap + '_' + soyis + t_pkodu + t_pkodu, lakap + '_' + soyis + '_' + t_pkodu + t_pkodu, lakap + soyis + '_' + t_pkodu + t_pkodu,
			soyis + lakap + t_pkodu + t_pkodu,							soyis + '_' + lakap + t_pkodu + t_pkodu, soyis + '_' + lakap + '_' + t_pkodu + t_pkodu, soyis + lakap + '_' + t_pkodu + t_pkodu,
			
			#######################################################################################################################################################
			
			lakap.upper() + soyis + pkodu,								lakap.upper() + '_' + soyis + pkodu, lakap.upper() + '_' + soyis + '_' + pkodu, lakap.upper() + soyis + '_' + pkodu,
			lakap.upper() + soyis.upper() + pkodu,						lakap.upper() + '_' + soyis.upper() + pkodu, lakap.upper() + '_' + soyis.upper() + '_' + pkodu, lakap.upper() + soyis.upper() + '_' + pkodu,
			lakap.upper() + soyis.title() + pkodu,						lakap.upper() + '_' + soyis.title() + pkodu, lakap.upper() + '_' + soyis.title() + '_' + pkodu, lakap.upper() + soyis.title() + '_' + pkodu,
			lakap.title() + soyis + pkodu,								lakap.title() + '_' + soyis + pkodu, lakap.title() + '_' + soyis + '_' + pkodu, lakap.title() + soyis + '_' + pkodu,
			lakap.title() + soyis.upper() + pkodu,						lakap.title() + '_' + soyis.upper() + pkodu, lakap.title() + '_' + soyis.upper() + '_' + pkodu, lakap.title() + soyis.upper() + '_' + pkodu,
			lakap.title() + soyis.title() + pkodu,						lakap.title() + '_' + soyis.title() + pkodu, lakap.title() + '_' + soyis.title() + '_' + pkodu, lakap.title() + soyis.title() + '_' + pkodu,

			lakap.upper() + soyis + pkodu + pkodu,						lakap.upper() + '_' + soyis + pkodu + pkodu, lakap.upper() + '_' + soyis + '_' + pkodu + pkodu, lakap.upper() + soyis + '_' + pkodu + pkodu,
			lakap.upper() + soyis.upper() + pkodu + pkodu,				lakap.upper() + '_' + soyis.upper() + pkodu + pkodu, lakap.upper() + '_' + soyis.upper() + '_' + pkodu + pkodu, lakap.upper() + soyis.upper() + '_' + pkodu + pkodu,
			lakap.upper() + soyis.title() + pkodu + pkodu,				lakap.upper() + '_' + soyis.title() + pkodu + pkodu, lakap.upper() + '_' + soyis.title() + '_' + pkodu + pkodu, lakap.upper() + soyis.title() + '_' + pkodu + pkodu,
			lakap.title() + soyis + pkodu + pkodu,						lakap.title() + '_' + soyis + pkodu + pkodu, lakap.title() + '_' + soyis + '_' + pkodu + pkodu, lakap.title() + soyis + '_' + pkodu + pkodu,
			lakap.title() + soyis.upper() + pkodu + pkodu,				lakap.title() + '_' + soyis.upper() + pkodu + pkodu, lakap.title() + '_' + soyis.upper() + '_' + pkodu + pkodu, lakap.title() + soyis.upper() + '_' + pkodu + pkodu,
			lakap.title() + soyis.title() + pkodu + pkodu,				lakap.title() + '_' + soyis.title() + pkodu + pkodu, lakap.title() + '_' + soyis.title() + '_' + pkodu + pkodu, lakap.title() + soyis.title() + '_' + pkodu + pkodu,
			
			lakap.upper() + soyis + pkodu + t_pkodu,					lakap.upper() + '_' + soyis + pkodu + t_pkodu, lakap.upper() + '_' + soyis + '_' + pkodu + t_pkodu, lakap.upper() + soyis + '_' + pkodu + t_pkodu,
			lakap.upper() + soyis.upper() + pkodu + t_pkodu,			lakap.upper() + '_' + soyis.upper() + pkodu + t_pkodu, lakap.upper() + '_' + soyis.upper() + '_' + pkodu + t_pkodu, lakap.upper() + soyis.upper() + '_' + pkodu + t_pkodu,
			lakap.upper() + soyis.title() + pkodu + t_pkodu,			lakap.upper() + '_' + soyis.title() + pkodu + t_pkodu, lakap.upper() + '_' + soyis.title() + '_' + pkodu + t_pkodu, lakap.upper() + soyis.title() + '_' + pkodu + t_pkodu,
			lakap.title() + soyis + pkodu + t_pkodu,					lakap.title() + '_' + soyis + pkodu + t_pkodu, lakap.title() + '_' + soyis + '_' + pkodu + t_pkodu, lakap.title() + soyis + '_' + pkodu + t_pkodu,
			lakap.title() + soyis.upper() + pkodu + t_pkodu,			lakap.title() + '_' + soyis.upper() + pkodu + t_pkodu, lakap.title() + '_' + soyis.upper() + '_' + pkodu + t_pkodu, lakap.title() + soyis.upper() + '_' + pkodu + t_pkodu,
			lakap.title() + soyis.title() + pkodu + t_pkodu,			lakap.title() + '_' + soyis.title() + pkodu + t_pkodu, lakap.title() + '_' + soyis.title() + '_' + pkodu + t_pkodu, lakap.title() + soyis.title() + '_' + pkodu + t_pkodu,
			
			lakap.upper() + soyis + t_pkodu,							lakap.upper() + '_' + soyis + t_pkodu, lakap.upper() + '_' + soyis + '_' + t_pkodu, lakap.upper() + soyis + '_' + t_pkodu,
			lakap.upper() + soyis.upper() + t_pkodu,					lakap.upper() + '_' + soyis.upper() + t_pkodu, lakap.upper() + '_' + soyis.upper() + '_' + t_pkodu, lakap.upper() + soyis.upper() + '_' + t_pkodu,
			lakap.upper() + soyis.title() + t_pkodu,					lakap.upper() + '_' + soyis.title() + t_pkodu, lakap.upper() + '_' + soyis.title() + '_' + t_pkodu, lakap.upper() + soyis.title() + '_' + t_pkodu,
			lakap.title() + soyis + t_pkodu,							lakap.title() + '_' + soyis + t_pkodu, lakap.title() + '_' + soyis + '_' + t_pkodu, lakap.title() + soyis + '_' + t_pkodu,
			lakap.title() + soyis.upper() + t_pkodu,					lakap.title() + '_' + soyis.upper() + t_pkodu, lakap.title() + '_' + soyis.upper() + '_' + t_pkodu, lakap.title() + soyis.upper() + '_' + t_pkodu,
			lakap.title() + soyis.title() + t_pkodu,					lakap.title() + '_' + soyis.title() + t_pkodu, lakap.title() + '_' + soyis.title() + '_' + t_pkodu, lakap.title() + soyis.title() + '_' + t_pkodu,
			
			lakap.upper() + soyis + t_pkodu + pkodu,					lakap.upper() + '_' + soyis + t_pkodu + pkodu, lakap.upper() + '_' + soyis + '_' + t_pkodu + pkodu, lakap.upper() + soyis + '_' + t_pkodu + pkodu,
			lakap.upper() + soyis.upper() + t_pkodu + pkodu,			lakap.upper() + '_' + soyis.upper() + t_pkodu + pkodu, lakap.upper() + '_' + soyis.upper() + '_' + t_pkodu + pkodu, lakap.upper() + soyis.upper() + '_' + t_pkodu + pkodu,
			lakap.upper() + soyis.title() + t_pkodu + pkodu,			lakap.upper() + '_' + soyis.title() + t_pkodu + pkodu, lakap.upper() + '_' + soyis.title() + '_' + t_pkodu + pkodu, lakap.upper() + soyis.title() + '_' + t_pkodu + pkodu,
			lakap.title() + soyis + t_pkodu + pkodu,					lakap.title() + '_' + soyis + t_pkodu + pkodu, lakap.title() + '_' + soyis + '_' + t_pkodu + pkodu, lakap.title() + soyis + '_' + t_pkodu + pkodu,
			lakap.title() + soyis.upper() + t_pkodu + pkodu,			lakap.title() + '_' + soyis.upper() + t_pkodu + pkodu, lakap.title() + '_' + soyis.upper() + '_' + t_pkodu + pkodu, lakap.title() + soyis.upper() + '_' + t_pkodu + pkodu,
			lakap.title() + soyis.title() + t_pkodu + pkodu,			lakap.title() + '_' + soyis.title() + t_pkodu + pkodu, lakap.title() + '_' + soyis.title() + '_' + t_pkodu + pkodu, lakap.title() + soyis.title() + '_' + t_pkodu + pkodu,
			
			lakap.upper() + soyis + t_pkodu + t_pkodu,					lakap.upper() + '_' + soyis + t_pkodu + t_pkodu, lakap.upper() + '_' + soyis + '_' + t_pkodu + t_pkodu, lakap.upper() + soyis + '_' + t_pkodu + t_pkodu,
			lakap.upper() + soyis.upper() + t_pkodu + t_pkodu,			lakap.upper() + '_' + soyis.upper() + t_pkodu + t_pkodu, lakap.upper() + '_' + soyis.upper() + '_' + t_pkodu + t_pkodu, lakap.upper() + soyis.upper() + '_' + t_pkodu + t_pkodu,
			lakap.upper() + soyis.title() + t_pkodu + t_pkodu,			lakap.upper() + '_' + soyis.title() + t_pkodu + t_pkodu, lakap.upper() + '_' + soyis.title() + '_' + t_pkodu + t_pkodu, lakap.upper() + soyis.title() + '_' + t_pkodu + t_pkodu,
			lakap.title() + soyis + t_pkodu + t_pkodu,					lakap.title() + '_' + soyis + t_pkodu + t_pkodu, lakap.title() + '_' + soyis + '_' + t_pkodu + t_pkodu, lakap.title() + soyis + '_' + t_pkodu + t_pkodu,
			lakap.title() + soyis.upper() + t_pkodu + t_pkodu,			lakap.title() + '_' + soyis.upper() + t_pkodu + t_pkodu, lakap.title() + '_' + soyis.upper() + '_' + t_pkodu + t_pkodu, lakap.title() + soyis.upper() + '_' + t_pkodu + t_pkodu,
			lakap.title() + soyis.title() + t_pkodu + t_pkodu,			lakap.title() + '_' + soyis.title() + t_pkodu + t_pkodu, lakap.title() + '_' + soyis.title() + '_' + t_pkodu + t_pkodu, lakap.title() + soyis.title() + '_' + t_pkodu + t_pkodu,
			
			soyis.upper() + lakap + pkodu,								soyis.upper() + '_' + lakap + pkodu, soyis.upper() + '_' + lakap + '_' + pkodu, soyis.upper() + lakap + '_' + pkodu,
			soyis.upper() + lakap.upper() + pkodu,						soyis.upper() + '_' + lakap.upper() + pkodu, soyis.upper() + '_' + lakap.upper() + '_' + pkodu, soyis.upper() + lakap.upper() + '_' + pkodu,
			soyis.upper() + lakap.title() + pkodu,						soyis.upper() + '_' + lakap.title() + pkodu, soyis.upper() + '_' + lakap.title() + '_' + pkodu, soyis.upper() + lakap.title() + '_' + pkodu,
			soyis.title() + lakap + pkodu,								soyis.title() + '_' + lakap + pkodu, soyis.title() + '_' + lakap + '_' + pkodu, soyis.title() + lakap + '_' + pkodu,
			soyis.title() + lakap.upper() + pkodu,						soyis.title() + '_' + lakap.upper() + pkodu, soyis.title() + '_' + lakap.upper() + '_' + pkodu, soyis.title() + lakap.upper() + '_' + pkodu,
			soyis.title() + lakap.title() + pkodu,						soyis.title() + '_' + lakap.title() + pkodu, soyis.title() + '_' + lakap.title() + '_' + pkodu, soyis.title() + lakap.title() + '_' + pkodu,
			
			soyis.upper() + lakap + pkodu + pkodu,						soyis.upper() + '_' + lakap + pkodu + pkodu, soyis.upper() + '_' + lakap + '_' + pkodu + pkodu, soyis.upper() + lakap + '_' + pkodu + pkodu,
			soyis.upper() + lakap.upper() + pkodu + pkodu,				soyis.upper() + '_' + lakap.upper() + pkodu + pkodu, soyis.upper() + '_' + lakap.upper() + '_' + pkodu + pkodu, soyis.upper() + lakap.upper() + '_' + pkodu + pkodu,
			soyis.upper() + lakap.title() + pkodu + pkodu,				soyis.upper() + '_' + lakap.title() + pkodu + pkodu, soyis.upper() + '_' + lakap.title() + '_' + pkodu + pkodu, soyis.upper() + lakap.title() + '_' + pkodu + pkodu,
			soyis.title() + lakap + pkodu + pkodu,						soyis.title() + '_' + lakap + pkodu + pkodu, soyis.title() + '_' + lakap + '_' + pkodu + pkodu, soyis.title() + lakap + '_' + pkodu + pkodu,
			soyis.title() + lakap.upper() + pkodu + pkodu,				soyis.title() + '_' + lakap.upper() + pkodu + pkodu, soyis.title() + '_' + lakap.upper() + '_' + pkodu + pkodu, soyis.title() + lakap.upper() + '_' + pkodu + pkodu,
			soyis.title() + lakap.title() + pkodu + pkodu,				soyis.title() + '_' + lakap.title() + pkodu + pkodu, soyis.title() + '_' + lakap.title() + '_' + pkodu + pkodu, soyis.title() + lakap.title() + '_' + pkodu + pkodu,
			
			soyis.upper() + lakap + pkodu + t_pkodu,					soyis.upper() + '_' + lakap + pkodu + t_pkodu, soyis.upper() + '_' + lakap + '_' + pkodu + t_pkodu, soyis.upper() + lakap + '_' + pkodu + t_pkodu,
			soyis.upper() + lakap.upper() + pkodu + t_pkodu,  			soyis.upper() + '_' + lakap.upper() + pkodu + t_pkodu, soyis.upper() + '_' + lakap.upper() + '_' + pkodu + t_pkodu, soyis.upper() + lakap.upper() + '_' + pkodu + t_pkodu,
			soyis.upper() + lakap.title() + pkodu + t_pkodu,			soyis.upper() + '_' + lakap.title() + pkodu + t_pkodu, soyis.upper() + '_' + lakap.title() + '_' + pkodu + t_pkodu, soyis.upper() + lakap.title() + '_' + pkodu + t_pkodu,
			soyis.title() + lakap + pkodu + t_pkodu,					soyis.title() + '_' + lakap + pkodu + t_pkodu, soyis.title() + '_' + lakap + '_' + pkodu + t_pkodu, soyis.title() + lakap + '_' + pkodu + t_pkodu,
			soyis.title() + lakap.upper() + pkodu + t_pkodu,			soyis.title() + '_' + lakap.upper() + pkodu + t_pkodu, soyis.title() + '_' + lakap.upper() + '_' + pkodu + t_pkodu, soyis.title() + lakap.upper() + '_' + pkodu + t_pkodu,
			soyis.title() + lakap.title() + pkodu + t_pkodu,			soyis.title() + '_' + lakap.title() + pkodu + t_pkodu, soyis.title() + '_' + lakap.title() + '_' + pkodu + t_pkodu, soyis.title() + lakap.title() + '_' + pkodu + t_pkodu,
			
			soyis.upper() + lakap + t_pkodu,							soyis.upper() + '_' + lakap + t_pkodu, soyis.upper() + '_' + lakap + '_' + t_pkodu, soyis.upper() + lakap + '_' + t_pkodu,
			soyis.upper() + lakap.upper() + t_pkodu,					soyis.upper() + '_' + lakap.upper() + t_pkodu, soyis.upper() + '_' + lakap.upper() + '_' + t_pkodu, soyis.upper() + lakap.upper() + '_' + t_pkodu,
			soyis.upper() + lakap.title() + t_pkodu,					soyis.upper() + '_' + lakap.title() + t_pkodu, soyis.upper() + '_' + lakap.title() + '_' + t_pkodu, soyis.upper() + lakap.title() + '_' + t_pkodu,
			soyis.title() + lakap + t_pkodu,							soyis.title() + '_' + lakap + t_pkodu, soyis.title() + '_' + lakap + '_' + t_pkodu, soyis.title() + lakap + '_' + t_pkodu,
			soyis.title() + lakap.upper() + t_pkodu,					soyis.title() + '_' + lakap.upper() + t_pkodu, soyis.title() + '_' + lakap.upper() + '_' + t_pkodu, soyis.title() + lakap.upper() + '_' + t_pkodu,
			soyis.title() + lakap.title() + t_pkodu,					soyis.title() + '_' + lakap.title() + t_pkodu, soyis.title() + '_' + lakap.title() + '_' + t_pkodu, soyis.title() + lakap.title() + '_' + t_pkodu,
			
			soyis.upper() + lakap + t_pkodu + pkodu,					soyis.upper() + '_' + lakap + t_pkodu + pkodu, soyis.upper() + '_' + lakap + '_' + t_pkodu + pkodu, soyis.upper() + lakap + '_' + t_pkodu + pkodu,
			soyis.upper() + lakap.upper() + t_pkodu + pkodu,			soyis.upper() + '_' + lakap.upper() + t_pkodu + pkodu, soyis.upper() + '_' + lakap.upper() + '_' + t_pkodu + pkodu, soyis.upper() + lakap.upper() + '_' + t_pkodu + pkodu,
			soyis.upper() + lakap.title() + t_pkodu + pkodu,			soyis.upper() + '_' + lakap.title() + t_pkodu + pkodu, soyis.upper() + '_' + lakap.title() + '_' + t_pkodu + pkodu, soyis.upper() + lakap.title() + '_' + t_pkodu + pkodu,
			soyis.title() + lakap + t_pkodu + pkodu,					soyis.title() + '_' + lakap + t_pkodu + pkodu, soyis.title() + '_' + lakap + '_' + t_pkodu + pkodu, soyis.title() + lakap + '_' + t_pkodu + pkodu,
			soyis.title() + lakap.upper() + t_pkodu + pkodu,			soyis.title() + '_' + lakap.upper() + t_pkodu + pkodu, soyis.title() + '_' + lakap.upper() + '_' + t_pkodu + pkodu, soyis.title() + lakap.upper() + '_' + t_pkodu + pkodu,
			soyis.title() + lakap.title() + t_pkodu + pkodu,			soyis.title() + '_' + lakap.title() + t_pkodu + pkodu, soyis.title() + '_' + lakap.title() + '_' + t_pkodu + pkodu, soyis.title() + lakap.title() + '_' + t_pkodu + pkodu,
			
			soyis.upper() + lakap + t_pkodu + t_pkodu,					soyis.upper() + '_' + lakap + t_pkodu + t_pkodu, soyis.upper() + '_' + lakap + '_' + t_pkodu + t_pkodu, soyis.upper() + lakap + '_' + t_pkodu + t_pkodu,
			soyis.upper() + lakap.upper() + t_pkodu + t_pkodu,			soyis.upper() + '_' + lakap.upper() + t_pkodu + t_pkodu, soyis.upper() + '_' + lakap.upper() + '_' + t_pkodu + t_pkodu, soyis.upper() + lakap.upper() + '_' + t_pkodu + t_pkodu,
			soyis.upper() + lakap.title() + t_pkodu + t_pkodu,			soyis.upper() + '_' + lakap.title() + t_pkodu + t_pkodu, soyis.upper() + '_' + lakap.title() + '_' + t_pkodu + t_pkodu, soyis.upper() + lakap.title() + '_' + t_pkodu + t_pkodu,
			soyis.title() + lakap + t_pkodu + t_pkodu,					soyis.title() + '_' + lakap + t_pkodu + t_pkodu, soyis.title() + '_' + lakap + '_' + t_pkodu + t_pkodu, soyis.title() + lakap + '_' + t_pkodu + t_pkodu,
			soyis.title() + lakap.upper() + t_pkodu + t_pkodu,			soyis.title() + '_' + lakap.upper() + t_pkodu + t_pkodu, soyis.title() + '_' + lakap.upper() + '_' + t_pkodu + t_pkodu, soyis.title() + lakap.upper() + '_' + t_pkodu + t_pkodu,
			soyis.title() + lakap.title() + t_pkodu + t_pkodu,			soyis.title() + '_' + lakap.title() + t_pkodu + t_pkodu, soyis.title() + '_' + lakap.title() + '_' + t_pkodu + t_pkodu, soyis.title() + lakap.title() + '_' + t_pkodu + t_pkodu,
			
			#########################################################################################################################################################################################

			lakap + soyis + dyili, 										lakap + '_' + soyis + dyili, lakap + '_' + soyis + '_' + dyili, lakap + soyis + '_' + dyili,
			soyis + lakap + dyili,										soyis + '_' + lakap + dyili, soyis + '_' + lakap + '_' + dyili, soyis + lakap + '_' + dyili,
			
			lakap + soyis + dyili + dyili,								lakap + '_' + soyis + dyili + dyili, lakap + '_' + soyis + '_' + dyili + dyili, lakap + soyis + '_' + dyili + dyili,
			soyis + lakap + dyili + dyili,								soyis + '_' + lakap + dyili + dyili, soyis + '_' + lakap + '_' + dyili + dyili, soyis + lakap + '_' + dyili + dyili,
									
			lakap + soyis + dyili + t_dyili,							lakap + '_' + soyis + dyili + t_dyili, lakap + '_' + soyis + '_' + dyili + t_dyili, lakap + soyis + '_' + dyili + t_dyili,
			soyis + lakap + dyili + t_dyili,							soyis + '_' + lakap + dyili + t_dyili, soyis + '_' + lakap + '_' + dyili + t_dyili, soyis + lakap + '_' + dyili + t_dyili,
			
			lakap + soyis + t_dyili, 									lakap + '_' + soyis + t_dyili, lakap + '_' + soyis + '_' + t_dyili, lakap + soyis + '_' + t_dyili,
			soyis + lakap + t_dyili,									soyis + '_' + lakap + t_dyili, soyis + '_' + lakap + '_' + t_dyili, soyis + lakap + '_' + t_dyili,
			
			lakap + soyis + t_dyili + dyili,							lakap + '_' + soyis + t_dyili + dyili, lakap + '_' + soyis + '_' + t_dyili + dyili, lakap + soyis + '_' + t_dyili + dyili,
			soyis + lakap + t_dyili + dyili,							soyis + '_' + lakap + t_dyili + dyili, soyis + '_' + lakap + '_' + t_dyili + dyili, soyis + lakap + '_' + t_dyili + dyili,
			
			lakap + soyis + t_dyili + t_dyili,							lakap + '_' + soyis + t_dyili + t_dyili, lakap + '_' + soyis + '_' + t_dyili + t_dyili, lakap + soyis + '_' + t_dyili + t_dyili,
			soyis + lakap + t_dyili + t_dyili,							soyis + '_' + lakap + t_dyili + t_dyili, soyis + '_' + lakap + '_' + t_dyili + t_dyili, soyis + lakap + '_' + t_dyili + t_dyili,
			
			lakap + soyis + daygun,										lakap + '_' + soyis + daygun, lakap + '_' + soyis + '_' + daygun, lakap + soyis + '_' + daygun,
			soyis + lakap + daygun,										soyis + '_' + lakap + daygun, soyis + '_' + lakap + '_' + daygun, soyis + lakap + '_' + daygun,
			
			lakap + soyis + t_daygun,									lakap + '_' + soyis + t_daygun, lakap + '_' + soyis + '_' + t_daygun, lakap + soyis + '_' + t_daygun,
			soyis + lakap + t_daygun,									soyis + '_' + lakap + t_daygun, soyis + '_' + lakap + '_' + t_daygun, soyis + lakap + '_' + t_daygun,
			
			lakap + dtarihi,											lakap + '_' + dtarihi,
			lakap + t_dtarihi,											lakap + '_' + t_dtarihi,
			
			lakap + soyis + dtarihi,									lakap + '_' + soyis + dtarihi, lakap + '_' + soyis + '_' + dtarihi, lakap + soyis + '_' + dtarihi,
			lakap + soyis + t_dtarihi,									lakap + '_' + soyis + t_dtarihi, lakap + '_' + soyis + '_' + t_dtarihi, lakap + soyis + '_' + t_dtarihi,
			
			soyis + lakap + dtarihi,									soyis + '_' + lakap + dtarihi, soyis + '_' + lakap + '_' + dtarihi, soyis + lakap + '_' + dtarihi,
			soyis + lakap + t_dtarihi,									soyis + '_' + lakap + t_dtarihi, soyis + '_' + lakap + '_' + t_dtarihi, soyis + lakap + '_' + t_dtarihi,
			
			#######################################################################################################################################################
			
			lakap.upper() + soyis + dyili,								lakap.upper() + '_' + soyis + dyili, lakap.upper() + '_' + soyis + '_' + dyili, lakap.upper() + soyis + '_' + dyili,
			lakap.upper() + soyis.upper() + dyili,						lakap.upper() + '_' + soyis.upper() + dyili, lakap.upper() + '_' + soyis.upper() + '_' + dyili, lakap.upper() + soyis.upper() + '_' + dyili,
			lakap.upper() + soyis.title() + dyili,						lakap.upper() + '_' + soyis.title() + dyili, lakap.upper() + '_' + soyis.title() + '_' + dyili, lakap.upper() + soyis.title() + '_' + dyili,
			lakap.title() + soyis + dyili,								lakap.title() + '_' + soyis + dyili, lakap.title() + '_' + soyis + '_' + dyili, lakap.title() + soyis + '_' + dyili,
			lakap.title() + soyis.upper() + dyili,						lakap.title() + '_' + soyis.upper() + dyili, lakap.title() + '_' + soyis.upper() + '_' + dyili, lakap.title() + soyis.upper() + '_' + dyili,
			lakap.title() + soyis.title() + dyili,						lakap.title() + '_' + soyis.title() + dyili, lakap.title() + '_' + soyis.title() + '_' + dyili, lakap.title() + soyis.title() + '_' + dyili,
			
			lakap.upper() + soyis + dyili + dyili,						lakap.upper() + '_' + soyis + dyili + dyili, lakap.upper() + '_' + soyis + '_' + dyili + dyili, lakap.upper() + soyis + '_' + dyili + dyili,
			lakap.upper() + soyis.upper() + dyili + dyili,				lakap.upper() + '_' + soyis.upper() + dyili + dyili, lakap.upper() + '_' + soyis.upper() + '_' + dyili + dyili, lakap.upper() + soyis.upper() + '_' + dyili + dyili,
			lakap.upper() + soyis.title() + dyili + dyili,				lakap.upper() + '_' + soyis.title() + dyili + dyili, lakap.upper() + '_' + soyis.title() + '_' + dyili + dyili, lakap.upper() + soyis.title() + '_' + dyili + dyili,
			lakap.title() + soyis + dyili + dyili,						lakap.title() + '_' + soyis + dyili + dyili, lakap.title() + '_' + soyis + '_' + dyili + dyili, lakap.title() + soyis + '_' + dyili + dyili,
			lakap.title() + soyis.upper() + dyili + dyili,				lakap.title() + '_' + soyis.upper() + dyili + dyili, lakap.title() + '_' + soyis.upper() + '_' + dyili + dyili, lakap.title() + soyis.upper() + '_' + dyili + dyili,
			lakap.title() + soyis.title() + dyili + dyili,				lakap.title() + '_' + soyis.title() + dyili + dyili, lakap.title() + '_' + soyis.title() + '_' + dyili + dyili, lakap.title() + soyis.title() + '_' + dyili + dyili,
			
			lakap.upper() + soyis + dyili + t_dyili,					lakap.upper() + '_' + soyis + dyili + t_dyili, lakap.upper() + '_' + soyis + '_' + dyili + t_dyili, lakap.upper() + soyis + '_' + dyili + t_dyili,
			lakap.upper() + soyis.upper() + dyili + t_dyili,			lakap.upper() + '_' + soyis.upper() + dyili + t_dyili, lakap.upper() + '_' + soyis.upper() + '_' + dyili + t_dyili, lakap.upper() + soyis.upper() + '_' + dyili + t_dyili,
			lakap.upper() + soyis.title() + dyili + t_dyili,			lakap.upper() + '_' + soyis.title() + dyili + t_dyili, lakap.upper() + '_' + soyis.title() + '_' + dyili + t_dyili, lakap.upper() + soyis.title() + '_' + dyili + t_dyili,
			lakap.title() + soyis + dyili + t_dyili,					lakap.title() + '_' + soyis + dyili + t_dyili, lakap.title() + '_' + soyis + '_' + dyili + t_dyili, lakap.title() + soyis + '_' + dyili + t_dyili,
			lakap.title() + soyis.upper() + dyili + t_dyili,			lakap.title() + '_' + soyis.upper() + dyili + t_dyili, lakap.title() + '_' + soyis.upper() + '_' + dyili + t_dyili, lakap.title() + soyis.upper() + '_' + dyili + t_dyili,
			lakap.title() + soyis.title() + dyili + t_dyili,			lakap.title() + '_' + soyis.title() + dyili + t_dyili, lakap.title() + '_' + soyis.title() + '_' + dyili + t_dyili, lakap.title() + soyis.title() + '_' + dyili + t_dyili,
			
			lakap.upper() + soyis + t_dyili,							lakap.upper() + '_' + soyis + t_dyili, lakap.upper() + '_' + soyis + '_' + t_dyili, lakap.upper() + soyis + '_' + t_dyili,
			lakap.upper() + soyis.upper() + t_dyili,					lakap.upper() + '_' + soyis.upper() + t_dyili, lakap.upper() + '_' + soyis.upper() + '_' + t_dyili, lakap.upper() + soyis.upper() + '_' + t_dyili,
			lakap.upper() + soyis.title() + t_dyili,					lakap.upper() + '_' + soyis.title() + t_dyili, lakap.upper() + '_' + soyis.title() + '_' + t_dyili, lakap.upper() + soyis.title() + '_' + t_dyili,
			lakap.title() + soyis + t_dyili,							lakap.title() + '_' + soyis + t_dyili, lakap.title() + '_' + soyis + '_' + t_dyili, lakap.title() + soyis + '_' + t_dyili,
			lakap.title() + soyis.upper() + t_dyili,					lakap.title() + '_' + soyis.upper() + t_dyili, lakap.title() + '_' + soyis.upper() + '_' + t_dyili, lakap.title() + soyis.upper() + '_' + t_dyili,
			lakap.title() + soyis.title() + t_dyili,					lakap.title() + '_' + soyis.title() + t_dyili, lakap.title() + '_' + soyis.title() + '_' + t_dyili, lakap.title() + soyis.title() + '_' + t_dyili,

			lakap.upper() + soyis + t_dyili + dyili,					lakap.upper() + '_' + soyis + t_dyili + dyili, lakap.upper() + '_' + soyis + '_' + t_dyili + dyili, lakap.upper() + soyis + '_' + t_dyili + dyili,
			lakap.upper() + soyis.upper() + t_dyili + dyili,			lakap.upper() + '_' + soyis.upper() + t_dyili + dyili, lakap.upper() + '_' + soyis.upper() + '_' + t_dyili + dyili, lakap.upper() + soyis.upper() + '_' + t_dyili + dyili,
			lakap.upper() + soyis.title() + t_dyili + dyili,			lakap.upper() + '_' + soyis.title() + t_dyili + dyili, lakap.upper() + '_' + soyis.title() + '_' + t_dyili + dyili, lakap.upper() + soyis.title() + '_' + t_dyili + dyili,
			lakap.title() + soyis + t_dyili + dyili,					lakap.title() + '_' + soyis + t_dyili + dyili, lakap.title() + '_' + soyis + '_' + t_dyili + dyili, lakap.title() + soyis + '_' + t_dyili + dyili,
			lakap.title() + soyis.upper() + t_dyili + dyili,			lakap.title() + '_' + soyis.upper() + t_dyili + dyili, lakap.title() + '_' + soyis.upper() + '_' + t_dyili + dyili, lakap.title() + soyis.upper() + '_' + t_dyili + dyili,
			lakap.title() + soyis.title() + t_dyili + dyili,			lakap.title() + '_' + soyis.title() + t_dyili + dyili, lakap.title() + '_' + soyis.title() + '_' + t_dyili + dyili, lakap.title() + soyis.title() + '_' + t_dyili + dyili,

			lakap.upper() + soyis + t_dyili + t_dyili,					lakap.upper() + '_' + soyis + t_dyili + t_dyili, lakap.upper() + '_' + soyis + '_' + t_dyili + t_dyili, lakap.upper() + soyis + '_' + t_dyili + t_dyili,
			lakap.upper() + soyis.upper() + t_dyili + t_dyili,			lakap.upper() + '_' + soyis.upper() + t_dyili + t_dyili, lakap.upper() + '_' + soyis.upper() + '_' + t_dyili + t_dyili,lakap.upper() + soyis.upper() + '_' + t_dyili + t_dyili,
			lakap.upper() + soyis.title() + t_dyili + t_dyili,			lakap.upper() + '_' + soyis.title() + t_dyili + t_dyili, lakap.upper() + '_' + soyis.title() + '_' + t_dyili + t_dyili, lakap.upper() + soyis.title() + '_' + t_dyili + t_dyili,
			lakap.title() + soyis + t_dyili + t_dyili,					lakap.title() + '_' + soyis + t_dyili + t_dyili, lakap.title() + '_' + soyis + '_' + t_dyili + t_dyili, lakap.title() + soyis + '_' + t_dyili + t_dyili,
			lakap.title() + soyis.upper() + t_dyili + t_dyili,			lakap.title() + '_' + soyis.upper() + t_dyili + t_dyili, lakap.title() + '_' + soyis.upper() + '_' + t_dyili + t_dyili, lakap.title() + soyis.upper() + '_' + t_dyili + t_dyili,
			lakap.title() + soyis.title() + t_dyili + t_dyili,			lakap.title() + '_' + soyis.title() + t_dyili + t_dyili, lakap.title() + '_' + soyis.title() + '_' + t_dyili + t_dyili, lakap.title() + soyis.title() + '_' + t_dyili + t_dyili,

			soyis.upper() + lakap + dyili,								soyis.upper() + '_' + lakap + dyili, soyis.upper() + '_' + lakap + '_' + dyili, soyis.upper() + lakap + '_' + dyili,
			soyis.upper() + lakap.upper() + dyili,						soyis.upper() + '_' + lakap.upper() + dyili, soyis.upper() + '_' + lakap.upper() + '_' + dyili, soyis.upper() + lakap.upper() + '_' + dyili,
			soyis.upper() + lakap.title() + dyili,						soyis.upper() + '_' + lakap.title() + dyili, soyis.upper() + '_' + lakap.title() + '_' + dyili, soyis.upper() + lakap.title() + '_' + dyili,
			soyis.title() + lakap + dyili,								soyis.title() + '_' + lakap + dyili, soyis.title() + '_' + lakap + '_' + dyili, soyis.title() + lakap + '_' + dyili,
			soyis.title() + lakap.upper() + dyili,						soyis.title() + '_' + lakap.upper() + dyili, soyis.title() + '_' + lakap.upper() + '_' + dyili, soyis.title() + lakap.upper() + '_' + dyili,
			soyis.title() + lakap.title() + dyili,						soyis.title() + '_' + lakap.title() + dyili, soyis.title() + '_' + lakap.title() + '_' + dyili, soyis.title() + lakap.title() + '_' + dyili,
			
			soyis.upper() + lakap + dyili + dyili,						soyis.upper() + '_' + lakap + dyili + dyili, soyis.upper() + '_' + lakap + '_' + dyili + dyili, soyis.upper() + lakap + '_' + dyili + dyili,
			soyis.upper() + lakap.upper() + dyili + dyili,				soyis.upper() + '_' + lakap.upper() + dyili + dyili, soyis.upper() + '_' + lakap.upper() + '_' + dyili + dyili, soyis.upper() + lakap.upper() + '_' + dyili + dyili,
			soyis.upper() + lakap.title() + dyili + dyili,				soyis.upper() + '_' + lakap.title() + dyili + dyili, soyis.upper() + '_' + lakap.title() + '_' + dyili + dyili, soyis.upper() + lakap.title() + '_' + dyili + dyili,
			soyis.title() + lakap + dyili + dyili,						soyis.title() + '_' + lakap + dyili + dyili, soyis.title() + '_' + lakap + '_' + dyili + dyili, soyis.title() + lakap + '_' + dyili + dyili,
			soyis.title() + lakap.upper() + dyili + dyili,				soyis.title() + '_' + lakap.upper() + dyili + dyili, soyis.title() + '_' + lakap.upper() + '_' + dyili + dyili, soyis.title() + lakap.upper() + '_' + dyili + dyili,
			soyis.title() + lakap.title() + dyili + dyili,				soyis.title() + '_' + lakap.title() + dyili + dyili, soyis.title() + '_' + lakap.title() + '_' + dyili + dyili, soyis.title() + lakap.title() + '_' + dyili + dyili,
			
			soyis.upper() + lakap + dyili + t_dyili,					soyis.upper() + '_' + lakap + dyili + t_dyili, soyis.upper() + '_' + lakap + '_' + dyili + t_dyili, soyis.upper() + lakap + '_' + dyili + t_dyili,
			soyis.upper() + lakap.upper() + dyili + t_dyili,  			soyis.upper() + '_' + lakap.upper() + dyili + t_dyili, soyis.upper() + '_' + lakap.upper() + '_' + dyili + t_dyili, soyis.upper() + lakap.upper() + '_' + dyili + t_dyili,
			soyis.upper() + lakap.title() + dyili + t_dyili,			soyis.upper() + '_' + lakap.title() + dyili + t_dyili, soyis.upper() + '_' + lakap.title() + '_' + dyili + t_dyili, soyis.upper() + lakap.title() + '_' + dyili + t_dyili,
			soyis.title() + lakap + dyili + t_dyili,					soyis.title() + '_' + lakap + dyili + t_dyili, soyis.title() + '_' + lakap + '_' + dyili + t_dyili, soyis.title() + lakap + '_' + dyili + t_dyili,
			soyis.title() + lakap.upper() + dyili + t_dyili,			soyis.title() + '_' + lakap.upper() + dyili + t_dyili, soyis.title() + '_' + lakap.upper() + '_' + dyili + t_dyili, soyis.title() + lakap.upper() + '_' + dyili + t_dyili,
			soyis.title() + lakap.title() + dyili + t_dyili,			soyis.title() + '_' + lakap.title() + dyili + t_dyili, soyis.title() + '_' + lakap.title() + '_' + dyili + t_dyili, soyis.title() + lakap.title() + '_' + dyili + t_dyili,
			
			soyis.upper() + lakap + t_dyili,							soyis.upper() + '_' + lakap + t_dyili, soyis.upper() + '_' + lakap + '_' + t_dyili, soyis.upper() + lakap + '_' + t_dyili,
			soyis.upper() + lakap.upper() + t_dyili,					soyis.upper() + '_' + lakap.upper() + t_dyili, soyis.upper() + '_' + lakap.upper() + '_' + t_dyili, soyis.upper() + lakap.upper() + '_' + t_dyili,
			soyis.upper() + lakap.title() + t_dyili,					soyis.upper() + '_' + lakap.title() + t_dyili, soyis.upper() + '_' + lakap.title() + '_' + t_dyili, soyis.upper() + lakap.title() + '_' + t_dyili,
			soyis.title() + lakap + t_dyili,							soyis.title() + '_' + lakap + t_dyili, soyis.title() + '_' + lakap + '_' + t_dyili, soyis.title() + lakap + '_' + t_dyili,
			soyis.title() + lakap.upper() + t_dyili,					soyis.title() + '_' + lakap.upper() + t_dyili, soyis.title() + '_' + lakap.upper() + '_' + t_dyili, soyis.title() + lakap.upper() + '_' + t_dyili,
			soyis.title() + lakap.title() + t_dyili,					soyis.title() + '_' + lakap.title() + t_dyili, soyis.title() + '_' + lakap.title() + '_' + t_dyili, soyis.title() + lakap.title() + '_' + t_dyili,
			
			soyis.upper() + lakap + t_dyili + dyili,					soyis.upper() + '_' + lakap + t_dyili + dyili, soyis.upper() + '_' + lakap + '_' + t_dyili + dyili, soyis.upper() + lakap + '_' + t_dyili + dyili,
			soyis.upper() + lakap.upper() + t_dyili + dyili,			soyis.upper() + '_' + lakap.upper() + t_dyili + dyili, soyis.upper() + '_' + lakap.upper() + '_' + t_dyili + dyili, soyis.upper() + lakap.upper() + '_' + t_dyili + dyili,
			soyis.upper() + lakap.title() + t_dyili + dyili,			soyis.upper() + '_' + lakap.title() + t_dyili + dyili, soyis.upper() + '_' + lakap.title() + '_' + t_dyili + dyili, soyis.upper() + lakap.title() + '_' + t_dyili + dyili,
			soyis.title() + lakap + t_dyili + dyili,					soyis.title() + '_' + lakap + t_dyili + dyili, soyis.title() + '_' + lakap + '_' + t_dyili + dyili, soyis.title() + lakap + '_' + t_dyili + dyili,
			soyis.title() + lakap.upper() + t_dyili + dyili,			soyis.title() + '_' + lakap.upper() + t_dyili + dyili, soyis.title() + '_' + lakap.upper() + '_' + t_dyili + dyili, soyis.title() + lakap.upper() + '_' + t_dyili + dyili,
			soyis.title() + lakap.title() + t_dyili + dyili,			soyis.title() + '_' + lakap.title() + t_dyili + dyili, soyis.title() + '_' + lakap.title() + '_' + t_dyili + dyili, soyis.title() + lakap.title() + '_' + t_dyili + dyili,
			
			soyis.upper() + lakap + t_dyili + t_dyili,					soyis.upper() + '_' + lakap + t_dyili + t_dyili, soyis.upper() + '_' + lakap + '_' + t_dyili + t_dyili, soyis.upper() + lakap + '_' + t_dyili + t_dyili,
			soyis.upper() + lakap.upper() + t_dyili + t_dyili,			soyis.upper() + '_' + lakap.upper() + t_dyili + t_dyili, soyis.upper() + '_' + lakap.upper() + '_' + t_dyili + t_dyili, soyis.upper() + lakap.upper() + '_' + t_dyili + t_dyili,
			soyis.upper() + lakap.title() + t_dyili + t_dyili,		    soyis.upper() + '_' + lakap.title() + t_dyili + t_dyili, soyis.upper() + '_' + lakap.title() + '_' + t_dyili + t_dyili, soyis.upper() + lakap.title() + '_' + t_dyili + t_dyili,
			soyis.title() + lakap + t_dyili + t_dyili,					soyis.title() + '_' + lakap + t_dyili + t_dyili, soyis.title() + '_' + lakap + '_' + t_dyili + t_dyili, soyis.title() + lakap + '_' + t_dyili + t_dyili,
			soyis.title() + lakap.upper() + t_dyili + t_dyili,			soyis.title() + '_' + lakap.upper() + t_dyili + t_dyili, soyis.title() + '_' + lakap.upper() + '_' + t_dyili + t_dyili, soyis.title() + lakap.upper() + '_' + t_dyili + t_dyili,
			soyis.title() + lakap.title() + t_dyili + t_dyili,			soyis.title() + '_' + lakap.title() + t_dyili + t_dyili, soyis.title() + '_' + lakap.title() + '_' + t_dyili + t_dyili, soyis.title() + lakap.title() + '_' + t_dyili + t_dyili,
			
			lakap.upper() + soyis + daygun,								lakap.upper() + '_' + soyis + daygun, lakap.upper() + '_' + soyis + '_' + daygun, lakap.upper() + soyis + '_' + daygun,
			lakap.upper() + soyis.upper() + daygun,						lakap.upper() + '_' + soyis.upper() + daygun, lakap.upper() + '_' + soyis.upper() + '_' + daygun, lakap.upper() + soyis.upper() + '_' + daygun,
			lakap.upper() + soyis.title() + daygun,						lakap.upper() + '_' + soyis.title() + daygun, lakap.upper() + '_' + soyis.title() + '_' + daygun, lakap.upper() + soyis.title() + '_' + daygun,
			lakap.title() + soyis + daygun,								lakap.title() + '_' + soyis + daygun, lakap.title() + '_' + soyis + '_' + daygun, lakap.title() + soyis + '_' + daygun,
			lakap.title() + soyis.upper() + daygun,						lakap.title() + '_' + soyis.upper() + daygun, lakap.title() + '_' + soyis.upper() + '_' + daygun, lakap.title() + soyis.upper() + '_' + daygun,
			lakap.title() + soyis.title() + daygun,						lakap.title() + '_' + soyis.title() + daygun, lakap.title() + '_' + soyis.title() + '_' + daygun, lakap.title() + soyis.title() + '_' + daygun,
			
			lakap.upper() + soyis + daygun + daygun,					lakap.upper() + '_' + soyis + daygun + daygun, lakap.upper() + '_' + soyis + '_' + daygun + daygun, lakap.upper() + soyis + '_' + daygun + daygun,
			lakap.upper() + soyis.upper() + daygun + daygun,			lakap.upper() + '_' + soyis.upper() + daygun + daygun, lakap.upper() + '_' + soyis.upper() + '_' + daygun + daygun, lakap.upper() + soyis.upper() + '_' + daygun + daygun,
			lakap.upper() + soyis.title() + daygun + daygun,			lakap.upper() + '_' + soyis.title() + daygun + daygun, lakap.upper() + '_' + soyis.title() + '_' + daygun + daygun, lakap.upper() + soyis.title() + '_' + daygun + daygun,
			lakap.title() + soyis + daygun + daygun,					lakap.title() + '_' + soyis + daygun + daygun, lakap.title() + '_' + soyis + '_' + daygun + daygun, lakap.title() + soyis + '_' + daygun + daygun,
			lakap.title() + soyis.upper() + daygun + daygun,			lakap.title() + '_' + soyis.upper() + daygun + daygun, lakap.title() + '_' + soyis.upper() + '_' + daygun + daygun, lakap.title() + soyis.upper() + '_' + daygun + daygun,
			lakap.title() + soyis.title() + daygun + daygun,			lakap.title() + '_' + soyis.title() + daygun + daygun, lakap.title() + '_' + soyis.title() + '_' + daygun + daygun, lakap.title() + soyis.title() + '_' + daygun + daygun,
			
			lakap.upper() + soyis + daygun + t_daygun,					lakap.upper() + '_' + soyis + daygun + t_daygun, lakap.upper() + '_' + soyis + '_' + daygun + t_daygun, lakap.upper() + soyis + '_' + daygun + t_daygun,
			lakap.upper() + soyis.upper() + daygun + t_daygun,			lakap.upper() + '_' + soyis.upper() + daygun + t_daygun, lakap.upper() + '_' + soyis.upper() + '_' + daygun + t_daygun, lakap.upper() + soyis.upper() + '_' + daygun + t_daygun,
			lakap.upper() + soyis.title() + daygun + t_daygun,			lakap.upper() + '_' + soyis.title() + daygun + t_daygun, lakap.upper() + '_' + soyis.title() + '_' + daygun + t_daygun, lakap.upper() + soyis.title() + '_' + daygun + t_daygun,
			lakap.title() + soyis + daygun + t_daygun,					lakap.title() + '_' + soyis + daygun + t_daygun, lakap.title() + '_' + soyis + '_' + daygun + t_daygun, lakap.title() + soyis + '_' + daygun + t_daygun,
			lakap.title() + soyis.upper() + daygun + t_daygun,			lakap.title() + '_' + soyis.upper() + daygun + t_daygun, lakap.title() + '_' + soyis.upper() + '_' + daygun + t_daygun, lakap.title() + soyis.upper() + '_' + daygun + t_daygun,
			lakap.title() + soyis.title() + daygun + t_daygun,			lakap.title() + '_' + soyis.title() + daygun + t_daygun, lakap.title() + '_' + soyis.title() + '_' + daygun + t_daygun, lakap.title() + soyis.title() + '_' + daygun + t_daygun,
			
			lakap.upper() + soyis + t_daygun,							lakap.upper() + '_' + soyis + t_daygun, lakap.upper() + '_' + soyis + '_' + t_daygun, lakap.upper() + soyis + '_' + t_daygun,
			lakap.upper() + soyis.upper() + t_daygun,					lakap.upper() + '_' + soyis.upper() + t_daygun, lakap.upper() + '_' + soyis.upper() + '_' + t_daygun, lakap.upper() + soyis.upper() + '_' + t_daygun,
			lakap.upper() + soyis.title() + t_daygun,					lakap.upper() + '_' + soyis.title() + t_daygun, lakap.upper() + '_' + soyis.title() + '_' + t_daygun, lakap.upper() + soyis.title() + '_' + t_daygun,
			lakap.title() + soyis + t_daygun,							lakap.title() + '_' + soyis + daygun, lakap.title() + '_' + soyis + '_' + t_daygun, lakap.title() + soyis + '_' + t_daygun,
			lakap.title() + soyis.upper() + t_daygun,					lakap.title() + '_' + soyis.upper() + daygun, lakap.title() + '_' + soyis.upper() + '_' + t_daygun, lakap.title() + soyis.upper() + '_' + t_daygun,
			lakap.title() + soyis.title() + t_daygun,					lakap.title() + '_' + soyis.title() + daygun, lakap.title() + '_' + soyis.title() + '_' + t_daygun, lakap.title() + soyis.title() + '_' + t_daygun,

			lakap.upper() + soyis + t_daygun + daygun,					lakap.upper() + '_' + soyis + t_daygun + daygun, lakap.upper() + '_' + soyis + '_' + t_daygun + daygun, lakap.upper() + soyis + '_' + t_daygun + daygun,
			lakap.upper() + soyis.upper() + t_daygun + daygun,			lakap.upper() + '_' + soyis.upper() + t_daygun + daygun, lakap.upper() + '_' + soyis.upper() + '_' + t_daygun + daygun, lakap.upper() + soyis.upper() + '_' + t_daygun + daygun,
			lakap.upper() + soyis.title() + t_daygun + daygun,			lakap.upper() + '_' + soyis.title() + t_daygun + daygun, lakap.upper() + '_' + soyis.title() + '_' + t_daygun + daygun, lakap.upper() + soyis.title() + '_' + t_daygun + daygun,
			lakap.title() + soyis + t_daygun + daygun,					lakap.title() + '_' + soyis + t_daygun + daygun, lakap.title() + '_' + soyis + '_' + t_daygun + daygun, lakap.title() + soyis + '_' + t_daygun + daygun,
			lakap.title() + soyis.upper() + t_daygun + daygun,			lakap.title() + '_' + soyis.upper() + t_daygun + daygun, lakap.title() + '_' + soyis.upper() + '_' + t_daygun + daygun, lakap.title() + soyis.upper() + '_' + t_daygun + daygun,
			lakap.title() + soyis.title() + t_daygun + daygun,			lakap.title() + '_' + soyis.title() + t_daygun + daygun, lakap.title() + '_' + soyis.title() + '_' + t_daygun + daygun, lakap.title() + soyis.title() + '_' + t_daygun + daygun,

			lakap.upper() + soyis + t_daygun + t_daygun,				lakap.upper() + '_' + soyis + t_daygun + t_daygun, lakap.upper() + '_' + soyis + '_' + t_daygun + t_daygun, lakap.upper() + soyis + '_' + t_daygun + t_daygun,
			lakap.upper() + soyis.upper() + t_daygun + t_daygun,		lakap.upper() + '_' + soyis.upper() + t_daygun + t_daygun, lakap.upper() + '_' + soyis.upper() + '_' + t_daygun + t_daygun, lakap.upper() + soyis.upper() + '_' + t_daygun + t_daygun,
			lakap.upper() + soyis.title() + t_daygun + t_daygun,		lakap.upper() + '_' + soyis.title() + t_daygun + t_daygun, lakap.upper() + '_' + soyis.title() + '_' + t_daygun + t_daygun, lakap.upper() + soyis.title() + '_' + t_daygun + t_daygun,
			lakap.title() + soyis + t_daygun + t_daygun,				lakap.title() + '_' + soyis + t_daygun + daygun, lakap.title() + '_' + soyis + '_' + t_daygun + t_daygun, lakap.title() + soyis + '_' + t_daygun + t_daygun,
			lakap.title() + soyis.upper() + t_daygun + t_daygun,		lakap.title() + '_' + soyis.upper() + t_daygun + daygun, lakap.title() + '_' + soyis.upper() + '_' + t_daygun + t_daygun, lakap.title() + soyis.upper() + '_' + t_daygun + t_daygun,
			lakap.title() + soyis.title() + t_daygun + t_daygun,		lakap.title() + '_' + soyis.title() + t_daygun + daygun, lakap.title() + '_' + soyis.title() + '_' + t_daygun + t_daygun, lakap.title() + soyis.title() + '_' + t_daygun + t_daygun,

			soyis.upper() + lakap + daygun,								soyis.upper() + '_' + lakap + daygun, soyis.upper() + '_' + lakap + '_' + daygun, soyis.upper() + lakap + '_' + daygun,
			soyis.upper() + lakap.upper() + daygun,						soyis.upper() + '_' + lakap.upper() + daygun, soyis.upper() + '_' + lakap.upper() + '_' + daygun, soyis.upper() + lakap.upper() + '_' + daygun,
			soyis.upper() + lakap.title() + daygun,						soyis.upper() + '_' + lakap.title() + daygun, soyis.upper() + '_' + lakap.title() + '_' + daygun, soyis.upper() + lakap.title() + '_' + daygun,
			soyis.title() + lakap + daygun,								soyis.title() + '_' + lakap + daygun, soyis.title() + '_' + lakap + '_' + daygun, soyis.title() + lakap + '_' + daygun,
			soyis.title() + lakap.upper() + daygun,						soyis.title() + '_' + lakap.upper() + daygun, soyis.title() + '_' + lakap.upper() + '_' + daygun, soyis.title() + lakap.upper() + '_' + daygun,
			soyis.title() + lakap.title() + daygun,						soyis.title() + '_' + lakap.title() + daygun, soyis.title() + '_' + lakap.title() + '_' + daygun, soyis.title() + lakap.title() + '_' + daygun,
			
			soyis.upper() + lakap + daygun + daygun,					soyis.upper() + '_' + lakap + daygun + daygun, soyis.upper() + '_' + lakap + '_' + daygun + daygun, soyis.upper() + lakap + '_' + daygun + daygun,
			soyis.upper() + lakap.upper() + daygun + daygun,			soyis.upper() + '_' + lakap.upper() + daygun + daygun, soyis.upper() + '_' + lakap.upper() + '_' + daygun + daygun, soyis.upper() + lakap.upper() + '_' + daygun + daygun,
			soyis.upper() + lakap.title() + daygun + daygun,			soyis.upper() + '_' + lakap.title() + daygun + daygun, soyis.upper() + '_' + lakap.title() + '_' + daygun + daygun, soyis.upper() + lakap.title() + '_' + daygun + daygun,
			soyis.title() + lakap + daygun + daygun,					soyis.title() + '_' + lakap + daygun + daygun, soyis.title() + '_' + lakap + '_' + daygun + daygun, soyis.title() + lakap + '_' + daygun + daygun,
			soyis.title() + lakap.upper() + daygun + daygun,			soyis.title() + '_' + lakap.upper() + daygun + daygun, soyis.title() + '_' + lakap.upper() + '_' + daygun + daygun, soyis.title() + lakap.upper() + '_' + daygun + daygun,
			soyis.title() + lakap.title() + daygun + daygun,			soyis.title() + '_' + lakap.title() + daygun + daygun, soyis.title() + '_' + lakap.title() + '_' + daygun + daygun, soyis.title() + lakap.title() + '_' + daygun + daygun,
			
			soyis.upper() + lakap + daygun + t_daygun,					soyis.upper() + '_' + lakap + daygun + t_daygun, soyis.upper() + '_' + lakap + '_' + daygun + t_daygun, soyis.upper() + lakap + '_' + daygun + t_daygun,
			soyis.upper() + lakap.upper() + daygun + t_daygun,			soyis.upper() + '_' + lakap.upper() + daygun + t_daygun, soyis.upper() + '_' + lakap.upper() + '_' + daygun + t_daygun, soyis.upper() + lakap.upper() + '_' + daygun + t_daygun,
			soyis.upper() + lakap.title() + daygun + t_daygun,			soyis.upper() + '_' + lakap.title() + daygun + t_daygun, soyis.upper() + '_' + lakap.title() + '_' + daygun + t_daygun, soyis.upper() + lakap.title() + '_' + daygun + t_daygun,
			soyis.title() + lakap + daygun + t_daygun,					soyis.title() + '_' + lakap + daygun + t_daygun, soyis.title() + '_' + lakap + '_' + daygun + t_daygun, soyis.title() + lakap + '_' + daygun + t_daygun,
			soyis.title() + lakap.upper() + daygun + t_daygun,			soyis.title() + '_' + lakap.upper() + daygun + t_daygun, soyis.title() + '_' + lakap.upper() + '_' + daygun + t_daygun, soyis.title() + lakap.upper() + '_' + daygun + t_daygun,
			soyis.title() + lakap.title() + daygun + t_daygun,			soyis.title() + '_' + lakap.title() + daygun + t_daygun, soyis.title() + '_' + lakap.title() + '_' + daygun + t_daygun, soyis.title() + lakap.title() + '_' + daygun + t_daygun,
			
			soyis.upper() + lakap + t_daygun,							soyis.upper() + '_' + lakap + t_daygun, soyis.upper() + '_' + lakap + '_' + t_daygun, soyis.upper() + lakap + '_' + t_daygun,
			soyis.upper() + lakap.upper() + t_daygun,					soyis.upper() + '_' + lakap.upper() + t_daygun, soyis.upper() + '_' + lakap.upper() + '_' + t_daygun, soyis.upper() + lakap.upper() + '_' + t_daygun,
			soyis.upper() + lakap.title() + t_daygun,					soyis.upper() + '_' + lakap.title() + t_daygun, soyis.upper() + '_' + lakap.title() + '_' + t_daygun, soyis.upper() + lakap.title() + '_' + t_daygun,
			soyis.title() + lakap + t_daygun,							soyis.title() + '_' + lakap + daygun, soyis.title() + '_' + lakap + '_' + t_daygun, soyis.title() + lakap + '_' + t_daygun,
			soyis.title() + lakap.upper() + t_daygun,					soyis.title() + '_' + lakap.upper() + daygun, soyis.title() + '_' + lakap.upper() + '_' + t_daygun, soyis.title() + lakap.upper() + '_' + t_daygun,
			soyis.title() + lakap.title() + t_daygun,					soyis.title() + '_' + lakap.title() + daygun, soyis.title() + '_' + lakap.title() + '_' + t_daygun, soyis.title() + lakap.title() + '_' + t_daygun,
			
			soyis.upper() + lakap + t_daygun + daygun,					soyis.upper() + '_' + lakap + t_daygun + daygun, soyis.upper() + '_' + lakap + '_' + t_daygun + daygun, soyis.upper() + lakap + '_' + t_daygun + daygun,
			soyis.upper() + lakap.upper() + t_daygun + daygun,			soyis.upper() + '_' + lakap.upper() + t_daygun + daygun, soyis.upper() + '_' + lakap.upper() + '_' + t_daygun + daygun, soyis.upper() + lakap.upper() + '_' + t_daygun + daygun,
			soyis.upper() + lakap.title() + t_daygun + daygun,			soyis.upper() + '_' + lakap.title() + t_daygun + daygun, soyis.upper() + '_' + lakap.title() + '_' + t_daygun + daygun, soyis.upper() + lakap.title() + '_' + t_daygun + daygun,
			soyis.title() + lakap + t_daygun + daygun,					soyis.title() + '_' + lakap + t_daygun + daygun, soyis.title() + '_' + lakap + '_' + t_daygun + daygun, soyis.title() + lakap + '_' + t_daygun + daygun,
			soyis.title() + lakap.upper() + t_daygun + daygun,			soyis.title() + '_' + lakap.upper() + t_daygun + daygun, soyis.title() + '_' + lakap.upper() + '_' + t_daygun + daygun, soyis.title() + lakap.upper() + '_' + t_daygun + daygun,
			soyis.title() + lakap.title() + t_daygun + daygun,			soyis.title() + '_' + lakap.title() + t_daygun + daygun, soyis.title() + '_' + lakap.title() + '_' + t_daygun + daygun, soyis.title() + lakap.title() + '_' + t_daygun + daygun,
			
			soyis.upper() + lakap + t_daygun + t_daygun,				soyis.upper() + '_' + lakap + t_daygun + t_daygun, soyis.upper() + '_' + lakap + '_' + t_daygun + t_daygun, soyis.upper() + lakap + '_' + t_daygun + t_daygun,
			soyis.upper() + lakap.upper() + t_daygun + t_daygun,		soyis.upper() + '_' + lakap.upper() + t_daygun + t_daygun, soyis.upper() + '_' + lakap.upper() + '_' + t_daygun + t_daygun, soyis.upper() + lakap.upper() + '_' + t_daygun + t_daygun,
			soyis.upper() + lakap.title() + t_daygun + t_daygun,		soyis.upper() + '_' + lakap.title() + t_daygun + t_daygun, soyis.upper() + '_' + lakap.title() + '_' + t_daygun + t_daygun, soyis.upper() + lakap.title() + '_' + t_daygun + t_daygun,
			soyis.title() + lakap + t_daygun + t_daygun,				soyis.title() + '_' + lakap + t_daygun + daygun, soyis.title() + '_' + lakap + '_' + t_daygun + t_daygun, soyis.title() + lakap + '_' + t_daygun + t_daygun,
			soyis.title() + lakap.upper() + t_daygun + t_daygun,		soyis.title() + '_' + lakap.upper() + t_daygun + daygun, soyis.title() + '_' + lakap.upper() + '_' + t_daygun + t_daygun, soyis.title() + lakap.upper() + '_' + t_daygun + t_daygun,
			soyis.title() + lakap.title() + t_daygun + t_daygun,		soyis.title() + '_' + lakap.title() + t_daygun + daygun, soyis.title() + '_' + lakap.title() + '_' + t_daygun + t_daygun, soyis.title() + lakap.title() + '_' + t_daygun + t_daygun,
			
			lakap.upper() + soyis + dtarihi,							lakap.upper() + '_' + soyis + dtarihi, lakap.upper() + '_' + soyis + '_' + dtarihi, lakap.upper() + soyis + '_' + dtarihi,
			lakap.upper() + soyis.upper() + dtarihi,					lakap.upper() + '_' + soyis.upper() + dtarihi, lakap.upper() + '_' + soyis.upper() + '_' + dtarihi, lakap.upper() + soyis.upper() + '_' + dtarihi,
			lakap.upper() + soyis.title() + dtarihi,					lakap.upper() + '_' + soyis.title() + dtarihi, lakap.upper() + '_' + soyis.title() + '_' + dtarihi, lakap.upper() + soyis.title() + '_' + dtarihi,
			lakap.title() + soyis + dtarihi,							lakap.title() + '_' + soyis + dtarihi, lakap.title() + '_' + soyis + '_' + dtarihi, lakap.title() + soyis + '_' + dtarihi,
			lakap.title() + soyis.upper() + dtarihi,					lakap.title() + '_' + soyis.upper() + dtarihi, lakap.title() + '_' + soyis.upper() + '_' + dtarihi, lakap.title() + soyis.upper() + '_' + dtarihi,
			lakap.title() + soyis.title() + dtarihi,					lakap.title() + '_' + soyis.title() + dtarihi, lakap.title() + '_' + soyis.title() + '_' + dtarihi, lakap.title() + soyis.title() + '_' + dtarihi,
			
			lakap.upper() + soyis + t_dtarihi,							lakap.upper() + '_' + soyis + t_dtarihi, lakap.upper() + '_' + soyis + '_' + t_dtarihi, lakap.upper() + soyis + '_' + t_dtarihi,
			lakap.upper() + soyis.upper() + t_dtarihi,					lakap.upper() + '_' + soyis.upper() + t_dtarihi, lakap.upper() + '_' + soyis.upper() + '_' + t_dtarihi, lakap.upper() + soyis.upper() + '_' + t_dtarihi,
			lakap.upper() + soyis.title() + t_dtarihi,					lakap.upper() + '_' + soyis.title() + t_dtarihi, lakap.upper() + '_' + soyis.title() + '_' + t_dtarihi, lakap.upper() + soyis.title() + '_' + t_dtarihi,
			lakap.title() + soyis + t_dtarihi,							lakap.title() + '_' + soyis + dtarihi, lakap.title() + '_' + soyis + '_' + t_dtarihi, lakap.title() + soyis + '_' + t_dtarihi,
			lakap.title() + soyis.upper() + t_dtarihi,					lakap.title() + '_' + soyis.upper() + dtarihi, lakap.title() + '_' + soyis.upper() + '_' + t_dtarihi, lakap.title() + soyis.upper() + '_' + t_dtarihi,
			lakap.title() + soyis.title() + t_dtarihi,					lakap.title() + '_' + soyis.title() + dtarihi, lakap.title() + '_' + soyis.title() + '_' + t_dtarihi, lakap.title() + soyis.title() + '_' + t_dtarihi,

			soyis.upper() + lakap + dtarihi,							soyis.upper() + '_' + lakap + dtarihi, soyis.upper() + '_' + lakap + '_' + dtarihi, soyis.upper() + lakap + '_' + dtarihi,
			soyis.upper() + lakap.upper() + dtarihi,					soyis.upper() + '_' + lakap.upper() + dtarihi, soyis.upper() + '_' + lakap.upper() + '_' + dtarihi, soyis.upper() + lakap.upper() + '_' + dtarihi,
			soyis.upper() + lakap.title() + dtarihi,					soyis.upper() + '_' + lakap.title() + dtarihi, soyis.upper() + '_' + lakap.title() + '_' + dtarihi, soyis.upper() + lakap.title() + '_' + dtarihi,
			soyis.title() + lakap + dtarihi,							soyis.title() + '_' + lakap + dtarihi, soyis.title() + '_' + lakap + '_' + dtarihi, soyis.title() + lakap + '_' + dtarihi,
			soyis.title() + lakap.upper() + dtarihi,					soyis.title() + '_' + lakap.upper() + dtarihi, soyis.title() + '_' + lakap.upper() + '_' + dtarihi, soyis.title() + lakap.upper() + '_' + dtarihi,
			soyis.title() + lakap.title() + dtarihi,					soyis.title() + '_' + lakap.title() + dtarihi, soyis.title() + '_' + lakap.title() + '_' + dtarihi, soyis.title() + lakap.title() + '_' + dtarihi,
			
			soyis.upper() + lakap + t_dtarihi,							soyis.upper() + '_' + lakap + t_dtarihi, soyis.upper() + '_' + lakap + '_' + t_dtarihi, soyis.upper() + lakap + '_' + t_dtarihi,
			soyis.upper() + lakap.upper() + t_dtarihi,					soyis.upper() + '_' + lakap.upper() + t_dtarihi, soyis.upper() + '_' + lakap.upper() + '_' + t_dtarihi, soyis.upper() + lakap.upper() + '_' + t_dtarihi,
			soyis.upper() + lakap.title() + t_dtarihi,					soyis.upper() + '_' + lakap.title() + t_dtarihi, soyis.upper() + '_' + lakap.title() + '_' + t_dtarihi, soyis.upper() + lakap.title() + '_' + t_dtarihi,
			soyis.title() + lakap + t_dtarihi,							soyis.title() + '_' + lakap + dtarihi, soyis.title() + '_' + lakap + '_' + t_dtarihi, soyis.title() + lakap + '_' + t_dtarihi,
			soyis.title() + lakap.upper() + t_dtarihi,					soyis.title() + '_' + lakap.upper() + dtarihi, soyis.title() + '_' + lakap.upper() + '_' + t_dtarihi, soyis.title() + lakap.upper() + '_' + t_dtarihi,
			soyis.title() + lakap.title() + t_dtarihi,					soyis.title() + '_' + lakap.title() + dtarihi, soyis.title() + '_' + lakap.title() + '_' + t_dtarihi, soyis.title() + lakap.title() + '_' + t_dtarihi,]

	if soru2 != '5' : 
		lakapli_takim_sifreleri = [lakap + takim,
						lakap + ktakim,
						
						lakap + ad + takim,
						lakap + soyis + takim,
						soyis + lakap + takim,
						
						lakap + ad + ktakim,
						lakap + soyis + ktakim,
						soyis + lakap + ktakim,
						
						lakap.upper() + takim,
						lakap.upper() + ktakim,
						
						lakap.upper() + ad + takim,
						lakap.upper() + soyis + takim,
						soyis.upper() + lakap + takim,
						
						lakap.upper() + ad + ktakim,
						lakap.upper() + soyis + ktakim,
						soyis.upper() + lakap + ktakim,
						
						lakap + takim.upper(),
						lakap + ktakim.upper(),
						
						lakap + ad.upper() + takim,
						lakap + soyis.upper() + takim,
						soyis + lakap.upper() + takim,
						
						lakap + ad.upper() + ktakim,
						lakap + soyis.upper() + ktakim,
						soyis + lakap.upper() + ktakim,
						
						lakap + ad + takim.upper(),
						lakap + soyis + takim.upper(),
						soyis + lakap + takim.upper(),
						
						lakap + ad + ktakim.upper(),
						lakap + soyis + ktakim.upper(),
						soyis + lakap + ktakim.upper(),
						
						lakap.upper() + takim.upper(),
						lakap.upper() + ktakim.upper(),
						
						lakap.upper() + ad.upper() + takim,
						lakap.upper() + soyis.upper() + takim,
						soyis.title() + lakap.upper() + takim,
						
						lakap.upper() + ad.upper() + ktakim,
						lakap.upper() + soyis.upper() + ktakim,
						soyis.title() + lakap.upper() + ktakim,
						
						lakap.upper() + ad + takim.upper(),
						lakap.upper() + soyis + takim.upper(),
						soyis.upper() + lakap + takim.upper(),
						
						lakap.upper() + ad + ktakim.upper(),
						lakap.upper() + soyis + ktakim.upper(),
						soyis.upper() + lakap + ktakim.upper(),
						
						lakap + ad.upper() + takim.upper(),
						lakap + soyis.upper() + takim.upper(),
						soyis + lakap.upper() + takim.upper(),
						
						lakap + ad.upper() + ktakim.upper(),
						lakap + soyis.upper() + ktakim.upper(),
						soyis + lakap.upper() + ktakim.upper(),
						
						lakap.upper() + ad.upper() + takim.upper(),
						lakap.upper() + soyis.upper() + takim.upper(),
						soyis.title() + lakap.upper() + takim.upper(),
						
						lakap.upper() + ad.upper() + ktakim.upper(),
						lakap.upper() + soyis.upper() + ktakim.upper(),
						soyis.title() + lakap.upper() + ktakim.upper(),
						
						lakap.title() + takim,
						lakap.title() + ktakim,
						
						lakap.title() + ad + takim,
						lakap.title() + soyis + takim,
						soyis.title() + lakap + takim,
						
						lakap.title() + ad + ktakim,
						lakap.title() + soyis + ktakim,
						soyis.title() + lakap + ktakim,
						
						lakap + takim.title(),
						lakap + ktakim.title(),
						
						lakap + ad.title() + takim,
						lakap + soyis.title() + takim,
						soyis + lakap.title() + takim,
						
						lakap + ad.title() + ktakim,
						lakap + soyis.title() + ktakim,
						soyis + lakap.title() + ktakim,
						
						lakap + ad + takim.title(),
						lakap + soyis + takim.title(),
						soyis + lakap + takim.title(),
						
						lakap + ad + ktakim.title(),
						lakap + soyis + ktakim.title(),
						soyis + lakap + ktakim.title(),
						
						lakap.title() + takim.title(),
						lakap.title() + ktakim.title(),
						
						lakap.title() + ad.title() + takim,
						lakap.title() + soyis.title() + takim,
						soyis.title() + lakap.title() + takim,
						
						lakap.title() + ad.title() + ktakim,
						lakap.title() + soyis.title() + ktakim,
						soyis.title() + lakap.title() + ktakim,
						
						lakap.title() + ad + takim.title(),
						lakap.title() + soyis + takim.title(),
						soyis.title() + lakap + takim.title(),
						
						lakap.title() + ad + ktakim.title(),
						lakap.title() + soyis + ktakim.title(),
						soyis.title() + lakap + ktakim.title(),
						
						lakap + ad.title() + takim.title(),
						lakap + soyis.title() + takim.title(),
						soyis + lakap.title() + takim.title(),
						
						lakap + ad.title() + ktakim.title(),
						lakap + soyis.title() + ktakim.title(),
						soyis + lakap.title() + ktakim.title(),
						
						lakap.title() + ad.title() + takim.title(),
						lakap.title() + soyis.title() + takim.title(),
						soyis.title() + lakap.title() + takim.title(),
						
						lakap.title() + ad.title() + ktakim.title(),
						lakap.title() + soyis.title() + ktakim.title(),
						soyis.title() + lakap.title() + ktakim.title(),
						
						lakap.upper() + takim.title(),
						lakap.upper() + ktakim.title(),
						
						lakap.upper() + ad.title() + takim,
						lakap.upper() + soyis.title() + takim,
						soyis.title() + lakap.title() + takim,
						
						lakap.upper() + ad.title() + ktakim,
						lakap.upper() + soyis.title() + ktakim,
						soyis.title() + lakap.title() + ktakim,
						
						lakap.upper() + ad + takim.title(),
						lakap.upper() + soyis + takim.title(),
						soyis.upper() + lakap + takim.title(),
						
						lakap.upper() + ad + ktakim.title(),
						lakap.upper() + soyis + ktakim.title(),
						soyis.upper() + lakap + ktakim.title(),
						
						lakap + ad.upper() + takim.title(),
						lakap + soyis.upper() + takim.title(),
						soyis + lakap.upper() + takim.title(),
						
						lakap + ad.upper() + ktakim.title(),
						lakap + soyis.upper() + ktakim.title(),
						soyis + lakap.upper() + ktakim.title(),
						
						lakap.title() + takim.upper(),
						lakap.title() + ktakim.upper(),
						
						lakap.title() + ad.upper() + takim,
						lakap.title() + soyis.upper() + takim,
						soyis.title() + lakap.upper() + takim,
						
						lakap.title() + ad.upper() + ktakim,
						lakap.title() + soyis.upper() + ktakim,
						soyis.title() + lakap.upper() + ktakim,
						
						lakap.title() + ad + takim.upper(),
						lakap.title() + soyis + takim.upper(),
						soyis.title() + lakap + takim.upper(),
						
						lakap.title() + ad + ktakim.upper(),
						lakap.title() + soyis + ktakim.upper(),
						soyis.title() + lakap + ktakim.upper(),
						
						lakap + ad.title() + takim.upper(),
						lakap + soyis.title() + takim.upper(),
						soyis + lakap.title() + takim.upper(),
						
						lakap + ad.title() + ktakim.upper(),
						lakap + soyis.title() + ktakim.upper(),
						soyis + lakap.title() + ktakim.upper(),
						
						lakap.upper() + ad.upper() + takim.title(),
						lakap.upper() + soyis.upper() + takim.title(),
						soyis.title() + lakap.upper() + takim.title(),
						
						lakap.upper() + ad.upper() + ktakim.title(),
						lakap.upper() + soyis.upper() + ktakim.title(),
						soyis.title() + lakap.upper() + ktakim.title(),
						
						lakap.upper() + ad.title() + takim.upper(),
						lakap.upper() + soyis.title() + takim.upper(),
						soyis.title() + lakap.title() + takim.upper(),
						
						lakap.upper() + ad.title() + ktakim.upper(),
						lakap.upper() + soyis.title() + ktakim.upper(),
						soyis.title() + lakap.title() + ktakim.upper(),
					
						lakap.upper() + ad.title() + takim.title(),
						lakap.upper() + soyis.title() + takim.title(),
						soyis.title() + lakap.title() + takim.title(),
						
						lakap.upper() + ad.title() + ktakim.title(),
						lakap.upper() + soyis.title() + ktakim.title(),
						soyis.title() + lakap.title() + ktakim.title(),
						
						lakap.title() + ad.upper() + takim.title(),
						lakap.title() + soyis.upper() + takim.title(),
						soyis.title() + lakap.upper() + takim.title(),
						
						lakap.title() + ad.upper() + ktakim.title(),
						lakap.title() + soyis.upper() + ktakim.title(),
						soyis.title() + lakap.upper() + ktakim.title(),
						
						lakap.title() + ad.title() + takim.upper(),
						lakap.title() + soyis.title() + takim.upper(),
						soyis.title() + lakap.title() + takim.upper(),
						
						lakap.title() + ad.title() + ktakim.upper(),
						lakap.title() + soyis.title() + ktakim.upper(),
						soyis.title() + lakap.title() + ktakim.upper(),
						
						lakap + takim + kurulus,
						lakap + ktakim + kurulus,
						
						lakap + ad + takim + kurulus,
						lakap + soyis + takim + kurulus,
						soyis + lakap + takim + kurulus,
						
						lakap + ad + ktakim + kurulus,
						lakap + soyis + ktakim + kurulus,
						soyis + lakap + ktakim + kurulus,
						
						lakap.upper() + takim + kurulus,
						lakap.upper() + ktakim + kurulus,
						
						lakap.upper() + ad + takim + kurulus,
						lakap.upper() + soyis + takim + kurulus,
						soyis.upper() + lakap + takim + kurulus,
						
						lakap.upper() + ad + ktakim + kurulus,
						lakap.upper() + soyis + ktakim + kurulus,
						soyis.upper() + lakap + ktakim + kurulus,
						
						lakap + takim.upper() + kurulus,
						lakap + ktakim.upper() + kurulus,
						
						lakap + ad.upper() + takim + kurulus,
						lakap + soyis.upper() + takim + kurulus,
						soyis + lakap.upper() + takim + kurulus,
						
						lakap + ad.upper() + ktakim + kurulus,
						lakap + soyis.upper() + ktakim + kurulus,
						soyis + lakap.upper() + ktakim + kurulus,
						
						lakap + ad + takim.upper() + kurulus,
						lakap + soyis + takim.upper() + kurulus,
						soyis + lakap + takim.upper() + kurulus,
						
						lakap + ad + ktakim.upper() + kurulus,
						lakap + soyis + ktakim.upper() + kurulus,
						soyis + lakap + ktakim.upper() + kurulus,
						
						lakap.upper() + takim.upper() + kurulus,
						lakap.upper() + ktakim.upper() + kurulus,
						
						lakap.upper() + ad.upper() + takim + kurulus,
						lakap.upper() + soyis.upper() + takim + kurulus,
						soyis.title() + lakap.upper() + takim + kurulus,
						
						lakap.upper() + ad.upper() + ktakim + kurulus,
						lakap.upper() + soyis.upper() + ktakim + kurulus,
						soyis.title() + lakap.upper() + ktakim + kurulus,
						
						lakap.upper() + ad + takim.upper() + kurulus,
						lakap.upper() + soyis + takim.upper() + kurulus,
						soyis.upper() + lakap + takim.upper() + kurulus,
						
						lakap.upper() + ad + ktakim.upper() + kurulus,
						lakap.upper() + soyis + ktakim.upper() + kurulus,
						soyis.upper() + lakap + ktakim.upper() + kurulus,
						
						lakap + ad.upper() + takim.upper() + kurulus,
						lakap + soyis.upper() + takim.upper() + kurulus,
						soyis + lakap.upper() + takim.upper() + kurulus,
						
						lakap + ad.upper() + ktakim.upper() + kurulus,
						lakap + soyis.upper() + ktakim.upper() + kurulus,
						soyis + lakap.upper() + ktakim.upper() + kurulus,
						
						lakap.upper() + ad.upper() + takim.upper() + kurulus,
						lakap.upper() + soyis.upper() + takim.upper() + kurulus,
						soyis.title() + lakap.upper() + takim.upper() + kurulus,
						
						lakap.upper() + ad.upper() + ktakim.upper() + kurulus,
						lakap.upper() + soyis.upper() + ktakim.upper() + kurulus,
						soyis.title() + lakap.upper() + ktakim.upper() + kurulus,
						
						lakap.title() + takim + kurulus,
						lakap.title() + ktakim + kurulus,
						
						lakap.title() + ad + takim + kurulus,
						lakap.title() + soyis + takim + kurulus,
						soyis.title() + lakap + takim + kurulus,
						
						lakap.title() + ad + ktakim + kurulus,
						lakap.title() + soyis + ktakim + kurulus,
						soyis.title() + lakap + ktakim + kurulus,
						
						lakap + takim.title() + kurulus,
						lakap + ktakim.title() + kurulus,
						
						lakap + ad.title() + takim + kurulus,
						lakap + soyis.title() + takim + kurulus,
						soyis + lakap.title() + takim + kurulus,
						
						lakap + ad.title() + ktakim + kurulus,
						lakap + soyis.title() + ktakim + kurulus,
						soyis + lakap.title() + ktakim + kurulus,
						
						lakap + ad + takim.title() + kurulus,
						lakap + soyis + takim.title() + kurulus,
						soyis + lakap + takim.title() + kurulus,
						
						lakap + ad + ktakim.title() + kurulus,
						lakap + soyis + ktakim.title() + kurulus,
						soyis + lakap + ktakim.title() + kurulus,
						
						lakap.title() + takim.title() + kurulus,
						lakap.title() + ktakim.title() + kurulus,
						
						lakap.title() + ad.title() + takim + kurulus,
						lakap.title() + soyis.title() + takim + kurulus,
						soyis.title() + lakap.title() + takim + kurulus,
						
						lakap.title() + ad.title() + ktakim + kurulus,
						lakap.title() + soyis.title() + ktakim + kurulus,
						soyis.title() + lakap.title() + ktakim + kurulus,
						
						lakap.title() + ad + takim.title() + kurulus,
						lakap.title() + soyis + takim.title() + kurulus,
						soyis.title() + lakap + takim.title() + kurulus,
						
						lakap.title() + ad + ktakim.title() + kurulus,
						lakap.title() + soyis + ktakim.title() + kurulus,
						soyis.title() + lakap + ktakim.title() + kurulus,
						
						lakap + ad.title() + takim.title() + kurulus,
						lakap + soyis.title() + takim.title() + kurulus,
						
						lakap + ad.title() + ktakim.title() + kurulus,
						lakap + soyis.title() + ktakim.title() + kurulus,
						soyis + lakap.title() + ktakim.title() + kurulus,
						
						lakap.title() + ad.title() + takim.title() + kurulus,
						lakap.title() + soyis.title() + takim.title() + kurulus,
						soyis.title() + lakap.title() + takim.title() + kurulus,
						
						lakap.title() + ad.title() + ktakim.title() + kurulus,
						lakap.title() + soyis.title() + ktakim.title() + kurulus,
						soyis.title() + lakap.title() + ktakim.title() + kurulus,
						
						lakap.upper() + takim.title() + kurulus,
						lakap.upper() + ktakim.title() + kurulus,
						
						lakap.upper() + ad.title() + takim + kurulus,
						lakap.upper() + soyis.title() + takim + kurulus,
						soyis.title() + lakap.title() + takim + kurulus,
						
						lakap.upper() + ad.title() + ktakim + kurulus,
						lakap.upper() + soyis.title() + ktakim + kurulus,
						soyis.title() + lakap.title() + ktakim + kurulus,
						
						lakap.upper() + ad + takim.title() + kurulus,
						lakap.upper() + soyis + takim.title() + kurulus,
						soyis.upper() + lakap + takim.title() + kurulus,
						
						lakap.upper() + ad + ktakim.title() + kurulus,
						lakap.upper() + soyis + ktakim.title() + kurulus,
						soyis.upper() + lakap + ktakim.title() + kurulus,
						
						lakap + ad.upper() + takim.title() + kurulus,
						lakap + soyis.upper() + takim.title() + kurulus,
						soyis + lakap.upper() + takim.title() + kurulus,
						
						lakap + ad.upper() + ktakim.title() + kurulus,
						lakap + soyis.upper() + ktakim.title() + kurulus,
						soyis + lakap.upper() + ktakim.title() + kurulus,
						
						lakap.title() + takim.upper() + kurulus,
						lakap.title() + ktakim.upper() + kurulus,
						
						lakap.title() + ad.upper() + takim + kurulus,
						lakap.title() + soyis.upper() + takim + kurulus,
						soyis.title() + lakap.upper() + takim + kurulus,
						
						lakap.title() + ad.upper() + ktakim + kurulus,
						lakap.title() + soyis.upper() + ktakim + kurulus,
						soyis.title() + lakap.upper() + ktakim + kurulus,
						
						lakap.title() + ad + takim.upper() + kurulus,
						lakap.title() + soyis + takim.upper() + kurulus,
						soyis.title() + lakap + takim.upper() + kurulus,
						
						lakap.title() + ad + ktakim.upper() + kurulus,
						lakap.title() + soyis + ktakim.upper() + kurulus,
						soyis.title() + lakap + ktakim.upper() + kurulus,
						
						lakap + ad.title() + takim.upper() + kurulus,
						lakap + soyis.title() + takim.upper() + kurulus,
						soyis + lakap.title() + takim.upper() + kurulus,
						
						lakap + ad.title() + ktakim.upper() + kurulus,
						lakap + soyis.title() + ktakim.upper() + kurulus,
						soyis + lakap.title() + ktakim.upper() + kurulus,
						
						lakap.upper() + ad.upper() + takim.title() + kurulus,
						lakap.upper() + soyis.upper() + takim.title() + kurulus,
						soyis.title() + lakap.upper() + takim.title() + kurulus,
						
						lakap.upper() + ad.upper() + ktakim.title() + kurulus,
						lakap.upper() + soyis.upper() + ktakim.title() + kurulus,
						soyis.title() + lakap.upper() + ktakim.title() + kurulus,
						
						lakap.upper() + ad.title() + takim.upper() + kurulus,
						lakap.upper() + soyis.title() + takim.upper() + kurulus,
						soyis.title() + lakap.title() + takim.upper() + kurulus,
						
						lakap.upper() + ad.title() + ktakim.upper() + kurulus,
						lakap.upper() + soyis.title() + ktakim.upper() + kurulus,
						soyis.title() + lakap.title() + ktakim.upper() + kurulus,
						
						lakap.upper() + ad.title() + takim.title() + kurulus,
						lakap.upper() + soyis.title() + takim.title() + kurulus,
						soyis.title() + lakap.title() + takim.title() + kurulus,
						
						lakap.upper() + ad.title() + ktakim.title() + kurulus,
						lakap.upper() + soyis.title() + ktakim.title() + kurulus,
						soyis.title() + lakap.title() + ktakim.title() + kurulus,
						
						lakap.title() + ad.upper() + takim.title() + kurulus,
						lakap.title() + soyis.upper() + takim.title() + kurulus,
						soyis.title() + lakap.upper() + takim.title() + kurulus,
						
						lakap.title() + ad.upper() + ktakim.title() + kurulus,
						lakap.title() + soyis.upper() + ktakim.title() + kurulus,
						soyis.title() + lakap.upper() + ktakim.title() + kurulus,
							
						lakap.title() + ad.title() + takim.upper() + kurulus,
						lakap.title() + soyis.title() + takim.upper() + kurulus,
						soyis.title() + lakap.title() + takim.upper() + kurulus,
						
						lakap.title() + ad.title() + ktakim.upper() + kurulus,
						lakap.title() + soyis.title() + ktakim.upper() + kurulus,
						soyis.title() + lakap.title() + ktakim.upper() + kurulus,
						
						lakap.title() + ad.title() + takim.title() + kurulus,
						lakap.title() + soyis.title() + takim.title() + kurulus,
						soyis.title() + lakap.title() + takim.title() + kurulus,
						
						lakap + takim + dyili,
						lakap + ktakim + dyili,
						
						lakap + ad + takim + dyili,
						lakap + soyis + takim + dyili,
						soyis + lakap + takim + dyili,
						
						lakap + ad + ktakim + dyili,
						lakap + soyis + ktakim + dyili,
						soyis + lakap + ktakim + dyili,
						
						lakap.upper() + takim + dyili,
						lakap.upper() + ktakim + dyili,
						
						lakap.upper() + ad + takim + dyili,
						lakap.upper() + soyis + takim + dyili,
						soyis.upper() + lakap + takim + dyili,
						
						lakap.upper() + ad + ktakim + dyili,
						lakap.upper() + soyis + ktakim + dyili,
						soyis.upper() + lakap + ktakim + dyili,
						
						lakap + takim.upper() + dyili,
						lakap + ktakim.upper() + dyili,
						
						lakap + ad.upper() + takim + dyili,
						lakap + soyis.upper() + takim + dyili,
						soyis + lakap.upper() + takim + dyili,
						
						lakap + ad.upper() + ktakim + dyili,
						lakap + soyis.upper() + ktakim + dyili,
						soyis + lakap.upper() + ktakim + dyili,
						
						lakap + ad + takim.upper() + dyili,
						lakap + soyis + takim.upper() + dyili,
						soyis + lakap + takim.upper() + dyili,
						
						lakap + ad + ktakim.upper() + dyili,
						lakap + soyis + ktakim.upper() + dyili,
						soyis + lakap + ktakim.upper() + dyili,
						
						lakap.upper() + takim.upper() + dyili,
						soyis.upper() + takim.upper() + dyili,
						lakap.upper() + ktakim.upper() + dyili,
						
						lakap.upper() + ad.upper() + takim + dyili,
						lakap.upper() + soyis.upper() + takim + dyili,
						soyis.title() + lakap.upper() + takim + dyili,
						
						lakap.upper() + ad.upper() + ktakim + dyili,
						lakap.upper() + soyis.upper() + ktakim + dyili,
						soyis.title() + lakap.upper() + ktakim + dyili,
						
						lakap.upper() + ad + takim.upper() + dyili,
						lakap.upper() + soyis + takim.upper() + dyili,
						soyis.upper() + lakap + takim.upper() + dyili,
						
						lakap.upper() + ad + ktakim.upper() + dyili,
						lakap.upper() + soyis + ktakim.upper() + dyili,
						soyis.upper() + lakap + ktakim.upper() + dyili,
						
						lakap + ad.upper() + takim.upper() + dyili,
						lakap + soyis.upper() + takim.upper() + dyili,
						soyis + lakap.upper() + takim.upper() + dyili,
						
						lakap + ad.upper() + ktakim.upper() + dyili,
						lakap + soyis.upper() + ktakim.upper() + dyili,
						soyis + lakap.upper() + ktakim.upper() + dyili,
						
						lakap.upper() + ad.upper() + takim.upper() + dyili,
						lakap.upper() + soyis.upper() + takim.upper() + dyili,
						soyis.title() + lakap.upper() + takim.upper() + dyili,
						
						lakap.upper() + ad.upper() + ktakim.upper() + dyili,
						lakap.upper() + soyis.upper() + ktakim.upper() + dyili,
						soyis.title() + lakap.upper() + ktakim.upper() + dyili,
						
						lakap.title() + takim + dyili,
						lakap.title() + ktakim + dyili,
						
						lakap.title() + ad + takim + dyili,
						lakap.title() + soyis + takim + dyili,
						soyis.title() + lakap + takim + dyili,
						
						lakap.title() + ad + ktakim + dyili,
						lakap.title() + soyis + ktakim + dyili,
						soyis.title() + lakap + ktakim + dyili,
						
						lakap + takim.title() + dyili,
						lakap + ktakim.title() + dyili,
						
						lakap + ad.title() + takim + dyili,
						lakap + soyis.title() + takim + dyili,
						soyis + lakap.title() + takim + dyili,
						
						lakap + ad.title() + ktakim + dyili,
						lakap + soyis.title() + ktakim + dyili,
						soyis + lakap.title() + ktakim + dyili,
						
						lakap + ad + takim.title() + dyili,
						lakap + soyis + takim.title() + dyili,
						soyis + lakap + takim.title() + dyili,
						
						lakap + ad + ktakim.title() + dyili,
						lakap + soyis + ktakim.title() + dyili,
						soyis + lakap + ktakim.title() + dyili,
						
						lakap.title() + takim.title() + dyili,
						lakap.title() + ktakim.title() + dyili,
						
						lakap.title() + ad.title() + takim + dyili,
						lakap.title() + soyis.title() + takim + dyili,
						soyis.title() + lakap.title() + takim + dyili,
						
						lakap.title() + ad.title() + ktakim + dyili,
						lakap.title() + soyis.title() + ktakim + dyili,
						soyis.title() + lakap.title() + ktakim + dyili,
						
						lakap.title() + ad + takim.title() + dyili,
						lakap.title() + soyis + takim.title() + dyili,
						soyis.title() + lakap + takim.title() + dyili,
						
						lakap.title() + ad + ktakim.title() + dyili,
						lakap.title() + soyis + ktakim.title() + dyili,
						soyis.title() + lakap + ktakim.title() + dyili,
						
						lakap + ad.title() + takim.title() + dyili,
						lakap + soyis.title() + takim.title() + dyili,
						soyis + lakap.title() + takim.title() + dyili,
						
						lakap + ad.title() + ktakim.title() + dyili,
						lakap + soyis.title() + ktakim.title() + dyili,
						soyis + lakap.title() + ktakim.title() + dyili,
						
						lakap.title() + ad.title() + takim.title() + dyili,
						lakap.title() + soyis.title() + takim.title() + dyili,
						soyis.title() + lakap.title() + takim.title() + dyili,
						
						lakap.title() + ad.title() + ktakim.title() + dyili,
						lakap.title() + soyis.title() + ktakim.title() + dyili,
						soyis.title() + lakap.title() + ktakim.title() + dyili,
						
						lakap.upper() + takim.title() + dyili,
						lakap.upper() + ktakim.title() + dyili,
						
						lakap.upper() + ad.title() + takim + dyili,
						lakap.upper() + soyis.title() + takim + dyili,
						soyis.title() + lakap.title() + takim + dyili,
						
						lakap.upper() + ad.title() + ktakim + dyili,
						lakap.upper() + soyis.title() + ktakim + dyili,
						soyis.title() + lakap.title() + ktakim + dyili,
						
						lakap.upper() + ad + takim.title() + dyili,
						lakap.upper() + soyis + takim.title() + dyili,
						soyis.upper() + lakap + takim.title() + dyili,
						
						lakap.upper() + ad + ktakim.title() + dyili,
						lakap.upper() + soyis + ktakim.title() + dyili,
						soyis.upper() + lakap + ktakim.title() + dyili,
						
						lakap + ad.upper() + takim.title() + dyili,
						lakap + soyis.upper() + takim.title() + dyili,
						soyis + lakap.upper() + takim.title() + dyili,
						
						lakap + ad.upper() + ktakim.title() + dyili,
						lakap + soyis.upper() + ktakim.title() + dyili,
						soyis + lakap.upper() + ktakim.title() + dyili,
						
						lakap.title() + takim.upper() + dyili,
						soyis.title() + takim.upper() + dyili,
						lakap.title() + ktakim.upper() + dyili,
						
						lakap.title() + ad.upper() + takim + dyili,
						lakap.title() + soyis.upper() + takim + dyili,
						soyis.title() + lakap.upper() + takim + dyili,
						
						lakap.title() + ad.upper() + ktakim + dyili,
						lakap.title() + soyis.upper() + ktakim + dyili,
						soyis.title() + lakap.upper() + ktakim + dyili,
						
						lakap.title() + ad + takim.upper() + dyili,
						soyis.title() + lakap + takim.upper() + dyili,
						
						lakap.title() + ad + ktakim.upper() + dyili,
						lakap.title() + soyis + ktakim.upper() + dyili,
						soyis.title() + lakap + ktakim.upper() + dyili,
						
						lakap + ad.title() + takim.upper() + dyili,
						lakap + soyis.title() + takim.upper() + dyili,
						soyis + lakap.title() + takim.upper() + dyili,
						
						lakap + ad.title() + ktakim.upper() + dyili,
						lakap + soyis.title() + ktakim.upper() + dyili,
						soyis + lakap.title() + ktakim.upper() + dyili,
						
						lakap.upper() + ad.upper() + takim.title() + dyili,
						lakap.upper() + soyis.upper() + takim.title() + dyili,
						soyis.title() + lakap.upper() + takim.title() + dyili,
						
						lakap.upper() + ad.upper() + ktakim.title() + dyili,
						lakap.upper() + soyis.upper() + ktakim.title() + dyili,
						soyis.title() + lakap.upper() + ktakim.title() + dyili,
						
						lakap.upper() + ad.title() + takim.upper() + dyili,
						lakap.upper() + soyis.title() + takim.upper() + dyili,
						soyis.title() + lakap.title() + takim.upper() + dyili,
						
						lakap.upper() + ad.title() + ktakim.upper() + dyili,
						lakap.upper() + soyis.title() + ktakim.upper() + dyili,
						soyis.title() + lakap.title() + ktakim.upper() + dyili,
						
						lakap.upper() + ad.title() + takim.title() + dyili,
						lakap.upper() + soyis.title() + takim.title() + dyili,
						soyis.title() + lakap.title() + takim.title() + dyili,
						
						lakap.upper() + ad.title() + ktakim.title() + dyili,
						lakap.upper() + soyis.title() + ktakim.title() + dyili,
						soyis.title() + lakap.title() + ktakim.title() + dyili,
						
						lakap.title() + ad.upper() + takim.title() + dyili,
						lakap.title() + soyis.upper() + takim.title() + dyili,
						soyis.title() + lakap.upper() + takim.title() + dyili,
						
						lakap.title() + ad.upper() + ktakim.title() + dyili,
						lakap.title() + soyis.upper() + ktakim.title() + dyili,
						soyis.title() + lakap.upper() + ktakim.title() + dyili,
						
						lakap.title() + ad.title() + takim.upper() + dyili,
						lakap.title() + soyis.title() + takim.upper() + dyili,
						soyis.title() + lakap.title() + takim.upper() + dyili,
						
						lakap.title() + ad.title() + ktakim.upper() + dyili,
						lakap.title() + soyis.title() + ktakim.upper() + dyili,
						soyis.title() + lakap.title() + ktakim.upper() + dyili,
						
						lakap + takim + pkodu,
						lakap + ktakim + pkodu,
						
						lakap + ad + takim + pkodu,
						lakap + soyis + takim + pkodu,
						soyis + lakap + takim + pkodu,
						
						lakap + ad + ktakim + pkodu,
						lakap + soyis + ktakim + pkodu,
						soyis + lakap + ktakim + pkodu,
						
						lakap.upper() + takim + pkodu,
						lakap.upper() + ktakim + pkodu,
						
						lakap.upper() + ad + takim + pkodu,
						lakap.upper() + soyis + takim + pkodu,
						
						soyis.upper() + lakap + takim + pkodu,
						
						lakap.upper() + ad + ktakim + pkodu,
						lakap.upper() + soyis + ktakim + pkodu,
						soyis.upper() + lakap + ktakim + pkodu,
						
						lakap + takim.upper() + pkodu,
						lakap + ktakim.upper() + pkodu,
						
						lakap + ad.upper() + takim + pkodu,
						lakap + soyis.upper() + takim + pkodu,
						soyis + lakap.upper() + takim + pkodu,
						
						lakap + ad.upper() + ktakim + pkodu,
						lakap + soyis.upper() + ktakim + pkodu,
						soyis + lakap.upper() + ktakim + pkodu,
						
						lakap + ad + takim.upper() + pkodu,
						lakap + soyis + takim.upper() + pkodu,
						soyis + lakap + takim.upper() + pkodu,
						
						lakap + ad + ktakim.upper() + pkodu,
						lakap + soyis + ktakim.upper() + pkodu,
						soyis + lakap + ktakim.upper() + pkodu,
						
						lakap.upper() + takim.upper() + pkodu,
						lakap.upper() + ktakim.upper() + pkodu,
						
						lakap.upper() + ad.upper() + takim + pkodu,
						lakap.upper() + soyis.upper() + takim + pkodu,
						soyis.title() + lakap.upper() + takim + pkodu,
						
						lakap.upper() + ad.upper() + ktakim + pkodu,
						lakap.upper() + soyis.upper() + ktakim + pkodu,
						soyis.title() + lakap.upper() + ktakim + pkodu,
						
						lakap.upper() + ad + takim.upper() + pkodu,
						lakap.upper() + soyis + takim.upper() + pkodu,
						soyis.upper() + lakap + takim.upper() + pkodu,
						
						lakap.upper() + ad + ktakim.upper() + pkodu,
						lakap.upper() + soyis + ktakim.upper() + pkodu,
						soyis.upper() + lakap + ktakim.upper() + pkodu,
						
						lakap + ad.upper() + takim.upper() + pkodu,
						lakap + soyis.upper() + takim.upper() + pkodu,
						soyis + lakap.upper() + takim.upper() + pkodu,
						
						lakap + ad.upper() + ktakim.upper() + pkodu,
						lakap + soyis.upper() + ktakim.upper() + pkodu,
						soyis + lakap.upper() + ktakim.upper() + pkodu,
						
						lakap.upper() + ad.upper() + takim.upper() + pkodu,
						lakap.upper() + soyis.upper() + takim.upper() + pkodu,
						soyis.title() + lakap.upper() + takim.upper() + pkodu,
						
						lakap.upper() + ad.upper() + ktakim.upper() + pkodu,
						lakap.upper() + soyis.upper() + ktakim.upper() + pkodu,
						soyis.title() + lakap.upper() + ktakim.upper() + pkodu,
						
						lakap.title() + takim + pkodu,
						lakap.title() + ktakim + pkodu,
						
						lakap.title() + ad + takim + pkodu,
						lakap.title() + soyis + takim + pkodu,
						soyis.title() + lakap + takim + pkodu,
						
						lakap.title() + ad + ktakim + pkodu,
						lakap.title() + soyis + ktakim + pkodu,
						soyis.title() + lakap + ktakim + pkodu,
						
						lakap + takim.title() + pkodu,
						lakap + ktakim.title() + pkodu,
						
						lakap + ad.title() + takim + pkodu,
						lakap + soyis.title() + takim + pkodu,
						soyis + lakap.title() + takim + pkodu,
						
						lakap + ad.title() + ktakim + pkodu,
						lakap + soyis.title() + ktakim + pkodu,
						soyis + lakap.title() + ktakim + pkodu,
						
						lakap + ad + takim.title() + pkodu,
						lakap + soyis + takim.title() + pkodu,
						soyis + lakap + takim.title() + pkodu,
						
						lakap + ad + ktakim.title() + pkodu,
						lakap + soyis + ktakim.title() + pkodu,
						soyis + lakap + ktakim.title() + pkodu,
						
						lakap.title() + takim.title() + pkodu,
						lakap.title() + ktakim.title() + pkodu,
						
						lakap.title() + ad.title() + takim + pkodu,
						lakap.title() + soyis.title() + takim + pkodu,
						soyis.title() + lakap.title() + takim + pkodu,
						
						lakap.title() + ad.title() + ktakim + pkodu,
						lakap.title() + soyis.title() + ktakim + pkodu,
						soyis.title() + lakap.title() + ktakim + pkodu,
						
						lakap.title() + ad + takim.title() + pkodu,
						lakap.title() + soyis + takim.title() + pkodu,
						soyis.title() + lakap + takim.title() + pkodu,
						
						lakap.title() + ad + ktakim.title() + pkodu,
						lakap.title() + soyis + ktakim.title() + pkodu,
						soyis.title() + lakap + ktakim.title() + pkodu,
						
						lakap + ad.title() + takim.title() + pkodu,
						lakap + soyis.title() + takim.title() + pkodu,
						soyis + lakap.title() + takim.title() + pkodu,
						
						lakap + ad.title() + ktakim.title() + pkodu,
						lakap + soyis.title() + ktakim.title() + pkodu,
						soyis + lakap.title() + ktakim.title() + pkodu,
						
						lakap.title() + ad.title() + takim.title() + pkodu,
						lakap.title() + soyis.title() + takim.title() + pkodu,
						soyis.title() + lakap.title() + takim.title() + pkodu,
						
						lakap.title() + ad.title() + ktakim.title() + pkodu,
						lakap.title() + soyis.title() + ktakim.title() + pkodu,
						soyis.title() + lakap.title() + ktakim.title() + pkodu,
						
						lakap.upper() + takim.title() + pkodu,
						lakap.upper() + ktakim.title() + pkodu,
						
						lakap.upper() + ad.title() + takim + pkodu,
						lakap.upper() + soyis.title() + takim + pkodu,
						soyis.title() + lakap.title() + takim + pkodu,
						
						lakap.upper() + ad.title() + ktakim + pkodu,
						lakap.upper() + soyis.title() + ktakim + pkodu,
						soyis.title() + lakap.title() + ktakim + pkodu,
						
						lakap.upper() + ad + takim.title() + pkodu,
						lakap.upper() + soyis + takim.title() + pkodu,
						soyis.upper() + lakap + takim.title() + pkodu,
						
						lakap.upper() + ad + ktakim.title() + pkodu,
						lakap.upper() + soyis + ktakim.title() + pkodu,
						soyis.upper() + lakap + ktakim.title() + pkodu,
						
						lakap + ad.upper() + takim.title() + pkodu,
						lakap + soyis.upper() + takim.title() + pkodu,
						soyis + lakap.upper() + takim.title() + pkodu,
						
						lakap + ad.upper() + ktakim.title() + pkodu,
						lakap + soyis.upper() + ktakim.title() + pkodu,
						soyis + lakap.upper() + ktakim.title() + pkodu,
						
						lakap.title() + takim.upper() + pkodu,
						lakap.title() + ktakim.upper() + pkodu,
						
						lakap.title() + ad.upper() + takim + pkodu,
						lakap.title() + soyis.upper() + takim + pkodu,
						soyis.title() + lakap.upper() + takim + pkodu,
						
						lakap.title() + ad.upper() + ktakim + pkodu,
						lakap.title() + soyis.upper() + ktakim + pkodu,
						soyis.title() + lakap.upper() + ktakim + pkodu,
						
						lakap.title() + ad + takim.upper() + pkodu,
						lakap.title() + soyis + takim.upper() + pkodu,
						soyis.title() + lakap + takim.upper() + pkodu,
						
						lakap.title() + ad + ktakim.upper() + pkodu,
						lakap.title() + soyis + ktakim.upper() + pkodu,
						soyis.title() + lakap + ktakim.upper() + pkodu,
						
						lakap + ad.title() + takim.upper() + pkodu,
						lakap + soyis.title() + takim.upper() + pkodu,
						soyis + lakap.title() + takim.upper() + pkodu,
						
						lakap + ad.title() + ktakim.upper() + pkodu,
						lakap + soyis.title() + ktakim.upper() + pkodu,
						soyis + lakap.title() + ktakim.upper() + pkodu,
						
						lakap.upper() + ad.upper() + takim.title() + pkodu,
						lakap.upper() + soyis.upper() + takim.title() + pkodu,
						soyis.title() + lakap.upper() + takim.title() + pkodu,
						
						lakap.upper() + ad.upper() + ktakim.title() + pkodu,
						lakap.upper() + soyis.upper() + ktakim.title() + pkodu,
						soyis.title() + lakap.upper() + ktakim.title() + pkodu,
						
						lakap.upper() + ad.title() + takim.upper() + pkodu,
						lakap.upper() + soyis.title() + takim.upper() + pkodu,
						soyis.title() + lakap.title() + takim.upper() + pkodu,
						
						lakap.upper() + ad.title() + ktakim.upper() + pkodu,
						lakap.upper() + soyis.title() + ktakim.upper() + pkodu,
						soyis.title() + lakap.title() + ktakim.upper() + pkodu,
						
						lakap.upper() + ad.title() + takim.title() + pkodu,
						lakap.upper() + soyis.title() + takim.title() + pkodu,
						soyis.title() + lakap.title() + takim.title() + pkodu,
						
						lakap.upper() + ad.title() + ktakim.title() + pkodu,
						lakap.upper() + soyis.title() + ktakim.title() + pkodu,
						soyis.title() + lakap.title() + ktakim.title() + pkodu,
						
						lakap.title() + ad.upper() + takim.title() + pkodu,
						lakap.title() + soyis.upper() + takim.title() + pkodu,
						soyis.title() + lakap.upper() + takim.title() + pkodu,
						
						lakap.title() + ad.upper() + ktakim.title() + pkodu,
						lakap.title() + soyis.upper() + ktakim.title() + pkodu,
						soyis.title() + lakap.upper() + ktakim.title() + pkodu,
						
						lakap.title() + ad.title() + takim.upper() + pkodu,
						lakap.title() + soyis.title() + takim.upper() + pkodu,
						soyis.title() + lakap.title() + takim.upper() + pkodu,
						
						lakap.title() + ad.title() + ktakim.upper() + pkodu,
						lakap.title() + soyis.title() + ktakim.upper() + pkodu,
						soyis.title() + lakap.title() + ktakim.upper() + pkodu,
						
						lakap + takim + t_pkodu,
						lakap + ktakim + t_pkodu,
						
						lakap + ad + takim + t_pkodu,
						lakap + soyis + takim + t_pkodu,
						soyis + lakap + takim + t_pkodu,
						
						lakap + ad + ktakim + t_pkodu,
						lakap + soyis + ktakim + t_pkodu,
						soyis + lakap + ktakim + t_pkodu,
						
						lakap.upper() + takim + t_pkodu,
						lakap.upper() + ktakim + t_pkodu,
						
						lakap.upper() + ad + takim + t_pkodu,
						lakap.upper() + soyis + takim + t_pkodu,
						soyis.upper() + lakap + takim + t_pkodu,
						
						lakap.upper() + ad + ktakim + t_pkodu,
						lakap.upper() + soyis + ktakim + t_pkodu,
						soyis.upper() + lakap + ktakim + t_pkodu,
						
						lakap + takim.upper() + t_pkodu,
						lakap + ktakim.upper() + t_pkodu,
						
						lakap + ad.upper() + takim + t_pkodu,
						lakap + soyis.upper() + takim + t_pkodu,
						soyis + lakap.upper() + takim + t_pkodu,
						
						lakap + ad.upper() + ktakim + t_pkodu,
						lakap + soyis.upper() + ktakim + t_pkodu,
						soyis + lakap.upper() + ktakim + t_pkodu,
						
						lakap + ad + takim.upper() + t_pkodu,
						lakap + soyis + takim.upper() + t_pkodu,
						soyis + lakap + takim.upper() + t_pkodu,
						
						lakap + ad + ktakim.upper() + t_pkodu,
						lakap + soyis + ktakim.upper() + t_pkodu,
						soyis + lakap + ktakim.upper() + t_pkodu,
						
						lakap.upper() + takim.upper() + t_pkodu,
						lakap.upper() + ktakim.upper() + t_pkodu,
						
						lakap.upper() + ad.upper() + takim + t_pkodu,
						lakap.upper() + soyis.upper() + takim + t_pkodu,
						soyis.title() + lakap.upper() + takim + t_pkodu,
						
						lakap.upper() + ad.upper() + ktakim + t_pkodu,
						lakap.upper() + soyis.upper() + ktakim + t_pkodu,
						soyis.title() + lakap.upper() + ktakim + t_pkodu,
						
						lakap.upper() + ad + takim.upper() + t_pkodu,
						lakap.upper() + soyis + takim.upper() + t_pkodu,
						soyis.upper() + lakap + takim.upper() + t_pkodu,
						
						lakap.upper() + ad + ktakim.upper() + t_pkodu,
						lakap.upper() + soyis + ktakim.upper() + t_pkodu,
						soyis.upper() + lakap + ktakim.upper() + t_pkodu,
						
						lakap + ad.upper() + takim.upper() + t_pkodu,
						lakap + soyis.upper() + takim.upper() + t_pkodu,
						soyis + lakap.upper() + takim.upper() + t_pkodu,
						
						lakap + ad.upper() + ktakim.upper() + t_pkodu,
						lakap + soyis.upper() + ktakim.upper() + t_pkodu,
						soyis + lakap.upper() + ktakim.upper() + t_pkodu,
						
						lakap.upper() + ad.upper() + takim.upper() + t_pkodu,
						lakap.upper() + soyis.upper() + takim.upper() + t_pkodu,
						soyis.title() + lakap.upper() + takim.upper() + t_pkodu,
						
						lakap.upper() + ad.upper() + ktakim.upper() + t_pkodu,
						lakap.upper() + soyis.upper() + ktakim.upper() + t_pkodu,
						soyis.title() + lakap.upper() + ktakim.upper() + t_pkodu,
						
						lakap.title() + takim + t_pkodu,
						lakap.title() + ktakim + t_pkodu,
						
						lakap.title() + ad + takim + t_pkodu,
						lakap.title() + soyis + takim + t_pkodu,
						soyis.title() + lakap + takim + t_pkodu,
						
						lakap.title() + ad + ktakim + t_pkodu,
						lakap.title() + soyis + ktakim + t_pkodu,
						soyis.title() + lakap + ktakim + t_pkodu,
						
						lakap + takim.title() + t_pkodu,
						lakap + ktakim.title() + t_pkodu,
						
						lakap + ad.title() + takim + t_pkodu,
						lakap + soyis.title() + takim + t_pkodu,
						soyis + lakap.title() + takim + t_pkodu,
						
						lakap + ad.title() + ktakim + t_pkodu,
						lakap + soyis.title() + ktakim + t_pkodu,
						soyis + lakap.title() + ktakim + t_pkodu,
						
						lakap + ad + takim.title() + t_pkodu,
						lakap + soyis + takim.title() + t_pkodu,
						soyis + lakap + takim.title() + t_pkodu,
						
						lakap + ad + ktakim.title() + t_pkodu,
						lakap + soyis + ktakim.title() + t_pkodu,
						soyis + lakap + ktakim.title() + t_pkodu,
						
						lakap.title() + takim.title() + t_pkodu,
						lakap.title() + ktakim.title() + t_pkodu,
						
						lakap.title() + ad.title() + takim + t_pkodu,
						lakap.title() + soyis.title() + takim + t_pkodu,
						soyis.title() + lakap.title() + takim + t_pkodu,
						
						lakap.title() + ad.title() + ktakim + t_pkodu,
						lakap.title() + soyis.title() + ktakim + t_pkodu,
						soyis.title() + lakap.title() + ktakim + t_pkodu,
						
						lakap.title() + ad + takim.title() + t_pkodu,
						lakap.title() + soyis + takim.title() + t_pkodu,
						soyis.title() + lakap + takim.title() + t_pkodu,
						
						lakap.title() + ad + ktakim.title() + t_pkodu,
						lakap.title() + soyis + ktakim.title() + t_pkodu,
						soyis.title() + lakap + ktakim.title() + t_pkodu,
						
						lakap + ad.title() + takim.title() + t_pkodu,
						lakap + soyis.title() + takim.title() + t_pkodu,
						soyis + lakap.title() + takim.title() + t_pkodu,
						
						lakap + ad.title() + ktakim.title() + t_pkodu,
						lakap + soyis.title() + ktakim.title() + t_pkodu,
						soyis + lakap.title() + ktakim.title() + t_pkodu,
						
						lakap.title() + ad.title() + takim.title() + t_pkodu,
						lakap.title() + soyis.title() + takim.title() + t_pkodu,
						soyis.title() + lakap.title() + takim.title() + t_pkodu,
						
						lakap.title() + ad.title() + ktakim.title() + t_pkodu,
						lakap.title() + soyis.title() + ktakim.title() + t_pkodu,
						soyis.title() + lakap.title() + ktakim.title() + t_pkodu,
						
						lakap.upper() + takim.title() + t_pkodu,
						lakap.upper() + ktakim.title() + t_pkodu,
						
						lakap.upper() + ad.title() + takim + t_pkodu,
						lakap.upper() + soyis.title() + takim + t_pkodu,
						soyis.title() + lakap.title() + takim + t_pkodu,
						
						lakap.upper() + ad.title() + ktakim + t_pkodu,
						lakap.upper() + soyis.title() + ktakim + t_pkodu,
						soyis.title() + lakap.title() + ktakim + t_pkodu,
						
						lakap.upper() + ad + takim.title() + t_pkodu,
						lakap.upper() + soyis + takim.title() + t_pkodu,
						soyis.upper() + lakap + takim.title() + t_pkodu,
						
						lakap.upper() + ad + ktakim.title() + t_pkodu,
						lakap.upper() + soyis + ktakim.title() + t_pkodu,
						soyis.upper() + lakap + ktakim.title() + t_pkodu,
						
						lakap + ad.upper() + takim.title() + t_pkodu,
						lakap + soyis.upper() + takim.title() + t_pkodu,
						soyis + lakap.upper() + takim.title() + t_pkodu,
						
						lakap + ad.upper() + ktakim.title() + t_pkodu,
						lakap + soyis.upper() + ktakim.title() + t_pkodu,
						soyis + lakap.upper() + ktakim.title() + t_pkodu,
						
						lakap.title() + takim.upper() + t_pkodu,
						lakap.title() + ktakim.upper() + t_pkodu,
						
						lakap.title() + ad.upper() + takim + t_pkodu,
						lakap.title() + soyis.upper() + takim + t_pkodu,
						soyis.title() + lakap.upper() + takim + t_pkodu,
						
						lakap.title() + ad.upper() + ktakim + t_pkodu,
						lakap.title() + soyis.upper() + ktakim + t_pkodu,
						soyis.title() + lakap.upper() + ktakim + t_pkodu,
						
						lakap.title() + ad + takim.upper() + t_pkodu,
						lakap.title() + soyis + takim.upper() + t_pkodu,
						soyis.title() + lakap + takim.upper() + t_pkodu,
						
						lakap.title() + ad + ktakim.upper() + t_pkodu,
						lakap.title() + soyis + ktakim.upper() + t_pkodu,
						soyis.title() + lakap + ktakim.upper() + t_pkodu,
						
						lakap + ad.title() + takim.upper() + t_pkodu,
						lakap + soyis.title() + takim.upper() + t_pkodu,
						soyis + lakap.title() + takim.upper() + t_pkodu,
						
						lakap + ad.title() + ktakim.upper() + t_pkodu,
						lakap + soyis.title() + ktakim.upper() + t_pkodu,
						soyis + lakap.title() + ktakim.upper() + t_pkodu,
						
						lakap.upper() + ad.upper() + takim.title() + t_pkodu,
						lakap.upper() + soyis.upper() + takim.title() + t_pkodu,
						soyis.title() + lakap.upper() + takim.title() + t_pkodu,
						
						lakap.upper() + ad.upper() + ktakim.title() + t_pkodu,
						lakap.upper() + soyis.upper() + ktakim.title() + t_pkodu,
						soyis.title() + lakap.upper() + ktakim.title() + t_pkodu,
						
						lakap.upper() + ad.title() + takim.upper() + t_pkodu,
						lakap.upper() + soyis.title() + takim.upper() + t_pkodu,
						soyis.title() + lakap.title() + takim.upper() + t_pkodu,
						
						lakap.upper() + ad.title() + ktakim.upper() + t_pkodu,
						lakap.upper() + soyis.title() + ktakim.upper() + t_pkodu,
						soyis.title() + lakap.title() + ktakim.upper() + t_pkodu,
						
						lakap.upper() + ad.title() + takim.title() + t_pkodu,
						lakap.upper() + soyis.title() + takim.title() + t_pkodu,
						soyis.title() + lakap.title() + takim.title() + t_pkodu,
						
						lakap.upper() + ad.title() + ktakim.title() + t_pkodu,
						lakap.upper() + soyis.title() + ktakim.title() + t_pkodu,
						soyis.title() + lakap.title() + ktakim.title() + t_pkodu,
						
						lakap.title() + ad.upper() + takim.title() + t_pkodu,
						lakap.title() + soyis.upper() + takim.title() + t_pkodu,
						soyis.title() + lakap.upper() + takim.title() + t_pkodu,
						
						lakap.title() + ad.upper() + ktakim.title() + t_pkodu,
						lakap.title() + soyis.upper() + ktakim.title() + t_pkodu,
						soyis.title() + lakap.upper() + ktakim.title() + t_pkodu,
						
						lakap.title() + ad.title() + takim.upper() + t_pkodu,
						lakap.title() + soyis.title() + takim.upper() + t_pkodu,
						soyis.title() + lakap.title() + takim.upper() + t_pkodu,
						
						lakap.title() + ad.title() + ktakim.upper() + t_pkodu,
						lakap.title() + soyis.title() + ktakim.upper() + t_pkodu,
						soyis.title() + lakap.title() + ktakim.upper() + t_pkodu,

						]
	for sifre in lakapli_sifreler :
		if sifre not in son and len(sifre) >= minimum and len(sifre) <= maksimum :
			son.append(sifre)
			a = sifre + '!'
			b = sifre + '.'
			if a not in son and len(a) >= minimum and len(a) <= maksimum :
				son.append(a)
				son.append(b)
		elif sifre not in son and len(sifre) < minimum :
			a = sifre + '!'
			b = sifre + '.'
			if a not in son and len(a) >= minimum and len(a) <= maksimum :
				son.append(a)
				random.shuffle(son)
				son.append(b)
				random.shuffle(son)

		
random.shuffle(son)
soru2 = str(input('\nOluşturulacak şifreleri bir txt dosyasında kaydetmek ister misiniz (e - h) : '))
while soru2 != 'e' and soru2 != 'E' and soru2 != 'h' and soru2 != "H" :
	print('Hatalı seçim yaptınız ! ')
	soru2 = str(input('\nOluşturulacak şifreleri bir txt dosyasında kaydetmek ister misiniz (e - h) : '))
if soru2 == 'h' or soru2 == 'H' :
	pass
elif soru2 == 'e' or 'E' :
	dosya_adi = str(input('Txt dosyasının adı ne olsun : '))
	with open('{}.txt'.format(dosya_adi) , 'w') as dosya :
		for sifre in son :
			dosya.write('{}\n'.format(sifre))
print('\nŞifreler oluşturuluyor...\n')
time.sleep(2)
print('Oluşturulan şifre sayısı : {}\n'.format(len(son)))
soru3 = str(input('Şifreleri şimdi görmek ister misiniz (e - h) : '))
while soru3 != 'e' and soru3 != 'E' and soru3 != 'h' and soru3 != "H" :
	print('Hatalı seçim yaptınız ! ')
	soru3 = str(input('\nŞifreleri şimdi görmek ister misiniz (e - h) : '))
print('')
if soru3 == 'h' or soru3 == 'H' :
	print('Ayyıldız Tim - Cyber1adam')
	time.sleep(3)
elif soru3 == 'e' or soru3 == 'E' :
	print('Sistem hazırlanıyor...\n')
	time.sleep(2)
	for sifre in son :
		print('Oluşturuldu ===============> {}'.format(sifre))
		time.sleep(0.110)
	print('Ayyıldız Tim - Cyber1adam')
	time.sleep(3)
	