"""用途別ページ(/for/)を追加する。ひな形は既存ページ。リポジトリ直下で実行。冪等。"""
import re, json, html
T = open('for/resume-pdf-under-1mb.html', encoding='utf-8').read()
BASE = 'https://pdfmikata.com'
E = html.escape

def ul(xs): return '<ul>' + ''.join('<li>%s</li>' % x for x in xs) + '</ul>'
def ol(xs): return '<ol>' + ''.join('<li>%s</li>' % x for x in xs) + '</ol>'

P = []
def add(slug, short, title, desc, h1, points, intro, cta_href, cta, steps, note, h2a, h2a_body, checks, faqs, tools, lead):
    P.append(dict(locals()))

add('heic-to-jpg-submission', 'iPhone写真をJPGにして提出する',
 'iPhoneの写真（HEIC）をJPGに変換して提出する方法｜PDFのミカタ',
 '応募フォームや申請サイトで「HEICは使えません」と出たときの対処。iPhoneの写真をJPGに変換する手順。ファイルは端末の外に送られません。無料・登録不要。',
 'iPhoneの写真（HEIC）をJPGにして提出する方法',
 ['HEICをJPGに変えれば、多くのフォームで受け付けられる', '複数枚をまとめて変換できる', '写真は端末の外に送られない'],
 '申請サイトにiPhoneの写真を添付しようとして、「この形式は使えません」と表示される。原因の多くは、iPhoneの写真がHEICという形式で保存されていることです。<a href="/heic-to-jpg.html">HEIC画像をJPGに変換</a> で、広く使われているJPGに変えられます。写真は端末の外に送られません。',
 '/heic-to-jpg.html', 'HEICをJPGに変換する（無料）',
 ['上のボタンでツールを開きます。', '「画像を選ぶ」で、HEICの写真を選びます。複数枚を同時に選べます。', '形式は、ふつうはJPGのままで構いません。', '「変換する」を押し、できたJPGを保存します。', '保存したJPGを、申請サイトに添付し直します。'],
 '変換しても、撮影日時や位置情報が写真に残る場合があります。人に渡す写真なら、<a href="/image-exif-remove.html">写真の位置情報・撮影情報を消す</a> も使ってください。',
 'うまくいかないとき', '<p>変換後も、容量の上限で弾かれることがあります。その場合は <a href="/image-resize.html">画像のサイズ変更</a> で縮めるか、<a href="/photo-to-pdf.html">写真をPDFに</a> まとめてPDFで出せないか、募集要項で確認します。</p><p>設定を変えずに済ませたい場合は、iPhoneの「設定」→「カメラ」→「フォーマット」で「互換性優先」を選ぶと、以後の撮影はJPGで保存されます。すでに撮った写真は変わらないので、変換が必要です。</p>',
 ['拡張子が .jpg（または .jpeg）になっている', '写真の向きが正しい', '容量の上限に収まっている', '文字や顔など、見せたい部分がはっきり写っている'],
 [('HEICとは何ですか？', 'iPhoneが標準で使う写真の形式です。容量が小さい一方、Windowsや一部のWebサイトでは扱えないことがあります。'), ('変換すると画質は落ちますか？', 'JPGは圧縮形式なので、わずかに劣化します。提出用としては、ふだん気づかない程度です。'), ('写真は、サーバーに送られますか？', '送られません。変換は、お使いの端末の中だけで行われます。'), ('元のHEIC写真は消えますか？', '消えません。変換後のJPGは、新しいファイルとして保存されます。')],
 [('/image-resize.html', '画像のサイズ変更'), ('/photo-to-pdf.html', '写真をPDFに'), ('/image-exif-remove.html', '写真の位置情報・撮影情報を消す')],
 'iPhoneのHEIC写真をJPGに変換して提出する手順')

