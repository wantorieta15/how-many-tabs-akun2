"""How Many Tabs Do You Have Open? -- entri revisi Akun 2 (@wantorieta15).

Program ini menulis satu angka saja ke /output/entry.txt: jumlah tab
browser yang sedang terbuka. Jawabannya: 5 -- minimalis ekstrem, jauh
di bawah median lapangan (137 tab), bisa dipercaya penuh, dan
mengisyaratkan hidup orang yang menutup semuanya begitu selesai.

Teks entri BEKU: satu karakter "5", tanpa trailing newline.
sha256("5") = ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d

Pure stdlib, deterministik, tanpa network. Menulis LANGSUNG ke file
output via open() + os.chmod(0o644) -- tanpa tempfile/atomic-replace.
"""

import hashlib
import os

EXPECTED_SHA256 = "ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d"


def build_entry():
    """Kembalikan teks entri beku, persis satu karakter: "5"."""
    return "5"


def validate_entry(text):
    """Validasi entri sebelum ditulis.

    Syarat: tepat satu baris, tanpa newline di mana pun, dan sha256
    harus sama dengan hash yang diharapkan untuk "5".
    """
    if not isinstance(text, str):
        raise ValueError("entri harus berupa str")
    if text == "":
        raise ValueError("entri kosong")
    if "\n" in text or "\r" in text:
        raise ValueError("entri mengandung newline")
    if len(text) != 1:
        raise ValueError("entri harus tepat 1 karakter, dapat %d" % len(text))
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError("sha256 entri tidak cocok: %s" % digest)
    return True


def write_entry():
    """Tulis entri langsung ke file output (tanpa tempfile/atomic-replace)."""
    entry = build_entry()
    validate_entry(entry)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    os.chmod(path, 0o644)
    return path


def main():
    path = write_entry()
    print("wrote", path)


if __name__ == "__main__":
    main()
