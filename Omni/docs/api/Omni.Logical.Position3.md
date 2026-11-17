# <a id="Omni_Logical_Position3"></a> Struct Position3

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

論理Position用途の<xref href="Omni.Logical.Vector3" data-throw-if-not-resolved="false"></xref>ラッパーです。Position専用の意味を持たせ、
単なる差分・方向ベクトルとしての<xref href="Omni.Logical.Vector3" data-throw-if-not-resolved="false"></xref>と区別するために
独立した型として定義します。

```csharp
public readonly struct Position3 : IEquatable<Position3>
```

#### 実装するインターフェース（Implements）

[IEquatable<Position3\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## コンストラクター（Constructors）

### <a id="Omni_Logical_Position3__ctor_Omni_Logical_Vector3__"></a> Position3\(in Vector3\)

ベクトル値から構築します。

```csharp
public Position3(in Vector3 value)
```

#### 引数（Parameters）

`value` [Vector3](Omni.Logical.Vector3.md)

## フィールド（Fields）

### <a id="Omni_Logical_Position3_Value"></a> Value

内包するベクトル値です。

```csharp
public readonly Vector3 Value
```

#### 値（Field Value）

 [Vector3](Omni.Logical.Vector3.md)

### <a id="Omni_Logical_Position3_Zero"></a> Zero

論理原点です。

```csharp
public static readonly Position3 Zero
```

#### 値（Field Value）

 [Position3](Omni.Logical.Position3.md)

## メソッド（Methods）

### <a id="Omni_Logical_Position3_Equals_Omni_Logical_Position3_"></a> Equals\(Position3\)

```csharp
public bool Equals(Position3 other)
```

#### 引数（Parameters）

`other` [Position3](Omni.Logical.Position3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Position3_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Position3_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_Position3_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_Position3_TryAdd_Omni_Logical_Position3__Omni_Logical_Vector3__Omni_Logical_Position3__"></a> TryAdd\(in Position3, in Vector3, out Position3\)

オフセットを加えた位置を試みます。

```csharp
public static bool TryAdd(in Position3 position, in Vector3 offset, out Position3 result)
```

#### 引数（Parameters）

`position` [Position3](Omni.Logical.Position3.md)

`offset` [Vector3](Omni.Logical.Vector3.md)

`result` [Position3](Omni.Logical.Position3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Position3_TryDifference_Omni_Logical_Position3__Omni_Logical_Position3__Omni_Logical_Vector3__"></a> TryDifference\(in Position3, in Position3, out Vector3\)

2つの論理Position間の差（left - right、Vector）を試みます。

```csharp
public static bool TryDifference(in Position3 left, in Position3 right, out Vector3 result)
```

#### 引数（Parameters）

`left` [Position3](Omni.Logical.Position3.md)

`right` [Position3](Omni.Logical.Position3.md)

`result` [Vector3](Omni.Logical.Vector3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Position3_TryFromFloat3_Unity_Mathematics_float3_Omni_Logical_Position3__"></a> TryFromFloat3\(float3, out Position3\)

IEEE 754単精度3成分からの変換を試みます。

```csharp
public static bool TryFromFloat3(float3 value, out Position3 result)
```

#### 引数（Parameters）

`value` float3

`result` [Position3](Omni.Logical.Position3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Position3_TryToFloat3_Unity_Mathematics_float3__"></a> TryToFloat3\(out float3\)

Unity描画境界向けの単精度3成分への変換を試みます。

```csharp
public bool TryToFloat3(out float3 result)
```

#### 引数（Parameters）

`result` float3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## 演算子（Operators）

### <a id="Omni_Logical_Position3_op_Equality_Omni_Logical_Position3_Omni_Logical_Position3_"></a> operator ==\(Position3, Position3\)

2つの値が等しい場合はtrueです。

```csharp
public static bool operator ==(Position3 left, Position3 right)
```

#### 引数（Parameters）

`left` [Position3](Omni.Logical.Position3.md)

`right` [Position3](Omni.Logical.Position3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_Position3_op_Inequality_Omni_Logical_Position3_Omni_Logical_Position3_"></a> operator \!=\(Position3, Position3\)

2つの値が異なる場合はtrueです。

```csharp
public static bool operator !=(Position3 left, Position3 right)
```

#### 引数（Parameters）

`left` [Position3](Omni.Logical.Position3.md)

`right` [Position3](Omni.Logical.Position3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
