#!/usr/bin/env python3
# Build a single, self-contained, content-encoded landing page (index.html).
import base64, os, json

ROOT = os.path.dirname(os.path.abspath(__file__))
OPT = os.path.join(ROOT, "assets", "opt")

def datauri(name):
    with open(os.path.join(OPT, name), "rb") as f:
        b = f.read()
    return "data:image/jpeg;base64," + base64.b64encode(b).decode("ascii")

HERO  = datauri("hero.jpg")
SPEC  = datauri("spec.jpg")
WHITE = datauri("white.jpg")
BLUE  = datauri("blue.jpg")

# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------
CSS = r"""
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --navy:#13203f;--navy2:#0c1730;--red:#e11900;--red2:#ff2d12;
  --orange:#ff7a00;--gold:#ffd23f;--green:#16a34a;--ink:#1a1a1a;
  --soft:#f4f6fb;--line:#e7eaf2;--wa:#1ebe5d;
}
html{-webkit-text-size-adjust:100%}
body{
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans","Apple Color Emoji","Segoe UI Emoji",sans-serif;
  color:var(--ink);background:#fff;line-height:1.5;overflow-x:hidden;
  -webkit-user-select:none;user-select:none;-webkit-tap-highlight-color:transparent;
}
img{max-width:100%;display:block;-webkit-user-drag:none;user-drag:none;pointer-events:none}
.wrap{width:100%;max-width:600px;margin:0 auto;padding:0 16px}
section{width:100%}
h1,h2,h3{line-height:1.18;letter-spacing:-.01em}
b,strong{font-weight:800}
.hl{color:var(--red);font-weight:900}
.hl2{background:linear-gradient(transparent 55%,var(--gold) 55%);padding:0 2px}

/* top bar */
.topbar{position:sticky;top:0;z-index:60;background:linear-gradient(90deg,var(--red),var(--red2));
  color:#fff;text-align:center;font-size:13px;font-weight:700;padding:9px 12px;letter-spacing:.2px}
.topbar b{background:rgba(0,0,0,.22);padding:1px 7px;border-radius:6px;font-variant-numeric:tabular-nums}

/* hero */
.hero{background:radial-gradient(120% 90% at 50% 0%,#1c2d57 0%,var(--navy) 45%,var(--navy2) 100%);color:#fff;padding:22px 0 30px;text-align:center}
.pill{display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.12);
  border:1px solid rgba(255,255,255,.22);color:#fff;font-size:11px;font-weight:700;
  padding:5px 11px;border-radius:999px;margin:0 4px 10px;text-transform:uppercase;letter-spacing:.4px}
.pill .d{color:var(--gold)}
.hero h1{font-size:30px;font-weight:900;margin:6px 0 8px}
.hero h1 em{font-style:normal;color:var(--gold)}
.hero .sub{font-size:15px;color:#cfd8ee;max-width:480px;margin:0 auto 14px}
.heroimg{position:relative;max-width:420px;margin:6px auto 6px}
.heroimg img{border-radius:18px;box-shadow:0 22px 50px rgba(0,0,0,.45)}
.heroimg .flame{position:absolute;top:-8px;right:6px;background:var(--red);color:#fff;font-size:11px;
  font-weight:800;padding:6px 10px;border-radius:999px;transform:rotate(7deg);box-shadow:0 6px 16px rgba(225,25,0,.5)}
.stars{color:var(--gold);font-size:18px;letter-spacing:2px}
.rate{font-size:13px;color:#dfe6f6;margin:8px 0 4px}
.rate b{color:#fff}
.pricewrap{margin:14px 0 6px}
.old{color:#9fb0d6;text-decoration:line-through;font-size:18px;font-weight:700}
.now{color:var(--gold);font-size:44px;font-weight:900;line-height:1;display:block;margin-top:2px}
.save{display:inline-block;background:var(--red);color:#fff;font-size:12px;font-weight:800;
  padding:4px 10px;border-radius:8px;margin-top:8px;text-transform:uppercase}

/* CTA */
.cta{display:block;width:100%;max-width:440px;margin:16px auto 0;background:linear-gradient(90deg,#ff8a00,#ff5a00);
  color:#fff;text-decoration:none;font-size:19px;font-weight:900;padding:17px 18px;border-radius:14px;
  border:none;cursor:pointer;box-shadow:0 12px 26px rgba(255,90,0,.45);text-transform:uppercase;letter-spacing:.3px;
  animation:pulse 1.5s infinite}
.cta small{display:block;font-size:11px;font-weight:700;opacity:.95;letter-spacing:.4px;text-transform:none;margin-top:2px}
@keyframes pulse{0%{transform:scale(1)}50%{transform:scale(1.025)}100%{transform:scale(1)}}
.cta:active{transform:scale(.98)}
.undercta{font-size:12px;color:#bcc8e6;margin-top:10px}

/* social bar */
.social{background:#fff7e6;border-top:1px solid #ffe6ad;border-bottom:1px solid #ffe6ad;padding:12px 0}
.social .wrap{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;text-align:center;font-size:12.5px;font-weight:700;color:#7a5a00}
.social b{color:var(--red);font-size:15px}

/* generic section */
.sec{padding:34px 0}
.sec.alt{background:var(--soft)}
.sec.dark{background:var(--navy);color:#fff}
.kicker{text-align:center;color:var(--red);font-weight:800;font-size:12px;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:6px}
.sec.dark .kicker{color:var(--gold)}
.h2{text-align:center;font-size:24px;font-weight:900;margin-bottom:6px}
.lead{text-align:center;color:#5b6479;max-width:520px;margin:0 auto 20px;font-size:15px}
.sec.dark .lead{color:#c6cfe6}

/* problem cards */
.prob{display:grid;grid-template-columns:1fr;gap:12px}
.prob .c{background:#fff;border:1px solid var(--line);border-left:5px solid var(--red);border-radius:12px;padding:14px 16px;font-size:14.5px}
.prob .c b{display:block;font-size:15px;margin-bottom:2px}
.prob .c .em{font-size:22px;margin-right:6px}

/* feature list */
.feat{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.feat .f{background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px 14px;text-align:center;box-shadow:0 4px 14px rgba(15,25,60,.05)}
.feat .f .ic{font-size:30px}
.feat .f b{display:block;font-size:14px;margin:8px 0 3px}
.feat .f p{font-size:12.5px;color:#5b6479}

.specimg{margin:18px auto 0;max-width:460px}
.specimg img{border-radius:16px;box-shadow:0 12px 30px rgba(15,25,60,.18)}

/* comparison */
.cmp{width:100%;border-collapse:collapse;font-size:13px;background:#fff;border-radius:14px;overflow:hidden;box-shadow:0 8px 24px rgba(15,25,60,.1)}
.cmp th,.cmp td{padding:11px 9px;text-align:center;border-bottom:1px solid var(--line)}
.cmp thead th{background:var(--navy);color:#fff;font-size:12px}
.cmp thead th.us{background:var(--red)}
.cmp td.lbl{text-align:left;font-weight:700;background:var(--soft);font-size:12.5px}
.cmp td.us{background:#fff5f3;font-weight:800;color:var(--green)}
.cmp .x{color:#c0392b;font-weight:800}
.cmp .ok{color:var(--green);font-weight:800}

/* variants / bundles */
.opts{display:grid;grid-template-columns:1fr;gap:12px;margin-top:6px}
.opt{display:flex;align-items:center;gap:12px;border:2px solid var(--line);background:#fff;border-radius:14px;padding:12px;cursor:pointer;position:relative;transition:.15s}
.opt.act{border-color:var(--red);box-shadow:0 8px 22px rgba(225,25,0,.16)}
.opt img{width:64px;height:64px;border-radius:10px;object-fit:cover;flex:none;border:1px solid var(--line)}
.opt .oi{flex:1}
.opt .oi b{font-size:15px}
.opt .oi .d{font-size:12px;color:#5b6479}
.opt .op{text-align:right;flex:none}
.opt .op .o{color:#9aa3b8;text-decoration:line-through;font-size:12px}
.opt .op .n{font-weight:900;font-size:17px;color:var(--navy)}
.opt .tag{position:absolute;top:-10px;left:12px;background:var(--green);color:#fff;font-size:10px;font-weight:800;padding:3px 8px;border-radius:7px;text-transform:uppercase}
.opt .tag.hot{background:var(--red)}
.radio{width:20px;height:20px;border-radius:50%;border:2px solid #c2cadb;flex:none;display:grid;place-items:center}
.opt.act .radio{border-color:var(--red)}
.opt.act .radio::after{content:"";width:10px;height:10px;border-radius:50%;background:var(--red)}

/* testimonials */
.tsts{display:grid;grid-template-columns:1fr;gap:14px}
.tst{background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px;box-shadow:0 6px 18px rgba(15,25,60,.06)}
.tst .top{display:flex;align-items:center;gap:10px;margin-bottom:8px}
.tst .av{width:42px;height:42px;border-radius:50%;background:var(--navy);color:#fff;display:grid;place-items:center;font-weight:800;font-size:16px;flex:none}
.tst .nm{font-weight:800;font-size:14px}
.tst .vf{font-size:11px;color:var(--green);font-weight:700}
.tst .st{color:var(--gold);font-size:14px;margin-left:auto}
.tst p{font-size:14px;color:#374151}
.tst .q{font-weight:800;color:var(--ink)}

/* guarantee */
.guar{display:grid;grid-template-columns:1fr;gap:12px}
.guar .g{display:flex;gap:12px;align-items:flex-start;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-radius:14px;padding:14px}
.guar .g .ic{font-size:26px;flex:none}
.guar .g b{font-size:15px;color:var(--gold)}
.guar .g p{font-size:13px;color:#cfd8ee}

/* faq */
.faq{max-width:560px;margin:0 auto}
.qa{background:#fff;border:1px solid var(--line);border-radius:12px;margin-bottom:10px;overflow:hidden}
.qa .q{padding:14px 16px;font-weight:700;font-size:14.5px;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:10px}
.qa .q .pm{color:var(--red);font-weight:900;font-size:20px;flex:none;transition:.2s}
.qa.open .q .pm{transform:rotate(45deg)}
.qa .a{max-height:0;overflow:hidden;transition:max-height .25s ease;padding:0 16px}
.qa.open .a{max-height:320px;padding:0 16px 14px}
.qa .a p{font-size:13.5px;color:#4b5563}

/* order form */
.order{background:linear-gradient(160deg,#1c2d57,var(--navy2));color:#fff}
.card{background:#fff;color:var(--ink);border-radius:18px;padding:18px;box-shadow:0 18px 40px rgba(0,0,0,.35);max-width:520px;margin:0 auto}
.card h3{text-align:center;font-size:20px;margin-bottom:4px}
.card .small{text-align:center;font-size:12px;color:#6b7280;margin-bottom:14px}
.fld{margin-bottom:12px}
.fld label{display:block;font-size:12.5px;font-weight:700;margin-bottom:5px}
.fld input,.fld textarea,.fld select{width:100%;border:1.5px solid var(--line);border-radius:10px;padding:12px;font-size:15px;font-family:inherit;background:#fff;-webkit-user-select:text;user-select:text}
.fld textarea{min-height:70px;resize:vertical}
.fld input:focus,.fld textarea:focus,.fld select:focus{outline:none;border-color:var(--red)}
.qty{display:flex;gap:8px}
.qty button{flex:none;width:46px;font-size:22px;font-weight:800;border:1.5px solid var(--line);background:var(--soft);border-radius:10px;cursor:pointer}
.qty input{text-align:center}
.totbox{background:var(--soft);border-radius:12px;padding:12px 14px;margin:4px 0 14px;font-size:14px}
.totbox .r{display:flex;justify-content:space-between;margin:3px 0}
.totbox .r.tot{font-size:18px;font-weight:900;border-top:1px dashed #cbd2e0;padding-top:8px;margin-top:6px}
.totbox .r.tot b{color:var(--red)}
.btnwa{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;background:var(--wa);color:#fff;border:none;
  font-size:18px;font-weight:900;padding:16px;border-radius:13px;cursor:pointer;box-shadow:0 10px 24px rgba(30,190,93,.4)}
.btnwa:active{transform:scale(.98)}
.formnote{text-align:center;font-size:11.5px;color:#dfe6f6;margin-top:12px}
.err{color:var(--red);font-size:12px;margin-top:4px;display:none}

/* sticky buy bar */
.sticky{position:fixed;left:0;right:0;bottom:0;z-index:55;background:#fff;border-top:1px solid var(--line);
  box-shadow:0 -6px 20px rgba(0,0,0,.12);padding:9px 12px;display:flex;align-items:center;gap:10px;
  transform:translateY(120%);transition:transform .3s}
.sticky.show{transform:translateY(0)}
.sticky .p{flex:1;line-height:1.1}
.sticky .p .o{color:#9aa3b8;text-decoration:line-through;font-size:12px}
.sticky .p .n{font-weight:900;font-size:19px;color:var(--navy)}
.sticky .p .s{font-size:10.5px;color:var(--red);font-weight:800}
.sticky a{flex:none;background:linear-gradient(90deg,#ff8a00,#ff5a00);color:#fff;text-decoration:none;
  font-weight:900;font-size:15px;padding:13px 18px;border-radius:11px}
@media(max-width:380px){.sticky a{padding:13px 13px;font-size:14px}}

/* toast */
.toast{position:fixed;left:12px;bottom:74px;z-index:50;background:#fff;border:1px solid var(--line);
  border-radius:12px;box-shadow:0 10px 26px rgba(0,0,0,.18);padding:10px 12px;display:flex;gap:10px;align-items:center;
  max-width:300px;transform:translateX(-130%);transition:transform .4s;opacity:0}
.toast.show{transform:translateX(0);opacity:1}
.toast .ti{width:38px;height:38px;border-radius:9px;flex:none;background-size:cover;background-position:center;border:1px solid var(--line)}
.toast .tt{font-size:12px;line-height:1.3}
.toast .tt b{font-size:12.5px}
.toast .tt .ag{color:#8a93a6;font-size:10.5px}
.toast .chk{color:var(--green);font-weight:800;font-size:11px}

/* footer */
.foot{background:var(--navy2);color:#8c99bd;text-align:center;font-size:11.5px;padding:22px 16px 90px}
.foot b{color:#cfd8ee}

.spacer{height:18px}
.center{text-align:center}
.countbig{font-variant-numeric:tabular-nums}
.timer{display:flex;gap:8px;justify-content:center;margin:10px 0 4px}
.timer .t{background:var(--navy);color:#fff;border-radius:10px;padding:8px 10px;min-width:54px;text-align:center}
.sec.dark .timer .t,.timer .t{background:rgba(0,0,0,.25)}
.timer .t b{font-size:24px;display:block;line-height:1}
.timer .t span{font-size:10px;text-transform:uppercase;opacity:.8;letter-spacing:.5px}
.order .timer .t{background:rgba(255,255,255,.12)}

/* OrderOnline embed — let OO use its own styling; just enable input usability */
.ooef{position:relative;min-height:56px}
.ooef,.ooef *{ -webkit-user-select:auto;user-select:auto}
"""

