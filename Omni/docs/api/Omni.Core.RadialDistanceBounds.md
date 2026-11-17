# <a id="Omni_Core_RadialDistanceBounds"></a> Class RadialDistanceBounds

Namespace: [Omni.Core](Omni.Core.md)  
Assembly: Radial.Runtime.dll  

Logicalカメラ位置またはLogical可動領域とLogical AABBから、放射距離の保守的な範囲を求めます。
GPU側のRadial Warpが再写像するのはこのEuclidean距離であり、Unity行列のZ深度ではありません。
ここで扱う空間値はすべてLogicalであり、失敗時の呼び出し側は可視側へ倒さなければなりません。

```csharp
public static class RadialDistanceBounds
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialDistanceBounds](Omni.Core.RadialDistanceBounds.md)

## メソッド（Methods）

### <a id="Omni_Core_RadialDistanceBounds_TryGetRange_Omni_Logical_Position3__Omni_Logical_Aabb__Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryGetRange\(in Position3, in Aabb, out Scalar, out Scalar\)

Logicalカメラ位置からLogical AABBまでの放射距離範囲を返します。
カメラがAABB内部にある場合、最小距離はゼロです。

```csharp
public static bool TryGetRange(in Position3 cameraPosition, in Aabb bounds, out Scalar minimumDistance, out Scalar maximumDistance)
```

#### 引数（Parameters）

`cameraPosition` [Position3](Omni.Logical.Position3.md)

`bounds` [Aabb](Omni.Logical.Aabb.md)

`minimumDistance` [Scalar](Omni.Logical.Scalar.md)

`maximumDistance` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Core_RadialDistanceBounds_TryGetRangeFromRegion_Omni_Logical_Aabb__Omni_Logical_Aabb__Omni_Logical_Scalar__Omni_Logical_Scalar__"></a> TryGetRangeFromRegion\(in Aabb, in Aabb, out Scalar, out Scalar\)

Logicalカメラ可動領域からLogical AABBまでの放射距離範囲を返します。
可動領域内のどのカメラ位置からも成り立つ保守的な範囲で、ベイク時の距離帯分類に使います。

```csharp
public static bool TryGetRangeFromRegion(in Aabb cameraRegion, in Aabb bounds, out Scalar minimumDistance, out Scalar maximumDistance)
```

#### 引数（Parameters）

`cameraRegion` [Aabb](Omni.Logical.Aabb.md)

`bounds` [Aabb](Omni.Logical.Aabb.md)

`minimumDistance` [Scalar](Omni.Logical.Scalar.md)

`maximumDistance` [Scalar](Omni.Logical.Scalar.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
