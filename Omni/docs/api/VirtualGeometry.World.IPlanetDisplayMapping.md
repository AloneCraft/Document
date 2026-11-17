# <a id="VirtualGeometry_World_IPlanetDisplayMapping"></a> Interface IPlanetDisplayMapping

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Radial で圧縮した描画空間での、Cell の見え方（<xref href="VirtualGeometry.World.PlanetCellSelector" data-throw-if-not-resolved="false"></xref> が誤差と cull に使う）。
実距離の画面上の大きさは、圧縮した空間を別のカメラ（俯瞰）から見るときには合わない。

```csharp
public interface IPlanetDisplayMapping
```

## プロパティ（Properties）

### <a id="VirtualGeometry_World_IPlanetDisplayMapping_NearPlane"></a> NearPlane

描画空間の near（見ているカメラの near）。

```csharp
float NearPlane { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_IPlanetDisplayMapping_ViewerPlanes"></a> ViewerPlanes

見ているカメラを原点にした、描画空間の視錐台の平面（far は無限遠）。

```csharp
Plane[] ViewerPlanes { get; }
```

#### 値（Property Value）

 Plane\[\]

## メソッド（Methods）

### <a id="VirtualGeometry_World_IPlanetDisplayMapping_TryMap_UnityEngine_Vector3_System_Single_UnityEngine_Vector3__System_Single__System_Single__System_Single__"></a> TryMap\(Vector3, float, out Vector3, out float, out float, out float\)

Cell の bounds（中心は選択のカメラ eye からの相対位置、惑星のローカル座標の向き。radius は実際の半径）を、描画空間へ写す。
centerFromViewer は中心の、見ているカメラからの相対位置。scale は Cell の最も近い点での大きさの倍率（描画空間の大きさ ÷ 実際の大きさ。画面の誤差に使う。
圧縮した空間では近い点ほど大きく写るので、中心の倍率より大きい）。cullRadius は bounds を必ず囲む球の、描画空間での半径（cull に使う。大きい Cell は、
点ごとに方向と距離が違って圧縮され、中心の倍率 × 半径では囲めない）。errorRadius は誤差のための、近い側までの実質の広がり（cullRadius 以下）。
写せないときは false（呼び出し側は実距離と従来の cull に戻す。落とさない）。

```csharp
bool TryMap(Vector3 centerFromEye, float radius, out Vector3 centerFromViewer, out float scale, out float cullRadius, out float errorRadius)
```

#### 引数（Parameters）

`centerFromEye` Vector3

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

`centerFromViewer` Vector3

`scale` [float](https://learn.microsoft.com/dotnet/api/system.single)

`cullRadius` [float](https://learn.microsoft.com/dotnet/api/system.single)

`errorRadius` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
