# <a id="VirtualGeometry_Streaming_StreamedCubicHeightBounds"></a> Class StreamedCubicHeightBounds

Namespace: [VirtualGeometry.Streaming](VirtualGeometry.Streaming.md)  
Assembly: Omni.VirtualGeometry.Streaming.dll  

Catmull-RomをBezier制御点へ写し、補間値の凸包で囲う。元の格子を変更しない。

```csharp
public static class StreamedCubicHeightBounds
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[StreamedCubicHeightBounds](VirtualGeometry.Streaming.StreamedCubicHeightBounds.md)

## メソッド（Methods）

### <a id="VirtualGeometry_Streaming_StreamedCubicHeightBounds_TryRange_VirtualGeometry_Streaming_CellHeightGrid_System_Double_System_Double_System_Double_System_Double_System_Double__System_Double__"></a> TryRange\(CellHeightGrid, double, double, double, double, out double, out double\)

```csharp
public static bool TryRange(CellHeightGrid grid, double minU, double minV, double maxU, double maxV, out double minimum, out double maximum)
```

#### 引数（Parameters）

`grid` [CellHeightGrid](VirtualGeometry.Streaming.CellHeightGrid.md)

`minU` [double](https://learn.microsoft.com/dotnet/api/system.double)

`minV` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maxU` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maxV` [double](https://learn.microsoft.com/dotnet/api/system.double)

`minimum` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maximum` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
