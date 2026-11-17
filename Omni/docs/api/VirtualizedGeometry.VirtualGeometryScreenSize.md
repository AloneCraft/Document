# <a id="VirtualizedGeometry_VirtualGeometryScreenSize"></a> Class VirtualGeometryScreenSize

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

画面上の大きさ（画素）の式の正本。VG の選択（cluster の誤差、Cell の大きさ）と VO の選択（物の見かけの直径）が、この関数を呼ぶ。
同じ意味の式を別の場所に書かない（演算の順序が変わると、float の結果が bit 単位で変わり、選択の境目がずれる）。
線形の画素（<xref href="VirtualizedGeometry.VirtualGeometryScreenSize.LinearPixels(System.Single%2cSystem.Single%2cSystem.Single)" data-throw-if-not-resolved="false"></xref>）と角直径の画素（<xref href="VirtualizedGeometry.VirtualGeometryScreenSize.AngularDiameterPixels(System.Double%2cSystem.Double%2cSystem.Double%2cSystem.Double)" data-throw-if-not-resolved="false"></xref>）は同じ尺度ではない（視野角 70° で前者が約 0.87 倍）。閾値を比べるときは、どちらの画素かをそろえる。

```csharp
public static class VirtualGeometryScreenSize
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryScreenSize](VirtualizedGeometry.VirtualGeometryScreenSize.md)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryScreenSize_AngularDiameterPixels_System_Double_System_Double_System_Double_System_Double_"></a> AngularDiameterPixels\(double, double, double, double\)

半径 radius の球が、距離 distance で画面の高さ screenHeight（画素）に占める直径（画素）。見かけの角直径 2 asin(r / d) を、縦の視野角 fovRadians に対する割合にする。

```csharp
public static double AngularDiameterPixels(double radius, double distance, double fovRadians, double screenHeight)
```

#### 引数（Parameters）

`radius` [double](https://learn.microsoft.com/dotnet/api/system.double)

`distance` [double](https://learn.microsoft.com/dotnet/api/system.double)

`fovRadians` [double](https://learn.microsoft.com/dotnet/api/system.double)

`screenHeight` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualizedGeometry_VirtualGeometryScreenSize_LinearPixels_System_Single_System_Single_System_Single_"></a> LinearPixels\(float, float, float\)

長さ length が距離 distance で画面に占める大きさ（画素。小さい角の直線近似 length × projectionScale / distance）。

```csharp
public static float LinearPixels(float length, float distance, float projectionScale)
```

#### 引数（Parameters）

`length` [float](https://learn.microsoft.com/dotnet/api/system.single)

`distance` [float](https://learn.microsoft.com/dotnet/api/system.single)

`projectionScale` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryScreenSize_MaximumScale_UnityEngine_Matrix4x4_"></a> MaximumScale\(Matrix4x4\)

行列の線形部分の列の長さの最大（非一様な拡大で、最も伸びる軸の倍率）。

```csharp
public static float MaximumScale(Matrix4x4 matrix)
```

#### 引数（Parameters）

`matrix` Matrix4x4

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryScreenSize_OrthographicProjectionScale_System_Single_System_Single_"></a> OrthographicProjectionScale\(float, float\)

正射影の射影の倍率（画素 / 長さ。距離で割らない）。

```csharp
public static float OrthographicProjectionScale(float orthographicSize, float pixelHeight)
```

#### 引数（Parameters）

`orthographicSize` [float](https://learn.microsoft.com/dotnet/api/system.single)

`pixelHeight` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryScreenSize_PerspectiveProjectionScale_System_Single_System_Single_"></a> PerspectiveProjectionScale\(float, float\)

透視投影の射影の倍率（画素 / 距離 1 あたりの長さ）。縦の視野角は度。長さ L が距離 d で L × 倍率 / d 画素に見える。

```csharp
public static float PerspectiveProjectionScale(float verticalFieldOfViewDegrees, float pixelHeight)
```

#### 引数（Parameters）

`verticalFieldOfViewDegrees` [float](https://learn.microsoft.com/dotnet/api/system.single)

`pixelHeight` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryScreenSize_PerspectiveProjectionScaleRadians_System_Single_System_Single_"></a> PerspectiveProjectionScaleRadians\(float, float\)

<xref href="VirtualizedGeometry.VirtualGeometryScreenSize.PerspectiveProjectionScale(System.Single%2cSystem.Single)" data-throw-if-not-resolved="false"></xref> の、視野角をラジアンで受け取る形（VO の選択が使う）。

```csharp
public static float PerspectiveProjectionScaleRadians(float verticalFieldOfViewRadians, float pixelHeight)
```

#### 引数（Parameters）

`verticalFieldOfViewRadians` [float](https://learn.microsoft.com/dotnet/api/system.single)

`pixelHeight` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryScreenSize_ProjectionScale_UnityEngine_Camera_System_Single_"></a> ProjectionScale\(Camera, float\)

camera の射影の倍率（正射影なら <xref href="VirtualizedGeometry.VirtualGeometryScreenSize.OrthographicProjectionScale(System.Single%2cSystem.Single)" data-throw-if-not-resolved="false"></xref>、それ以外は <xref href="VirtualizedGeometry.VirtualGeometryScreenSize.PerspectiveProjectionScale(System.Single%2cSystem.Single)" data-throw-if-not-resolved="false"></xref>）。

```csharp
public static float ProjectionScale(Camera camera, float pixelHeight)
```

#### 引数（Parameters）

`camera` Camera

`pixelHeight` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)
