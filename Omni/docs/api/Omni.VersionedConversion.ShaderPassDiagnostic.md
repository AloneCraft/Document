# <a id="Omni_VersionedConversion_ShaderPassDiagnostic"></a> Class ShaderPassDiagnostic

Namespace: [Omni.VersionedConversion](Omni.VersionedConversion.md)  
Assembly: Omni.VersionedConversion.dll  

Pass ごとの元の判定と診断を、共通入口へ渡します。

```csharp
public sealed class ShaderPassDiagnostic
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ShaderPassDiagnostic](Omni.VersionedConversion.ShaderPassDiagnostic.md)

## プロパティ（Properties）

### <a id="Omni_VersionedConversion_ShaderPassDiagnostic_Detail"></a> Detail

```csharp
public string Detail { get; set; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_VersionedConversion_ShaderPassDiagnostic_IsError"></a> IsError

```csharp
public bool IsError { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VersionedConversion_ShaderPassDiagnostic_IsNoteworthy"></a> IsNoteworthy

```csharp
public bool IsNoteworthy { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VersionedConversion_ShaderPassDiagnostic_LightMode"></a> LightMode

```csharp
public string LightMode { get; set; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_VersionedConversion_ShaderPassDiagnostic_Outcome"></a> Outcome

```csharp
public ShaderPassOutcome Outcome { get; set; }
```

#### 値（Property Value）

 [ShaderPassOutcome](Omni.VersionedConversion.ShaderPassOutcome.md)

### <a id="Omni_VersionedConversion_ShaderPassDiagnostic_PassIndex"></a> PassIndex

```csharp
public int PassIndex { get; set; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_VersionedConversion_ShaderPassDiagnostic_PassLabel"></a> PassLabel

```csharp
public string PassLabel { get; set; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_VersionedConversion_ShaderPassDiagnostic_SubShaderIndex"></a> SubShaderIndex

```csharp
public int SubShaderIndex { get; set; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_VersionedConversion_ShaderPassDiagnostic_ToString"></a> ToString\(\)

既存の変換診断と同じ利用者向け表記を保持します。

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
