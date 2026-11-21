"""英語版ツールページに id="detail" セクションを入れる。texts: scripts/en_detail/*.txt
書式: "@@ tool-name" の後に "## h2"、"### h3"、"- 箇条書き"、それ以外は段落。リンクは <a href="/x.html">..</a>（/en/ は自動付与）。
リポジトリ直下で実行。冪等。"""
import glob, html, os, re

def en_title(path):
    p = 'en/' + path.lstrip('/')
    if not os.path.exists(p): return None
    t = re.search(r'<title>(.*?)</title>', open(p, encoding='utf-8').read(), re.S).group(1)
    return re.split(r'\s*[|｜]\s*', t)[0]

def fix_links(s): return re.sub(r'href="/(?!en/)([^"]*)"', r'href="/en/\1"', s)

def render(block, ja_html):
    lines = [l for l in block.strip().split('\n') if l.strip()]
    out, ul = [], []
    def flush():
        if ul: out.append('<ul>' + ''.join('<li>%s</li>' % x for x in ul) + '</ul>'); ul.clear()
    for l in lines:
        if l.startswith('## '): flush(); out.append('<h2>%s</h2>' % l[3:])
        elif l.startswith('### '): flush(); out.append('<h3>%s</h3>' % l[4:])
        elif l.startswith('- '): ul.append(l[2:])
        else: flush(); out.append('<p>%s</p>' % l)
    flush()
    links = re.findall(r'<li><a href="(/[^"]+)">', ja_html.split('<h3>くわしい解説</h3>')[-1]) if 'くわしい解説' in ja_html else []
    li = ''.join('<li><a href="/en/%s">%s</a></li>' % (l.lstrip('/'), en_title(l)) for l in links if en_title(l))
    if li: out.append('<h3>More guides</h3><ul>%s</ul>' % li)
    return fix_links(''.join(out))

blocks = {}
for f in sorted(glob.glob('scripts/en_detail/*.txt')):
    for chunk in re.split(r'^@@ ', open(f, encoding='utf-8').read(), flags=re.M)[1:]:
        name, _, rest = chunk.partition('\n'); blocks[name.strip()] = rest
n = 0
for name, rest in blocks.items():
    page = 'en/%s.html' % name; ja = '%s.html' % name
    s = open(page, encoding='utf-8').read()
    if 'id="detail"' in s: continue
    jas = open(ja, encoding='utf-8').read()
    m = re.search(r'<section lang="ja" id="detail">(.*?)</section>', jas, re.S)
    sec = '<section lang="en" id="detail">%s</section>\n' % render(rest, m.group(1) if m else '')
    i = s.find('</main>'); assert i > 0, page
    open(page, 'w', encoding='utf-8').write(s[:i] + sec + s[i:]); n += 1
print('inserted', n, 'of', len(blocks))
