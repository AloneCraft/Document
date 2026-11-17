# <a id="Omni_Lighting_OmniLightProbeSpace"></a> Class OmniLightProbeSpace

Namespace: [Omni.Lighting](Omni.Lighting.md)  
Assembly: Radial.Runtime.dll  

対数表示のために移動した表示Rootと、原点付近に焼かれたLight Probe空間を対応付けます。

```csharp
[ExecuteAlways]
[DisallowMultipleComponent]
public sealed class OmniLightProbeSpace : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[OmniLightProbeSpace](Omni.Lighting.OmniLightProbeSpace.md)

## プロパティ（Properties）

### <a id="Omni_Lighting_OmniLightProbeSpace_BakedSpaceRoot"></a> BakedSpaceRoot

ベイク空間の原点です。未指定時はUnityワールド原点を使います。

```csharp
public Transform BakedSpaceRoot { get; }
```

#### 値（Property Value）

 Transform

## メソッド（Methods）

### <a id="Omni_Lighting_OmniLightProbeSpace_Configure_UnityEngine_Transform_"></a> Configure\(Transform\)

検証用にベイク空間の原点を設定します。nullはUnityワールド原点を表します。

```csharp
public void Configure(Transform finiteBakedSpaceRoot)
```

#### 引数（Parameters）

`finiteBakedSpaceRoot` Transform

### <a id="Omni_Lighting_OmniLightProbeSpace_TryToBakedPosition_UnityEngine_Vector3_UnityEngine_Vector3__"></a> TryToBakedPosition\(Vector3, out Vector3\)

表示空間の位置をLight Probeが焼かれた有限空間へ変換します。

```csharp
public bool TryToBakedPosition(Vector3 displayWorldPosition, out Vector3 bakedWorldPosition)
```

#### 引数（Parameters）

`displayWorldPosition` Vector3

`bakedWorldPosition` Vector3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Lighting_OmniLightProbeSpace_LightProbeSpaceChanged"></a> LightProbeSpaceChanged

有効なLight Probe空間対応が変更されたことを通知します。

```csharp
public static event Action LightProbeSpaceChanged
```

#### 型（Event Type）

 [Action](https://learn.microsoft.com/dotnet/api/system.action)
