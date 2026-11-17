# <a id="VirtualGeometry_Streaming_DirectionColorSampler"></a> Delegate DirectionColorSampler

Namespace: [VirtualGeometry.Streaming](VirtualGeometry.Streaming.md)  
Assembly: Omni.VirtualGeometry.Streaming.dll  

方向(単位ベクトル)の色を返す(0〜255、sRGB)。例: 正距円筒の画像の双一次補間。

```csharp
public delegate void DirectionColorSampler(double x, double y, double z, out byte r, out byte g, out byte b)
```

#### 引数（Parameters）

`x` [double](https://learn.microsoft.com/dotnet/api/system.double)

`y` [double](https://learn.microsoft.com/dotnet/api/system.double)

`z` [double](https://learn.microsoft.com/dotnet/api/system.double)

`r` [byte](https://learn.microsoft.com/dotnet/api/system.byte)

`g` [byte](https://learn.microsoft.com/dotnet/api/system.byte)

`b` [byte](https://learn.microsoft.com/dotnet/api/system.byte)
