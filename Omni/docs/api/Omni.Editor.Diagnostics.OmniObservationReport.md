# <a id="Omni_Editor_Diagnostics_OmniObservationReport"></a> Class OmniObservationReport

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

JsonUtility で保存できる観測の報告です。enum は読みやすさのため名前の文字列で持ちます。

```csharp
[Serializable]
public sealed class OmniObservationReport
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)

## フィールド（Fields）

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_CurrentSchemaVersion"></a> CurrentSchemaVersion

この報告の JSON 形式の版です。

```csharp
public const int CurrentSchemaVersion = 1
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_MarkerPrefix"></a> MarkerPrefix

応答本文の 1 行目に置くマーカー行の接頭辞です。

```csharp
public const string MarkerPrefix = "omni-observation-outcome="
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_capturedAtUtc"></a> capturedAtUtc

```csharp
public string capturedAtUtc
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_detail"></a> detail

```csharp
public string detail
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_environment"></a> environment

```csharp
public OmniObservationEnvironment environment
```

#### 値（Field Value）

 [OmniObservationEnvironment](Omni.Editor.Diagnostics.OmniObservationEnvironment.md)

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_observer"></a> observer

```csharp
public string observer
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_outcome"></a> outcome

```csharp
public string outcome
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_reasons"></a> reasons

```csharp
public string[] reasons
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_schemaVersion"></a> schemaVersion

```csharp
public int schemaVersion
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_ExitCode"></a> ExitCode

外部ランナーの終了コード（0/1/2）です。

```csharp
public int ExitCode { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_IsPassed"></a> IsPassed

合格したときだけ true です。

```csharp
public bool IsPassed { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_Outcome"></a> Outcome

<xref href="Omni.Editor.Diagnostics.OmniObservationReport.outcome" data-throw-if-not-resolved="false"></xref> の文字列から復元した結果です。JSON から読み戻した後も同じ値になるよう、
保存はせずに毎回計算します。読めない値は成功側へ倒さず <xref href="Omni.Editor.Diagnostics.OmniObservationOutcome.Failed" data-throw-if-not-resolved="false"></xref> にします。

```csharp
public OmniObservationOutcome Outcome { get; }
```

#### 値（Property Value）

 [OmniObservationOutcome](Omni.Editor.Diagnostics.OmniObservationOutcome.md)

## メソッド（Methods）

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_Create_System_String_Omni_Editor_Diagnostics_OmniObservationOutcome_System_Collections_Generic_IReadOnlyList_Omni_Editor_Diagnostics_OmniObservationReason__System_String_"></a> Create\(string, OmniObservationOutcome, IReadOnlyList<OmniObservationReason\>, string\)

報告を作ります。理由は重複を除いて enum の宣言順に並べるため、同じ入力からは同じ文字列になります。

```csharp
public static OmniObservationReport Create(string observer, OmniObservationOutcome outcome, IReadOnlyList<OmniObservationReason> reasons, string detail)
```

#### 引数（Parameters）

`observer` [string](https://learn.microsoft.com/dotnet/api/system.string)

観測した入口の名前です。

`outcome` [OmniObservationOutcome](Omni.Editor.Diagnostics.OmniObservationOutcome.md)

観測の結果です。

`reasons` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniObservationReason](Omni.Editor.Diagnostics.OmniObservationReason.md)\>

観測を無効にした理由です。Passed では空でなければなりません。

`detail` [string](https://learn.microsoft.com/dotnet/api/system.string)

人が読む補足です。

#### 戻り値（Returns）

 [OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)

#### 例外（Exceptions）

 [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception)

Passed に理由がある、または Unavailable に理由が無い場合。

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_GetReasons"></a> GetReasons\(\)

保存された理由の名前を enum として返します。未知の名前は読み飛ばします。

```csharp
public OmniObservationReason[] GetReasons()
```

#### 戻り値（Returns）

 [OmniObservationReason](Omni.Editor.Diagnostics.OmniObservationReason.md)\[\]

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_PrependMarker_System_String_"></a> PrependMarker\(string\)

マーカー行、改行、本文の順に連結します。本文が既にマーカー行で始まる場合は、その行をこの報告の行で
置き換え、マーカー行を二重にしません。

```csharp
public string PrependMarker(string body)
```

#### 引数（Parameters）

`body` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_ToJson_System_Boolean_"></a> ToJson\(bool\)

JsonUtility で JSON にします。

```csharp
public string ToJson(bool prettyPrint = true)
```

#### 引数（Parameters）

`prettyPrint` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_ToMarkerLine"></a> ToMarkerLine\(\)

応答本文の 1 行目に置くマーカー行です。例 "omni-observation-outcome=Unavailable; reasons=ZeroTests"。

```csharp
public string ToMarkerLine()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_TryFromJson_System_String_Omni_Editor_Diagnostics_OmniObservationReport__"></a> TryFromJson\(string, out OmniObservationReport\)

JSON から報告を読み戻します。形式が違う場合は false を返します。

```csharp
public static bool TryFromJson(string json, out OmniObservationReport report)
```

#### 引数（Parameters）

`json` [string](https://learn.microsoft.com/dotnet/api/system.string)

`report` [OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniObservationReport_TryParseMarkerLine_System_String_Omni_Editor_Diagnostics_OmniObservationOutcome__System_String____"></a> TryParseMarkerLine\(string, out OmniObservationOutcome, out string\[\]\)

マーカー行を読みます。書式が違う行は false です。

```csharp
public static bool TryParseMarkerLine(string line, out OmniObservationOutcome outcome, out string[] reasons)
```

#### 引数（Parameters）

`line` [string](https://learn.microsoft.com/dotnet/api/system.string)

`outcome` [OmniObservationOutcome](Omni.Editor.Diagnostics.OmniObservationOutcome.md)

`reasons` [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