add('photo-remove-location-before-send', '写真の位置情報を消してから送る',
 '写真の位置情報・撮影情報を消してから送る方法｜PDFのミカタ',
 '自宅で撮った写真を送る前に、位置情報（GPS）や撮影日時などの撮影情報を消す手順。ファイルは端末の外に送られません。無料・登録不要。',
 '写真の位置情報を消してから送る方法',
 ['写真には、撮影した場所や日時が入っていることがある', '消した新しいファイルを作って送れる', '写真は端末の外に送られない'],
 'フリマアプリの出品写真、ブログ用の画像、知人に送る写真。スマホで撮った写真には、撮影場所の位置情報（GPS）や、撮影日時、機種名が入っていることがあります。<a href="/image-exif-remove.html">写真の位置情報・撮影情報を消す</a> では、これらを取り除いた新しい写真を作れます。写真は端末の外に送られません。',
 '/image-exif-remove.html', '位置情報を消す（無料）',
 ['上のボタンでツールを開きます。', '「画像を選ぶ」で、写真を選びます。複数枚を同時に選べます。', '保存形式を選びます。ふつうはJPGで構いません。', '「消して保存」の操作をして、できた写真を保存します。', '保存した写真を送る、または投稿します。元の写真は、そのまま残ります。'],
 'この方法で消えるのは、写真の中に埋め込まれた撮影情報です。写真に写っている景色、表札、制服、車のナンバーなどは消えません。場所が特定されそうな部分は、<a href="/image-mosaic.html">画像にモザイクをかける</a> で隠してください。',
 '消えるものと、消えないもの', '<h3>消えるもの</h3><p>撮影場所（GPS）、撮影日時、カメラの機種名など、写真ファイルの中に記録された撮影情報です。</p><h3>消えないもの</h3><p>写真そのものに写っている内容です。背景の建物や看板から、場所が分かることがあります。</p>',
 ['送る前に、新しく保存した写真を使っている', '背景に、住所が分かるものが写っていない', '顔や表札など、写してよいか確認した', '投稿先で、画像が正しく表示される'],
 [('位置情報は、初めから入らないようにできますか？', 'スマホのカメラ設定で、位置情報の利用をオフにできます。すでに撮った写真には入っているので、消す操作が必要です。'), ('SNSに上げれば、自動で消えますか？', 'サービスによって扱いが違います。確実にするなら、投稿前に自分で消しておく方法が安全です。'), ('写真は、サーバーに送られますか？', '送られません。処理は、お使いの端末の中だけで行われます。'), ('画質は変わりますか？', '新しい画像として書き出すため、わずかに変わることがあります。見た目には、ほとんど分かりません。')],
 [('/image-mosaic.html', '画像にモザイクをかける'), ('/image-resize.html', '画像のサイズ変更'), ('/heic-to-jpg.html', 'HEIC画像をJPGに変換')],
 '写真の位置情報・撮影情報を消す手順')

