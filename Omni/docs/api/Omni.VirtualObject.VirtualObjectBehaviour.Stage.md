# <a id="Omni_VirtualObject_VirtualObjectBehaviour_Stage"></a> Struct VirtualObjectBehaviour.Stage

Namespace: [Omni.VirtualObject](Omni.VirtualObject.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

```csharp
[Serializable]
public struct VirtualObjectBehaviour.Stage
```

## フィールド（Fields）

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_Stage_destroyOnHide"></a> destroyOnHide

GameObject の段で、描くのをやめたときに破棄するか（false なら非アクティブにして持つ）。

```csharp
public bool destroyOnHide
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_Stage_enterPixels"></a> enterPixels

この段へ上がる画素の大きさ（段 0 では使わない）。段ごとに昇順。

```csharp
public double enterPixels
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_Stage_kind"></a> kind

```csharp
public VirtualObjectBehaviour.StageKind kind
```

#### 値（Field Value）

 [VirtualObjectBehaviour](Omni.VirtualObject.VirtualObjectBehaviour.md).[StageKind](Omni.VirtualObject.VirtualObjectBehaviour.StageKind.md)

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_Stage_prefab"></a> prefab

```csharp
public GameObject prefab
```

#### 値（Field Value）

 GameObject

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_Stage_script"></a> script

```csharp
public Behaviour script
```

#### 値（Field Value）

 Behaviour

### <a id="Omni_VirtualObject_VirtualObjectBehaviour_Stage_vfx"></a> vfx

```csharp
public VisualEffectAsset vfx
```

#### 値（Field Value）

 VisualEffectAsset
