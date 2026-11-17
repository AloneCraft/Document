# <a id="Omni_Bake_RadialBakeSpatialIndex"></a> Struct RadialBakeSpatialIndex

Namespace: [Omni.Bake](Omni.Bake.md)  
Assembly: Radial.Runtime.dll  

<xref href="Omni.Rendering.Radial.BakeData" data-throw-if-not-resolved="false"></xref>に直列化される決定的BVHのペイロードです。
実体はDataの個別配列で保持し、この型はBakerとquery間の不変な受け渡しにだけ使います。

```csharp
public readonly struct RadialBakeSpatialIndex
```

## プロパティ（Properties）

### <a id="Omni_Bake_RadialBakeSpatialIndex_ContentFingerprint"></a> ContentFingerprint

Entry内容とBVH構造から計算した決定的fingerprintです。

```csharp
public string ContentFingerprint { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Bake_RadialBakeSpatialIndex_FallbackEntryIndices"></a> FallbackEntryIndices

境界構築不能等によりBVH外で常に候補へ残す静的Entry IDです。

```csharp
public int[] FallbackEntryIndices { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)\[\]

### <a id="Omni_Bake_RadialBakeSpatialIndex_SpatialNodes"></a> SpatialNodes

pre-orderで格納した空間ノードです。

```csharp
public RadialBakeSpatialNode[] SpatialNodes { get; }
```

#### 値（Property Value）

 [RadialBakeSpatialNode](Omni.Bake.RadialBakeSpatialNode.md)\[\]

### <a id="Omni_Bake_RadialBakeSpatialIndex_StaticEntryOrder"></a> StaticEntryOrder

葉が参照する静的Entry IDの順序です。

```csharp
public int[] StaticEntryOrder { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)\[\]
