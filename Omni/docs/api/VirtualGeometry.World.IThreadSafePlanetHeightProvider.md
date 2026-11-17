# <a id="VirtualGeometry_World_IThreadSafePlanetHeightProvider"></a> Interface IThreadSafePlanetHeightProvider

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

複数のスレッドから同時に呼べる高さの供給元（呼び出しが状態を変えない）。<xref href="VirtualGeometry.World.PlanetHeightTerrainSource" data-throw-if-not-resolved="false"></xref> は、これを実装する供給元の Cell をワーカースレッドで作る
（WebGL などスレッドを使えない環境では main thread で、frame の予算内で作る）。

```csharp
public interface IThreadSafePlanetHeightProvider : IPlanetHeightProvider
```

#### 実装するインターフェース（Implements）

[IPlanetHeightProvider](VirtualGeometry.World.IPlanetHeightProvider.md)
