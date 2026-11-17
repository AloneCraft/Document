# <a id="Omni_Converter_OmniBuildRadialDecision"></a> Class OmniBuildRadialDecision

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

Player Build 1回分の判定です。

```csharp
public sealed class OmniBuildRadialDecision
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniBuildRadialDecision](Omni.Converter.OmniBuildRadialDecision.md)

## プロパティ（Properties）

### <a id="Omni_Converter_OmniBuildRadialDecision_Determined"></a> Determined

判定できたなら true です。false のとき <xref href="Omni.Converter.OmniBuildRadialDecision.UsesRadial" data-throw-if-not-resolved="false"></xref> は Fail Closed の true です。

```csharp
public bool Determined { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniBuildRadialDecision_Reason"></a> Reason

判定の理由です（ビルドログと拒否文に使います）。

```csharp
public string Reason { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniBuildRadialDecision_Scenes"></a> Scenes

判定に使ったビルドの Scene です。

```csharp
public IReadOnlyList<string> Scenes { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_OmniBuildRadialDecision_UsesRadial"></a> UsesRadial

対数を使うなら true です。判定できなかったときも true です（Fail Closed）。

```csharp
public bool UsesRadial { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
