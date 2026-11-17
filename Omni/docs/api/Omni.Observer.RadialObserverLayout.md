# <a id="Omni_Observer_RadialObserverLayout"></a> Class RadialObserverLayout

Namespace: [Omni.Observer](Omni.Observer.md)  
Assembly: Omni.RadialObserver.dll  

観察枠のCamera.rect（正規化viewport）を計算します。副作用を持たない純粋関数です。
枠0が周回、枠1〜4が固定（Front／Right／Top／Iso）です。

```csharp
public static class RadialObserverLayout
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialObserverLayout](Omni.Observer.RadialObserverLayout.md)

## フィールド（Fields）

### <a id="Omni_Observer_RadialObserverLayout_FirstFixedSlot"></a> FirstFixedSlot

```csharp
public const int FirstFixedSlot = 1
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Observer_RadialObserverLayout_FixedSlotCount"></a> FixedSlotCount

```csharp
public const int FixedSlotCount = 4
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Observer_RadialObserverLayout_MinimumArea"></a> MinimumArea

表示する枠の占有面積の下限（画面幅・高さに対する比）です。

```csharp
public const float MinimumArea = 0.05
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Observer_RadialObserverLayout_OrbitSlot"></a> OrbitSlot

```csharp
public const int OrbitSlot = 0
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Observer_RadialObserverLayout_SlotCount"></a> SlotCount

```csharp
public const int SlotCount = 5
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Observer_RadialObserverLayout_Compute_Omni_Observer_ObserverLayoutPreset_Omni_Observer_ObserverCorner_System_Single_System_Single_System_Span_UnityEngine_Rect__System_Span_System_Boolean__"></a> Compute\(ObserverLayoutPreset, ObserverCorner, float, float, Span<Rect\>, Span<bool\>\)

rectsとvisibleを埋めます。非表示の枠のrectは幅・高さ0です。

```csharp
public static void Compute(ObserverLayoutPreset preset, ObserverCorner corner, float orbitWipeArea, float gridArea, Span<Rect> rects, Span<bool> visible)
```

#### 引数（Parameters）

`preset` [ObserverLayoutPreset](Omni.Observer.ObserverLayoutPreset.md)

`corner` [ObserverCorner](Omni.Observer.ObserverCorner.md)

`orbitWipeArea` [float](https://learn.microsoft.com/dotnet/api/system.single)

OrbitWipeの周回枠の一辺（画面幅・高さに対する比）。

`gridArea` [float](https://learn.microsoft.com/dotnet/api/system.single)

FixedGrid／Combinedが占める正方ブロックの一辺（同上）。

`rects` [Span](https://learn.microsoft.com/dotnet/api/system.span\-1)<Rect\>

`visible` [Span](https://learn.microsoft.com/dotnet/api/system.span\-1)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>
