# 自分のマークダウンで書いた勉強ノートをhtmlに変換

[VS CodeでMarkdownをHTMLやPDFに変換するには？：Visual Studio Code TIPS - ＠IT (atmarkit.co.jp)](https://www.atmarkit.co.jp/ait/articles/1804/27/news034.html)

Markdown PDFをインストール、保存と同時に変換を実行してくれるよう設定を変更。

[VSCodeでMarkdownの改行をする - Qiita](https://qiita.com/fuk101/items/0fea05c93e70195275c3)

変換してできたhtmlで改行が思った通りにならなかったので、ここでちょっと設定を変えて調整。

[VSCode の Markdown で数式を表示して PDF 化する - Qiita](https://qiita.com/1gy/items/5b1f3c772b6da43cc13e)

Markdown Mathをインストールしてtemplate.htmlを書き換える。これでマークダウンで記述したものがTeX数式を含めhtmlに変換されるようになった。

ただし、数式を一行に書かないと数式として認識されなかった。(謎)

OK

```
$$\begin{aligned}&_nP_r=\frac{n!}{(n-r)!}\\\\&_nC_r=\frac{n!}{r!(n-r)!}\end{aligned}$$
```

NG

```
$$
\begin{aligned}
&_nP_r=\frac{n!}{(n-r)!} \\\\
&_nC_r=\frac{n!}{r!(n-r)!}
\end{aligned}
$$
```



最後に、Typoraのデフォルトのテーマ(Github)が好きなのでTyporaのテーマのCSSをぶっこ抜いてくる。(Typoraをアンインストールしたときとかで使えなくなると困るので)好きなテーマのCSSを適当な場所にコピーして、そのCSSファイルをMarkdown PDFのオプション`Markdown-pdf:Styles`に登録。

