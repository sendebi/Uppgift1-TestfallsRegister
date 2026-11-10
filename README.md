Testfallsregister

1. Projektbeskrivning

Testfallsregister är ett enkelt konsolbaserat system som ska hjälpa en testgrupp att registrera, organisera och hantera testfall.

Syftet med systemet är att göra det enkelt att hålla ordning på testfall och deras information.

2. Syfte

Syftet med projektet är att skapa ett enkelt system där användaren kan registrera nya testfall, visa befintliga testfall samt redigera och ta bort testfall.

Projektet är också ett tillfälle att träna på objektorienterad programmering (OOP) i Python.

3. Information om testfall

Varje testfall ska innehålla följande information:

ID: Ett unikt ID för varje testfall.

Titel: Namnet på testfallet.

Beskrivning: En kort beskrivning av vad som ska testas.

Förväntat resultat: Beskriver vilket resultat som förväntas när testet utförs.

4. Planerade funktioner

Systemet ska innehålla följande funktioner:

Registrera testfall: Användaren ska kunna lägga till ett nytt testfall.

Visa testfall: Användaren ska kunna visa alla registrerade testfall.

Redigera testfall: Användaren ska kunna ändra informationen i ett befintligt testfall.

Ta bort testfall: Användaren ska kunna ta bort ett registrerat testfall.

Avsluta programmet: Användaren ska kunna avsluta konsolapplikationen.

5. Planerad klassstruktur

Lösningen planeras bestå av två klasser:

TestCase

Representerar ett enskilt testfall och innehåller dess information:

ID

Titel

Beskrivning

Förväntat resultat

TestCaseManager

Ansvarar för att hantera samtliga testfall.

Klassen ska innehålla funktioner för att:

Registrera testfall.

Visa alla testfall.

Redigera befintliga testfall.

Ta bort testfall.

6. Teknisk information

Programmeringsspråk: Python

Programtyp: Konsolapplikation

Programmeringsparadigm: Objektorienterad programmering (OOP)

Datalagring: Testfallen lagras i en lista i programmets minne.

Databas: Ingen databas används.

Informationen sparas endast medan programmet körs och försvinner när programmet avslutas.

7. UML-diagram

Projektets design dokumenteras med följande UML-diagram:

Klassdiagram – visar systemets klasser, attribut, metoder och relationer.

Aktivitetsdiagram – visar systemets arbetsflöde.

Sekvensdiagram – visar kommunikationen mellan användaren och systemets olika delar.

Diagrammen finns i mappen diagrams.

