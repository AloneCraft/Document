# <a id="Omni_Diagnostics_OmniBenchmarkSceneDescriptor"></a> Struct OmniBenchmarkSceneDescriptor

Namespace: [Omni.Diagnostics](Omni.Diagnostics.md)  
Assembly: Radial.Runtime.dll  

シーンが確定した描画backendと比較可能性をRunnerへ返す不変の記述子です。

```csharp
public readonly struct OmniBenchmarkSceneDescriptor
```

## コンストラクター（Constructors）

### <a id="Omni_Diagnostics_OmniBenchmarkSceneDescriptor__ctor_System_String_System_String_System_Boolean_System_String_"></a> OmniBenchmarkSceneDescriptor\(string, string, bool, string\)

シーン記述子を作成します。

```csharp
public OmniBenchmarkSceneDescriptor(string backend, string contentFingerprint, bool validForComparison, string comparisonInvalidReason)
```

#### 引数（Parameters）

`backend` [string](https://learn.microsoft.com/dotnet/api/system.string)

実際の描画backend名です。

`contentFingerprint` [string](https://learn.microsoft.com/dotnet/api/system.string)

固定コンテンツのfingerprintです。

`validForComparison` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

シーン固有の比較可能性です。

`comparisonInvalidReason` [string](https://learn.microsoft.com/dotnet/api/system.string)

比較不能理由です。

## プロパティ（Properties）

### <a id="Omni_Diagnostics_OmniBenchmarkSceneDescriptor_Backend"></a> Backend

実際に使用する描画backend名です。例: BRG、MacroOnly、Fallback。

```csharp
public string Backend { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniBenchmarkSceneDescriptor_ComparisonInvalidReason"></a> ComparisonInvalidReason

比較不能な場合の機械可読な理由です。比較可能なら空文字列です。

```csharp
public string ComparisonInvalidReason { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniBenchmarkSceneDescriptor_ContentFingerprint"></a> ContentFingerprint

同一のDefinition、Seed、アセット内容から計算した固定fingerprintです。

```csharp
public string ContentFingerprint { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Diagnostics_OmniBenchmarkSceneDescriptor_ValidForComparison"></a> ValidForComparison

シーン側の前提が比較可能ならtrueです。

```csharp
public bool ValidForComparison { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
