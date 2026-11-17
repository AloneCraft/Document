# <a id="Omni_Converter_Guarantees_OmniConversionGuarantee"></a> Class OmniConversionGuarantee

Namespace: [Omni.Converter.Guarantees](Omni.Converter.Guarantees.md)  
Assembly: Omni.Converter.dll  

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

```csharp
public static class OmniConversionGuarantee
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniConversionGuarantee](Omni.Converter.Guarantees.OmniConversionGuarantee.md)

## プロパティ（Properties）

### <a id="Omni_Converter_Guarantees_OmniConversionGuarantee_LoadedTable"></a> LoadedTable

```csharp
public static OmniConversionGuaranteeTable LoadedTable { get; }
```

#### 値（Property Value）

 [OmniConversionGuaranteeTable](Omni.Converter.Guarantees.OmniConversionGuaranteeTable.md)

### <a id="Omni_Converter_Guarantees_OmniConversionGuarantee_Snapshot"></a> Snapshot

```csharp
public static IReadOnlyList<OmniConversionVerdict> Snapshot { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniConversionVerdict](Omni.Converter.Guarantees.OmniConversionVerdict.md)\>

## メソッド（Methods）

### <a id="Omni_Converter_Guarantees_OmniConversionGuarantee_EvaluateVfxAssets_System_Collections_Generic_IEnumerable_System_String__"></a> EvaluateVfxAssets\(IEnumerable<string\>\)

VFX 資産の判定を記録します。VFX は取り込みのフックがパッチを当てるので、準備（取り込み直し）が済んだ後に呼びます。
系統の指紋（雛形の組と patcher の schema）は1回だけ取り、資産ごとに描画シェーダーのパッチと出力の種類を確かめます。

```csharp
public static void EvaluateVfxAssets(IEnumerable<string> vfxAssetPaths)
```

#### 引数（Parameters）

`vfxAssetPaths` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_Guarantees_OmniConversionGuarantee_RunGuarded_System_String_System_Func_System_String_System_String__"></a> RunGuarded\(string, Func<string, string\>\)

分類された元だけを門で包んで変換し、判定を記録します。自作 Shader はそのまま <code class="paramref">convert</code> を呼びます。
引退した規約しか合わない元と、規約の無い元は、変換器を呼ばずに変換不能として null を返します。

```csharp
public static string RunGuarded(string sourcePath, Func<string, string> convert)
```

#### 引数（Parameters）

`sourcePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`convert` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_Guarantees_OmniConversionGuarantee_TryGetVerdict_System_String_Omni_Converter_Guarantees_OmniConversionVerdict__"></a> TryGetVerdict\(string, out OmniConversionVerdict\)

```csharp
public static bool TryGetVerdict(string item, out OmniConversionVerdict verdict)
```

#### 引数（Parameters）

`item` [string](https://learn.microsoft.com/dotnet/api/system.string)

`verdict` [OmniConversionVerdict](Omni.Converter.Guarantees.OmniConversionVerdict.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_Guarantees_OmniConversionGuarantee_Changed"></a> Changed

```csharp
public static event Action Changed
```

#### 型（Event Type）

 [Action](https://learn.microsoft.com/dotnet/api/system.action)
