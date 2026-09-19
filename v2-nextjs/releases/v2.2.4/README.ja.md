# [2026-07-18] v2.2.4 バグ修正

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

## はじめに確認いただく点

v2.2.4 は、**構造要約の計算式と採点表の入力方式を変えていない**、参照文書・AI 検索・安全性の補完リリースです。完成したプロトコルの構造要約の結果を再計算する必要はありません。API キーなしで計算機だけを使う場合も、新たに入力しなければならない被検者情報はありません。

このリリースでは、参照文書と AI 検索資料を改善しました。5 言語の臨床用語は単純な直訳で揃えず、各言語圏の専門文献と学術資料で実際に使われている表現を優先しました。文書の題名と配列も、アルファベット順ではなく採点と構造要約を追いやすい順序に整理しました。

任意機能であるコーディングアシスタントと解釈アシスタントは、Exner 包括システム（CS）の範囲内でのみ答えます。他の検査体系や非公開情報を求める質問には答えません。

## 参照文書

### 画面で読みやすい題名と順序

既存の参照文書のリンクはそのまま維持しつつ、画面に表示される題名を各言語の臨床用語に合わせて変えました。ボタンには `スコアリング`、`形態質（FQ）`、`特殊指標` のように意味の分かる題名が表示されます。

上位の文書は次の流れで配列しました。

1. スコアリング
2. 解釈
3. Upper Section
4. Lower Section
5. Special Indices

スコアリングの文書は、カード、領域、発達質（DQ）、決定因、形態質（FQ）、ペア反応、内容、平凡反応（P）、組織化活動（Z）、スコア、GHR/PHR、特殊スコアの順に続きます。アルファベット順は、同じ範疇の細目を探すときにだけ使います。

### 5 言語の臨床用語

韓国語、英語、日本語、スペイン語、ブラジルポルトガル語の文書は、各言語で自然な専門用語を使います。各文書は中核的な定義、適用条件、注意点、関連項目を説明します。

代表的には次の内容を正しました。

- 英語の PHR 文書で、`ALOG` が判定順の初期の PHR 条件に含まれる点を明確にしました。
- 英語とスペイン語の自然内容の符号で、`Na` が適用されると同じ反応に `Bt` または `Ls` を併せて符号化しない優先順位を明確にしました。
- 日本語の文書で、`Ay` を解剖学的内容ではなく文化的・歴史的内容として説明するように正しました。
- 韓国語の文書で、原頻度である `S-` と別の比率である `S-%` を区別しました。
- 韓国語の S-CON 文書に、満 15 歳以上という適用の境界と 12 の構成基準を明記しました。

これらの変更は、臨床家が反応記録と質問段階（Inquiry）を確認して行う符号化に代わるものではありません。参照文書は符号の定義と区別の基準を確認する補助資料であり、個々の反応の最終的な符号化は引き続き人間の採点者の責任です。

## AI による参照文書検索

AI アシスタントは、現在の参照文書から質問に関連する内容を探します。

次のような短い質問でも関連する説明を併せて探します。

- Cn と WSumC の関係を尋ねる短い質問でも、Cn を含む画面上の値と、Cn を含まない WSumC の説明を併せて探すようにしました。
- `Na`、`Bt`、`Ls` の優先順位を尋ねる質問が、三つの内容符号の一般的な説明だけを探して正確な優先順位の文を見落とすことがないようにしました。

## コーディングアシスタントと解釈アシスタントの範囲

二つのアシスタントは次の原則に従います。

- Exner 包括システム（CS）の符号化と構造要約の質問にだけ答えます。
- R-PAS、MMPI のような別の検査体系や、一般的な相談・診断の質問に回答範囲を広げません。
- サービスの非公開情報や、利用者の API キー・接続情報の開示を求める要求は断ります。
- 解釈に年齢が実際に必要な場合は、AI の会話の中で必要な理由を説明して質問することがありますが、計算機本体に年齢の入力を求めません。
- 構造要約だけで診断や危険を確定せず、面接・行動観察・原資料と臨床家の判断を優先します。

