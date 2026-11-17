# <a id="Omni_Logical_Aabb"></a> Struct Aabb

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

Logicalワールド軸に沿ったAABBです。

```csharp
public readonly struct Aabb : IEquatable<Aabb>
```

#### 実装するインターフェース（Implements）

[IEquatable<Aabb\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## フィールド（Fields）

### <a id="Omni_Logical_Aabb_Center"></a> Center

AABBのLogicalワールド中心です。

```csharp
public readonly Position3 Center
```

#### 値（Field Value）

 [Position3](Omni.Logical.Position3.md)

### <a id="Omni_Logical_Aabb_Extents"></a> Extents

非負のLogicalワールド半径です。

```csharp
public readonly Vector3 Extents
```

#### 値（Field Value）

 [Vector3](Omni.Logical.Vector3.md)

## メソッド（Methods）

### <a id="Omni_Logical_Aabb_Equals_Omni_Logical_Aabb_"></a> Equals\(Aabb\)

```csharp
public bool Equals(Aabb other)
```

#### 引数（Parameters）

`other` [Aabb](Omni.Logical.Aabb.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Aabb_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Aabb_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_Aabb_TryCreate_Omni_Logical_Position3__Omni_Logical_Vector3__Omni_Logical_Aabb__"></a> TryCreate\(in Position3, in Vector3, out Aabb\)

中心と非負ExtentsからAABBを生成します。

```csharp
public static bool TryCreate(in Position3 center, in Vector3 extents, out Aabb bounds)
```

#### 引数（Parameters）

`center` [Position3](Omni.Logical.Position3.md)

`extents` [Vector3](Omni.Logical.Vector3.md)

`bounds` [Aabb](Omni.Logical.Aabb.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Aabb_TryGetMaximum_Omni_Logical_Position3__"></a> TryGetMaximum\(out Position3\)

AABBのLogical最大座標を返します。

```csharp
public bool TryGetMaximum(out Position3 maximum)
```

#### 引数（Parameters）

`maximum` [Position3](Omni.Logical.Position3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Aabb_TryGetMinimum_Omni_Logical_Position3__"></a> TryGetMinimum\(out Position3\)

AABBのLogical最小座標を返します。

```csharp
public bool TryGetMinimum(out Position3 minimum)
```

#### 引数（Parameters）

`minimum` [Position3](Omni.Logical.Position3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
