# -*- coding: utf-8 -*-
def L(*a): return "<ul>" + "".join("<li>%s</li>" % x for x in a) + "</ul>"
MORE8 = {
"vlookup-formula-builder": ("VLOOKUP・XLOOKUPの式を作る前に知っておきたいこと", [
 ("向いている場面", L("VLOOKUPの書き方を、忘れたとき", "商品コードから、商品名や価格を引きたいとき", "表から、別の表へ値を持ってきたいとき")),
 ("式のしくみ", L("探す値のセルと、探す範囲、取り出す列の番号の3つを入れます", "範囲の1列目に、探す値が入っている必要があります", "完全一致、$の有無、エラー時に空欄にするかを選べます")),
 ("VLOOKUPとXLOOKUPの使い分け", "<p>同じ内容のXLOOKUPの式も、同時に作ります。XLOOKUPは、新しいExcelやGoogleスプレッドシートで使えます。探す列より左の値を取り出したいときは、<a href=\"/index-match-builder.html\">INDEX・MATCH</a> か、XLOOKUPが向いています。</p>")],
 ["/vlookup-formula-builder-howto.html", "/vlookup-formula-builder-trouble.html", "/xlookup-formula-builder.html"]),
"excel-if-builder": ("IF関数の式を作る前に知っておきたいこと", [
 ("向いている場面", L("合格・不合格のように、条件で表示を分けたいとき", "金額が基準を超えたときだけ、印を付けたいとき", "空欄のときだけ、別の表示にしたいとき")),
 ("式のしくみ", L("調べるセルと、比較と、比べる値を入れます", "合うときの結果と、合わないときの結果を入れます", "数字やセルはそのまま、文字は自動で引用符で囲みます")),
 ("IFSについて", "<p>同じ内容のIFSの式も、同時に作ります。条件が3つ以上に分かれるときは、IFSのほうが読みやすくなります。IFSは、新しいExcelやGoogleスプレッドシートで使えます。結果を空欄にしたいときは、結果の欄を空にします。</p>")],
 ["/excel-if-builder-howto.html", "/excel-if-builder-ifs.html", "/countif-formula-builder.html"]),
"sumif-formula-builder": ("SUMIF・COUNTIFの式を作る前に知っておきたいこと", [
 ("向いている場面", L("条件に合うセルだけを、合計したいとき", "条件に合うセルの数を、数えたいとき", "条件に合うセルの、平均を出したいとき")),
 ("式のしくみ", L("SUMIF、COUNTIF、AVERAGEIFから選べます", "条件を調べる範囲と、条件、合計する範囲を入れます", "条件に「>=80」のような比較も入れられます")),
 ("複数の条件のとき", "<p>複数条件に使えるSUMIFSなどの式も、同時に作ります。COUNTIFでは、合計する範囲は使いません。</p>")],
 ["/sumif-formula-builder-howto.html", "/sumif-formula-builder-sumifs.html", "/countif-formula-builder.html"]),
"countif-formula-builder": ("条件に合う数を数える式を作る前に知っておきたいこと", [
 ("向いている場面", L("条件に合うデータが、何件あるか数えたいとき", "空のセルや、入っているセルの数を知りたいとき", "重なりを除いた件数を知りたいとき")),
 ("種類の選び方", L("COUNTIF：条件に合うセルの数。COUNTIFSは、2つの条件に合うセルの数です", "COUNTBLANK：空のセルの数。COUNTA：入っているセルの数です", "CONTAINS：文字を含むセルの数。UNIQUE：重なりを除いた数です")),
 ("注意すること", "<p>UNIQUEは、空のセルがあるときは、2つ目の式を使います。</p>")],
 ["/countif-formula-builder-howto.html", "/countif-formula-builder-unique.html", "/sumif-formula-builder.html"]),
"xlookup-formula-builder": ("XLOOKUPの式を作る前に知っておきたいこと", [
 ("向いている場面", L("VLOOKUPより柔軟に、表から値を探したいとき", "探す列より左の値を、取り出したいとき", "下から探したいときや、近い値を探したいとき")),
 ("種類の選び方", L("XLOOKUP：探す列で見つけた行の、返す列の値を出します", "XMATCH：見つけた位置の番号を出します", "LAST：下から探します。APPROX：近い小さい値を探します。REVERSE：右の列から左の列の値を出します")),
 ("古いExcelの場合", "<p>2つ目の式は、XLOOKUPがない古いExcelでも使えます。</p>")],
 ["/xlookup-formula-builder-howto.html", "/xlookup-formula-builder-old.html", "/vlookup-formula-builder.html"]),
"index-match-builder": ("INDEX・MATCHの式を作る前に知っておきたいこと", [
 ("向いている場面", L("VLOOKUPでは、左の列を取り出せないとき", "行と列の両方から、値を探したいとき（表から取り出すとき）", "列の挿入にも強い式を、使いたいとき")),
 ("式のしくみ", "<p>INDEXで取り出す位置を、MATCHで探します。範囲には$を付けて固定するので、下にコピーしてもずれません。見つからないときに空にする式も、あわせて作ります。</p>"),
 ("一致の種類", L("EXACT：完全一致", "LESS：以下で近い値", "GREATER：以上で近い値"))],
 ["/index-match-builder-howto.html", "/index-match-builder-left.html", "/vlookup-formula-builder.html"]),
"filter-formula-builder": ("FILTERの式を作る前に知っておきたいこと", [
 ("向いている場面", L("表から、条件に合う行だけを取り出したいとき", "取り出した行を、小さい順に並べたいとき", "別のシートに、条件に合うデータだけを出したいとき")),
 ("式のしくみ", L("取り出したいデータの範囲を入れます", "条件を調べる列と、比較と、比べる値を入れます", "小さい順に並べるSORT付きの式も、同時に作ります")),
 ("注意すること", "<p>見つからないときの表示を空にすると、その指定は付きません。FILTERは、新しいExcelやGoogleスプレッドシートで使えます。</p>")],
 ["/filter-formula-builder-howto.html", "/filter-formula-builder-nomatch.html", "/sumif-formula-builder.html"]),
"textjoin-formula-builder": ("TEXTJOINの式を作る前に知っておきたいこと", [
 ("向いている場面", L("複数のセルの文字を、1つのセルにまとめたいとき", "名前や住所の列を、カンマや空白でつなぎたいとき", "空白のセルを飛ばして、つなぎたいとき")),
 ("2つの式の違い", L("TEXTJOIN：区切る文字を決められ、空白のセルを飛ばすかどうかを選べます", "&でつなぐ式：空白のセルも飛ばさずにつなぎます")),
 ("注意すること", "<p>TEXTJOINは、新しいExcelやGoogleスプレッドシートで使えます。</p>")],
 ["/textjoin-formula-builder-howto.html", "/textjoin-formula-builder-amp.html", "/excel-text-clean.html"]),
"datedif-formula-builder": ("DATEDIFの式を作る前に知っておきたいこと", [
 ("向いている場面", L("年齢や勤続年数など、日付の差を求めたいとき", "2つの日付の間の、月数や日数を知りたいとき", "「○年○か月」の形で表示したいとき")),
 ("単位の選び方", L("Y：年の差、M：月の差、D：日の差", "YM：年を除いた月数、MD：月を除いた日数")),
 ("注意すること", "<p>開始日は、終了日より前にします。年と月で表示する式も、同時に作ります。</p>")],
 ["/datedif-formula-builder-howto.html", "/datedif-formula-builder-age.html", "/date-calculator.html"]),
"round-formula-builder": ("丸めの式を作る前に知っておきたいこと", [
 ("向いている場面", L("金額や数値を、決まった桁で丸めたいとき", "10円単位や0.5単位に、そろえたいとき", "消費税の端数を、処理したいとき")),
 ("関数の選び方", L("ROUND：四捨五入。ROUNDUP：切り上げ。ROUNDDOWN：切り捨て", "CEILING・FLOOR・MROUND：10や0.5のような単位に丸めます")),
 ("桁数の考え方", "<p>桁数が0なら整数に、2なら小数第2位までになります。試しの数値を入れると、結果の例も確かめられます。</p>")],
 ["/round-formula-builder-howto.html", "/round-formula-builder-digits.html", "/tax-calculator.html"]),
"xlsx-formula-to-value": ("計算式を値にする前に知っておきたいこと", [
 ("向いている場面", L("ほかの人に渡す前に、計算の中身を見せたくないとき", "計算式を消して、結果の値だけを残したいとき")),
 ("仕組み", "<p>計算式を消して、その結果の値だけを残します。元のファイルは変わらず、新しいファイル（名前の末尾に _values）で保存されます。書式やシートの見た目は、そのまま残ります。</p>"),
 ("注意すること", L("保存されている計算結果が、そのまま値になります。最新の結果にしたいときは、先にExcelで保存し直してから使います", "新しいファイルの計算式は消えて、元には戻せません。元のファイルは、別に取っておいてください"))],
 ["/xlsx-formula-to-value-howto.html", "/xlsx-formula-to-value-stale.html", "/office-metadata-remove.html"]),
}
