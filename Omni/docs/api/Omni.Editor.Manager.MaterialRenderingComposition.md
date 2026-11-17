# <a id="Omni_Editor_Manager_MaterialRenderingComposition"></a> Struct MaterialRenderingComposition

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

選択範囲内の一意なMaterialへ現在設定されているShaderの構成です。
Camera、VFX、Renderer準備状態は切替検証の責務であり、この表示状態へ混ぜません。

```csharp
public readonly struct MaterialRenderingComposition
```

## コンストラクター（Constructors）

### <a id="Omni_Editor_Manager_MaterialRenderingComposition__ctor_System_Int32_System_Int32_System_Int32_System_Int32_System_Int32_System_Boolean_System_Int32_"></a> MaterialRenderingComposition\(int, int, int, int, int, bool, int\)

```csharp
public MaterialRenderingComposition(int standardMaterials, int radialMaterials, int diagnosticMaterials, int unresolvedMaterials, int excludedMaterials, bool reliable, int nativeMaterials = 0)
```

#### 引数（Parameters）

`standardMaterials` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`radialMaterials` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`diagnosticMaterials` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`unresolvedMaterials` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`excludedMaterials` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`reliable` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`nativeMaterials` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_MaterialRenderingComposition_DiagnosticMaterials"></a> DiagnosticMaterials

```csharp
public int DiagnosticMaterials { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_MaterialRenderingComposition_ExcludedMaterials"></a> ExcludedMaterials

```csharp
public int ExcludedMaterials { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_MaterialRenderingComposition_IsFullyRadial"></a> IsFullyRadial

```csharp
public bool IsFullyRadial { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_MaterialRenderingComposition_IsFullyStandard"></a> IsFullyStandard

標準へ戻せるMaterialがすべて標準の状態です。最初からRadialのMaterialは戻す先が無いので、
数に入れません。ネイティブだけのSceneは「標準」にならず、「対数」だけが選ばれます。

```csharp
public bool IsFullyStandard { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_MaterialRenderingComposition_IsMixedOrError"></a> IsMixedOrError

```csharp
public bool IsMixedOrError { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_MaterialRenderingComposition_IsRadialComplete"></a> IsRadialComplete

対数への切替が済んでいる（警告付きを含む）状態です。上部ラジオの「対数」に使います。

```csharp
public bool IsRadialComplete { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_MaterialRenderingComposition_IsRadialWithWarnings"></a> IsRadialWithWarnings

変換できたMaterialはすべて対数で、残りは変換できず診断表示になっている状態です。
切替は完了扱い（警告付き）で、診断表示が変換できない箇所を画面上で示します。

```csharp
public bool IsRadialWithWarnings { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_MaterialRenderingComposition_NativeMaterials"></a> NativeMaterials

最初からRadialのMaterial数です（<xref href="Omni.Editor.Manager.MaterialRenderingComposition.RadialMaterials" data-throw-if-not-resolved="false"></xref> の一部）。対数として数えますが、
標準へ戻す先が無いため、標準への切替の判定（<xref href="Omni.Editor.Manager.MaterialRenderingComposition.IsFullyStandard" data-throw-if-not-resolved="false"></xref>）からは外します（UB-009）。

```csharp
public int NativeMaterials { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_MaterialRenderingComposition_RadialMaterials"></a> RadialMaterials

```csharp
public int RadialMaterials { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_MaterialRenderingComposition_Reliable"></a> Reliable

```csharp
public bool Reliable { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_MaterialRenderingComposition_StandardMaterials"></a> StandardMaterials

```csharp
public int StandardMaterials { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_MaterialRenderingComposition_SwitchTargetMaterials"></a> SwitchTargetMaterials

```csharp
public int SwitchTargetMaterials { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_MaterialRenderingComposition_TotalMaterials"></a> TotalMaterials

```csharp
public int TotalMaterials { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_MaterialRenderingComposition_UnresolvedMaterials"></a> UnresolvedMaterials

```csharp
public int UnresolvedMaterials { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_MaterialRenderingComposition_FromEntries_System_Collections_Generic_IEnumerable_Omni_Editor_Manager_MaterialEntry__System_Boolean_"></a> FromEntries\(IEnumerable<MaterialEntry\>, bool\)

Material一覧の現在値から、ラジオ表示専用の構成を集計します。

```csharp
public static MaterialRenderingComposition FromEntries(IEnumerable<MaterialEntry> entries, bool reliable = true)
```

#### 引数（Parameters）

`entries` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[MaterialEntry](Omni.Editor.Manager.MaterialEntry.md)\>

`reliable` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [MaterialRenderingComposition](Omni.Editor.Manager.MaterialRenderingComposition.md)