# ---------------------------------------------------------------------------
# CONTENT (inner HTML, will be encoded)
# ---------------------------------------------------------------------------
CONTENT = r"""
<style>__CSS__</style>

<div class="topbar">🔥 FLASH SALE BERAKHIR DALAM <b id="cdTop">14:59</b> &nbsp;•&nbsp; STOK SISA <b id="stockTop">17</b> PCS</div>

<header class="hero">
  <div class="wrap">
    <span class="pill"><span class="d">●</span> #1 TERLARIS 2026</span>
    <span class="pill">🚚 BAYAR DI TEMPAT (COD)</span>
    <h1>Masak Jadi <em>10x Lebih Cepat</em><br>Tanpa Pisau, Tanpa Air Mata!</h1>
    <p class="sub">Electric Garlic Chopper &mdash; cincang bawang, cabai, daging & bumbu <b>HANYA 3 DETIK</b> cuma dengan SATU pencetan. Dapur kotor & jari teriris? Lupakan selamanya.</p>
    <div class="heroimg">
      <span class="flame">🔥 12.847 TERJUAL</span>
      <img src="__HERO__" alt="Electric Garlic Chopper" width="420" height="420" fetchpriority="high">
    </div>
    <div class="stars">★★★★★</div>
    <div class="rate"><b>4,9/5</b> dari <b>12.847+</b> pembeli puas se-Indonesia</div>
    <div class="pricewrap">
      <span class="old">Rp349.000</span>
      <span class="now">Rp159.000</span>
      <span class="save">⚡ HEMAT Rp190.000 (54%) — HARI INI SAJA</span>
    </div>
    <button class="cta" data-scroll="#order">PESAN SEKARANG 🛒<small>Bayar di tempat • Gratis ongkir hari ini</small></button>
    <div class="undercta">✅ Tanpa DP &nbsp; ✅ Cek barang dulu &nbsp; ✅ Kirim hari ini juga</div>
  </div>
</header>

<section class="social">
  <div class="wrap">
    <div>🛒 <b>347</b> orang beli hari ini</div>
    <div>👀 <b>91</b> orang lihat sekarang</div>
    <div>⭐ <b>4,9</b> rating toko</div>
  </div>
</section>

<!-- PROBLEM / hidden education -->
<section class="sec">
  <div class="wrap">
    <div class="kicker">Berhenti menyiksa diri sendiri</div>
    <h2 class="h2">Masih Cincang Bawang Pakai Pisau? 😤</h2>
    <p class="lead">Setiap hari kamu buang waktu & tenaga untuk hal yang bisa selesai dalam <b>3 detik</b>. Ini yang diam-diam bikin masak terasa berat:</p>
    <div class="prob">
      <div class="c"><b><span class="em">😭</span>Mata perih & nangis tiap iris bawang</b>Bukan kamu lemah — uap bawang memang bikin mata pedih. Wadah tertutup chopper ini bikin nangis jadi sejarah.</div>
      <div class="c"><b><span class="em">⏰</span>15 menit cuma buat bumbu</b>Belum masak sudah capek. Padahal motor torsi tinggi kami selesaikan dalam <b>3 detik</b>.</div>
      <div class="c"><b><span class="em">🩹</span>Jari kena pisau</b>Sekali lengah, luka seminggu. Pisau berputar aman di dalam wadah — tangan tidak akan pernah menyentuh mata pisau.</div>
      <div class="c"><b><span class="em">🍳</span>Hasil potongan tidak rata</b>Potongan besar-kecil bikin matang tidak merata & masakan kurang sedap. 4 mata pisau baja kami mencincang <b>rata sempurna</b>.</div>
    </div>
  </div>
</section>

<!-- FEATURES -->
<section class="sec alt">
  <div class="wrap">
    <div class="kicker">Kenapa ini beda</div>
    <h2 class="h2">1 Alat, Ganti 5 Peralatan Dapur 🔪</h2>
    <p class="lead">Diam-diam ini "senjata rahasia" para chef rumahan. Begini cara kerjanya:</p>
    <div class="feat">
      <div class="f"><div class="ic">⚡</div><b>Cincang 3 Detik</b><p>Motor torsi tinggi 360°. Pencet sekali, langsung halus merata.</p></div>
      <div class="f"><div class="ic">🔋</div><b>USB Cas, Tanpa Kabel</b><p>Sekali cas tahan sampai <b>1 bulan</b> pemakaian. Bawa ke mana saja.</p></div>
      <div class="f"><div class="ic">🗡️</div><b>4 Mata Pisau Baja</b><p>Stainless steel anti karat & super tajam. Tembus daging beku sekalipun.</p></div>
      <div class="f"><div class="ic">🧼</div><b>Cuci 5 Detik</b><p>Bilas wadah & pisau, selesai. Tidak ada lagi talenan & pisau menumpuk.</p></div>
      <div class="f"><div class="ic">👶</div><b>Aman & Senyap</b><p>Tutup terkunci, tidak nyala kalau belum rapat. Aman dekat anak.</p></div>
      <div class="f"><div class="ic">🥗</div><b>Serba Bisa</b><p>Bawang, cabai, daging, MPASI, salsa, pesto — semua beres.</p></div>
    </div>
    <div class="specimg"><img src="__SPEC__" alt="Spesifikasi Electric Garlic Chopper" width="460" height="460" loading="lazy"></div>
  </div>
</section>

<!-- COMPARISON / overclaim -->
<section class="sec">
  <div class="wrap">
    <div class="kicker">Bandingkan sendiri</div>
    <h2 class="h2">Kenapa Ribuan Orang Pindah ke Sini</h2>
    <p class="lead">Sekali lihat tabel ini, kamu nggak akan mau balik ke pisau lagi.</p>
    <table class="cmp">
      <thead><tr><th>&nbsp;</th><th class="us">PRODUK KAMI</th><th>Pisau Manual</th><th>Chopper Murahan</th></tr></thead>
      <tbody>
        <tr><td class="lbl">Waktu cincang</td><td class="us">3 detik ⚡</td><td class="x">10–15 mnt</td><td>1–2 mnt</td></tr>
        <tr><td class="lbl">Bikin nangis?</td><td class="us ok">Tidak ✓</td><td class="x">Selalu 😭</td><td class="x">Sering</td></tr>
        <tr><td class="lbl">Hasil rata</td><td class="us ok">Sempurna ✓</td><td class="x">Acak-acakan</td><td>Lumayan</td></tr>
        <tr><td class="lbl">Tenaga tangan</td><td class="us ok">0 (1 pencet)</td><td class="x">Pegal ✗</td><td>Perlu colok</td></tr>
        <tr><td class="lbl">Baterai isi ulang</td><td class="us ok">USB, 1 bln ✓</td><td class="x">—</td><td class="x">Pakai kabel</td></tr>
        <tr><td class="lbl">Mata pisau baja</td><td class="us ok">4 buah ✓</td><td class="x">1 (bahaya)</td><td>2</td></tr>
        <tr><td class="lbl">Harga</td><td class="us ok">Rp159rb</td><td>Rp50rb+luka</td><td>Rp250rb+</td></tr>
      </tbody>
    </table>
  </div>
</section>

<!-- VARIANTS / BUNDLE -->
<section class="sec alt" id="pilih">
  <div class="wrap">
    <div class="kicker">Pilih punyamu</div>
    <h2 class="h2">Pilih Paket Hemat 🎁</h2>
    <p class="lead">Paket isi lebih dari 1 jadi <b>rebutan</b> — banyak yang beli buat stok & kado. Stok paket bundling terbatas!</p>

    <p class="center" style="font-weight:800;margin-bottom:8px">Pilih Paket:</p>
    <div class="opts" id="bundleOpts">
      <div class="opt" data-qty="1" data-price="159000">
        <div class="radio"></div>
        <div class="oi"><b>1 PCS</b><div class="d">Coba dulu</div></div>
        <div class="op"><span class="o">Rp349.000</span><span class="n">Rp159.000</span></div>
      </div>
      <div class="opt act" data-qty="2" data-price="289000">
        <div class="radio"></div>
        <span class="tag hot">Paling Laris 🔥</span>
        <div class="oi"><b>2 PCS</b><div class="d">1 dipakai, 1 buat kado</div></div>
        <div class="op"><span class="o">Rp698.000</span><span class="n">Rp289.000</span></div>
      </div>
      <div class="opt" data-qty="3" data-price="399000">
        <div class="radio"></div>
        <span class="tag">Hemat Maksimal</span>
        <div class="oi"><b>3 PCS</b><div class="d">Rp133rb/pcs — termurah!</div></div>
        <div class="op"><span class="o">Rp1.047.000</span><span class="n">Rp399.000</span></div>
      </div>
    </div>
    <button class="cta" data-scroll="#order" style="margin-top:18px">AMBIL PAKET INI 🛒<small>Stok bundling tinggal sedikit hari ini</small></button>
  </div>
</section>

<!-- TESTIMONIALS -->
<section class="sec">
  <div class="wrap">
    <div class="kicker">Kata mereka (jujur, brutal)</div>
    <h2 class="h2">12.847 Orang, Rating 4,9 ⭐</h2>
    <p class="lead">Bukan testimoni settingan. Ini suara ibu, mahasiswa & bapak rumahan beneran:</p>
    <div class="tsts">
      <div class="tst"><div class="top"><div class="av">SR</div><div><div class="nm">Siti Rahayu</div><div class="vf">✔ Pembeli Terverifikasi</div></div><div class="st">★★★★★</div></div><p><span class="q">"Nyesel baru beli sekarang!"</span> Biasa cincang bawang 15 menit sambil nangis, sekarang 3 detik kelar. Suami sampai kaget. Wajib punya!</p></div>
      <div class="tst"><div class="top"><div class="av">BW</div><div><div class="nm">Budi Wijaya</div><div class="vf">✔ Pembeli Terverifikasi</div></div><div class="st">★★★★★</div></div><p>Awalnya mikir "ah paling lebay". Ternyata <span class="q">daging beku aja kelar.</span> Baterai dicas sekali sebulan masih nyala. Worth banget Rp159rb.</p></div>
      <div class="tst"><div class="top"><div class="av">DA</div><div><div class="nm">Dewi Anggraini</div><div class="vf">✔ Pembeli Terverifikasi</div></div><div class="st">★★★★★</div></div><p>Buat MPASI anak juara! Halus merata, cuci gampang. <span class="q">Langsung order 2 lagi buat kado ke adik & mertua.</span> 😍</p></div>
      <div class="tst"><div class="top"><div class="av">RP</div><div><div class="nm">Rizky Pratama</div><div class="vf">✔ Pembeli Terverifikasi</div></div><div class="st">★★★★★</div></div><p>Anak kos wajib beli. Masak jadi rajin karena bumbu gampang. <span class="q">Barang sampai cuma 2 hari, COD lancar</span>, nggak PHP. Mantap.</p></div>
      <div class="tst"><div class="top"><div class="av">NK</div><div><div class="nm">Nur Kholifah</div><div class="vf">✔ Pembeli Terverifikasi</div></div><div class="st">★★★★★</div></div><p><span class="q">Jualan online ku kebantu banget</span> buat bikin sambal & bumbu kiloan. Tajem & kuat. Recommended buat yg punya usaha kuliner!</p></div>
      <div class="tst"><div class="top"><div class="av">AS</div><div><div class="nm">Andi Saputra</div><div class="vf">✔ Pembeli Terverifikasi</div></div><div class="st">★★★★★</div></div><p>Hadiah buat istri, eh malah aku yang ketagihan masak 😂. <span class="q">Build quality solid</span>, bukan barang abal-abal. 5 bintang!</p></div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="sec alt">
  <div class="wrap">
    <div class="kicker">Masih ragu?</div>
    <h2 class="h2">Pertanyaan yang Sering Ditanya</h2>
    <div class="faq" id="faq">
      <div class="qa"><div class="q">Sistem COD-nya aman? <span class="pm">+</span></div><div class="a"><p>Sangat aman. Kamu <b>baru bayar saat barang sampai</b> di tangan & sudah dicek. Tidak perlu transfer/DP di depan. Kurir yang antar langsung ke alamatmu.</p></div></div>
      <div class="qa"><div class="q">Baterainya awet nggak? <span class="pm">+</span></div><div class="a"><p>Sangat awet. Sekali cas via USB bisa untuk pemakaian normal <b>hingga 1 bulan</b>. Tidak perlu colok listrik tiap pakai — bebas kabel.</p></div></div>
      <div class="qa"><div class="q">Susah dibersihkan? <span class="pm">+</span></div><div class="a"><p>Justru paling gampang. <b>Bilas wadah & mata pisau ±5 detik</b>, lap, selesai. Tidak ada lagi tumpukan talenan dan pisau kotor.</p></div></div>
      <div class="qa"><div class="q">Aman buat dipakai dekat anak? <span class="pm">+</span></div><div class="a"><p>Aman. Mesin <b>hanya menyala kalau tutup sudah terkunci rapat</b>, dan mata pisau berputar di dalam wadah tertutup. Tangan tidak menyentuh pisau.</p></div></div>
      <div class="qa"><div class="q">Kalau barang rusak / tidak sesuai? <span class="pm">+</span></div><div class="a"><p>Kami <b>ganti baru</b> jika ada cacat/rusak saat sampai. Plus garansi 30 hari. Cukup chat tim kami via WhatsApp, dibantu sampai beres.</p></div></div>
      <div class="qa"><div class="q">Berapa lama sampai? <span class="pm">+</span></div><div class="a"><p>Pesanan diproses & <b>dikirim di hari yang sama</b> (sebelum jam 3 sore). Estimasi tiba 1–3 hari kerja tergantung kota. Resi dikirim ke WhatsApp-mu.</p></div></div>
    </div>
  </div>
</section>

<!-- ORDER FORM -->
<section class="sec order" id="order">
  <div class="wrap">
    <div class="kicker" style="color:var(--gold)">Selangkah lagi</div>
    <h2 class="h2">Amankan Punyamu Sekarang 🛒</h2>
    <p class="lead">Harga promo & gratis ongkir bisa berakhir kapan saja. Isi data di bawah, bayar di tempat (COD).</p>
    <div class="timer" id="timerOrder">
      <div class="t"><b id="cdH">00</b><span>Jam</span></div>
      <div class="t"><b id="cdM">14</b><span>Menit</span></div>
      <div class="t"><b id="cdS">59</b><span>Detik</span></div>
    </div>
    <div class="card">
      <h3>Form Pemesanan COD</h3>
      <div class="small">Klik tombol di bawah → isi data → bayar di tempat (COD) ✅</div>
      <div class="ooef">
<form class="orderonline-embed-form" data-username="ahtashop" data-product-slug="electric-garlic-chopper-f-ur" data-product-id="6a181e67139a350cea0f50aa" id="oo-embed-form-electric-garlic-chopper-f-ur-8769" data-origin="orderonline">
<div class="ooef-loader"><style>.ooef-loader{visibility: hidden;opacity: 0;position: absolute;left: 0;right: 0;top: 0;bottom: 0;display: flex;justify-content: center;align-items: center;flex-direction: column;animation: ooLoadingIn 10s ease;-webkit-animation: ooLoadingIn 10s ease;animation-fill-mode: forwards;overflow: hidden}@keyframes ooLoadingIn{0%{visibility: hidden;opacity: 0}20%{visibility: visible;opacity: 0}100%{visibility: visible;opacity: 1}}@-webkit-keyframes ooLoadingIn{0%{visibility: hidden;opacity: 0}20%{visibility: visible;opacity: 0}100%{visibility: visible;opacity: 1}}.ooef-loader>div,.ooef-loader>div:after{border-radius: 50%;width: 2.5rem;height: 2.5rem}.ooef-loader>div{font-size: 10px;position: relative;text-indent: -9999em;border: .25rem solid #f5f5f5;border-left: .25rem solid #55c4cf;-webkit-transform: translateZ(0);-ms-transform: translateZ(0);transform: translateZ(0);-webkit-animation: ooLoading 1.1s infinite linear;animation: ooLoading 1.1s infinite linear}.ooef-loader.error>div{border-left: .25rem solid #ff4500;animation-duration: 5s}@-webkit-keyframes ooLoading{0%{-webkit-transform: rotate(0);transform: rotate(0)}100%{-webkit-transform: rotate(360deg);transform: rotate(360deg)}}@keyframes ooLoading{0%{-webkit-transform: rotate(0);transform: rotate(0)}100%{-webkit-transform: rotate(360deg);transform: rotate(360deg)}}</style><div aria-live="polite" role="status"><div>Loading...</div></div></div>
</form>
      </div>
      <p class="center" style="font-size:11.5px;color:#6b7280;margin-top:10px">🔒 Pemesanan diproses aman via sistem OrderOnline • COD</p>
    </div>
    <p class="formnote">⚡ <b id="stockBtm">17</b> stok tersisa • 🔥 <b>347</b> orang memesan hari ini</p>
  </div>
</section>

<div class="foot">
  <b>Electric Garlic Chopper</b> — Dapur cepat, rapi, tanpa drama.<br>
  © 2026 • Pemesanan resmi via WhatsApp • COD seluruh Indonesia<br>
  <span style="font-size:10px;opacity:.6">Gambar & hasil dapat bervariasi sesuai pemakaian.</span>
</div>

<div class="sticky" id="sticky">
  <div class="p"><span class="o">Rp349.000</span><br><span class="n">Rp159.000</span> <span class="s">HEMAT 54%</span></div>
  <a href="#order" data-scroll="#order">PESAN 🛒</a>
</div>

<div class="toast" id="toast">
  <div class="ti" id="toastImg"></div>
  <div class="tt"><b id="toastName">Andi</b> <span class="chk">baru saja memesan ✔</span><br><span id="toastCity" class="ag">Jakarta</span> <span class="ag">• <span id="toastAgo">2</span> mnt lalu</span></div>
</div>
"""

