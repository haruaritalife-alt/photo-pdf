"""英語版の解説ページ(ツール本体以外)をnoindexにし、sitemapから外す。冪等。リポジトリ直下で実行。"""
import glob, os, re
en = sorted(glob.glob('en/*.html'))
def read(f): return open(f, encoding='utf-8').read()
tools = {os.path.basename(f)[:-5] for f in en if any(k in read(f) for k in ('id="go"', 'id="clr"', 'id="file"', 'id="detail"'))}
skip = {'index', 'guides', 'privacy', 'support', 'about', 'terms', 'contact'}
done = []
for f in en:
    b = os.path.basename(f)[:-5]; s = read(f)
    if b in tools or b in skip or b.endswith('-builder') or 'noindex' in s: continue
    if '</head>' not in s: continue
    open(f, 'w', encoding='utf-8').write(s.replace('</head>', '<meta content="noindex,follow" name="robots"/></head>', 1)); done.append(b)
sm = open('sitemap.xml', encoding='utf-8').read()
urls = {'https://pdfmikata.com/en/%s.html' % b for b in done}
lines = sm.split('\n')
keep = [l for l in lines if not any(('<loc>%s</loc>' % u) in l for u in urls)]
open('sitemap.xml', 'w', encoding='utf-8').write('\n'.join(keep))
print('noindexed', len(done), 'sitemap lines removed', len(lines) - len(keep))
