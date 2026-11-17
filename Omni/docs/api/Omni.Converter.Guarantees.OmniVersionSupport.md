# <a id="Omni_Converter_Guarantees_OmniVersionSupport"></a> Class OmniVersionSupport

Namespace: [Omni.Converter.Guarantees](Omni.Converter.Guarantees.md)  
Assembly: Omni.Converter.dll  

導入済みの Unity と URP／Shader Graph／VFX Graph の版が、Omni の変換規約を検証した範囲の内かを調べます。

```csharp
public static class OmniVersionSupport
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniVersionSupport](Omni.Converter.Guarantees.OmniVersionSupport.md)

## 補足（Remarks）

変換規約は URP の HLSL を文字列として書き換えるので、規約の範囲より新しい版では書き換え位置が合わず、
Fail Closed で変換不能になります（Unity 7.0／URP 17.7.0 の URP Package Samples で確認）。
切替のあとにログを掘らなくても分かるよう、版の組み合わせの時点で知らせるための判定です。
変換そのものは止めません（範囲より新しい版は従来どおり最新の規約で試します）。

## フィールド（Fields）

### <a id="Omni_Converter_Guarantees_OmniVersionSupport_VerifiedUnityLine"></a> VerifiedUnityLine

Omni を検証した Unity の系統です（package.json の <code>unity</code> と同じ値）。

```csharp
public const string VerifiedUnityLine = "6000.6"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Converter_Guarantees_OmniVersionSupport_Describe_System_Collections_Generic_IReadOnlyList_Omni_Converter_Guarantees_OmniVersionSupportFinding__"></a> Describe\(IReadOnlyList<OmniVersionSupportFinding\>\)

版ごとの1行と、起こりうる影響をまとめた全文です。

```csharp
public static string Describe(IReadOnlyList<OmniVersionSupportFinding> findings)
```

#### 引数（Parameters）

`findings` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniVersionSupportFinding](Omni.Converter.Guarantees.OmniVersionSupportFinding.md)\>

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniVersionSupport_Evaluate_System_String_System_Collections_Generic_IReadOnlyList_Omni_Converter_Guarantees_OmniConversionRule__System_Func_System_String_System_String__"></a> Evaluate\(string, IReadOnlyList<OmniConversionRule\>, Func<string, string\>\)

範囲の外の版を返します。パッケージが入っていない系統（版が取れない）は対象にしません。
規約と版の取得を引数で受けるので、EditMode テストが任意の版で試せます。

```csharp
public static List<OmniVersionSupportFinding> Evaluate(string unityVersion, IReadOnlyList<OmniConversionRule> rules, Func<string, string> installedVersionOf)
```

#### 引数（Parameters）

`unityVersion` [string](https://learn.microsoft.com/dotnet/api/system.string)

`rules` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniConversionRule](Omni.Converter.Guarantees.OmniConversionRule.md)\>

`installedVersionOf` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

#### 戻り値（Returns）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniVersionSupportFinding](Omni.Converter.Guarantees.OmniVersionSupportFinding.md)\>

### <a id="Omni_Converter_Guarantees_OmniVersionSupport_EvaluateInstalled"></a> EvaluateInstalled\(\)

現在の環境の判定です。

```csharp
public static List<OmniVersionSupportFinding> EvaluateInstalled()
```

#### 戻り値（Returns）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniVersionSupportFinding](Omni.Converter.Guarantees.OmniVersionSupportFinding.md)\>

### <a id="Omni_Converter_Guarantees_OmniVersionSupport_FailureHint_Omni_Converter_Guarantees_OmniRuleMatch_System_String_System_String_"></a> FailureHint\(OmniRuleMatch, string, string\)

変換が失敗した判定の詳細へ足す、版が原因かもしれない旨の文です。範囲内なら null です。

```csharp
public static string FailureHint(OmniRuleMatch match, string ruleId, string installedVersion)
```

#### 引数（Parameters）

`match` [OmniRuleMatch](Omni.Converter.Guarantees.OmniRuleMatch.md)

`ruleId` [string](https://learn.microsoft.com/dotnet/api/system.string)

`installedVersion` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniVersionSupport_Headline"></a> Headline\(\)

見出し（1行）です。

```csharp
public static string Headline()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniVersionSupport_Signature_System_Collections_Generic_IReadOnlyList_Omni_Converter_Guarantees_OmniVersionSupportFinding__"></a> Signature\(IReadOnlyList<OmniVersionSupportFinding\>\)

同じ版の組み合わせで警告を繰り返さないための署名です。

```csharp
public static string Signature(IReadOnlyList<OmniVersionSupportFinding> findings)
```

#### 引数（Parameters）

`findings` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniVersionSupportFinding](Omni.Converter.Guarantees.OmniVersionSupportFinding.md)\>

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