CONTENT = CONTENT.replace("__CSS__", CSS)
CONTENT = CONTENT.replace("__HERO__", HERO).replace("__SPEC__", SPEC)
CONTENT = CONTENT.replace("__WHITE__", WHITE).replace("__BLUE__", BLUE)

# ---------------------------------------------------------------------------
# Encode the content (XOR + base64) so view-source / copy is defeated.
# ---------------------------------------------------------------------------
KEY = b"GcHpR_2026_xK9q"
raw = CONTENT.encode("utf-8")
xored = bytes(raw[i] ^ KEY[i % len(KEY)] for i in range(len(raw)))
PAYLOAD = base64.b64encode(xored).decode("ascii")
KEY_JS = json.dumps(list(KEY))
TOAST_IMG = BLUE  # small thumb for live-sale toasts

# ---------------------------------------------------------------------------
# Outer HTML + protection + interactivity
# ---------------------------------------------------------------------------
OUTER = r"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#13203f">
<meta name="format-detection" content="telephone=no">
<meta name="robots" content="noindex,nofollow,noarchive,nosnippet,noimageindex">
<meta name="referrer" content="no-referrer">
<title>Electric Garlic Chopper — Cincang 3 Detik Tanpa Air Mata | PROMO 54%</title>
<style>
html,body{margin:0;background:#13203f}
#__ld{position:fixed;inset:0;background:#13203f;display:flex;align-items:center;justify-content:center;z-index:9999;color:#ffd23f;font-family:-apple-system,Segoe UI,Roboto,sans-serif}
#__ld .s{width:46px;height:46px;border:4px solid rgba(255,255,255,.2);border-top-color:#ffd23f;border-radius:50%;animation:sp 1s linear infinite}
@keyframes sp{to{transform:rotate(360deg)}}
@media print{html{display:none!important}}
#__blk{position:fixed;inset:0;background:#0c1730;color:#fff;z-index:2147483647;display:none;align-items:center;justify-content:center;text-align:center;padding:24px;font-family:-apple-system,Segoe UI,Roboto,sans-serif;font-size:18px;font-weight:700}
.__guard-blur{filter:blur(22px) brightness(.4)!important;transition:filter .05s}
</style>
</head>
<body oncontextmenu="return false">
<div id="__ld"><div class="s"></div></div>
<div id="__root"></div>
<div id="__blk">🔒 Konten dilindungi.<br>Tutup developer tools untuk melanjutkan.</div>
<noscript><div style="padding:40px;text-align:center;font-family:sans-serif;color:#fff">Aktifkan JavaScript untuk melihat penawaran ini.</div></noscript>
<script>
(function(){
"use strict";
/* ===== payload ===== */
var P="__PAYLOAD__",K=__KEY__;
function decode(){
  var bin=atob(P),n=bin.length,u=new Uint8Array(n);
  for(var i=0;i<n;i++){u[i]=bin.charCodeAt(i)^K[i%K.length];}
  return new TextDecoder("utf-8").decode(u);
}

/* ===== protections (deterrents) ===== */
function noop(e){e.preventDefault();return false;}
document.addEventListener("contextmenu",noop,{passive:false});
document.addEventListener("dragstart",noop,{passive:false});
document.addEventListener("selectstart",function(e){
  var t=e.target;
  if(t&&(t.tagName==="INPUT"||t.tagName==="TEXTAREA"||t.isContentEditable))return true;
  e.preventDefault();return false;
},{passive:false});
document.addEventListener("copy",function(e){e.preventDefault();},{passive:false});
document.addEventListener("keydown",function(e){
  var k=e.key||"",K2=k.toUpperCase();
  if(k==="F12"){e.preventDefault();return false;}
  if((e.ctrlKey||e.metaKey)&&e.shiftKey&&(K2==="I"||K2==="J"||K2==="C")){e.preventDefault();return false;}
  if((e.ctrlKey||e.metaKey)&&(K2==="U"||K2==="S"||K2==="P")){e.preventDefault();return false;}
  if(k==="PrintScreen"){wipeClip();flashBlock();}
},{passive:false});
document.addEventListener("keyup",function(e){if((e.key||"")==="PrintScreen"){wipeClip();}});
function wipeClip(){try{if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(" ");}catch(_){}}
var blk=function(){return document.getElementById("__blk");};
function flashBlock(){var b=blk();if(!b)return;b.style.display="flex";setTimeout(function(){b.style.display="none";},900);}

/* screenshot/app-switch deterrent: blur when window loses focus */
var root=function(){return document.getElementById("__root");};
function blur(){var r=root();if(r)r.classList.add("__guard-blur");}
function unblur(){var r=root();if(r)r.classList.remove("__guard-blur");}
window.addEventListener("blur",blur);
window.addEventListener("focus",unblur);
document.addEventListener("visibilitychange",function(){document.hidden?blur():unblur();});

/* devtools detector — DESKTOP, TOP-LEVEL ONLY (never on mobile or when embedded,
   to avoid ever blocking a real buyer). Conservative threshold + self-healing. */
var isTouch=("ontouchstart" in window)||navigator.maxTouchPoints>0;
var isTop=(function(){try{return window.top===window.self;}catch(_){return false;}})();
if(isTop&&!isTouch&&Math.min(screen.width,screen.height)>=800){
  var TH=220; /* trigger only on a SHARP increase vs the page's own baseline */
  var baseW=window.outerWidth-window.innerWidth, baseH=window.outerHeight-window.innerHeight;
  setInterval(function(){
    var wd=window.outerWidth-window.innerWidth, hd=window.outerHeight-window.innerHeight;
    if(wd<baseW)baseW=wd; if(hd<baseH)baseH=hd; /* track the smallest gap seen (devtools closed) */
    var b=blk();if(!b)return;
    if((wd-baseW)>TH||(hd-baseH)>TH){b.style.display="flex";}else if(b.style.display==="flex"){b.style.display="none";}
  },1100);
}

/* ===== boot ===== */
function boot(){
  var r=root();
  r.innerHTML=decode();
  var ld=document.getElementById("__ld");if(ld)ld.parentNode.removeChild(ld);
  init();
}

/* ===== app logic ===== */
function init(){
  /* scroll buttons */
  document.querySelectorAll("[data-scroll]").forEach(function(el){
    el.addEventListener("click",function(e){
      e.preventDefault();
      var t=document.querySelector(el.getAttribute("data-scroll"));
      if(t)t.scrollIntoView({behavior:"smooth",block:"start"});
    });
  });

  /* bundle options (visual highlight / pricing anchor) */
  var bOpts=document.querySelectorAll("#bundleOpts .opt");
  bOpts.forEach(function(o){o.addEventListener("click",function(){
    bOpts.forEach(function(x){x.classList.remove("act");});
    o.classList.add("act");
  });});

  /* faq */
  document.querySelectorAll("#faq .qa").forEach(function(qa){
    qa.querySelector(".q").addEventListener("click",function(){qa.classList.toggle("open");});
  });

  startCountdown();
  startSticky();
  startStock();
  startToasts();
  initOrderOnline();
}

/* OrderOnline embed bootstrap — runs AFTER content injection so the form
   element exists in the DOM (innerHTML-injected <script> would not execute). */
function initOrderOnline(){
  try{
    var xLogError=function(error){
      try{
        var req=new XMLHttpRequest();
        var payload=JSON.stringify({url:document.location.href,line:error.line,stack:error.stack});
        var params="message="+encodeURIComponent(error.name)+"&payload="+encodeURIComponent(payload)+"&type=embed&level=error";
        req.open("POST","https://api.orderonline.id/log",true);
        req.setRequestHeader("Content-type","application/x-www-form-urlencoded");
        req.send(params);
      }catch(_){}
    };
    var xEmbedScript=function(){
      !function(w,d,e,v,id,t,s){if(d.getElementById(id))return;t=d.createElement(e);t.async=!0;t.src=v;t.id=id;s=d.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s);}
      (window,document,"script","https://cdn.orderonline.id/js/embed-v2-slim.min.js?v=8.0.2","oo-embed-js");
    };
    var xEmbedInit=function(w,n){if(w.ooe)return;n=w.ooe=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!w._ooe)w._ooe=n;n.push=n;n.loaded=!0;n.version="8.0.2";n.queue=[];};
    xEmbedInit(window);
    window.ooe("setup","redirect","https://ahtashop.orderonline.id");
    window.ooe("init","5f5ebafe9d8e8e277831b563","6a181e67139a350cea0f50aa",null,"oo-embed-form-electric-garlic-chopper-f-ur-8769",{"mode":"page","action":"Klik untuk pemesanan","title":"Form Pemesanan","triggerPixel":false,"triggerGtm":false});
    if(!window.jQuery){
      !function(w,d,e,v,id,t,s){if(d.getElementById(id))return;t=d.createElement(e);t.async=!0;t.src=v;t.id=id;t.addEventListener("load",xEmbedScript);s=d.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s);}
      (window,document,"script","https://cdn.orderonline.id/js/vendor/jquery.min.js","oo-embed-jquery");
    }else{xEmbedScript();}
  }catch(e){}
}

