[English](Usage) · [Dansk](Usage-da) · **Bahasa Malaysia**

# Penggunaan

## Larian cuba

Larian cuba memaparkan e-mel dan tidak menghantar apa-apa. Ia tidak memerlukan sebarang kelayakan log masuk.

```bash
python -m monday_motivation --dry-run --force
```

![Larian cuba yang memaparkan e-mel](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/raw/branch/main/docs/images/run-dry-run.png)

## Penghantaran sebenar

Tetapkan tiga pemboleh ubah persekitaran, kemudian jalankan program pada hari Isnin. Jangan sekali-kali menulisnya dalam fail yang di-commit.

```bash
export GMAIL_ADDRESS="you@gmail.com"
export GMAIL_TOKEN="your app password"
export MONDAY_RECIPIENT="friend@example.com"
python -m monday_motivation
```

Dalam PowerShell gunakan `$env:GMAIL_ADDRESS = "you@gmail.com"` dan seterusnya. Gmail memerlukan [kata laluan aplikasi](https://support.google.com/accounts/answer/185833) (pengesahan 2 langkah mesti dihidupkan).

## Pilihan

| Pilihan | Maksud |
| --- | --- |
| `--dry-run` | Papar e-mel dan bukan menghantarnya |
| `--force` | Jalankan pada mana-mana hari, bukan hanya hari Isnin |
| `--quotes PATH` | Guna fail petikan lain, satu petikan setiap baris |

## Bukan hari Isnin

![Larian pada hari yang bukan Isnin](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/raw/branch/main/docs/images/run-not-monday.png)

Program ini tidak menjadualkan dirinya sendiri. Mulakannya setiap Isnin dengan penjadual sistem anda jika mahu ia berjalan secara automatik.
