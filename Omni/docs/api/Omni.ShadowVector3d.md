# <a id="Omni_ShadowVector3d"></a> Struct ShadowVector3d

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

double の 3 次元ベクトル(仮想シャドウマップの CPU の計算用)。

```csharp
public readonly struct ShadowVector3d
```

## コンストラクター（Constructors）

### <a id="Omni_ShadowVector3d__ctor_System_Double_System_Double_System_Double_"></a> ShadowVector3d\(double, double, double\)

```csharp
public ShadowVector3d(double x, double y, double z)
```

#### 引数（Parameters）

`x` [double](https://learn.microsoft.com/dotnet/api/system.double)

`y` [double](https://learn.microsoft.com/dotnet/api/system.double)

`z` [double](https://learn.microsoft.com/dotnet/api/system.double)

## フィールド（Fields）

### <a id="Omni_ShadowVector3d_X"></a> X

```csharp
public readonly double X
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_ShadowVector3d_Y"></a> Y

```csharp
public readonly double Y
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_ShadowVector3d_Z"></a> Z

```csharp
public readonly double Z
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## プロパティ（Properties）

### <a id="Omni_ShadowVector3d_IsFinite"></a> IsFinite

```csharp
public bool IsFinite { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_ShadowVector3d_Length"></a> Length

```csharp
public double Length { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_ShadowVector3d_Normalized"></a> Normalized

```csharp
public ShadowVector3d Normalized { get; }
```

#### 値（Property Value）

 [ShadowVector3d](Omni.ShadowVector3d.md)

## メソッド（Methods）

### <a id="Omni_ShadowVector3d_Cross_Omni_ShadowVector3d_Omni_ShadowVector3d_"></a> Cross\(ShadowVector3d, ShadowVector3d\)

```csharp
public static ShadowVector3d Cross(ShadowVector3d a, ShadowVector3d b)
```

#### 引数（Parameters）

`a` [ShadowVector3d](Omni.ShadowVector3d.md)

`b` [ShadowVector3d](Omni.ShadowVector3d.md)

#### 戻り値（Returns）

 [ShadowVector3d](Omni.ShadowVector3d.md)

### <a id="Omni_ShadowVector3d_Dot_Omni_ShadowVector3d_Omni_ShadowVector3d_"></a> Dot\(ShadowVector3d, ShadowVector3d\)

```csharp
public static double Dot(ShadowVector3d a, ShadowVector3d b)
```

#### 引数（Parameters）

`a` [ShadowVector3d](Omni.ShadowVector3d.md)

`b` [ShadowVector3d](Omni.ShadowVector3d.md)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_ShadowVector3d_FromVector_UnityEngine_Vector3_"></a> FromVector\(Vector3\)

```csharp
public static ShadowVector3d FromVector(Vector3 v)
```

#### 引数（Parameters）

`v` Vector3

#### 戻り値（Returns）

 [ShadowVector3d](Omni.ShadowVector3d.md)

### <a id="Omni_ShadowVector3d_ToVector"></a> ToVector\(\)

```csharp
public Vector3 ToVector()
```

#### 戻り値（Returns）

 Vector3

## 演算子（Operators）

### <a id="Omni_ShadowVector3d_op_Addition_Omni_ShadowVector3d_Omni_ShadowVector3d_"></a> operator \+\(ShadowVector3d, ShadowVector3d\)

```csharp
public static ShadowVector3d operator +(ShadowVector3d a, ShadowVector3d b)
```

#### 引数（Parameters）

`a` [ShadowVector3d](Omni.ShadowVector3d.md)

`b` [ShadowVector3d](Omni.ShadowVector3d.md)

#### 戻り値（Returns）

 [ShadowVector3d](Omni.ShadowVector3d.md)

### <a id="Omni_ShadowVector3d_op_Multiply_Omni_ShadowVector3d_System_Double_"></a> operator \*\(ShadowVector3d, double\)

```csharp
public static ShadowVector3d operator *(ShadowVector3d a, double s)
```

#### 引数（Parameters）

`a` [ShadowVector3d](Omni.ShadowVector3d.md)

`s` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [ShadowVector3d](Omni.ShadowVector3d.md)

### <a id="Omni_ShadowVector3d_op_Subtraction_Omni_ShadowVector3d_Omni_ShadowVector3d_"></a> operator \-\(ShadowVector3d, ShadowVector3d\)

```csharp
public static ShadowVector3d operator -(ShadowVector3d a, ShadowVector3d b)
```

#### 引数（Parameters）

`a` [ShadowVector3d](Omni.ShadowVector3d.md)

`b` [ShadowVector3d](Omni.ShadowVector3d.md)

#### 戻り値（Returns）

 [ShadowVector3d](Omni.ShadowVector3d.md)
