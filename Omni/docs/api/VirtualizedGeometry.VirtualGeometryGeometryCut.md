# <a id="VirtualizedGeometry_VirtualGeometryGeometryCut"></a> Class VirtualGeometryGeometryCut

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

可変数の置換入力を扱う、手続きsourceのlazyな完全cut。Cameraごとに履歴と出力を保持する。

```csharp
public sealed class VirtualGeometryGeometryCut
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryGeometryCut](VirtualizedGeometry.VirtualGeometryGeometryCut.md)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryGeometryCut_Complete"></a> Complete

```csharp
public IReadOnlyList<int> Complete { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

### <a id="VirtualizedGeometry_VirtualGeometryGeometryCut_Selected"></a> Selected

```csharp
public IReadOnlyList<int> Selected { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryGeometryCut_Select_VirtualizedGeometry_IVirtualGeometryGeometrySource_VirtualizedGeometry_VirtualGeometryGeometryView__VirtualizedGeometry_IVirtualGeometryGeometryResidency_System_Single_System_Single_System_Int32_"></a> Select\(IVirtualGeometryGeometrySource, in VirtualGeometryGeometryView, IVirtualGeometryGeometryResidency, float, float, int\)

```csharp
public void Select(IVirtualGeometryGeometrySource source, in VirtualGeometryGeometryView view, IVirtualGeometryGeometryResidency residency, float targetPixels, float hysteresis, int maximumSelected)
```

#### 引数（Parameters）

`source` [IVirtualGeometryGeometrySource](VirtualizedGeometry.IVirtualGeometryGeometrySource.md)

`view` [VirtualGeometryGeometryView](VirtualizedGeometry.VirtualGeometryGeometryView.md)

`residency` [IVirtualGeometryGeometryResidency](VirtualizedGeometry.IVirtualGeometryGeometryResidency.md)

`targetPixels` [float](https://learn.microsoft.com/dotnet/api/system.single)

`hysteresis` [float](https://learn.microsoft.com/dotnet/api/system.single)

`maximumSelected` [int](https://learn.microsoft.com/dotnet/api/system.int32)