Exner CS の範囲を外れる要求や非公開情報を求める要求には答えず、回答可能な符号化または構造要約の質問を案内します。

## AI リクエストの過度な繰り返しの防止

AI 会話のリクエストが 1 分に 12 回、または 1 時間に 120 回を超えると、しばらく待つよう案内します。この制限は、誤って同じリクエストを繰り返したり、費用が予想より大きくなったりすることを減らします。リクエスト回数を制限するために、API キー、質問、回答、構造要約の原文、臨床的な内容を別途保存することはありません。

「役に立った」「役に立たなかった」の評価は会話の原文を保存せず、最長 180 日保管します。

## 画面とサービス説明の変更点

- 左のサイドバーは、背後の本文が透けない不透明な背景に固定しました。
- サイドバーが折りたたまれた状態で言語メニューを開くと、メニューが切れたり本文の上でずれたりする問題を直しました。
- 参照文書のボタンには、5 言語の題名と採点・解釈の流れに合わせた順序を適用しました。
- 採点画面に入るたびに、新しいデータ、サンプルデータ、保存データのうち開始方法を選び直す画面が開くように戻しました。
- 参照文書のコード形式の重要語句は、ライト・ダークモードのどちらでも区別しやすい赤色で表示します。
- コーディングアシスタントで以前の会話を読むために上へ移動すると現れる下向き矢印を、入力領域のすぐ上に配置しました。長い回答でも矢印が会話画面の中央を隠しません。
- バージョン 2 とバージョン 1 の記録は、最初に開いたときは折りたたまれた状態で表示します。
- サービスの名称は `Exner ロールシャッハ包括システム構造要約計算機` に統一しました。
- サービス紹介には、MOW（モオ）による制作と、ソウル臨床心理研究所（Seoul Institute of Clinical Psychology, SICP）による初期の計算結果の確認および実際の臨床使用の観点からの検討という貢献を表示します。

採点表の列、ドロップダウン、計算ボタン、拡大・縮小の操作、構造要約の結果画面は変わっていません。モバイル画面もそのままです。

AI の応答は毎回異なることがあり、すべての実際の質問に対する臨床的な正確性を保証するものではありません。構造要約の計算の正解を AI の回答で判定することもありません。

## 5 言語の用語の公開出典

各言語の専門的な用例を優先し、包括システムの符号と識別子はそのまま維持します。単一の出典をすべての言語の正解とはしません。

- 韓国語: [KCI - Construction of the Korean Rorschach Comprehensive System for Children based on Exner's Comprehensive System](https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART001392063), [KCI - Coping and defense of North Korean defectors on the Rorschach](https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART001391524)
- 英語: [International Rorschach Institute manuals](https://www.rorschach-institute.org/manuals.html), [Meyer and Viglione, An Introduction to Rorschach Assessment](https://www.utoledo.edu/al/psychology/pdfs/meyer/MeyerViglione2008IntroRorschach.pdf)
- 日本語: [誠信書房 - 包括システムによるロールシャッハ臨床](https://www.seishinshobo.co.jp/book/b88274.html)
- スペイン語: [Sociedad Española de Rorschach y Métodos Proyectivos](https://www.rorschach.es/index.php/programas-de-los-cursos), [CHESSSS](https://rorschachspain.org/chessss/), [Manual de codificación del Rorschach para el Sistema Comprehensivo](https://www.psimatica.com/tienda/psicodiagnostico/23-manual-de-codificacion-del-rorschach-autor-john-exner.html)
- ブラジルポルトガル語: [SciELO - Localização e qualidade formal do Rorschach-SC no Brasil](https://www.scielo.br/j/pusf/a/kFHxFGKH3qx9gdVtyC6nqWS/), [SciELO - Indícios de validade do déficit relacional no Método de Rorschach](https://www.scielo.br/j/pusf/a/6Xy8zSJGCNq49BWjXRpYNhx/)
- 共通の翻訳・適応の原則: [International Test Commission Guidelines](https://www.intestcom.org/page/14)