/* evergreen countdown (resets to keep urgency) */
function startCountdown(){
  var KEYLS="gcchop_deadline";
  var dl=parseInt(localStorage.getItem(KEYLS)||"0",10);
  var now=Date.now();
  if(!dl||dl<now){dl=now+15*60*1000;localStorage.setItem(KEYLS,String(dl));}
  function tick(){
    var left=Math.max(0,Math.floor((dl-Date.now())/1000));
    if(left<=0){dl=Date.now()+15*60*1000;localStorage.setItem(KEYLS,String(dl));left=900;}
    var h=Math.floor(left/3600),m=Math.floor((left%3600)/60),s=left%60;
    var mm=(m<10?"0":"")+m, ss=(s<10?"0":"")+s, hh=(h<10?"0":"")+h;
    set("cdTop",mm+":"+ss);set("cdH",hh);set("cdM",mm);set("cdS",ss);
  }
  tick();setInterval(tick,1000);
}
function set(id,v){var e=document.getElementById(id);if(e)e.textContent=v;}

/* sticky bar appears after scrolling past hero */
function startSticky(){
  var s=document.getElementById("sticky");
  window.addEventListener("scroll",function(){
    if(window.scrollY>520)s.classList.add("show");else s.classList.remove("show");
  },{passive:true});
}

