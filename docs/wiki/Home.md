**English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

# Monday Motivation

Monday Motivation sends a motivational quote by email every Monday. It is a small Python solution to day 32 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp", with tests and no runtime dependencies.

![A dry run showing the email](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/raw/branch/main/docs/images/run-dry-run.png)

## Pages

- [Getting started](Getting-Started): requirements, `.venv`, `pip`, installation
- [Usage](Usage): run, dry run, options, Gmail app password
- [Development](Development): layout, tests, checks, Doxygen

## How it works

1. Check that today is a Monday (`is_monday`).
2. Read the quotes (`read_quotes`) and pick one at random (`pick_random_quote`).
3. Build the email with the subject "Monday Motivation" (`build_message`) and send it through Gmail (`send_email`).
