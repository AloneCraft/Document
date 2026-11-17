# <a id="Omni_Logical_RenderPose"></a> Struct RenderPose

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

LogicalTransformまたは通常Transformから解決する描画用Logicalワールド姿勢です。
PositionとBasisだけを空間値の正本とし、浮動小数の残差は保持しません。

```csharp
public readonly struct RenderPose
```

## フィールド（Fields）

### <a id="Omni_Logical_RenderPose_Basis"></a> Basis

回転、非一様Scale、Shearを含むobject-to-logical基底です。

```csharp
public readonly Matrix3x3 Basis
```

#### 値（Field Value）

 [Matrix3x3](Omni.Logical.Matrix3x3.md)

### <a id="Omni_Logical_RenderPose_Position"></a> Position

Logicalワールド位置です。

```csharp
public readonly Position3 Position
```

#### 値（Field Value）

 [Position3](Omni.Logical.Position3.md)

### <a id="Omni_Logical_RenderPose_PrecisionGuaranteed"></a> PrecisionGuaranteed

LogicalTransformを起点に解決できた場合はtrueです。

```csharp
public readonly bool PrecisionGuaranteed
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Logical_RenderPose_TryCreate_Omni_Logical_Position3__Omni_Logical_Matrix3x3__System_Boolean_Omni_Logical_RenderPose__"></a> TryCreate\(in Position3, in Matrix3x3, bool, out RenderPose\)

Logical値から描画姿勢を生成します。

```csharp
public static bool TryCreate(in Position3 position, in Matrix3x3 basis, bool precisionGuaranteed, out RenderPose pose)
```

#### 引数（Parameters）

`position` [Position3](Omni.Logical.Position3.md)

`basis` [Matrix3x3](Omni.Logical.Matrix3x3.md)

`precisionGuaranteed` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`pose` [RenderPose](Omni.Logical.RenderPose.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RenderPose_TryCreateWorldDerived_Omni_Logical_Vector3__Omni_Logical_Matrix3x3__Omni_Logical_RenderPose__"></a> TryCreateWorldDerived\(in Vector3, in Matrix3x3, out RenderPose\)

Logicalワールドoffsetとbasisを持つ派生姿勢を生成します。

```csharp
public bool TryCreateWorldDerived(in Vector3 worldOffset, in Matrix3x3 worldBasis, out RenderPose pose)
```

#### 引数（Parameters）

`worldOffset` [Vector3](Omni.Logical.Vector3.md)

`worldBasis` [Matrix3x3](Omni.Logical.Matrix3x3.md)

`pose` [RenderPose](Omni.Logical.RenderPose.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RenderPose_TryGetPosition_Omni_Logical_Position3__"></a> TryGetPosition\(out Position3\)

既存の呼び出し側向けにLogicalワールド位置を返します。

```csharp
public bool TryGetPosition(out Position3 position)
```

#### 引数（Parameters）

`position` [Position3](Omni.Logical.Position3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RenderPose_TryGetRelative_Omni_Logical_Position3__Omni_Logical_Vector3__"></a> TryGetRelative\(in Position3, out Vector3\)

指定Logical中心から見た相対中心をLogicalVector3で返します。

```csharp
public bool TryGetRelative(in Position3 logicalCenter, out Vector3 relative)
```

#### 引数（Parameters）

`logicalCenter` [Position3](Omni.Logical.Position3.md)

`relative` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RenderPose_TryGetWorldAabb_UnityEngine_Bounds__Omni_Logical_Aabb__"></a> TryGetWorldAabb\(in Bounds, out Aabb\)

RendererのローカルBoundsをLogicalワールドAABBへ変換します。
下流のカリングはこのLogical値を権威値として保持できます。

```csharp
public bool TryGetWorldAabb(in Bounds localBounds, out Aabb worldBounds)
```

#### 引数（Parameters）

`localBounds` Bounds

`worldBounds` [Aabb](Omni.Logical.Aabb.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RenderPose_TryGetWorldPosition_Omni_Logical_Position3__"></a> TryGetWorldPosition\(out Position3\)

Logicalワールド位置を返します。

```csharp
public bool TryGetWorldPosition(out Position3 position)
```

#### 引数（Parameters）

`position` [Position3](Omni.Logical.Position3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RenderPose_TryResolve_UnityEngine_Transform_Omni_Logical_RenderPose__"></a> TryResolve\(Transform, out RenderPose\)

指定TransformのLogicalワールド姿勢を解決します。
LogicalTransformの通常Transform子もLogical演算で親子合成します。

```csharp
public static bool TryResolve(Transform target, out RenderPose pose)
```

#### 引数（Parameters）

`target` Transform

`pose` [RenderPose](Omni.Logical.RenderPose.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
