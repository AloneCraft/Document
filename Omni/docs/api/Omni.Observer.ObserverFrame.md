# <a id="Omni_Observer_ObserverFrame"></a> Struct ObserverFrame

Namespace: [Omni.Observer](Omni.Observer.md)  
Assembly: Omni.RadialObserver.dll  

変形後の世界を俯瞰するための枠取り結果です。Focusはワープ中心Cを原点とした
有限の描画座標（メートル＝描画単位）、BoundingRadiusは近遠クリップ用の球の半径です。

```csharp
public readonly struct ObserverFrame
```

## コンストラクター（Constructors）

### <a id="Omni_Observer_ObserverFrame__ctor_Unity_Mathematics_float3_System_Single_System_Single_"></a> ObserverFrame\(float3, float, float\)

```csharp
public ObserverFrame(float3 focus, float boundingRadius, float fixedDistance)
```

#### 引数（Parameters）

`focus` float3

`boundingRadius` [float](https://learn.microsoft.com/dotnet/api/system.single)

`fixedDistance` [float](https://learn.microsoft.com/dotnet/api/system.single)

## フィールド（Fields）

### <a id="Omni_Observer_ObserverFrame_BoundingRadius"></a> BoundingRadius

```csharp
public readonly float BoundingRadius
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Observer_ObserverFrame_FixedDistance"></a> FixedDistance

カメラ距離です。Radialの尺度Sに比例した一定距離で俯瞰します。

```csharp
public readonly float FixedDistance
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Observer_ObserverFrame_Focus"></a> Focus

```csharp
public readonly float3 Focus
```

#### 値（Field Value）

 float3
