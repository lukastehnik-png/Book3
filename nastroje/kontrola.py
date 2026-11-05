#!/usr/bin/env python3
"""Kontrola kapitol: slova, pomlčky, zakázané fráze, přírodní slova (k ruční kontrole perspektivy)."""
import sys, re, glob
ZAKAZANE = ["v tu chvíli","najednou si","uvědomil","srdce se jí sevřelo","srdce se mu sevřelo","ohlušující",
 "čas jako by se zastavil","něco v ní se zlomilo","něco v něm se zlomilo","nicméně","v rámci","realizovat",
 "provést","nedokázala popsat","slovy nepopsateln","vlna emocí","jako by svět"]
PRIRODA = r"\b(strom|list[íy]?\b|květ|kořen|peří|vosk|med\b|chleb|chléb|mouk|bavln|dřev|tráv|semen|semín|les[aeyů]?\b|pták|ptač|zvíř|kůr[ay]|ovoc|jabl|hmyz|motýl|psí|kočk|ryb[aéy]|louk|zelen|rostl|mech|houb|hnízd|křídl|kos[ae]?\b|rorýs|hejn)"
files = sys.argv[1:] or sorted(glob.glob('kapitoly/[0-9]*.md'))
celkem=0
for f in files:
    t=open(f).read()
    w=len(t.split()); celkem+=w
    print(f"== {f}: {w} slov")
    if '–' in t or '—' in t: print("  !! POMLČKA", t.count('–')+t.count('—'))
    if ' - ' in t: print("  !! spojovník jako pomlčka")
    for z in ZAKAZANE:
        for m in re.finditer(re.escape(z), t, re.I): print("  !! zakázané:", z, "|", t[max(0,m.start()-40):m.end()+20].replace('\n',' '))
    if '-v' in sys.argv[0:0] : pass
    hits=[(m.group(0), t[max(0,m.start()-50):m.end()+30].replace('\n',' ')) for m in re.finditer(PRIRODA,t,re.I)]
    if hits: print(f"  příroda ({len(hits)}):"); [print("    -",h,"|",c) for h,c in hits]
print(f"CELKEM {celkem} slov = {celkem/300:.1f} stran")