add('scan-pdf-rotate-fix', 'スキャンしたPDFの向きを直す',
 'スキャンしたPDFの向きを直す方法｜横向き・逆さのページを回転｜PDFのミカタ',
 'スキャンしたPDFが横向きや逆さになっているとき、ページごとに回転して直す手順。ファイルは端末の外に送られません。無料・登録不要。',
 'スキャンしたPDFの向きを直す方法',
 ['横向き・逆さのページだけを回転できる', '並べ替えもあわせてできる', 'ファイルは端末の外に送られない'],
 '複合機やスキャナーアプリで取り込んだら、一部のページが横向きや逆さになっていた。そんなときは <a href="/pdf-rotate.html">PDFのページを回転・並べ替え</a> で直せます。ページごとに向きを変えられます。ファイルは端末の外に送られません。',
 '/pdf-rotate.html', 'PDFの向きを直す（無料）',
 ['上のボタンでツールを開きます。', '「PDFを選ぶ」で、直したいPDFを選びます。', '向きの違うページを選び、回転します。', '必要なら、ページの順番も入れ替えます。', '保存して、向きがそろったかを最後まで見て確認します。'],
 '回転は、ページの向きの設定を変える操作です。ページの内容そのものは変わりません。',
 'よくある原因と対処', '<p>原稿をセットする向きと、スキャナーの設定が合っていないと、向きがそろいません。複数の書類をまとめて取り込むときは、一度スキャンしたあとに、このツールで一括して直すと確実です。</p><p>写真から作ったPDFの向きが違う場合は、<a href="/pdf-rotate-iphone-photo-pdf.html">iPhone写真のPDFの向き</a>も参考にしてください。</p>',
 ['すべてのページが、同じ向きになっている', 'ページの順番が正しい', '余白や端が切れていない', '保存後に、最初と最後のページを確認した'],
 [('一部のページだけ回転できますか？', 'できます。向きの違うページだけを選んで回転します。'), ('回転すると、画質は落ちますか？', '落ちません。ページの向きの設定を変えるだけです。'), ('ファイルは、サーバーに送られますか？', '送られません。処理は、お使いの端末の中だけで行われます。'), ('元のPDFは、変わりますか？', '変わりません。新しいファイルとして保存されます。')],
 [('/merge-pdf.html', 'PDFを結合'), ('/split-pdf.html', 'PDFのページを抜き出し・削除'), ('/compress-pdf.html', 'PDFを圧縮')],
 'スキャンしたPDFの向きを直す手順')

add('pdf-password-before-email', 'メールで送る前にPDFにパスワード',
 'メールで送る前にPDFにパスワードをかける方法｜PDFのミカタ',
 'PDFをメールで送る前にパスワードをかける手順。パスワードの伝え方の注意点つき。ファイルは端末の外に送られません。無料・登録不要。',
 'メールで送る前にPDFにパスワードをかける方法',
 ['開くときにパスワードが必要なPDFを作れる', 'パスワードは別の手段で伝える', 'ファイルは端末の外に送られない'],
 '個人情報や契約に関わるPDFをメールで送るとき、そのまま添付するのは不安です。<a href="/pdf-protect.html">PDFにパスワードをかける</a> で、開くときにパスワードが必要なPDFを作れます。ファイルは端末の外に送られません。',
 '/pdf-protect.html', 'PDFにパスワードをかける（無料）',
 ['上のボタンでツールを開きます。', '「PDFを選ぶ」で、守りたいPDFを選びます。', 'パスワードを2回入力します。', '「保存」を押して、できたPDFを保存します。', '保存したPDFを開き、パスワードで開けることを確認してから送ります。'],
 'パスワードを忘れると、このサイトでは復元できません。パスワードは、自分でも控えておいてください。',
 'パスワードの伝え方', '<p>同じメールにパスワードを書くと、意味がなくなります。メールとは別の手段（電話、チャットなど）で伝えてください。</p><p>推測されにくいパスワードにするため、誕生日や連番は避け、長めの文字列にします。</p>',
 ['パスワードで、実際に開けることを確認した', 'パスワードは、別の手段で伝える', 'パスワードを自分でも控えた', '送る相手と、ファイルが合っている'],
 [('パスワードをかけると、完全に安全ですか？', '安全性は上がりますが、絶対ではありません。パスワードが弱いと破られやすくなります。長く、推測されにくい文字列を使ってください。'), ('パスワードを忘れたら？', 'このサイトでは復元できません。元のPDFが手元に残っているなら、もう一度かけ直してください。'), ('ファイルは、サーバーに送られますか？', '送られません。処理は、お使いの端末の中だけで行われます。'), ('相手のPDFビューアで開けますか？', '一般的なPDFビューアなら、パスワードの入力画面が出て開けます。念のため、送る前に自分で開いて試してください。')],
 [('/pdf-redact.html', 'PDFを黒塗り'), ('/compress-pdf.html', 'PDFを圧縮'), ('/merge-pdf.html', 'PDFを結合')],
 'メール送信前にPDFへパスワードをかける手順')

