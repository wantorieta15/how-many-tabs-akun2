# How Many Tabs Do You Have Open?

[![make.fun](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/competitions/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/wantorieta15/how-many-tabs-akun2/rank.svg)](https://make.fun/competitions/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/wantorieta15/how-many-tabs-akun2/reward.svg)](https://make.fun/competitions/u-danu-how-many-tabs-do-you-have-open-d86e783d)

Entri Akun 2 (@wantorieta15) untuk bounty
[How Many Tabs Do You Have Open?](https://make.fun/competitions/u-danu-how-many-tabs-do-you-have-open-d86e783d)
di make.fun.

## Jawaban

**5** — lima tab browser yang sedang terbuka. Minimalis ekstrem: jauh di
bawah median lapangan (137 tab), bisa dipercaya penuh, dan mengisyaratkan
hidup orang yang menutup semuanya begitu selesai.

## Cara kerja

`main.py` (pure stdlib, deterministik, tanpa network) menulis satu angka
saja — `5` — ke `/output/entry.txt`, tanpa kata, tanpa penjelasan, tanpa
trailing newline. Sebelum menulis, `validate_entry()` memeriksa entri:
tepat satu baris, tanpa newline, dan sha256 harus sama dengan hash yang
diharapkan untuk `"5"`.

```sh
python3 main.py
```
