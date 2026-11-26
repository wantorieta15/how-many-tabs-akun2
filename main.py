"""How Many Tabs Do You Have Open? -- entri Akun 2 (@wantorieta15).

Program ini menulis satu angka saja ke /output/entry.txt: jumlah tab
browser yang sedang terbuka. Jawabannya: 5 -- minimalis ekstrem, jauh
di bawah median lapangan (137 tab), bisa dipercaya penuh, dan
mengisyaratkan hidup orang yang menutup semuanya begitu selesai.

Pure stdlib, deterministik, tanpa network.
"""

import os


def build_entry():
    """Kembalikan teks entri beku, persis satu karakter: "5"."""
    return "5"


def write_entry():
    """Tulis entri langsung ke file output (tanpa tempfile/atomic-replace)."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(build_entry())
    os.chmod(path, 0o644)
    return path


def main():
    path = write_entry()
    print("wrote", path)


if __name__ == "__main__":
    main()
