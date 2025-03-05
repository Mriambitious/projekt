# Enhetstestning med Pytest

## Projektuppgift
Denna uppgift består av tre delar, varav två ska utföras i grupp. Den tredje delen är individuell och beskrivs i filen `projektarbete_individuellt.pdf`.

### Krav
- Projektet ska läggas upp på **GitHub** och vara **publikt**.
- En **gruppledare** ska ansvara för att ladda upp projektet.
- Endast länken till repositoryt ska lämnas in.
- Projektet ska redovisas muntligt av hela gruppen.

---

## Del 1: Enhetstestning av en SQLite-databas
I denna del ska en **BookDAO-klass** testas, som hanterar en SQLite-databas för böcker.

### Syfte
- Strukturera tester för en databasapplikation.
- Skriva och köra **enhetstester** för CRUD-operationer (Create, Read, Update, Delete).
- Använda `setup_method` och `teardown_method` i pytest.

### Skapa projektet
1. Skapa en ny katalog för projektet och navigera dit.
2. Kopiera `BookDAO`-klassen och `Book`-klassen från [GitHub-repot](https://github.com/hakan-gleissman/projekt_testning_fsh).
3. Lägg filerna från `src/` i projektets **rotmapp**.
4. Skapa en mapp **`tests/`** i projektets rot.
5. I `tests/`, skapa en ny testfil, t.ex. `test_book_dao.py`.
6. Installera pytest om det inte redan finns:
   ```bash
   pip install pytest
   ```

### Strukturera testklassen
1. **Importera** `BookDAO` och `Book`.
2. **Skapa en testklass** där testmetoder organiseras.
3. **`setup_method`**:
   - Skapa en instans av `BookDAO` med en testdatabas.
   - Lägg till tre böcker i databasen.
4. **`teardown_method`**:
   - Töm tabellen `Book`.
   - Stäng databasen.

#### Exempel på `setup_method` och `teardown_method`
```python
class TestBookDAO:
    def setup_method(self):
        # Skapa instans av BookDAO
        # Lägg till tre böcker i databasen

    def teardown_method(self):
        # Töm tabellen Book
        # Stäng databasen
```

### Testkrav för **G**-betyg
- Testa att databasen innehåller tre böcker.
- Lägg till en bok och verifiera att databasen innehåller fyra böcker.
- Hämta en bok via titel och verifiera dess beskrivning.
- Uppdatera en boks beskrivning och verifiera ändringen.
- Radera en bok och verifiera att den inte längre finns.

### Testkrav för **VG**-betyg
- Läs på om **fixtures** i pytest.
- Ersätt `setup_method` med en **fixture**.

---

## Del 2: Testning av konfiguration på en Linux-server
Denna del testar klassen **NetworkConfigManager**, som hanterar nätverkskonfigurationer via en Linux-server i en Docker-container.

### Syfte
- Skriva och köra tester för att verifiera konfigurationsuppdateringar.

### Installation och setup
1. Använd samma projekt som i del 1.
2. Kopiera `network_config_manager.py` från samma GitHub-repo.
3. Lägg filen i projektets **rotmapp**.
4. Skapa en ny testfil i `tests/`, t.ex. `test_network_config.py`.
5. Installera **netmiko**:
   ```bash
   pip install netmiko
   ```

### Strukturera testklassen
1. **Importera** `NetworkConfigManager`.
2. **Skapa en testklass**.
3. **`setup_method`**:
   - Skapa en instans av `NetworkConfigManager`.
   - Anropa `connect()` för att etablera en **SSH-anslutning**.
   - Återställ konfigurationsvärden:
     ```python
     update_hostname("1")
     update_interface_state("down")
     update_response_prefix("Standard Response")
     ```
4. **`teardown_method`**:
   - Stäng SSH-anslutningen med `disconnect()`.

### Testkrav för **G**-betyg
- **Verifiera standardvärden efter setup:**
  - `show_host_name` ska returnera **"hostname : 1"**
  - `show_interface_state` ska returnera **"interface_state : down"**
  - `show_response_prefix` ska returnera **"response_prefix : Standard Response"**
- **Testa uppdatering av konfiguration:**
  - Uppdatera och verifiera ändringar för `hostname`, `interface_state` och `response_prefix`.
  - Endast **"up"** och **"down"** ska vara godkända värden för `interface_state`.

### Testkrav för **VG**-betyg
- Skriv en testmetod som försöker sätta `interface_state` till ett otillåtet värde och verifiera att ett **exception kastas**.
- Ersätt `setup_method` med en **fixture**.

---

## Köra testerna
För att köra testerna, navigera till projektets rotmapp och kör:
```bash
pytest
```

---

## Verktyg och bibliotek
- **Python** (3.x)
- **pytest**
- **SQLite**
- **Docker**
- **netmiko** (för nätverkstester)

---


---

