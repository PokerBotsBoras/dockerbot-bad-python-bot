# Välkommen till ditt Docker-baserade PokerBot-repo!

> Det här projektet är en **template-repo** i organisationen. När du går med i organisationen bör du automatiskt (eller inom kort) få ett eget repo baserat på den andra mallen. Om du istället vill använda denna mallen kan du starta ett nytt repo genom att gå till [denna repo-sida](https://github.com/PokerBotsBoras/BotTemplate.Docker) och klicka på den gröna knappen **"Use this template"** uppe till höger. Välj sedan "Create new repository", välj organisationen som ägare och döp det till något som börjar på `dockerbot-`(viktigt).

---

## 📦 Valfritt språk – Docker tar hand om det

Till skillnad från C#-botar behöver du inte skriva din bot i .NET. Du kan använda **valfritt språk** (t.ex. Python, C++, Java, Go) så länge din bot följer ett enkelt `stdin`/`stdout`-protokoll.

Ett fungerande exempel i Python finns redan i detta repo (`bot.py` + `Dockerfile`).

---

## 🧠 Bot-protokoll

Din bot kommer att:

- Läsa en `GameState` som JSON från `stdin`
- Svara med en `PokerAction` som JSON på `stdout`
- Hantera specialkommandon som `__name__` (returnerar bot-namn) och `__reset__`

Se `bot.py` för ett minimalt fungerande exempel.

---

## 🐳 Bygg & testa lokalt

```bash
docker build -t mybot .
echo '__name__' | docker run -i mybot
````

```bash
echo '{"MyStack":100,"OpponentStack":100,"Pot":0,"MyCard":{"Rank":"A","Suit":"♠"},"ToCall":0,"MinRaise":2,"ActionHistory":[]}' \
| docker run -i mybot
```

---

## 🚀 Publicera din bot

När du **pushar en tag som börjar på `v`**, t.ex. `v1.0.0`, så körs en GitHub Actions-workflow (`publish.yml`) som automatiskt:

1. Bygger din Docker-image
2. Publicerar den till **GitHub Container Registry (GHCR)**

TournamentRunner hittar och laddar din image därifrån.

### Exempel:

```bash
git tag v1.0.0
git push origin v1.0.0
```

---

## 🏷️ Namnstandard

* Namnge ditt repo `botdocker-vadduvill`
* Din image hamnar automatiskt på:

  ```
  ghcr.io/PokerBotsBoras/botdocker-vadduvill:1.0.0
  ```

TournamentRunner letar efter images i GHCR med prefixet `pokerbot-`.

---

## 📜 Regler

Vi spelar **Heads-Up Micro Hold’em** – ett snabbare och förenklat pokerspel.
Se [Docs/GameRules.md](Docs/GameRules.md) för detaljer.

---

## ❓ Behöver du hjälp?

* Fråga i Discord
* Eller kika på [TournamentRunner](https://github.com/PokerBotsBoras/TournamentRunner) för att förstå hur spelet körs
