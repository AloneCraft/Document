# <a id="Omni_Converter_Guarantees"></a> Namespace Omni.Converter.Guarantees

### クラス（Classes）

 [OmniConversionGuaranteeTable.Exclusion](Omni.Converter.Guarantees.OmniConversionGuaranteeTable.Exclusion.md)

 [OmniConversionGuaranteeTable.FileEntry](Omni.Converter.Guarantees.OmniConversionGuaranteeTable.FileEntry.md)

 [OmniConversionGuarantee](Omni.Converter.Guarantees.OmniConversionGuarantee.md)

変換の判定（保証済み／検査のみ合格／変換不能）を作る「門」と、判定の置き場です。

<p>
判定は、生成器（<code>OmniShaderGenerator.Generate</code> と <code>GenerateSsao</code>）を包む <xref href="Omni.Converter.Guarantees.OmniConversionGuarantee.RunGuarded(System.String%2cSystem.Func%7bSystem.String%2cSystem.String%7d)" data-throw-if-not-resolved="false"></xref> の中でだけ作ります。
判定がある ⇔ このドメインで、利用者と同じ変換器で生成して確かめた、が成り立つようにするためです（古い生成物に保証を付けない）。
変換不能と判定した元は null を返し、呼び出し側は古い生成物を使いません（部分変換をしない）。
</p>
<p>
置き場はドメイン内の辞書で、<xref href="UnityEditor.SessionState" data-throw-if-not-resolved="false"></xref> に写しを置きます（スクリプトを読み直しても警告が消えないように）。
写しから戻した判定は <code>restored=true</code> にし、パッケージの版が違う判定は捨てます。
</p>

 [OmniConversionGuaranteeTable](Omni.Converter.Guarantees.OmniConversionGuaranteeTable.md)

変換保証表（<code>OmniConversionGuarantees.json</code>）です。検証した Unity と元・出力・約束の版の指紋の組を行に持ちます。
本体の根からの相対パスで持ち、File IO で読みます（Resources には置きません）。表が1か所でも壊れていれば全体を使わず、
どの項目も保証済みにしません（Fail Closed）。

 [OmniConversionItem](Omni.Converter.Guarantees.OmniConversionItem.md)

保証表の対象として分類した元です。<xref href="Omni.Converter.Guarantees.OmniConversionItem.Item" data-throw-if-not-resolved="false"></xref> は判定の鍵（元の資産パス）、<xref href="Omni.Converter.Guarantees.OmniConversionItem.RowItem" data-throw-if-not-resolved="false"></xref> は保証表の行の鍵です。
<xref href="Omni.Converter.Guarantees.OmniConversionItem.UnitSources" data-throw-if-not-resolved="false"></xref> は1回の変換で一緒に生成する元（TerrainLit は4本の閉包）です。

 [OmniConversionReport](Omni.Converter.Guarantees.OmniConversionReport.md)

変換保証の判定を、Omni Manager の通知・Console・ビルドログの文面にします。
判定の写しを読むだけで、指紋の計算や生成はしません。

 [OmniConversionRule](Omni.Converter.Guarantees.OmniConversionRule.md)

版つきの変換規約です。公開した規約は凍結し、書き換えません（不具合は改訂した規約を足して直します）。

 [OmniConversionRuleRegistry](Omni.Converter.Guarantees.OmniConversionRuleRegistry.md)

系統ごとの変換規約の一覧と、元の分類、規約の選び方です。

<p>
規約はコードのデータとして凍結します（保証表が壊れていても、扱える元の範囲と TMP の原本の見分け方が変わらないように）。
範囲より新しい版は一番新しい規約で変換し、良くても「検査のみ合格」にします（決定15）。全ての範囲より古い版、
または引退した規約しか合わない元は「変換不能」です。
</p>

 [OmniConversionVerdict](Omni.Converter.Guarantees.OmniConversionVerdict.md)

1つの元の判定です（SessionState へ写すため Serializable）。

 [OmniFingerprint](Omni.Converter.Guarantees.OmniFingerprint.md)

