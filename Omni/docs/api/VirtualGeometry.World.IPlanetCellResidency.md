# <a id="VirtualGeometry_World_IPlanetCellResidency"></a> Interface IPlanetCellResidency

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Cell の生成と描画の状態を、選択から問い合わせる口。

```csharp
public interface IPlanetCellResidency
```

## メソッド（Methods）

### <a id="VirtualGeometry_World_IPlanetCellResidency_IsReady_VirtualGeometry_World_PlanetCellKey__"></a> IsReady\(in PlanetCellKey\)

頂点が生成済みで描けるか。

```csharp
bool IsReady(in PlanetCellKey key)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_IPlanetCellResidency_Request_VirtualGeometry_World_PlanetCellKey__System_Single_"></a> Request\(in PlanetCellKey, float\)

生成を要求する。priority が大きいほど先に生成する。

```csharp
void Request(in PlanetCellKey key, float priority)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_IPlanetCellResidency_Touch_VirtualGeometry_World_PlanetCellKey__"></a> Touch\(in PlanetCellKey\)

この frame で使った(退避しない)。

```csharp
void Touch(in PlanetCellKey key)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

### <a id="VirtualGeometry_World_IPlanetCellResidency_TryGetBounds_VirtualGeometry_World_PlanetCellKey__UnityEngine_Vector3__System_Single__"></a> TryGetBounds\(in PlanetCellKey, out Vector3, out float\)

生成した頂点から求めた実際の bounds。中心は Cell の原点(<xref href="VirtualGeometry.World.PlanetCellFrame.Origin" data-throw-if-not-resolved="false"></xref>、地表の高さまで持ち上げた点)からの相対位置。
まだ無ければ false(解析的な bounds を使う)。

```csharp
bool TryGetBounds(in PlanetCellKey key, out Vector3 offset, out float radius)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`offset` Vector3

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
