# <a id="Omni_Observer_RadialObserverSlot"></a> Class RadialObserverSlot

Namespace: [Omni.Observer](Omni.Observer.md)  
Assembly: Omni.RadialObserver.dll  

観察枠1つの設定です。Cameraとレイアウト上の番号（<xref href="Omni.Observer.RadialObserverLayout" data-throw-if-not-resolved="false"></xref> の枠番号）を持ち、
配置と表示は <xref href="Omni.Observer.RadialObserverRig" data-throw-if-not-resolved="false"></xref> が決めます。
平行投影のCameraは、Radialでは写像が常に恒等になり変形後の世界を見られないため使いません。

```csharp
[DisallowMultipleComponent]
[AddComponentMenu("Omni/Radial Observer Slot")]
public sealed class RadialObserverSlot : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[RadialObserverSlot](Omni.Observer.RadialObserverSlot.md)

## プロパティ（Properties）

### <a id="Omni_Observer_RadialObserverSlot_Camera"></a> Camera

この枠のCamera。未設定なら同じ階層の子から探します。

```csharp
public Camera Camera { get; }
```

#### 値（Property Value）

 Camera

### <a id="Omni_Observer_RadialObserverSlot_FieldOfView"></a> FieldOfView

```csharp
public float FieldOfView { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Observer_RadialObserverSlot_Index"></a> Index

<xref href="Omni.Observer.RadialObserverLayout" data-throw-if-not-resolved="false"></xref> の枠番号です。

```csharp
public int Index { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Observer_RadialObserverSlot_Kind"></a> Kind

```csharp
public ObserverSlotKind Kind { get; }
```

#### 値（Property Value）

 [ObserverSlotKind](Omni.Observer.ObserverSlotKind.md)

### <a id="Omni_Observer_RadialObserverSlot_Pitch"></a> Pitch

```csharp
public float Pitch { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Observer_RadialObserverSlot_Yaw"></a> Yaw

```csharp
public float Yaw { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## メソッド（Methods）

### <a id="Omni_Observer_RadialObserverSlot_Configure_UnityEngine_Camera_System_Int32_Omni_Observer_ObserverSlotKind_System_Single_System_Single_System_Single_"></a> Configure\(Camera, int, ObserverSlotKind, float, float, float\)

コードから枠を構成します（Prefab生成とテスト用）。

```csharp
public void Configure(Camera camera, int index, ObserverSlotKind kind, float yaw, float pitch, float fieldOfView)
```

#### 引数（Parameters）

`camera` Camera

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`kind` [ObserverSlotKind](Omni.Observer.ObserverSlotKind.md)

`yaw` [float](https://learn.microsoft.com/dotnet/api/system.single)

`pitch` [float](https://learn.microsoft.com/dotnet/api/system.single)

`fieldOfView` [float](https://learn.microsoft.com/dotnet/api/system.single)