add('pdf-watermark-submission-copy', '提出用コピーに透かし文字を入れる',
 'PDFに「提出用」「コピー」の透かし文字を入れる方法｜PDFのミカタ',
 '身分証や書類のコピーに「提出用」などの透かし文字を入れて、使い回しを防ぐ手順。ファイルは端末の外に送られません。無料・登録不要。',
 'PDFに「提出用」の透かし文字を入れる方法',
 ['用途と提出先を透かしで入れられる', '中央・全面・隅から選べる', 'ファイルは端末の外に送られない'],
 '本人確認書類や契約書のコピーを渡すとき、別の目的に使われないか心配です。<a href="/pdf-watermark.html">PDFに透かし文字を入れる</a> で、「提出用」「コピー」などの文字を全ページに入れられます。ファイルは端末の外に送られません。',
 '/pdf-watermark.html', '透かし文字を入れる（無料）',
 ['上のボタンでツールを開きます。', '「PDFを選ぶ」で、PDFを選びます。', '透かしの文字を入力します。たとえば「○○社 提出用」のように、提出先と用途を書きます。', '位置、角度、大きさを選びます。', '保存して、文字が読め、元の内容も見えることを確認します。'],
 '透かしは、使い回しを難しくするための目印です。完全に防ぐものではありません。',
 '文字の決め方', '<p>「コピー」だけより、「○○社 申込用 2026年11月」のように、提出先と日付を入れるほうが、別の目的に使われにくくなります。</p><p>書類の文字が読みにくくならないよう、大きさは小さめにするか、位置を隅にします。</p>',
 ['本文の文字が、読める状態を保っている', '提出先と用途が、透かしに入っている', '全ページに、透かしが入っている', '元のファイルと、提出用のファイルを分けて保存した'],
 [('透かしは、あとから消されませんか？', '完全に防ぐことはできません。入れておくことで、使い回しを難しくする目安です。'), ('文字は日本語でも入れられますか？', 'はい。日本語で入力できます。'), ('ファイルは、サーバーに送られますか？', '送られません。処理は、お使いの端末の中だけで行われます。'), ('元のPDFは、変わりますか？', '変わりません。新しいファイルとして保存されます。')],
 [('/pdf-redact.html', 'PDFを黒塗り'), ('/pdf-protect.html', 'PDFにパスワードをかける'), ('/compress-pdf.html', 'PDFを圧縮')],
 'PDFに提出用の透かし文字を入れる手順')

add('char-count-entry-sheet', 'ESの文字数を数える',
 'エントリーシート（ES）の文字数を数える方法｜PDFのミカタ',
 'エントリーシートや志望動機の文字数を、改行や空白を含めて数える手順。入力した文章は端末の外に送られません。無料・登録不要。',
 'エントリーシート（ES）の文字数を数える方法',
 ['400字・800字などの指定に合わせて数えられる', '改行や空白の扱いが選べる', '文章は端末の外に送られない'],
 '「400字以内」「800字程度」と指定されたESや志望動機を、貼り付けて数えます。<a href="/char-counter.html">文字数カウント</a> は、入力した文章を端末の外に送りません。目標の文字数を入れると、あと何字かも分かります。',
 '/char-counter.html', '文字数を数える（無料）',
 ['上のボタンでツールを開きます。', '文章を貼り付けます。', '「目標」に、指定の文字数（例：400）を入れます。', '表示された文字数と、あと何字かを確認します。', '指定に対して、足りない、または多い部分を直します。'],
 '企業によって、改行や空白を文字数に含めるかが違います。募集要項や入力フォームの注意書きを確認してください。',
 '数え方で迷ったとき', '<p>多くの入力フォームは、改行や空白も1字として数えます。一方で、企業の説明が「空白を除く」となっていることもあります。ツールの表示を見て、含める場合と除く場合の両方を確認すると安心です。</p><p>詳しい数え方は <a href="/char-counter-entry-sheet.html">ESの文字数の数え方</a> も参考にしてください。</p>',
 ['指定の文字数に収まっている', '改行や空白の扱いを確認した', '誤字、脱字がない', '入力フォームで、最終的な文字数が合っている'],
 [('「400字以内」は、何字までが対象ですか？', '多くの場合、400字ちょうどまでが対象です。企業の指示に従ってください。'), ('改行は、文字数に入りますか？', 'フォームによって違います。入力フォームの表示で確認してください。'), ('入力した文章は、サーバーに送られますか？', '送られません。数えるのは、お使いの端末の中だけです。'), ('志望動機以外にも使えますか？', 'はい。レポートや原稿など、どんな文章でも数えられます。')],
 [('/char-counter-report.html', 'レポートの文字数を数える'), ('/docx-to-text.html', 'Wordの文字を取り出す')],
 'エントリーシートの文字数を数える手順')

