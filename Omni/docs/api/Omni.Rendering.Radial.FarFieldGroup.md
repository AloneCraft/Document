# <a id="Omni_Rendering_Radial_FarFieldGroup"></a> Struct FarFieldGroup

Namespace: [Omni.Rendering.Radial](Omni.Rendering.Radial.md)  
Assembly: Radial.Runtime.dll  

空間的に近接する静的遠景Rendererのグループです。

```csharp
[Serializable]
public struct FarFieldGroup
```

## フィールド（Fields）

### <a id="Omni_Rendering_Radial_FarFieldGroup_EntryIndices"></a> EntryIndices

このグループに属する<xref href="Omni.Rendering.Radial.BakeData.Entries" data-throw-if-not-resolved="false"></xref>へのインデックス列です。

```csharp
public int[] EntryIndices
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)\[\]

### <a id="Omni_Rendering_Radial_FarFieldGroup_HasInvalidationDistance"></a> HasInvalidationDistance

無効化距離のLogical演算が成功した場合にtrueです。falseは更新を省略しません。

```csharp
public bool HasInvalidationDistance
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Rendering_Radial_FarFieldGroup_InvalidationDistance"></a> InvalidationDistance

カメラがこのLogical距離だけ動くまでキャッシュを再利用してよい閾値です。

```csharp
public ScalarField InvalidationDistance
```

#### 値（Field Value）

 [ScalarField](Omni.Logical.ScalarField.md)

### <a id="Omni_Rendering_Radial_FarFieldGroup_MinimumDistanceFromCameraRegion"></a> MinimumDistanceFromCameraRegion

グループ内エントリの最小放射距離（CameraRegionから見たLogical値）です。

```csharp
public ScalarField MinimumDistanceFromCameraRegion
```

#### 値（Field Value）

 [ScalarField](Omni.Logical.ScalarField.md)

### <a id="Omni_Rendering_Radial_FarFieldGroup_RepresentativeCenter"></a> RepresentativeCenter

グループの代表中心（実空間のLogicalワールド座標）です。

```csharp
public Position3 RepresentativeCenter
```

#### 値（Field Value）

 [Position3](Omni.Rendering.Radial.Position3.md)

## メソッド（Methods）

### <a id="Omni_Rendering_Radial_FarFieldGroup_TryGetInvalidationDistance_Omni_Logical_Scalar__"></a> TryGetInvalidationDistance\(out Scalar\)

キャッシュ再利用に使うLogical無効化距離を取得します。

```csharp
public bool TryGetInvalidationDistance(out Scalar distance)
```

#### 引数（Parameters）

`distance` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
