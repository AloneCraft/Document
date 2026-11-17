# <a id="Omni_Localization"></a> Namespace Omni.Localization

### クラス（Classes）

 [OmniL10n](Omni.Localization.OmniL10n.md)

Omni独自のgettext方式ローカライズAPIです。カタログは<code>Assets/Omni/Core/Localization~/&lt;locale&gt;.po</code>から
Editor専用に読み込みます。フォルダ名の<code>~</code>は、.poをUnityの翻訳機能（LocalizationImporter）に取り込ませないためです（取り込ませるとpackageで「will not be compiled」のエラーになります）。Playerビルドにはカタログを含めず、Tr()はmsgid(英語原文)をそのまま返します。

 [OmniPoParser](Omni.Localization.OmniPoParser.md)

gettext .po形式の必要最小サブセットを読むパーサです。
msgctxt/msgid/msgstrの複数行連結とエスケープ(\n \t \" \\)、
#, fuzzyと#~(廃止エントリ)のスキップに対応します。複数形(msgid_plural/msgstr[N])は非対応です。

### 構造体（Structs）

 [OmniPoParser.Entry](Omni.Localization.OmniPoParser.Entry.md)

1エントリ分の構造化データです。<xref href="Omni.Localization.OmniPoParser.Entry.Context" data-throw-if-not-resolved="false"></xref>は無ければnullです。
