# <a id="Omni_Converter_Guarantees_OmniConversionReport"></a> Class OmniConversionReport

Namespace: [Omni.Converter.Guarantees](Omni.Converter.Guarantees.md)  
Assembly: Omni.Converter.dll  

変換保証の判定を、Omni Manager の通知・Console・ビルドログの文面にします。
判定の写しを読むだけで、指紋の計算や生成はしません。

```csharp
public static class OmniConversionReport
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniConversionReport](Omni.Converter.Guarantees.OmniConversionReport.md)

## 補足（Remarks）

同じ項目の判定が重なって渡されても1件として数えます（後の判定を使います）。
「保証済み」は Console へ出しません（決定2: 表示は警告と変換不能だけ）。
保証の意味（2026-10-09 のユーザー判断）: 変換が再現すること、つまり変換の入力が検証済みのものと同じなら同じ出力になること。
見た目の正しさの保証ではありません（<xref href="Omni.Converter.Guarantees.OmniConversionReport.GuaranteeMeaningText" data-throw-if-not-resolved="false"></xref>）。Shader Graph の視線の警告（変換器が直せない使い方）は
見た目についての別の軸なので、保証済みの Graph（URP 同梱の SpeedTree の Graph など）に出ても矛盾しません。

## メソッド（Methods）

### <a id="Omni_Converter_Guarantees_OmniConversionReport_BuildLogLine_Omni_Converter_Guarantees_OmniConversionFamily_System_Collections_Generic_IReadOnlyList_Omni_Converter_Guarantees_OmniConversionVerdict__"></a> BuildLogLine\(OmniConversionFamily, IReadOnlyList<OmniConversionVerdict\>\)

ビルドログの1行です（ほかの <code>[Omni][Build Preparation]</code> の行と同じく、英語の原文を Omni の表示言語へ訳します）。
<code class="paramref">family</code> の判定だけを数えます。

```csharp
public static string BuildLogLine(OmniConversionFamily family, IReadOnlyList<OmniConversionVerdict> verdicts)
```

#### 引数（Parameters）

`family` [OmniConversionFamily](Omni.Converter.Guarantees.OmniConversionFamily.md)

`verdicts` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniConversionVerdict](Omni.Converter.Guarantees.OmniConversionVerdict.md)\>

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionReport_Details_System_Collections_Generic_IReadOnlyList_Omni_Converter_Guarantees_OmniConversionVerdict__System_Int32_"></a> Details\(IReadOnlyList<OmniConversionVerdict\>, int\)

1項目1行の詳細です。<code class="paramref">maxLines</code> を超えるときは、最後の行を残りの件数にします。
0 以下なら全てを出します。

```csharp
public static string Details(IReadOnlyList<OmniConversionVerdict> verdicts, int maxLines)
```

#### 引数（Parameters）

`verdicts` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniConversionVerdict](Omni.Converter.Guarantees.OmniConversionVerdict.md)\>

`maxLines` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionReport_FamilyLabel_Omni_Converter_Guarantees_OmniConversionFamily_"></a> FamilyLabel\(OmniConversionFamily\)

系統の表示名です（固有名なので訳しません）。

```csharp
public static string FamilyLabel(OmniConversionFamily family)
```

#### 引数（Parameters）

`family` [OmniConversionFamily](Omni.Converter.Guarantees.OmniConversionFamily.md)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionReport_GuaranteeMeaningText"></a> GuaranteeMeaningText\(\)

変換保証の意味の1文です（通知の本文の末尾、通知の tooltip、Console の詳細に添えます）。
保証は「変換が再現すること」で、見た目の正しさの保証ではありません。

```csharp
public static string GuaranteeMeaningText()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionReport_LogDetailsToConsole_System_Collections_Generic_IReadOnlyList_Omni_Converter_Guarantees_OmniConversionVerdict__"></a> LogDetailsToConsole\(IReadOnlyList<OmniConversionVerdict\>\)

Manager の「Console に詳細」の操作です。全項目と保証の意味を1回の Log にまとめます。

```csharp
public static void LogDetailsToConsole(IReadOnlyList<OmniConversionVerdict> verdicts)
```

#### 引数（Parameters）

`verdicts` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniConversionVerdict](Omni.Converter.Guarantees.OmniConversionVerdict.md)\>

### <a id="Omni_Converter_Guarantees_OmniConversionReport_NoticeText_Omni_Converter_Guarantees_OmniConversionVerdictKind_System_Collections_Generic_IReadOnlyList_Omni_Converter_Guarantees_OmniConversionVerdict__"></a> NoticeText\(OmniConversionVerdictKind, IReadOnlyList<OmniConversionVerdict\>\)

判定の種類ごとの通知の本文です。該当する判定が無いとき、または「保証済み」のときは空文字です。
「検査のみ合格」の本文には、保証の意味（<xref href="Omni.Converter.Guarantees.OmniConversionReport.GuaranteeMeaningText" data-throw-if-not-resolved="false"></xref>）を添えます（保証が適用されないことを、
見た目の誤りが見つかったと読ませないため）。

```csharp
public static string NoticeText(OmniConversionVerdictKind kind, IReadOnlyList<OmniConversionVerdict> verdicts)
```

#### 引数（Parameters）

`kind` [OmniConversionVerdictKind](Omni.Converter.Guarantees.OmniConversionVerdictKind.md)

`verdicts` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniConversionVerdict](Omni.Converter.Guarantees.OmniConversionVerdict.md)\>

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionReport_TableUnavailableText_System_String_"></a> TableUnavailableText\(string\)

変換保証表を読めないときの通知の本文です。

```csharp
public static string TableUnavailableText(string error)
```

#### 引数（Parameters）

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionReport_TooltipText_System_Collections_Generic_IReadOnlyList_Omni_Converter_Guarantees_OmniConversionVerdict__"></a> TooltipText\(IReadOnlyList<OmniConversionVerdict\>\)

系統ごとの規約、約束の版の先頭12桁、検証した Unity、Run ID、パッケージの版です（通知の tooltip）。

```csharp
public static string TooltipText(IReadOnlyList<OmniConversionVerdict> verdicts)
```

#### 引数（Parameters）

`verdicts` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniConversionVerdict](Omni.Converter.Guarantees.OmniConversionVerdict.md)\>

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