行の集合から作る指紋です。行は重複を除いて (種類, 鍵) の Ordinal 順に並べるので、集めた順序に依りません。
文化依存の比較や <xref href="System.Environment.NewLine" data-throw-if-not-resolved="false"></xref> を使わないのは、同じ入力が機械によらず同じ値になるためです。

 [OmniFingerprintText](Omni.Converter.Guarantees.OmniFingerprintText.md)

変換保証の指紋に使う本文の正規化と SHA-256 です。

<p>
改行と BOM だけを揃えます。Git の改行の変換や編集器の BOM で、同じ内容の指紋が変わらないようにするためです。
それ以上の正規化（空白・大小文字）はしません。変換器が見る本文の違いを指紋が見落とさないためです。
</p>

 [OmniLogicalKey](Omni.Converter.Guarantees.OmniLogicalKey.md)

資産パスを、機械や配置によらない指紋の鍵にします。
パッケージは <code>@hash</code> の無い論理パス、本体は <code>omni:</code>、生成物は <code>Assets/Radial/</code> のまま、
それ以外の <code>Assets/</code> は基準のフォルダからの相対（<code>asset:</code>）です。小文字化はしません。

 [OmniRadialContractVersion](Omni.Converter.Guarantees.OmniRadialContractVersion.md)

生成物が include する本体の HLSL（Radial の約束）の版です。
本体のファイルは元と出力の指紋に入れず、ここだけに入れます。約束を変えたら、表の行は
「約束が変わった」として検査のみ合格に下がります。中身を変えずに意味だけ変えるときは <xref href="Omni.Converter.Guarantees.OmniRadialContractVersion.Epoch" data-throw-if-not-resolved="false"></xref> を上げます。

 [OmniSourceFingerprints](Omni.Converter.Guarantees.OmniSourceFingerprints.md)

変換の元・出力の指紋を、決まった式（統合仕様 C 節）で取ります。
ShaderLab の include の閉包は Omni.Manager の HLSL 解析が辿るので、Manager が起動時に
<xref href="Omni.Converter.Guarantees.OmniSourceFingerprints.RegisterShaderLabClosure(Omni.Converter.Guarantees.OmniSourceFingerprints.ShaderLabClosure)" data-throw-if-not-resolved="false"></xref> で登録します（Converter は Manager を参照できないため）。

 [OmniTemplateSets](Omni.Converter.Guarantees.OmniTemplateSets.md)

Shader Graph と VFX の変換器が読む、パッケージの雛形の組です。
生成器の C# は重いので含めません（必要になったら IncludeGeneratorSources として足す拡張点です）。

 [OmniVersionSupport](Omni.Converter.Guarantees.OmniVersionSupport.md)

導入済みの Unity と URP／Shader Graph／VFX Graph の版が、Omni の変換規約を検証した範囲の内かを調べます。

 [OmniVersionSupportFinding](Omni.Converter.Guarantees.OmniVersionSupportFinding.md)

対応範囲の外にある、導入済みの Unity またはパッケージの版です。

 [OmniConversionGuaranteeTable.Row](Omni.Converter.Guarantees.OmniConversionGuaranteeTable.Row.md)

### 構造体（Structs）

 [OmniFingerprintEntry](Omni.Converter.Guarantees.OmniFingerprintEntry.md)

 [OmniRuleSelection](Omni.Converter.Guarantees.OmniRuleSelection.md)

### 列挙型（Enums）

 [OmniConversionFamily](Omni.Converter.Guarantees.OmniConversionFamily.md)

変換規約の系統です。系統ごとに別のライフサイクル（パッケージの版）を持ちます。

 [OmniConversionVerdictKind](Omni.Converter.Guarantees.OmniConversionVerdictKind.md)

変換の判定です。

 [OmniFingerprintEntryKind](Omni.Converter.Guarantees.OmniFingerprintEntryKind.md)

 [OmniRuleMatch](Omni.Converter.Guarantees.OmniRuleMatch.md)

インストールされたパッケージの版と、変換規約の範囲の合い方です。

 [OmniVerdictReason](Omni.Converter.Guarantees.OmniVerdictReason.md)

判定の理由です。Guaranteed には理由がありません。
