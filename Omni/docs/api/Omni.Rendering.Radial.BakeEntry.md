# <a id="Omni_Rendering_Radial_BakeEntry"></a> Struct BakeEntry

Namespace: [Omni.Rendering.Radial](Omni.Rendering.Radial.md)  
Assembly: Radial.Runtime.dll  

Rendererごとのカメラ非依存ベイク結果です。

```csharp
[Serializable]
public struct BakeEntry
```

## フィールド（Fields）

### <a id="Omni_Rendering_Radial_BakeEntry_BoundingRadius"></a> BoundingRadius

ベイク時に得たLogicalな保守半径です。LogicalBoundsが権威値であり、
この値は診断および移行内容確認向けにだけ保持します。

```csharp
public ScalarField BoundingRadius
```

#### 値（Field Value）

 [ScalarField](Omni.Logical.ScalarField.md)

### <a id="Omni_Rendering_Radial_BakeEntry_Bounds"></a> Bounds

実空間の権威値であるLogicalワールドAABBです。

```csharp
public Aabb Bounds
```

#### 値（Field Value）

 [Aabb](Omni.Rendering.Radial.Aabb.md)

### <a id="Omni_Rendering_Radial_BakeEntry_BoxProjectionError"></a> BoxProjectionError

反射プローブのボックス投影がワープ後座標を使った場合に生じ得た誤差の見積りです。
描画境界の診断情報であり、空間正本ではありません。

```csharp
public float BoxProjectionError
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Rendering_Radial_BakeEntry_FarFieldGroup"></a> FarFieldGroup

所属する遠景グループ（<xref href="Omni.Rendering.Radial.BakeData.Groups" data-throw-if-not-resolved="false"></xref>）のインデックス。無所属は-1。

```csharp
public int FarFieldGroup
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Rendering_Radial_BakeEntry_HasDistanceRange"></a> HasDistanceRange

距離レンジのLogical演算が成功した場合にtrueです。falseはfail-openです。

```csharp
public bool HasDistanceRange
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Rendering_Radial_BakeEntry_IsStatic"></a> IsStatic

GameObject.isStaticベースの静的判定。

```csharp
public bool IsStatic
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Rendering_Radial_BakeEntry_MaximumDistanceFromCameraRegion"></a> MaximumDistanceFromCameraRegion

CameraRegion内のどの点から見ても保証される最大放射距離です。

```csharp
public ScalarField MaximumDistanceFromCameraRegion
```

#### 値（Field Value）

 [ScalarField](Omni.Logical.ScalarField.md)

### <a id="Omni_Rendering_Radial_BakeEntry_MinimumDistanceFromCameraRegion"></a> MinimumDistanceFromCameraRegion

CameraRegion内のどの点から見ても保証される最小放射距離です。

```csharp
public ScalarField MinimumDistanceFromCameraRegion
```

#### 値（Field Value）

 [ScalarField](Omni.Logical.ScalarField.md)

### <a id="Omni_Rendering_Radial_BakeEntry_Tier"></a> Tier

距離帯の分類。

```csharp
public BakeTier Tier
```

#### 値（Field Value）

 [BakeTier](Omni.Rendering.Radial.BakeTier.md)

## メソッド（Methods）

### <a id="Omni_Rendering_Radial_BakeEntry_TryGetBounds_Omni_Logical_Aabb__"></a> TryGetBounds\(out Aabb\)

権威値のLogical AABBを取得します。

```csharp
public bool TryGetBounds(out Aabb bounds)
```

#### 引数（Parameters）

`bounds` [Aabb](Omni.Logical.Aabb.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Rendering_Radial_BakeEntry_TryGetDistanceRange_Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryGetDistanceRange\(out Scalar, out Scalar\)

ベイク済みのLogical距離範囲を取得します。

```csharp
public bool TryGetDistanceRange(out Scalar minimumDistance, out Scalar maximumDistance)
```

#### 引数（Parameters）

`minimumDistance` [Scalar](Omni.Logical.Scalar.md)

`maximumDistance` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