import os
bad = [l for p in P for l in [p['cta_href']] + [t[0] for t in p['tools']] if not os.path.exists(l.lstrip('/').split('#')[0])]
print('missing link targets:', bad)

def main_html(p, others):
    m = '<main id="main" tabindex="-1">\n<div lang="ja">\n'
    m += '<h1>%s</h1>\n<div class="points"><b>このページのポイント</b>%s</div>\n' % (p['h1'], ul(p['points']))
    m += '<p>%s</p>\n<a class="cta" href="%s">%s</a>\n' % (p['intro'], p['cta_href'], p['cta'])
    m += '<h2>手順</h2>%s\n<div class="note">%s</div>\n' % (ol(p['steps']), p['note'])
    m += '<h2>%s</h2>%s\n' % (p['h2a'], p['h2a_body'])
    m += '<h2>提出前のチェック</h2>%s\n' % ul(p['checks']).replace('<ul>', '<ul class="check">')
    m += '<h2>よくある質問</h2>' + ''.join('<h3>%s</h3><p>%s</p>' % q for q in p['faqs']) + '\n'
    m += '<a class="cta" href="%s">%s</a>\n' % (p['cta_href'], p['cta'])
    m += '<h2>あわせて使えるツール</h2>' + ul('<a href="%s">%s</a>' % t for t in p['tools']) + '\n'
    m += '<h2>ほかの用途別ページ</h2>' + ul('<a href="/for/%s.html">%s</a>' % (o['slug'], o['short']) for o in others if o['slug'] != p['slug']) + '\n'
    m += '<p><a href="/for/">用途別ページの一覧</a></p>\n</div>\n'
    return m

def build(p, others):
    s = T
    url = '%s/for/%s.html' % (BASE, p['slug'])
    s = re.sub(r'<title>.*?</title>', '<title>%s</title>' % E(p['title'], quote=False), s, 1)
    s = re.sub(r'<link href="[^"]*" rel="canonical"/>', '<link href="%s" rel="canonical"/>' % url, s, 1)
    s = re.sub(r'<meta content="[^"]*" name="description"/>', '<meta content="%s" name="description"/>' % E(p['desc']), s, 1)
    s = re.sub(r'<meta content="[^"]*" property="og:title"/>', '<meta content="%s" property="og:title"/>' % E(p['title']), s, 1)
    s = re.sub(r'<meta content="[^"]*" property="og:description"/>', '<meta content="%s" property="og:description"/>' % E(p['desc']), s)
    s = re.sub(r'<meta content="https://pdfmikata.com/for/[^"]*" property="og:url"/>', '<meta content="%s" property="og:url"/>' % url, s)
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "ホーム", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": "用途別", "item": BASE + "/for/"},
        {"@type": "ListItem", "position": 3, "name": p['short'], "item": url}]}
    fq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p['faqs']]}
    lds = ['<script type="application/ld+json">%s</script>' % json.dumps(x, ensure_ascii=False) for x in (bc, fq)]
    it = iter(lds)
    s = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: next(it), s, 2, flags=re.S)
    s = re.sub(r'<li><span aria-current="page">.*?</span></li>', '<li><span aria-current="page">%s</span></li>' % p['short'], s, 1)
    a = s.find('<main'); b = s.find('</main>')
    return s[:a] + main_html(p, others) + s[b:]

