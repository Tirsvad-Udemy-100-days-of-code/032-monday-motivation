[English](Usage) · **Dansk** · [Bahasa Malaysia](Usage-ms)

# Brug

## Prøvekørsel

En prøvekørsel viser e-mailen og sender ingenting. Den kræver ingen loginoplysninger.

```bash
python -m monday_motivation --dry-run --force
```

![En prøvekørsel der viser e-mailen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/raw/branch/main/docs/images/run-dry-run.png)

## Rigtig afsendelse

Sæt tre miljøvariabler og kør programmet en mandag. Skriv dem aldrig i en fil, der bliver committet.

```bash
export GMAIL_ADDRESS="you@gmail.com"
export GMAIL_TOKEN="your app password"
export MONDAY_RECIPIENT="friend@example.com"
python -m monday_motivation
```

I PowerShell bruges `$env:GMAIL_ADDRESS = "you@gmail.com"` og så videre. Gmail kræver en [appadgangskode](https://support.google.com/accounts/answer/185833) (totrinsbekræftelse skal være slået til).

## Valgmuligheder

| Valgmulighed | Betydning |
| --- | --- |
| `--dry-run` | Vis e-mailen i stedet for at sende den |
| `--force` | Kør på alle dage, ikke kun om mandagen |
| `--quotes PATH` | Brug en anden citatfil, ét citat pr. linje |

## Ikke en mandag

![Kørsel på en dag der ikke er mandag](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/raw/branch/main/docs/images/run-not-monday.png)

Programmet planlægger ikke sig selv. Start det hver mandag med dit systems planlægger, hvis det skal være automatisk.
