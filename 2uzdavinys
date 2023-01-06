#Parašyti programą, kuri spausdina šios dienos www.delfi.lt puslapyje yra antraštinių straipsnių ir iraaso i csv faila
from bs4 import BeautifulSoup
import requests
import csv
import re

source = requests.get('https://www.delfi.lt/').text
soup = BeautifulSoup(source, 'html.parser')
blocks = soup.find_all('div', class_="headline")

with open("delfi_straipsniai.csv", 'w', encoding="UTF-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['CATEGORY', 'TEXT', 'LINK'])

    for block in blocks:
        try:
            category = block.find('div', class_='headline-category').get_text().strip()
            text = block.find('a', class_="CBarticleTitle").get_text()
            link = block.find('a', class_="CBarticleTitle")['href']
            csv_writer.writerow([category, text, link])
            print("-----------------------------------------")
            print(category)
            print(text)
            print(link)
        except:
            pass
            
     #output
-----------------------------------------
Lietuvoje
Šimonytė – apie brangstantį gyvenimą: pasakysiu tai, kas nebūtinai patiks
https://www.delfi.lt/news/daily/lithuania/simonyte-apie-brangstanti-gyvenima-pasakysiu-tai-kas-nebutinai-patiks.d?id=92209391
-----------------------------------------
Užsienyje
Karas Ukrainoje. Rusiškos „paliaubos“: Putinas neištvėrė nė dviejų valandų
https://www.delfi.lt/news/daily/world/karas-ukrainoje-rusiskos-paliaubos-putinas-neistvere-ne-dvieju-valandu.d?id=92209485
-----------------------------------------
Veidai
Donatas Čižauskas palaidotas Žemaitijoje, prie kapo duobės – jautrūs Valinsko žodžiai ir svarbi žinia
https://www.delfi.lt/veidai/zmones/donatas-cizauskas-palaidotas-zemaitijoje-prie-kapo-duobes-jautrus-valinsko-zodziai-ir-svarbi-zinia.d?id=92207871
-----------------------------------------
Lietuvoje
Idėja: Vilniuje pastatyti paminklą Zelenskiui
https://www.delfi.lt/news/daily/lithuania/ideja-vilniuje-pastatyti-paminkla-zelenskiui.d?id=92216563
-----------------------------------------
Užsienyje
Arestovyčius okupantams: jokių paliaubų čia nebus, bus tik HIMARS ant jūsų galvų
https://www.delfi.lt/news/daily/world/arestovycius-okupantams-jokiu-paliaubu-cia-nebus-bus-tik-himars-ant-jusu-galvu.d?id=92216913
-----------------------------------------
Veidai
Po Agnės Jagelavičiūtės mirties prabilo jos mama
https://www.delfi.lt/veidai/zmones/po-agnes-jagelaviciutes-mirties-prabilo-jos-mama.d?id=92216939
-----------------------------------------
Veidai
Donato Čižausko šermenyse – garsių kolegų atsiminimai ir ašaros: atlikėjas savo gyvenimo kelionę baigė gimtinėje
https://www.delfi.lt/veidai/zmones/donato-cizausko-sermenyse-garsiu-kolegu-atsiminimai-ir-asaros-atlikejas-savo-gyvenimo-kelione-baige-gimtineje.d?id=92208069
-----------------------------------------
Sportas
Dakare Kancius traukiasi iš kovos dėl prizinių pozicijų, Baciuška išlaiko intrigą kovoje dėl titulo
https://www.delfi.lt/sportas/dakaras/dakare-kancius-traukiasi-is-kovos-del-priziniu-poziciju-baciuska-islaiko-intriga-kovoje-del-titulo.d?id=92209277
-----------------------------------------
Verslas
Ekspertai įvertino, kokių naftos kainų šiemet tikėtis: pernai buvusių aukštumų pasiekti neturėtų
https://www.delfi.lt/verslas/energetika/ekspertai-ivertino-kokiu-naftos-kainu-siemet-tiketis-pernai-buvusiu-aukstumu-pasiekti-neturetu.d?id=92217701
-----------------------------------------
Krepšinis
„Žalgiris“ skubiai ieško papildymo: nusitaikė į snaiperį, šią savaitę sušveitusį net 45 taškus
https://www.delfi.lt/krepsinis/naujienos/zalgiris-skubiai-iesko-papildymo-nusitaike-i-snaiperi-sia-savaite-susveitusi-net-45-taskus.d?id=92215553
-----------------------------------------
Užsienyje
Medvedevas dėl Ukrainos spjaudosi purvais: kiaulės
https://www.delfi.lt/news/daily/world/medvedevas-del-ukrainos-spjaudosi-purvais-kiaules.d?id=92212851
-----------------------------------------
Lietuvoje
Karo ekspertai įvertino Kremliaus paliaubas: jau aišku, ką darys rusai
https://www.delfi.lt/news/daily/lithuania/karo-ekspertai-ivertino-kremliaus-paliaubas-jau-aisku-ka-darys-rusai.d?id=92210259
-----------------------------------------
Video
Tiesioginė transliacija / Delfi diena. Nepaisant paskelbtų paliaubų, rusai atakavo Kramatorską ir politinė krizė JAV
https://www.delfi.lt/video/laidos/delfi-diena/delfi-diena-nepaisant-paskelbtu-paliaubu-rusai-atakavo-kramatorska-ir-politine-krize-jav.d?id=92215109
-----------------------------------------
Mokslas
Prasivėrė pragariškas lavos žiedas: po didžiausio pasaulyje ugnikalnio išsiveržimo lava ėmė kunkuliuoti nerimstančio kaimyno krateryje
https://www.delfi.lt/mokslas/mokslas/prasivere-pragariskas-lavos-ziedas-po-didziausio-pasaulyje-ugnikalnio-issiverzimo-lava-eme-kunkuliuoti-nerimstancio-kaimyno-krateryje.d?id=92217323
-----------------------------------------
Lietuvoje
Niūrios prognozės: Lietuvoje liks tik 2 mln. gyventojų
https://www.delfi.lt/news/daily/lithuania/niurios-prognozes-lietuvoje-liks-tik-2-mln-gyventoju.d?id=92211805
-----------------------------------------
Login
Lietuvių startuolis sukūrė lazerį, padedantį kovoti su vėžiu: papasakojo, kaip jis veikia ir kodėl darbuotojų neprašo diplomo
https://www.delfi.lt/login/verslas/startuoliai/lietuviu-startuolis-sukure-lazeri-padedanti-kovoti-su-veziu-papasakojo-kaip-jis-veikia-ir-kodel-darbuotoju-nepraso-diplomo.d?id=92206321
-----------------------------------------
Krepšinis
Evansui patyrus traumą buvęs jo komandos draugas neparodė jokių sentimentų, bet apsijuokė pats
https://www.delfi.lt/krepsinis/naujienos/evansui-patyrus-trauma-buves-jo-komandos-draugas-neparode-jokiu-sentimentu-bet-apsijuoke-pats.d?id=92212849
-----------------------------------------
Veidai
Į Žemaitiją plūdo garsūs žmonės, tarę „sudie“ netikėtai mirusiam Donatui Čižauskui: skambėjo jo dainos, riedėjo ašaros
https://www.delfi.lt/veidai/zmones/i-zemaitija-pludo-garsus-zmones-tare-sudie-netiketai-mirusiam-donatui-cizauskui-skambejo-jo-dainos-riedejo-asaros.d?id=92199681
-----------------------------------------
Užsienyje
Karas Ukrainoje. Į Rusijos skelbiamas laikinas paliaubas sureagavo Ukraina: veidmainystę pasilikite sau
https://www.delfi.lt/news/daily/world/karas-ukrainoje-i-rusijos-skelbiamas-laikinas-paliaubas-sureagavo-ukraina-veidmainyste-pasilikite-sau.d?id=92199047
-----------------------------------------
Lietuvoje
Šį itin iškalbingą karo epizodą studijuos ne tik ukrainiečiai ir rusai: kuo jis svarbus Lietuvai ir visai NATO
https://www.delfi.lt/news/daily/lithuania/si-itin-iskalbinga-karo-epizoda-studijuos-ne-tik-ukrainieciai-ir-rusai-kuo-jis-svarbus-lietuvai-ir-visai-nato.d?id=92198453
-----------------------------------------
Veidai
Vieni paskutinių Donato Čižausko žodžių po jo mirties sminga į širdį: neslėpė prislėgtų pečių ir žvaigždei keliamų reikalavimų
https://www.delfi.lt/veidai/zmones/vieni-paskutiniu-donato-cizausko-zodziu-po-jo-mirties-sminga-i-sirdi-neslepe-prislegtu-peciu-ir-zvaigzdei-keliamu-reikalavimu.d?id=92192733
-----------------------------------------
Teisė
Po slaptos kriminalistų operacijos – ypatingas laimikis: lietuviškai mafijai dirigavo mįslingas rusas
https://www.delfi.lt/news/daily/law/po-slaptos-kriminalistu-operacijos-ypatingas-laimikis-lietuviskai-mafijai-dirigavo-mislingas-rusas.d?id=92162429
-----------------------------------------
Verslas Plius
Išskirtinis interviu su JAV investuotoju Browderiu, kurio mirties labai norėtų Putinas: ką ten pamatėme, buvo daug blogiau, nei bet kas galėtų įsivaizduoti
https://www.delfi.lt/verslasplius/pulsas/isskirtinis-interviu-su-jav-investuotoju-browderiu-kurio-mirties-labai-noretu-putinas-ka-ten-pamateme-buvo-daug-blogiau-nei-bet-kas-galetu-isivaizduoti.d?id=92184941
-----------------------------------------
Plius
„P. O. 1142“ – slapta bazė JAV, kur žydų kilmės kariai tardė nacius: sunku suvokti, kuo baigėsi ši istorija
https://www.delfi.lt/plius/pasaulis/p-o-1142-slapta-baze-jav-kur-zydu-kilmes-kariai-tarde-nacius-sunku-suvokti-kuo-baigesi-si-istorija.d?id=92175759
-----------------------------------------
Lietuvoje
Iš NATO šalių į Ukrainą juda ypač rimta technika: ką šis lūžis gali pakeisti kare
https://www.delfi.lt/news/daily/lithuania/is-nato-saliu-i-ukraina-juda-ypac-rimta-technika-ka-sis-luzis-gali-pakeisti-kare.d?id=92208911
-----------------------------------------
Lietuvoje
Signataras užsipuolė prezidento patarėją: tikri lyderiai tokių dalykų viešai nesvarsto
https://www.delfi.lt/news/daily/lithuania/signataras-uzsipuole-prezidento-patareja-tikri-lyderiai-tokiu-dalyku-viesai-nesvarsto.d?id=92209927
-----------------------------------------
Lietuvoje
Didėja pensijos ir socialinės išmokos: kokios sumos ir kada pasieks gyventojus?
https://www.delfi.lt/news/daily/lithuania/dideja-pensijos-ir-socialines-ismokos-kokios-sumos-ir-kada-pasieks-gyventojus.d?id=92210111
-----------------------------------------
Lietuvoje
Į Lietuvą įsiveržė arktinis šaltis: sinoptikai skelbia, kada vėl galima tikėtis pokyčių
https://www.delfi.lt/news/daily/lithuania/i-lietuva-isiverze-arktinis-saltis-sinoptikai-skelbia-kada-vel-galima-tiketis-pokyciu.d?id=92209357
-----------------------------------------
Lietuvoje
Ką Lietuvoje turėjo ištverti migrantai: grotos ir įžeidinėjamai – tik ledkalnio viršūnė
https://www.delfi.lt/news/daily/lithuania/ka-lietuvoje-turejo-istverti-migrantai-grotos-ir-izeidinejamai-tik-ledkalnio-virsune.d?id=92187085
-----------------------------------------
Lietuvoje
Idėja: Vilniuje pastatyti paminklą Zelenskiui
https://www.delfi.lt/news/daily/lithuania/ideja-vilniuje-pastatyti-paminkla-zelenskiui.d?id=92216563
-----------------------------------------
Lietuvoje
Anušauskas apžiūrėjo naujai kylantį karinį miestelį: statybos vyksta greičiau nei buvo planuota
https://www.delfi.lt/news/daily/lithuania/anusauskas-apziurejo-naujai-kylanti-karini-miesteli-statybos-vyksta-greiciau-nei-buvo-planuota.d?id=92217315
-----------------------------------------
Lietuvoje
Druskininkuose fiksuotas sausio 5-osios šilumos rekordas
https://www.delfi.lt/news/daily/lithuania/druskininkuose-fiksuotas-sausio-5-osios-silumos-rekordas.d?id=92217269
-----------------------------------------
Lietuvoje
Dėl nesėkmių Ukrainoje Kremliaus propaganda skyrė mažiau laiko Lietuvai
https://www.delfi.lt/news/daily/lithuania/del-nesekmiu-ukrainoje-kremliaus-propaganda-skyre-maziau-laiko-lietuvai.d?id=92216197
-----------------------------------------
Lietuvoje
Šimonytė – apie brangstantį gyvenimą: pasakysiu tai, kas nebūtinai patiks
https://www.delfi.lt/news/daily/lithuania/simonyte-apie-brangstanti-gyvenima-pasakysiu-tai-kas-nebutinai-patiks.d?id=92209391
-----------------------------------------
Lietuvoje
Vasiliauskui pasitraukus iš pareigų, naujo premjerės patarėjo ieškoti neskubama: jis dirbo su konkrečiu projektu
https://www.delfi.lt/news/daily/lithuania/vasiliauskui-pasitraukus-is-pareigu-naujo-premjeres-patarejo-ieskoti-neskubama-jis-dirbo-su-konkreciu-projektu.d?id=92215311
-----------------------------------------
Lietuvoje
„Juventos“ gimnazija ieško naujo lietuvių kalbos mokytojo: neatskleidė, ar konkurse dalyvauja Astrauskaitė
https://www.delfi.lt/news/daily/lithuania/juventos-gimnazija-iesko-naujo-lietuviu-kalbos-mokytojo-neatskleide-ar-konkurse-dalyvauja-astrauskaite.d?id=92215007
-----------------------------------------
Lietuvoje
Karo ekspertai įvertino Kremliaus paliaubas: jau aišku, ką darys rusai
https://www.delfi.lt/news/daily/lithuania/karo-ekspertai-ivertino-kremliaus-paliaubas-jau-aisku-ka-darys-rusai.d?id=92210259
-----------------------------------------
Lietuvoje
Niūrios prognozės: Lietuvoje liks tik 2 mln. gyventojų
https://www.delfi.lt/news/daily/lithuania/niurios-prognozes-lietuvoje-liks-tik-2-mln-gyventoju.d?id=92211805
-----------------------------------------
Lietuvoje
Lietuvos pavyzdžiu dėl migrantų sekė kitos šalys, po kontrolierių kritikos sako ministrė
https://www.delfi.lt/news/daily/lithuania/lietuvos-pavyzdziu-del-migrantu-seke-kitos-salys-po-kontrolieriu-kritikos-sako-ministre.d?id=92212705
-----------------------------------------
Sveikata
Vilniaus klinikinei ligoninei vadovaus buvusi viceministrė Bilotienė Motiejūnienė
https://www.delfi.lt/sveikata/sveikatos-naujienos/vilniaus-klinikinei-ligoninei-vadovaus-buvusi-viceministre-bilotiene-motiejuniene.d?id=92212385
-----------------------------------------
Lietuvoje
Per parą Lietuvoje – 326 nauji koronaviruso atvejai, fiksuota viena mirtis
https://www.delfi.lt/news/daily/lithuania/per-para-lietuvoje-326-nauji-koronaviruso-atvejai-fiksuota-viena-mirtis.d?id=92210237
-----------------------------------------
Lietuvoje
Vasiliauskas palieka premjerės komandą, pradeda darbą TVF
https://www.delfi.lt/news/daily/lithuania/vasiliauskas-palieka-premjeres-komanda-pradeda-darba-tvf.d?id=92209539
-----------------------------------------
Lietuvoje
Rusijos bendrystė su sąjungininkėmis braška per visas siūles: pokyčiai akivaizdūs
https://www.delfi.lt/news/daily/lithuania/rusijos-bendryste-su-sajungininkemis-braska-per-visas-siules-pokyciai-akivaizdus.d?id=92157177
-----------------------------------------
Lietuvoje
Jakutai fronto linijoje išklojo, ką patyrė: Rusijos kariuomenėje tiesiog siaubinga
https://www.delfi.lt/news/daily/lithuania/jakutai-fronto-linijoje-isklojo-ka-patyre-rusijos-kariuomeneje-tiesiog-siaubinga.d?id=92200545
-----------------------------------------
Lietuvoje
Gedimino kalno remonto projektą koreguoti atsisakiusiai įmonei – teismo verdiktas: kita pusė sprendimą svarsto skųsti
https://www.delfi.lt/news/daily/lithuania/gedimino-kalno-remonto-projekta-koreguoti-atsisakiusiai-imonei-teismo-verdiktas-kita-puse-sprendima-svarsto-skusti.d?id=92208539
-----------------------------------------
Lietuvoje
„Sputnik Litva“ redaktorius sulaikytas Latvijoje už šnipinėjimą
https://www.delfi.lt/news/daily/lithuania/sputnik-litva-redaktorius-sulaikytas-latvijoje-uz-snipinejima.d?id=92207825
-----------------------------------------
Lietuvoje
Buvęs „Kauno švaros“ vadovas lieka nuteistas už kyšininkavimą
https://www.delfi.lt/news/daily/lithuania/buves-kauno-svaros-vadovas-lieka-nuteistas-uz-kysininkavima.d?id=92207397
-----------------------------------------
Lietuvoje
Šimonytės atsakymas į klausimą apie Prezidento rinkimus – kiek netikėtas
https://www.delfi.lt/news/daily/lithuania/simonytes-atsakymas-i-klausima-apie-prezidento-rinkimus-kiek-netiketas.d?id=92203501
-----------------------------------------
Lietuvoje
Karo ekspertai: ukrainiečių dronai pasiekė dar vieną Rusijos miestą – tai gali būti didelis žingsnis
https://www.delfi.lt/news/daily/lithuania/karo-ekspertai-ukrainieciu-dronai-pasieke-dar-viena-rusijos-miesta-tai-gali-buti-didelis-zingsnis.d?id=92200123
-----------------------------------------
Lietuvoje
Partija „Jaunoji Lietuva“ kandidatuos Vilniaus miesto savivaldos rinkimuose: sąrašą ves Buškevičius
https://www.delfi.lt/news/daily/lithuania/partija-jaunoji-lietuva-kandidatuos-vilniaus-miesto-savivaldos-rinkimuose-sarasa-ves-buskevicius.d?id=92206233
-----------------------------------------
Lietuvoje
Kasčiūnas neabejoja, kad dislokuoti Vokietijos brigadą Lietuva bus pasirengusi 2026-aisiais: bet yra ir vokiečių namų darbai
https://www.delfi.lt/news/daily/lithuania/kasciunas-neabejoja-kad-dislokuoti-vokietijos-brigada-lietuva-bus-pasirengusi-2026-aisiais-bet-yra-ir-vokieciu-namu-darbai.d?id=92206155
-----------------------------------------
Lietuvoje
Opozicija atsargiai vertina šauktinių tarnybos pertvarką: tikrai bus rimta diskusija
https://www.delfi.lt/news/daily/lithuania/opozicija-atsargiai-vertina-sauktiniu-tarnybos-pertvarka-tikrai-bus-rimta-diskusija.d?id=92204207
-----------------------------------------
Lietuvoje
VRK aptarė skundą dėl Majauskui suteiktos verslo paramos, tačiau sprendimo nepriėmė
https://www.delfi.lt/news/daily/lithuania/vrk-aptare-skunda-del-majauskui-suteiktos-verslo-paramos-taciau-sprendimo-neprieme.d?id=92204153
-----------------------------------------
Lietuvoje
Džiugelis konservatoriams tarpušvenčiu jau parengė siurprizą: bendražygiai gerokai nustebę
https://www.delfi.lt/news/daily/lithuania/dziugelis-konservatoriams-tarpusvenciu-jau-parenge-siurpriza-bendrazygiai-gerokai-nustebe.d?id=92197155
-----------------------------------------
Melas
Tikina, kad populiariame šokolade yra grafeno. Tai – melas
https://www.delfi.lt/news/melo-detektorius/melas/tikina-kad-populiariame-sokolade-yra-grafeno-tai-melas.d?id=92169717
-----------------------------------------
Melas
Plinta klaidinga imunologijos mokslo tėvui priskiriama citata
https://www.delfi.lt/news/melo-detektorius/melas/plinta-klaidinga-imunologijos-mokslo-tevui-priskiriama-citata.d?id=92169455
-----------------------------------------
Melas
Supykę dėl FNTT sprendimo netirti Vilniaus Kalėdų eglės įsigijimo aplinkybių išplatino suklastotą nuotrauką
https://www.delfi.lt/news/melo-detektorius/melas/supyke-del-fntt-sprendimo-netirti-vilniaus-kaledu-egles-isigijimo-aplinkybiu-isplatino-suklastota-nuotrauka.d?id=92167733
-----------------------------------------
Melas
Praneša apie Rusijos numuštą savo pačių naikintuvą naudodami seną nuotrauką: ji nėra susijusi su karu Ukrainoje
https://www.delfi.lt/news/melo-detektorius/melas/pranesa-apie-rusijos-numusta-savo-paciu-naikintuva-naudodami-sena-nuotrauka-ji-nera-susijusi-su-karu-ukrainoje.d?id=92167079
-----------------------------------------
Melas
Meluoja, kad žmonės staigiai miršta nuo dirbtinių saldiklių
https://www.delfi.lt/news/melo-detektorius/melas/meluoja-kad-zmones-staigiai-mirsta-nuo-dirbtiniu-saldikliu.d?id=92166599
-----------------------------------------
Melas
Ne, klimato aktyvistės Thunberg konferencija nebuvo atšaukta dėl subarktinio šalčio, tai – satyra
https://www.delfi.lt/news/melo-detektorius/melas/ne-klimato-aktyvistes-thunberg-konferencija-nebuvo-atsaukta-del-subarktinio-salcio-tai-satyra.d?id=92166079
-----------------------------------------
Melas
Iš Didžiosios Britanijos politiko lūpų – melo apie COVID-19 vakcinas porcija
https://www.delfi.lt/news/melo-detektorius/melas/is-didziosios-britanijos-politiko-lupu-melo-apie-covid-19-vakcinas-porcija.d?id=92165631
-----------------------------------------
Melas
Skleidžia sąmokslo teoriją apie kalio jodidą: išgalvojo nebūtų šalutinių poveikių, gąsdina slaptais vyriausybių kėslais
https://www.delfi.lt/news/melo-detektorius/melas/skleidzia-samokslo-teorija-apie-kalio-jodida-isgalvojo-nebutu-salutiniu-poveikiu-gasdina-slaptais-vyriausybiu-keslais.d?id=92163703
-----------------------------------------
Melas
Meluoja, kad rado naujų įrodymų apie COVID-19 vakcinas: jos tikrai nėra žmonijos naikinimo ginklas
https://www.delfi.lt/news/melo-detektorius/melas/meluoja-kad-rado-nauju-irodymu-apie-covid-19-vakcinas-jos-tikrai-nera-zmonijos-naikinimo-ginklas.d?id=92157917
-----------------------------------------
Melas
Ne, tyrimas įrodantis mikroplastikų naudą mitybai neegzistuoja
https://www.delfi.lt/news/melo-detektorius/melas/ne-tyrimas-irodantis-mikroplastiku-nauda-mitybai-neegzistuoja.d?id=92156397
-----------------------------------------
Melas
Dalinasi netikru „Time“ žurnalo viršeliu. Zelenskis pakeistas neatpažįstamai
https://www.delfi.lt/news/melo-detektorius/melas/dalinasi-netikru-time-zurnalo-virseliu-zelenskis-pakeistas-neatpazistamai.d?id=92156105
-----------------------------------------
Melas
Seną įrašą prikėlė antram gyvenimui: kada ir už ką gautas sąskaitas degino šie žmonės?
https://www.delfi.lt/news/melo-detektorius/melas/sena-irasa-prikele-antram-gyvenimui-kada-ir-uz-ka-gautas-saskaitas-degino-sie-zmones.d?id=92155555
-----------------------------------------
Panevėžys
Oficialu: Panevėžio arena nuo šiandien tampa „Kalnapilio arena“
https://www.delfi.lt/miestai/panevezys/oficialu-panevezio-arena-nuo-siandien-tampa-kalnapilio-arena.d?id=92197219
-----------------------------------------
Panevėžys
Šventvagystė Panevėžyje: iš kalėdinės prakartėlės pavogtas Jėzus
https://www.delfi.lt/miestai/panevezys/sventvagyste-panevezyje-is-kaledines-prakarteles-pavogtas-jezus.d?id=92004887

Process finished with exit code 0
     
