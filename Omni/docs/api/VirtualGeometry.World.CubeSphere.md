# <a id="VirtualGeometry_World_CubeSphere"></a> Class CubeSphere

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

cube-sphere の面の軸と、面の座標から球面の方向への写像(等角写像)。
面 f の点は n + a·u + b·v(a、b は −1〜1)。外向き法線は cross(v,u)=n になる向きに u・v を選ぶ
(VirtualGeometryGridLayout の三角形が外から時計回りに見える向き)。
面の番号: 0:+X、1:−X、2:+Y、3:−Y、4:+Z、5:−Z。

```csharp
public static class CubeSphere
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[CubeSphere](VirtualGeometry.World.CubeSphere.md)

## フィールド（Fields）

### <a id="VirtualGeometry_World_CubeSphere_FaceCount"></a> FaceCount

```csharp
public const int FaceCount = 6
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_CubeSphere_Direction_System_Int32_System_Single_System_Single_"></a> Direction\(int, float, float\)

面の座標(s、t は 0〜1)を球面の単位方向へ写す。等角写像(各軸の角度が均等)。

```csharp
public static Vector3 Direction(int face, float s, float t)
```

#### 引数（Parameters）

`face` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`s` [float](https://learn.microsoft.com/dotnet/api/system.single)

`t` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 Vector3

### <a id="VirtualGeometry_World_CubeSphere_FaceWithNormal_UnityEngine_Vector3Int_"></a> FaceWithNormal\(Vector3Int\)

法線が axis の面。

```csharp
public static int FaceWithNormal(Vector3Int axis)
```

#### 引数（Parameters）

`axis` Vector3Int

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_CubeSphere_Normal_System_Int32_"></a> Normal\(int\)

```csharp
public static Vector3Int Normal(int face)
```

#### 引数（Parameters）

`face` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 Vector3Int

### <a id="VirtualGeometry_World_CubeSphere_U_System_Int32_"></a> U\(int\)

```csharp
public static Vector3Int U(int face)
```

#### 引数（Parameters）

`face` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 Vector3Int

### <a id="VirtualGeometry_World_CubeSphere_V_System_Int32_"></a> V\(int\)

```csharp
public static Vector3Int V(int face)
```

#### 引数（Parameters）

`face` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 Vector3Int
