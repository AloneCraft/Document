# <a id="VirtualGeometry_World_PlanetDouble3"></a> Struct PlanetDouble3

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

倍精度の 3 次元ベクトル(接地の計算用)。

```csharp
public readonly struct PlanetDouble3
```

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetDouble3__ctor_System_Double_System_Double_System_Double_"></a> PlanetDouble3\(double, double, double\)

```csharp
public PlanetDouble3(double x, double y, double z)
```

#### 引数（Parameters）

`x` [double](https://learn.microsoft.com/dotnet/api/system.double)

`y` [double](https://learn.microsoft.com/dotnet/api/system.double)

`z` [double](https://learn.microsoft.com/dotnet/api/system.double)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetDouble3_X"></a> X

```csharp
public readonly double X
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetDouble3_Y"></a> Y

```csharp
public readonly double Y
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetDouble3_Z"></a> Z

```csharp
public readonly double Z
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetDouble3_Length"></a> Length

```csharp
public double Length { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetDouble3_Normalized"></a> Normalized

```csharp
public PlanetDouble3 Normalized { get; }
```

#### 値（Property Value）

 [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetDouble3_Cross_VirtualGeometry_World_PlanetDouble3_VirtualGeometry_World_PlanetDouble3_"></a> Cross\(PlanetDouble3, PlanetDouble3\)

```csharp
public static PlanetDouble3 Cross(PlanetDouble3 a, PlanetDouble3 b)
```

#### 引数（Parameters）

`a` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

`b` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

#### 戻り値（Returns）

 [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

### <a id="VirtualGeometry_World_PlanetDouble3_Dot_VirtualGeometry_World_PlanetDouble3_VirtualGeometry_World_PlanetDouble3_"></a> Dot\(PlanetDouble3, PlanetDouble3\)

```csharp
public static double Dot(PlanetDouble3 a, PlanetDouble3 b)
```

#### 引数（Parameters）

`a` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

`b` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetDouble3_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## 演算子（Operators）

### <a id="VirtualGeometry_World_PlanetDouble3_op_Addition_VirtualGeometry_World_PlanetDouble3_VirtualGeometry_World_PlanetDouble3_"></a> operator \+\(PlanetDouble3, PlanetDouble3\)

```csharp
public static PlanetDouble3 operator +(PlanetDouble3 a, PlanetDouble3 b)
```

#### 引数（Parameters）

`a` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

`b` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

#### 戻り値（Returns）

 [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

### <a id="VirtualGeometry_World_PlanetDouble3_op_Division_VirtualGeometry_World_PlanetDouble3_System_Double_"></a> operator /\(PlanetDouble3, double\)

```csharp
public static PlanetDouble3 operator /(PlanetDouble3 a, double s)
```

#### 引数（Parameters）

`a` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

`s` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

### <a id="VirtualGeometry_World_PlanetDouble3_op_Multiply_VirtualGeometry_World_PlanetDouble3_System_Double_"></a> operator \*\(PlanetDouble3, double\)

```csharp
public static PlanetDouble3 operator *(PlanetDouble3 a, double s)
```

#### 引数（Parameters）

`a` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

`s` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

### <a id="VirtualGeometry_World_PlanetDouble3_op_Subtraction_VirtualGeometry_World_PlanetDouble3_VirtualGeometry_World_PlanetDouble3_"></a> operator \-\(PlanetDouble3, PlanetDouble3\)

```csharp
public static PlanetDouble3 operator -(PlanetDouble3 a, PlanetDouble3 b)
```

#### 引数（Parameters）

`a` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

`b` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

#### 戻り値（Returns）

 [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

### <a id="VirtualGeometry_World_PlanetDouble3_op_UnaryNegation_VirtualGeometry_World_PlanetDouble3_"></a> operator \-\(PlanetDouble3\)

```csharp
public static PlanetDouble3 operator -(PlanetDouble3 a)
```

#### 引数（Parameters）

`a` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

#### 戻り値（Returns）

 [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)
