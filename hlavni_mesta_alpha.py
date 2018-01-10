# !/usr/bin/python3.6 # pro Linux
# -*- coding: utf-8 -*-  # kodování
from datetime import datetime  # import
import time

# -----------------------------------------------------------------
body = int(0)  # počet zodpovězených otázek
pocet = int(42)  # celkový počet otázek
# -----------------------------------------------------------------

print('Vítám tě u testu z hlavních měst Evropy.\n')  # uvítání
time.sleep(2)
print('Test zabere asi 5 minut tvého času. Čeká tě 42 otázek.\n')
time.sleep(2)
print('Svoji odpověď odešli stisknutím klávesy ENTER.\n')
time.sleep(2)
print('Gramatika je důležitá. Pozor na malá a velká písmena a na háčky a čárky.\n')  # gramatika
time.sleep(2)

# -----------------------------------------------------------------

uzivatel = input('Jak se jmenuješ?\n')  # jméno uživatele
print('To je ale hezké jméno,', uzivatel, '.\n')
time.sleep(1)
# -----------------------------------------------------------------
print('Jdeme na to!\n')  # začátek programu
time.sleep(1)
# -----------------------------------------------------------------

print('Nejdříve se podíváme do Severní Evropy.\n')
time.sleep(1)

start_time = datetime.now()  # začátek měření času

dansko = input('Jak se jmenuje hlavní město Dánska?\n')  # Dánsko, Kodaň 1, SEVERNÍ EVROPA
if dansko == 'Kodaň':
    print('Správně!\n')
    body += 1
