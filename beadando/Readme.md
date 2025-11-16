Blackjack KPM

Hallgató
Név:  Knapik Péter Mátyás
Neptunkód: JPAOEU

 A program leírása
A program egy egyszerű Blackjack (21) játék.  
A játék konzolról irányítható, a Turtle modul pedig kiírja az osztó és a játékos lapjait és pontszámait egy ablakba.

A játék addig megy, amíg a felhasználó ki nem lép.

Működés röviden
- A játékos és az osztó két-két lapot kap.
- Az osztó második lapja a játékos döntéséig rejtve van.
- A játékos beírhatja:
  - i – kérek még lapot  
  - n – megállok  
  - v – kilépek  
- Ha a játékos megáll, az osztó 17 pontig húz.
- Kiértékeljük, ki nyert.
- Új kör indul.

Az Ász értéke 11, de ha így túl sok lenne, akkor 1-nek számít.

Modulok
- random – pakli keverése és lapok húzása  
- turtle– a lapok és pontszámok egyszerű grafikus kiírása  
- beadando_KPM.py** – saját modul  

Saját modul és osztály
- Modul neve: `beadando_KPM.py`
- Saját osztály: `BlackjackKPM`
- Ebben vannak:
  - a paklikészítő függvény  
  - a pontszámító függvény  
  - a grafikus kiírás  
  - a játék fő ciklusa  

Minden saját függvény és az osztály neve is tartalmazza a KPM monogramot.

Indítás
A program a main.py fájlból indul:

bash
python main.py
