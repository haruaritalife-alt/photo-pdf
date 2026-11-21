# -*- coding: utf-8 -*-
# リポジトリのHTMLに直接、日本語ツールページの解説(id="detail")を差し込む。何度実行しても二重に入らない。
# 使い方: python3 scripts/apply_detail.py  (リポジトリのルートで)
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from detail_more8 import MORE8 as B

def title(l):
    try:
        t = re.search(r"<title>(.*?)</title>", open(l.lstrip("/"), encoding="utf-8").read(), re.S).group(1)
        return t.split("｜")[0]
    except Exception:
        return l

def inject():
    n = 0
    for t, (h, secs, links) in B.items():
        p = t + ".html"
        if not os.path.exists(p): continue
        s = open(p, encoding="utf-8").read()
        if 'id="detail"' in s or "</main>" not in s: continue
        body = '<section lang="ja" id="detail"><h2>%s</h2>%s<h3>くわしい解説</h3><ul>%s</ul></section>\n' % (
            h, "".join("<h3>%s</h3>%s" % (a, b if b.startswith("<") else "<p>%s</p>" % b) for a, b in secs),
            "".join('<li><a href="%s">%s</a></li>' % (l, title(l)) for l in links))
        open(p, "w", encoding="utf-8").write(s.replace("</main>", body + "</main>", 1)); n += 1
    return n

if __name__ == "__main__":
    print(inject())
