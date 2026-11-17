# <a id="Omni_Rendering_Radial_BakeData"></a> Class BakeData

Namespace: [Omni.Rendering.Radial](Omni.Rendering.Radial.md)  
Assembly: Radial.Runtime.dll  

```csharp
[MovedFrom(true, "Omni.Bake", null, "RadialBakeData")]
public sealed class BakeData : ScriptableObject
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
[BakeData](Omni.Rendering.Radial.BakeData.md)

## フィールド（Fields）

### <a id="Omni_Rendering_Radial_BakeData_CurrentSchemaVersion"></a> CurrentSchemaVersion

決定的BVHを含む現行Bake schemaです。

```csharp
public const int CurrentSchemaVersion = 2
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="Omni_Rendering_Radial_BakeData_BakedSettings"></a> BakedSettings

ベイク時点でのワープ設定です。RadialCameraの現在値と比較して陳腐化を検出します。

```csharp
public RadialSettings BakedSettings { get; }
```

#### 値（Property Value）

 [RadialSettings](Omni.RadialSettings.md)

### <a id="Omni_Rendering_Radial_BakeData_Entries"></a> Entries

Rendererごとのベイク結果です。並びは対応するRadialBakeBindingの配列と一致します。

```csharp
public BakeEntry[] Entries { get; }
```

#### 値（Property Value）

 [BakeEntry](Omni.Rendering.Radial.BakeEntry.md)\[\]

### <a id="Omni_Rendering_Radial_BakeData_FallbackEntryIndices"></a> FallbackEntryIndices

BVHへ入れず常に可視候補に残す静的Entry IDです。

```csharp
public int[] FallbackEntryIndices { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)\[\]

### <a id="Omni_Rendering_Radial_BakeData_Groups"></a> Groups

空間的に近接する静的遠景Rendererのグループです。

```csharp
public FarFieldGroup[] Groups { get; }
```

#### 値（Property Value）

 [FarFieldGroup](Omni.Rendering.Radial.FarFieldGroup.md)\[\]

### <a id="Omni_Rendering_Radial_BakeData_IsCurrentSchema"></a> IsCurrentSchema

現行schemaの完全なBVHペイロードを保持していればtrueです。

```csharp
public bool IsCurrentSchema { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Rendering_Radial_BakeData_SceneContentHash"></a> SceneContentHash

ベイク時のシーン内容（Renderer構成・Transform・Mesh）のハッシュです。

```csharp
public string SceneContentHash { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Rendering_Radial_BakeData_SceneGuid"></a> SceneGuid

ベイク元シーンのアセットGUIDです。

```csharp
public string SceneGuid { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Rendering_Radial_BakeData_SchemaVersion"></a> SchemaVersion

直列化されたBake schemaの版です。旧assetは0として扱います。

```csharp
public int SchemaVersion { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Rendering_Radial_BakeData_SpatialContentFingerprint"></a> SpatialContentFingerprint

Entry内容と決定的BVH構造を対応付けるfingerprintです。

```csharp
public string SpatialContentFingerprint { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Rendering_Radial_BakeData_SpatialNodes"></a> SpatialNodes

決定的BVHのpre-orderノードです。

```csharp
public RadialBakeSpatialNode[] SpatialNodes { get; }
```

#### 値（Property Value）

 [RadialBakeSpatialNode](Omni.Bake.RadialBakeSpatialNode.md)\[\]

### <a id="Omni_Rendering_Radial_BakeData_StaticEntryOrder"></a> StaticEntryOrder

BVH葉が参照する静的Entry IDの順序です。

```csharp
public int[] StaticEntryOrder { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)\[\]

## メソッド（Methods）

### <a id="Omni_Rendering_Radial_BakeData_SetData_System_String_Omni_RadialSettings_Omni_Logical_Aabb__System_Boolean_System_String_Omni_Rendering_Radial_BakeEntry___Omni_Rendering_Radial_FarFieldGroup___"></a> SetData\(string, RadialSettings, in Aabb, bool, string, BakeEntry\[\], FarFieldGroup\[\]\)

ベイク結果を設定します。RadialBakerからのみ呼ばれる想定です。

```csharp
public void SetData(string sceneGuid, RadialSettings bakedSettings, in Aabb cameraRegion, bool hasCameraRegion, string sceneContentHash, BakeEntry[] entries, FarFieldGroup[] groups)
```

#### 引数（Parameters）

`sceneGuid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`bakedSettings` [RadialSettings](Omni.RadialSettings.md)

`cameraRegion` [Aabb](Omni.Logical.Aabb.md)

`hasCameraRegion` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`sceneContentHash` [string](https://learn.microsoft.com/dotnet/api/system.string)

`entries` [BakeEntry](Omni.Rendering.Radial.BakeEntry.md)\[\]

`groups` [FarFieldGroup](Omni.Rendering.Radial.FarFieldGroup.md)\[\]

### <a id="Omni_Rendering_Radial_BakeData_SetData_System_String_Omni_RadialSettings_Omni_Logical_Aabb__System_Boolean_System_String_Omni_Rendering_Radial_BakeEntry___Omni_Rendering_Radial_FarFieldGroup___Omni_Bake_RadialBakeSpatialIndex__"></a> SetData\(string, RadialSettings, in Aabb, bool, string, BakeEntry\[\], FarFieldGroup\[\], in RadialBakeSpatialIndex\)

ベイク結果と決定的BVHを1回の更新で設定します。Bakerはこのoverloadを使い、
schema、Entry配列、fingerprint、空間ノードを部分更新しません。

```csharp
public void SetData(string sceneGuid, RadialSettings bakedSettings, in Aabb cameraRegion, bool hasCameraRegion, string sceneContentHash, BakeEntry[] entries, FarFieldGroup[] groups, in RadialBakeSpatialIndex spatialIndex)
```

#### 引数（Parameters）

`sceneGuid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`bakedSettings` [RadialSettings](Omni.RadialSettings.md)

`cameraRegion` [Aabb](Omni.Logical.Aabb.md)

`hasCameraRegion` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`sceneContentHash` [string](https://learn.microsoft.com/dotnet/api/system.string)

`entries` [BakeEntry](Omni.Rendering.Radial.BakeEntry.md)\[\]

`groups` [FarFieldGroup](Omni.Rendering.Radial.FarFieldGroup.md)\[\]

`spatialIndex` [RadialBakeSpatialIndex](Omni.Bake.RadialBakeSpatialIndex.md)

### <a id="Omni_Rendering_Radial_BakeData_TryGetCameraRegion_Omni_Logical_Aabb__"></a> TryGetCameraRegion\(out Aabb\)

ベイク時に想定したLogicalカメラ可動領域を返します。

```csharp
public bool TryGetCameraRegion(out Aabb cameraRegion)
```

#### 引数（Parameters）

`cameraRegion` [Aabb](Omni.Logical.Aabb.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Rendering_Radial_BakeData_TryGetSpatialIndex_Omni_Bake_RadialBakeSpatialIndex__"></a> TryGetSpatialIndex\(out RadialBakeSpatialIndex\)

現行schemaの空間索引ペイロードを取得します。

```csharp
public bool TryGetSpatialIndex(out RadialBakeSpatialIndex spatialIndex)
```

#### 引数（Parameters）

`spatialIndex` [RadialBakeSpatialIndex](Omni.Bake.RadialBakeSpatialIndex.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
