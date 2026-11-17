# <a id="VirtualGeometry_World_PlanetCellManagedJob"></a> Struct PlanetCellManagedJob

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

同じNative入出力でBurstだけを除いた対照。

```csharp
public struct PlanetCellManagedJob : IJob
```

#### 実装するインターフェース（Implements）

IJob

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetCellManagedJob_Job"></a> Job

```csharp
public PlanetCellBurstJob Job
```

#### 値（Field Value）

 [PlanetCellBurstJob](VirtualGeometry.World.PlanetCellBurstJob.md)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetCellManagedJob_Execute"></a> Execute\(\)

<p>Implement this method to perform work on a worker thread.</p>

```csharp
public void Execute()
```
