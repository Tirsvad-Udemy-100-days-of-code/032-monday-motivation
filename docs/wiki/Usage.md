**English** · [Dansk](Usage-da) · [Bahasa Malaysia](Usage-ms)

# Usage

## Dry run

A dry run shows the email and sends nothing. It needs no credential.

```bash
python -m monday_motivation --dry-run --force
```

![A dry run showing the email](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/raw/branch/main/docs/images/run-dry-run.png)

## Real send

Set three environment variables, then run the program on a Monday. Never put them in a committed file.

```bash
export GMAIL_ADDRESS="you@gmail.com"
export GMAIL_TOKEN="your app password"
export MONDAY_RECIPIENT="friend@example.com"
python -m monday_motivation
```

In PowerShell use `$env:GMAIL_ADDRESS = "you@gmail.com"` and so on. Gmail needs an [app password](https://support.google.com/accounts/answer/185833) (2-step verification must be on).

## Options

| Option | Meaning |
| --- | --- |
| `--dry-run` | Show the email instead of sending it |
| `--force` | Run on any day, not only on a Monday |
| `--quotes PATH` | Use another quotes file, one quote per line |

## Not a Monday

![Run on a day that is not a Monday](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/raw/branch/main/docs/images/run-not-monday.png)

The program does not schedule itself. Start it every Monday with the scheduler of your system if you want it automatic.
