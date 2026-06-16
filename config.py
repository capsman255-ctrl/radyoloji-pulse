# -*- coding: utf-8 -*-
"""
Radyoloji Pulse — ayarlar.

EN ÇOK BURAYI DÜZENLEYECEKSİN. Skorlamanın "gizli sosu" bu dosyadır:
hangi dergi kaç puan, hangi makale tipi öne çıkar. Veriyi herkes çekebilir;
asıl değer bu ağırlıklarda.

Dergi anahtarları PubMed'in NLM kısaltmalarıdır (ISOAbbreviation ile eşleşir).
Yeni dergi eklerken https://pubmed.ncbi.nlm.nih.gov adresinde derginin
"NLM Title Abbreviation" değerine bak.
"""

# --------------------------------------------------------------------------
# DERGİLER ve TIER'LARI
# Tier 1 = bayrak/üst düzey, Tier 2 = güçlü uzmanlık, Tier 3 = geniş/bölgesel
# --------------------------------------------------------------------------
JOURNAL_TIERS = {
    # --- Tier 1: genel/bayrak ---
    "Radiology": 1,
    "Radiol Artif Intell": 1,        # Radiology: Artificial Intelligence
    "Radiographics": 1,
    "Eur Radiol": 1,
    "Invest Radiol": 1,
    "AJR Am J Roentgenol": 1,
    "J Am Coll Radiol": 1,

    # --- Tier 2: güçlü uzmanlık ---
    "Eur J Radiol": 2,
    "Korean J Radiol": 2,
    "Insights Imaging": 2,
    "J Magn Reson Imaging": 2,
    "Neuroradiology": 2,
    "AJNR Am J Neuroradiol": 2,
    "Abdom Radiol (NY)": 2,
    "Pediatr Radiol": 2,
    "Acad Radiol": 2,

    # --- Senin alanların: girişimsel + US/elastografi ---
    "J Vasc Interv Radiol": 2,            # JVIR
    "Cardiovasc Intervent Radiol": 2,     # CVIR
    "Ultraschall Med": 2,                 # Ultraschall in der Medizin
    "J Ultrasound Med": 3,
    "Ultrasonography": 3,
    "Eur Radiol Exp": 3,
    "Diagn Interv Radiol": 3,
    "Clin Radiol": 3,
}

# Tier başına temel puan
JOURNAL_TIER_WEIGHT = {1: 100, 2: 60, 3: 35}

# Listede olmayan/eşleşmeyen dergi için varsayılan tier
DEFAULT_TIER = 3

# --------------------------------------------------------------------------
# MAKALE TİPİ AĞIRLIKLARI
# PubMed PublicationType etiketleriyle birebir eşleşir.
# Pozitif tip varsa en yükseği alınır; ceza tipi varsa düşülür.
# --------------------------------------------------------------------------
PUBTYPE_WEIGHTS = {
    "Meta-Analysis": 45,
    "Systematic Review": 40,
    "Practice Guideline": 38,
    "Guideline": 35,
    "Randomized Controlled Trial": 35,
    "Clinical Trial, Phase III": 30,
    "Multicenter Study": 18,
    "Clinical Trial": 15,
    "Validation Study": 12,
    "Review": 10,
    # cezalar
    "Case Reports": -15,
    "Editorial": -25,
    "Letter": -30,
    "Comment": -30,
    "Published Erratum": -100,
    "Retraction of Publication": -200,
}

# --------------------------------------------------------------------------
# GÜNCELLİK
# Her gün için küçük bir bonus (yeni olan biraz daha öne çıksın).
# --------------------------------------------------------------------------
RECENCY_PER_DAY = 2.0

# --------------------------------------------------------------------------
# ARAMA AYARLARI
# --------------------------------------------------------------------------
RELDATE_DAYS = 5         # son kaç gün
DATETYPE = "edat"         # "edat" = PubMed'e eklenme tarihi (taze radar için ideal)
                          # "pdat" = yayın tarihi  (sitedeki "yayınlanan" mantığı)
RETMAX = 300              # en fazla kaç makale çekilsin

# İstersen konuyla daralt (boş bırak = sadece dergi filtresi).
# Örn: 'hasta OR "Diagnostic Imaging"[Mesh]' gibi. Genelde boş bırakmak en temizi.
EXTRA_TERMS = ""

# Makale "tier" rozetleri için toplam skor eşikleri (görsel sınıflandırma)
TIER1_THRESHOLD = 110
TIER2_THRESHOLD = 80

# Dergi listesini sorgu için düz liste olarak çıkar
JOURNALS = list(JOURNAL_TIERS.keys())