/* gently decreasing stock */
function startStock(){
  var n=17;
  function upd(){set("stockTop",n);set("stockBtm",n);}
  upd();
  setInterval(function(){
    if(n>6&&Math.random()<0.5){n-=1;upd();}
  },14000);
}

/* live-sale toasts (social proof) */
function startToasts(){
  var t=document.getElementById("toast");if(!t)return;
  document.getElementById("toastImg").style.backgroundImage="url('__TOAST__')";
  var names=["Andi","Siti","Budi","Dewi","Rizky","Nur","Putri","Agus","Lala","Wawan","Fitri","Joko","Maya","Rina","Doni"];
  var cities=["Jakarta","Bandung","Surabaya","Medan","Bekasi","Depok","Tangerang","Semarang","Makassar","Bogor","Palembang","Malang","Yogyakarta"];
  function show(){
    set("toastName",names[(Math.random()*names.length)|0]);
    set("toastCity",cities[(Math.random()*cities.length)|0]);
    set("toastAgo",(1+(Math.random()*9|0)));
    t.classList.add("show");
    setTimeout(function(){t.classList.remove("show");},4200);
  }
  setTimeout(show,3500);
  setInterval(show,11000);
}

/* run */
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",boot);else boot();
})();
</script>
</body>
</html>
"""

OUTER = OUTER.replace("__PAYLOAD__", PAYLOAD).replace("__KEY__", KEY_JS).replace("__TOAST__", TOAST_IMG)

with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(OUTER)

size = os.path.getsize(os.path.join(ROOT, "index.html"))
print("index.html written: %.1f KB" % (size/1024))
print("payload chars:", len(PAYLOAD))