OLD = [('resume-pdf-under-1mb','履歴書PDFを1MB以下に'),('es-pdf-merge','ES提出用にPDFを結合'),('tax-return-documents-pdf','確定申告の書類PDFをまとめる'),('resume-photo-data','履歴書の写真データを用意する'),('iphone-photos-to-pdf','iPhoneの書類写真をPDFにする'),('receipts-monthly-pdf','領収書・請求書PDFを月ごとにまとめる'),('pdf-under-5mb-school','学校・提出用にPDFを5MB以下に'),('contract-delete-pages','契約書PDFの不要なページを削除'),('pdf-redact-personal-info','個人情報をPDFで黒塗りする'),('pdf-add-page-numbers-submission','提出書類のPDFにページ番号を入れる')]
ALL = [dict(slug=a, short=b) for a, b in OLD] + [dict(slug=p['slug'], short=p['short']) for p in P]

for p in P:
    open('for/%s.html' % p['slug'], 'w', encoding='utf-8').write(build(p, ALL))

# 既存ページの「ほかの用途別ページ」更新（新規分を追記・冪等）
new_li = ''.join('<li><a href="/for/%s.html">%s</a></li>' % (p['slug'], p['short']) for p in P)
for o in OLD:
    f = 'for/%s.html' % o[0]
    s = open(f, encoding='utf-8').read()
    if P[0]['slug'] in s: continue
    s2 = re.sub(r'(<h2>ほかの用途別ページ</h2><ul>.*?)(</ul>)', lambda m: m.group(1) + new_li + m.group(2), s, 1, flags=re.S)
    assert s2 != s, f
    open(f, 'w', encoding='utf-8').write(s2)

# for/index.html
f = 'for/index.html'; s = open(f, encoding='utf-8').read()
if P[0]['slug'] not in s:
    li = ''.join('<li><a href="/for/%s.html">%s</a>：%s</li>' % (p['slug'], p['short'], p['lead']) for p in P)
    s = s.replace('</ul>\n</div>', li + '</ul>\n</div>', 1) if '</ul>\n</div>' in s else re.sub(r'(<h1>用途別ガイド</h1>.*?)(</ul>)', lambda m: m.group(1) + li + m.group(2), s, 1, flags=re.S)
    open(f, 'w', encoding='utf-8').write(s)

# index.html / guides.html の用途ブロック
for f in ('index.html', 'guides.html'):
    s = open(f, encoding='utf-8').read()
    if P[0]['slug'] in s: continue
    if f == 'index.html':
        cards = ''.join('<li><a href="/for/%s.html"><b><span lang="ja">%s</span></b><span><span lang="ja">%s。</span></span></a></li>' % (p['slug'], p['short'], p['lead']) for p in P)
        s2 = re.sub(r'(id="usecase"><span lang="ja">用途から探す</span></h2>\n<ul class="g">.*?)(</ul>)', lambda m: m.group(1) + cards + m.group(2), s, count=1, flags=re.S)
    else:
        s2 = re.sub(r'(id="usecase"><h2>用途から探す</h2><ul>.*?)(</ul>)', lambda m: m.group(1) + new_li + m.group(2), s, count=1, flags=re.S)
    assert s2 != s, f
    open(f, 'w', encoding='utf-8').write(s2)
    continue
    open(f, 'w', encoding='utf-8').write(s2)

# sitemap
s = open('sitemap.xml', encoding='utf-8').read()
add_ = ''.join('<url><loc>%s/for/%s.html</loc></url>\n' % (BASE, p['slug']) for p in P if p['slug'] not in s)
if add_:
    s = s.replace('</urlset>', add_ + '</urlset>'); open('sitemap.xml', 'w', encoding='utf-8').write(s)
print('done')