else:
    print('Špatná odpověď! Správná odpověď je Kodaň.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

finsko = input('Jak se jmenuje hlavní město Finska?\n')  # Finsko, Helsinki 2
if finsko == 'Helsinki':
    print('Výborně!\n')
    body += 1
else:
    print('Bohužel, jsou to Helsinki.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

island = input('Jak se jmenuje hlavní město Islandu?\n')  # Island, Reykjavík 3
if island == 'Reykjavík':
    print('Ano!\n')
    body += 1
else:
    print('Správná odpověď je Reykjavík.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

norsko = input('Jak se jmenuje hlavní město Norska?\n')  # Norsko, Oslo 4
if norsko == 'Oslo':
    print('Super!\n')
    body += 1
else:
    print('Správná odpověď je Oslo.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

svedsko = input('Jak se jmenuje hlavní město Švédska?\n')  # Švédsko, Stockholm 5
if svedsko == 'Stockholm':
    print('Skvěle!\n')
    body += 1
else:
    print('Bohužel, je to Stockholm.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

print('Teď se podíváme do Pobaltí.\n')  # POBALTÍ
time.sleep(1)
# -----------------------------------------------------------------
estonsko = input('Jak se jmenuje hlavní město Estonska?\n')  # Estonsko, Tallinn 6
if estonsko == 'Tallinn' or estonsko == 'Talin':
    print('Bravo!\n')
    body += 1
else:
    print('Správná odpověď je Tallinn.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

lotyssko = input('Jak se jmenuje hlavní město Lotyšska?\n')  # Lotyšsko, Riga 7
if lotyssko == 'Riga':
    print('Správná odpověď!\n')
    body += 1
else:
    print('Bohužel, je to Riga.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

litva = input('Jak se jmenuje hlavní město Litvy?\n')  # Litva, Vilnius 8
if litva == 'Vilnius':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je Vilnius.\n')
time.sleep(0.5)
# -----------------------------------------------------------------
print('Teď za teplem do Jižní Evropy.\n')  # JIŽNÍ EVROPA
time.sleep(1)
# -----------------------------------------------------------------

italie = input('Jak se jmenuje hlavní město Itálie?\n')  # Itálie, Řím 9
if italie == 'Řím':
    print('Ano!\n')
    body += 1
else:
    print('Správná odpověď je Řím.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

malta = input('Jak se jmenuje hlavní město Malty?\n')  # Malta, Valletta 10
if malta == 'Valletta':
    print('Skvěle!\n')
    body += 1
else:
    print('Správná odpověď je Valletta.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

portugalsko = input('Jak se jmenuje hlavní město Portugalska?\n')  # Portugalsko, Lisabon 11
if portugalsko == 'Lisabon':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je Lisabon.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

recko = input('Jak se jmenuje hlavní město Řecka?\n')  # Řecko, Atény 12
if recko == 'Atény':
    print('Paráda!\n')
    body += 1
else:
    print('Správná odpověď je Atény.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

spanelsko = input('Jak se jmenuje hlavní město Španělska?\n')  # Španělsko, Madrid 13
if spanelsko == 'Madrid':
    print('Dobře!\n')
    body += 1
else:
    print('Správná odpověď je Madrid.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

andorra = input('Jak se jmenuje hlavní město státu Andorra?\n')  # Andorra, Andorra la Vella 14
if andorra == 'Andorra la Vella':
    print('Klobouk dolů!\n')
    body += 1
else:
    print('Správná odpověď je Andorra la Vella.\n')
time.sleep(0.5)
# -----------------------------------------------------------------
print('Teď zamíříme do Střední a Západní Evropy.\n')  # STŘEDNÍ A ZÁPADNÍ EVROPA
time.sleep(1)
# -----------------------------------------------------------------
rakousko = input('Jak se jmenuje hlavní město Rakouska?\n')  # Vídeň, Rakousko 15
if rakousko == 'Vídeň':
    body += 1
    print('Správně!\n')
else:
    print('Správná odpověď je Vídeň.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

nemecko = input('Jak se jmenuje hlavní město Německa?\n')  # Německo, Berlín 16
if nemecko == 'Berlín':
    print('Paráda!\n')
    body += 1
else:
    print('Správná odpověď je Berlín.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

svycarsko = input('Jak se jmenuje hlavní město Švýcarska?\n')  # Švýcarsko, Bern 17
if svycarsko == 'Bern':
    print('Bravo!\n')
    body += 1
else:
    print('Správná odpověď je Bern.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

lichtenstejnsko = input('Jak se jmenuje hlavní město Lichtenštejnska?\n')  # Lichtenštejnsko, Vaduz 18
if lichtenstejnsko == 'Vaduz':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je Vaduz.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

slovinsko = input('Jak se jmenuje hlavní město Slovinska?\n')  # Slovinsko, Lublaň 19
if slovinsko == 'Lublaň':
    print('Ano!\n')
    body += 1
else:
    print('Správná odpověď je Lublaň.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

madarsko = input('Jak se jmenuje hlavní město Maďarska?\n')  # Maďarsko, Budapešť 20
if madarsko == 'Budapešť':
    print('Jen tak dál!\n')
    body += 1
else:
    print('Správná odpověď je Budapešť.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

polsko = input('Jak se jmenuje hlavní město Polska?\n')  # Polsko, Varšava 21
if polsko == 'Varšava':
    print('Super!\n')
    body += 1
else:
    print('Správná odpověď je Varšava.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

cesko = input('Jak se jmenuje hlavní město České republiky?\n')  # Česká republika, Praha 22
if cesko == 'Praha':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je Praha.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

slovensko = input('Jak se jmenuje hlavní město Slovenska?\n')  # Slovensko, Bratislava 23
if slovensko == 'Bratislava':
    print('Správná odpověď!\n')
    body += 1
else:
    print('Správná odpověď je Bratislava.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

belgie = input('Jak se jmenuje hlavní město Belgie?\n')  # Belgie, Brusel 24
if belgie == 'Brusel':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je Brusel.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

francie = input('Jak se jmenuje hlavní město Francie?\n')  # Francie, Paříž 25
if francie == 'Paříž':
    print('Ano!\n')
    body += 1
else:
    print('Správná odpověď je Paříž.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

lucembursko = input('Jak se jmenuje hlavní město Lucemburska?\n')  # Lucembursko, Lucemburk 26
if lucembursko == 'Lucemburk':
    print('Super!\n')
    body += 1
else:
    print('Správná odpověď je Lucemburk.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

nizozemsko = input('Jak se jmenuje hlavní město Nizozemska?\n')  # Nizozemsko, Amsterdam 27
if nizozemsko == 'Amsterdam' or nizozemsko == 'Amsterodam':
    print('Bravo!\n')
    body += 1
else:
    print('Správná odpověď je Amsterdam.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

irsko = input('Jak se jmenuje hlavní město Irska?\n')  # Dublin, Irsko 28
if irsko == 'Dublin':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je Dublin.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

britanie = input('Jak se jmenuje hlavní město Velké Británie?\n')  # Velká Británie, Londýn 29
if britanie == 'Londýn':
    print('Skvěle!\n')
    body += 1
else:
    print('Správná odpověď je Londýn.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

print('Teď se podíváme do Jihovýchodní Evropy.\n')  # JIHOVÝCHODNÍ EVROPA
time.sleep(1)
# -----------------------------------------------------------------

albanie = input('Jak se jmenuje hlavní město Albánie?\n')  # Albánie, Tirana 30
if albanie == 'Tirana':
    print('Dobře!\n')
    body += 1
else:
    print('Správná odpověď je Tirana.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

turecko = input('Jak se jmenuje hlavní město Turecka?\n')  # Turecko, Ankara 31
if turecko == 'Ankara':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je Ankara.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

bosna = input('Jak se jmenuje hlavní město Bosny a Hercegoviny?\n')  # Bosna a Hercegovina, Sarajevo 32
if bosna == 'Sarajevo':
    print('Ano!\n')
    body += 1
else:
    print('Správná odpověď je Sarajevo.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

bulharsko = input('Jak se jmenuje hlavní město Bulharska?\n')  # Bulharsko, Sofie 33
if bulharsko == 'Sofie':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je Sofie.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

cernahora = input('Jak se jmenuje hlavní město Černé Hory?\n')  # Černá Hora, Podgorica 34
if cernahora == 'Podgorica':
    print('Paráda!\n')
    body += 1
else:
    print('Správná odpověď je Podgorica.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

chorvatsko = input('Jak se jmenuje hlavní město Chorvatska?\n')  # Chorvatsko, Záhřeb 35
if chorvatsko == 'Záhřeb':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je Záhřeb.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

makedonie = input('Jak se jmenuje hlavní město Makedonie?\n')  # Makedonie, Skopje 36
if makedonie == 'Skopje':
    print('Klobouk dolů!\n')
    body += 1
else:
    print('Správná odpověď je Skopje.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

rumunsko = input('Jak se jmenuje hlavní město Rumunska?\n')  # Rumunsko, Bukurešť 37
if rumunsko == 'Bukurešť':
    print('Správně!\n')
    body += 1
else:
    print('Správná odpověď je Bukurešť.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

srbsko = input('Jak se jmenuje hlavní město Srbska?\n')  # Srbsko, Bělehrad 38
if srbsko == 'Bělehrad':
    print('Super!\n')
    body += 1
else:
    print('Správná odpověď je Bělehrad.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

print('Na závěr nás čeká Východní Evropa.\n')  # VÝCHODNÍ EVROPA
time.sleep(1)
# -----------------------------------------------------------------

belorusko = input('Jak se jmenuje hlavní město Běloruska?\n')  # Bělorusko, Minsk 39
if belorusko == 'Minsk':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je Minsk.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

moldavsko = input('Jak se jmenuje hlavní město Moldavska?\n')  # Moldavsko, Kišiněv 40
if moldavsko == 'Kišiněv':
    print('Ano!\n')
    body += 1
else:
    print('Správná odpověď je Kišiněv.\n')
time.sleep(0.5)
# -----------------------------------------------------------------

rusko = input('Jak se jmenuje hlavní město Ruska?\n')  # Rusko, Moskva 41
if rusko == 'Moskva':
    print('Dobře!\n')
    body += 1
else:
    print('Správná odpověď je Moskva.\n')
time.sleep(1)
print('Poslední otázka!\n')  # poslední otázka
time.sleep(0.5)
# -----------------------------------------------------------------

ukrajina = input('Jak se jmenuje hlavní město Ukrajiny?\n')  # Ukrajina, Kyjev 42
if ukrajina == 'Kyjev':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je Kyjev.\n')
time.sleep(1)
# -----------------------------------------------------------------
end_time = datetime.now()  # konec měření času
# -----------------------------------------------------------------

c = float(body / pocet * 100)  # úspěšnost v procentech, výpočet
# -----------------------------------------------------------------

print('KONEC TESTU! GRATULUJI!\n')  # konec testu
time.sleep(1)
# -----------------------------------------------------------------

print('POČET SPRÁVNÝCH ODPOVĚDÍ:', body)  # vyhodnocení
time.sleep(1)
# -----------------------------------------------------------------

print('TVOJE ÚSPĚŠNOST JE:', '{0:.2f}%'.format(c))
time.sleep(1)
# -----------------------------------------------------------------

print('TVŮJ ČAS: {}'.format(end_time - start_time))  # konečný čas
time.sleep(1)
# -----------------------------------------------------------------

print('KONEC PROGRAMU.')
input()
