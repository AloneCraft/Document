# <a id="Omni_Editor_Manager_OmniMaterialScanner"></a> Class OmniMaterialScanner

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

Projectまたは全ロード済みSceneから、実Materialアセット単位の共通解析結果を作ります。
GUI描画中には呼ばず、Managerの遅延更新からのみ実行します。

```csharp
public static class OmniMaterialScanner
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniMaterialScanner](Omni.Editor.Manager.OmniMaterialScanner.md)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_OmniMaterialScanner_CanConvert_UnityEngine_Material_"></a> CanConvert\(Material\)

```csharp
public static bool CanConvert(Material material)
```

#### 引数（Parameters）

`material` Material

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_OmniMaterialScanner_CountShaderExcluded_System_Collections_Generic_IEnumerable_Omni_Editor_Manager_MaterialEntry__"></a> CountShaderExcluded\(IEnumerable<MaterialEntry\>\)

Shaderが未対応のため切替対象から外したMaterial数です（読取専用・埋込み・生成物は含みません）。

```csharp
public static int CountShaderExcluded(IEnumerable<MaterialEntry> entries)
```

#### 引数（Parameters）

`entries` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[MaterialEntry](Omni.Editor.Manager.MaterialEntry.md)\>

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_OmniMaterialScanner_CountSwitchTargets_System_Collections_Generic_IEnumerable_Omni_Editor_Manager_MaterialEntry__"></a> CountSwitchTargets\(IEnumerable<MaterialEntry\>\)

切替対象のMaterial数です。対象外（Shaderが未対応）を除き、同じMaterialは1件と数えます。
変更対象の一覧（確認ダイアログの件数）と同じ定義です。

```csharp
public static int CountSwitchTargets(IEnumerable<MaterialEntry> entries)
```

#### 引数（Parameters）

`entries` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[MaterialEntry](Omni.Editor.Manager.MaterialEntry.md)\>

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_OmniMaterialScanner_Scan_System_String_"></a> Scan\(string\)

```csharp
public static List<MaterialEntry> Scan(string folder)
```

#### 引数（Parameters）

`folder` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[MaterialEntry](Omni.Editor.Manager.MaterialEntry.md)\>

### <a id="Omni_Editor_Manager_OmniMaterialScanner_Scan_System_String___"></a> Scan\(string\[\]\)

```csharp
public static List<MaterialEntry> Scan(string[] folders)
```

#### 引数（Parameters）

`folders` [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

#### 戻り値（Returns）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[MaterialEntry](Omni.Editor.Manager.MaterialEntry.md)\>

### <a id="Omni_Editor_Manager_OmniMaterialScanner_ScanUsedInActiveScene"></a> ScanUsedInActiveScene\(\)

名前は互換性のため維持しますが、対象はアクティブSceneだけでなく全ロード済みSceneです。
非アクティブなRenderer、Terrain、DecalProjectorも含みます。

```csharp
public static List<MaterialEntry> ScanUsedInActiveScene()
```

#### 戻り値（Returns）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[MaterialEntry](Omni.Editor.Manager.MaterialEntry.md)\>

### <a id="Omni_Editor_Manager_OmniMaterialScanner_ScanWritableProjectAssets"></a> ScanWritableProjectAssets\(\)

<code>Assets/</code>配下の、独立して書換え可能なMaterialアセットだけを走査します。
読取専用または埋込みMaterialは理由付きで除外します。

```csharp
public static ProjectMaterialScanResult ScanWritableProjectAssets()
```

#### 戻り値（Returns）

 [ProjectMaterialScanResult](Omni.Editor.Manager.ProjectMaterialScanResult.md)

### <a id="Omni_Editor_Manager_OmniMaterialScanner_TryGetWritableProjectMaterial_UnityEngine_Material_System_String_System_String__"></a> TryGetWritableProjectMaterial\(Material, string, out string\)

```csharp
public static bool TryGetWritableProjectMaterial(Material material, string path, out string reason)
```

#### 引数（Parameters）

`material` Material

`path` [string](https://learn.microsoft.com/dotnet/api/system.string)

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
