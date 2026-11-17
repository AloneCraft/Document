# <a id="Omni_Lighting_OmniLightingSpace"></a> Class OmniLightingSpace

Namespace: [Omni.Lighting](Omni.Lighting.md)  
Assembly: Radial.Runtime.dll  

巨大Logical座標と、Reflection Probe・APV・Lightmapが扱う有限ベイク空間を対応付けます。

```csharp
[DisallowMultipleComponent]
public sealed class OmniLightingSpace : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[OmniLightingSpace](Omni.Lighting.OmniLightingSpace.md)

## プロパティ（Properties）

### <a id="Omni_Lighting_OmniLightingSpace_LightingSpaceRoot"></a> LightingSpaceRoot

有限ベイク空間の原点です。

```csharp
public Transform LightingSpaceRoot { get; }
```

#### 値（Property Value）

 Transform

### <a id="Omni_Lighting_OmniLightingSpace_LogicalOrigin"></a> LogicalOrigin

Logical原点として使うTransformです。

```csharp
public Transform LogicalOrigin { get; }
```

#### 値（Property Value）

 [Transform](Omni.Logical.Transform.md)

## メソッド（Methods）

### <a id="Omni_Lighting_OmniLightingSpace_Configure_Omni_Logical_Transform_UnityEngine_Transform_"></a> Configure\(Transform, Transform\)

検証シーン生成時に照明空間の対応を設定します。

```csharp
public void Configure(Transform logicalOriginTransform, Transform finiteLightingRoot)
```

#### 引数（Parameters）

`logicalOriginTransform` [Transform](Omni.Logical.Transform.md)

`finiteLightingRoot` Transform

### <a id="Omni_Lighting_OmniLightingSpace_TryToLightingPosition_Omni_Logical_Position3__UnityEngine_Vector3__"></a> TryToLightingPosition\(in Position3, out Vector3\)

巨大な絶対値をfloatへ変換せず、Logical原点との差を取ってから有限座標へ変換します。

```csharp
public bool TryToLightingPosition(in Position3 logicalPosition, out Vector3 lightingPosition)
```

#### 引数（Parameters）

`logicalPosition` [Position3](Omni.Logical.Position3.md)

`lightingPosition` Vector3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Lighting_OmniLightingSpace_TryToLogicalPosition_UnityEngine_Vector3_Omni_Logical_Position3__"></a> TryToLogicalPosition\(Vector3, out Position3\)

有限ベイク空間の位置をLogical位置へ戻します。

```csharp
public bool TryToLogicalPosition(Vector3 lightingPosition, out Position3 logicalPosition)
```

#### 引数（Parameters）

`lightingPosition` Vector3

`logicalPosition` [Position3](Omni.Logical.Position3.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
