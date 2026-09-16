# Comprehensive HTML Plan + Report Skill

Repository publik ini berisi skill universal untuk membantu AI Agent merencanakan dan melaporkan pekerjaan proyek apa pun dengan dua HTML yang mudah dipahami. Tidak ada runtime dependency dan tidak ada data proyek tertentu.

## Isi repository

- `skills/comprehensive-html-plan-report/SKILL.md` — aturan workflow untuk AI Agent.
- `PROJECT_PLAN_TEMPLATE.html` — template yang diisi sebelum implementasi.
- `PROJECT_REPORT_TEMPLATE.html` — template yang diisi setelah verifikasi.
- `scripts/validate_templates.py` — validator offline untuk anchor, toggle, dan privacy marker.

## Hasil yang selalu dibuat

1. **Plan HTML** dibuat sebelum implementasi. Ini menjadi kontrak kerja untuk AI Agent dan manusia: tujuan, urutan checklist, risiko, security boundary, definition of done, serta detail tiap item.
2. **Report HTML** dibuat setelah implementasi dan verifikasi. Ini menjadi pertanggungjawaban AI Agent kepada manusia: status, bukti command, test, commit, link MR/PR, blocker, dan action owner.

Format standarnya: TL;DR non-teknis, tabel keputusan/evidence, checklist, CTA `Lihat detail` ke section detail di bagian bawah, dan link kembali ke checklist. Untuk proyek lain, nama file dan isinya mengikuti proyek tersebut; jangan menyalin identifier atau claim dari project contoh.

## Contoh template generic

- [PROJECT_PLAN_TEMPLATE.html](./PROJECT_PLAN_TEMPLATE.html) — salin dan isi sebelum implementasi.
- [PROJECT_REPORT_TEMPLATE.html](./PROJECT_REPORT_TEMPLATE.html) — salin dan isi setelah verifikasi.

Kedua template tidak mengandung data proyek tertentu. Ganti semua placeholder `[dalam kurung siku]`, sesuaikan jumlah checklist, lalu pertahankan pasangan ID CTA dan detailnya.

## Cara memakai

Salin folder `skills/comprehensive-html-plan-report` ke direktori skill AI Agent yang dipakai, misalnya `~/.codex/skills/comprehensive-html-plan-report/`. Pada prompt task, sebutkan:

```text
Gunakan skill comprehensive-html-plan-report. Buat PLAN.html sebelum perubahan,
jalankan implementasi setelah plan jelas, lalu buat REPORT.html berbasis bukti.
Gunakan nama/path output ini: <path-plan> dan <path-report>.
Jangan memasukkan secret. Commit/push hanya jika saya minta.
```

Skill ini tidak menggantikan instruksi system, developer, repository, atau user. Ia hanya memberi kontrak output dan verifikasi yang konsisten.

## Privacy dan lisensi

Repository ini sengaja tidak memuat password, token, private key, credential file, path komputer, IP address, email pribadi, atau data project contoh. Lisensinya MIT; baca `SECURITY.md` sebelum mengirim perubahan.

## Aturan skill yang penting

- Ponytail **wajib dibaca dan digunakan 100% untuk semua jenis task**, tanpa pengecualian.
- `ui-ux-pro-max` dan `emil-design-eng` **wajib dibaca lengkap hanya jika task berkaitan dengan UI/UX**, termasuk layout HTML, navigasi anchor, accessibility, motion, atau interaksi.
- Jika task tidak berkaitan dengan UI/UX, dua skill UI/UX tersebut **dilarang dibaca atau digunakan**. Jangan load “just in case”.
- Plan checklist dan report checklist-result wajib memiliki CTA kecil yang bisa di-keyboard dan auto-scroll ke detail item yang sama di bagian bawah.
- Section `Detail setiap checklist` wajib berupa native `<details>` yang **hidden/collapsed by default**. CTA boleh membukanya saat diklik; jangan menambahkan atribut `open` saat page load.
- Report harus jujur terhadap evidence: `BLOCKED`, `SKIPPED`, dan `NOT RUN` lebih benar daripada claim pass tanpa bukti.

## Cek cepat sebelum handoff

```sh
git diff --check
tidy -q -e -utf8 <PLAN.html> <REPORT.html>
python3 scripts/validate_templates.py
```

Pastikan setiap `href="#detail-..."` punya target ID tepat satu kali, setiap detail punya link kembali, HTML bisa dibuka offline, dan tidak ada password, token, private key, atau service-account JSON di file.
