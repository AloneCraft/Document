# <a id="Omni_Rendering_Radial_DrawTransform"></a> Struct DrawTransform

Namespace: [Omni.Rendering.Radial](Omni.Rendering.Radial.md)  
Assembly: Radial.Runtime.dll  

1台のRadialカメラから見た、1オブジェクトの一時的な表示変換です。
Componentではなく、Scene/Prefabへシリアライズされません。

```csharp
public readonly struct DrawTransform
```

## フィールド（Fields）

### <a id="Omni_Rendering_Radial_DrawTransform_BasisExponent"></a> BasisExponent

object-to-logical基底へ掛ける2進指数です。

```csharp
public readonly float BasisExponent
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Rendering_Radial_DrawTransform_BasisRow0"></a> BasisRow0

2進指数を除いたobject-to-logical基底の第1行です。

```csharp
public readonly Vector4 BasisRow0
```

#### 値（Field Value）

 Vector4

### <a id="Omni_Rendering_Radial_DrawTransform_BasisRow1"></a> BasisRow1

2進指数を除いたobject-to-logical基底の第2行です。

```csharp
public readonly Vector4 BasisRow1
```

#### 値（Field Value）

 Vector4

### <a id="Omni_Rendering_Radial_DrawTransform_BasisRow2"></a> BasisRow2

2進指数を除いたobject-to-logical基底の第3行です。

```csharp
public readonly Vector4 BasisRow2
```

#### 値（Field Value）

 Vector4

### <a id="Omni_Rendering_Radial_DrawTransform_NormalRow0"></a> NormalRow0

法線用の逆転置基底第1行です。

```csharp
public readonly Vector4 NormalRow0
```

#### 値（Field Value）

 Vector4

### <a id="Omni_Rendering_Radial_DrawTransform_NormalRow1"></a> NormalRow1

法線用の逆転置基底第2行です。

```csharp
public readonly Vector4 NormalRow1
```

#### 値（Field Value）

 Vector4

### <a id="Omni_Rendering_Radial_DrawTransform_NormalRow2"></a> NormalRow2

法線用の逆転置基底第3行です。

```csharp
public readonly Vector4 NormalRow2
```

#### 値（Field Value）

 Vector4

### <a id="Omni_Rendering_Radial_DrawTransform_PrecisionGuaranteed"></a> PrecisionGuaranteed

対象のLogicalTransformから精度を保って導出できた場合はtrueです。

```csharp
public readonly bool PrecisionGuaranteed
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Rendering_Radial_DrawTransform_RelativePositionExponent"></a> RelativePositionExponent

カメラ相対位置へ掛ける2進指数です。

```csharp
public readonly float RelativePositionExponent
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Rendering_Radial_DrawTransform_RelativePositionMantissa"></a> RelativePositionMantissa

2進指数を除いたカメラ相対位置です。

```csharp
public readonly Vector3 RelativePositionMantissa
```

#### 値（Field Value）

 Vector3

## メソッド（Methods）

### <a id="Omni_Rendering_Radial_DrawTransform_TryComposeLocalPoint_Unity_Mathematics_float3__Unity_Mathematics_float3__System_Single__"></a> TryComposeLocalPoint\(in float3, out float3, out float\)

GPUのRadial頂点処理と同じ仮数・指数演算で、ローカル頂点を
ワープ中心相対のLogical頂点へ合成します。

```csharp
public bool TryComposeLocalPoint(in float3 positionOS, out float3 relativeMantissa, out float relativeExponent)
```

#### 引数（Parameters）

`positionOS` float3

`relativeMantissa` float3

`relativeExponent` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 補足（Remarks）

Mesh頂点は描画時だけ存在する連続な相対値です。Logicalの最小量子より小さい
表面オフセットを保持するため、合成結果をLogical.Vector3へ戻しません。

### <a id="Omni_Rendering_Radial_DrawTransform_TryCreate_UnityEngine_Transform_UnityEngine_Transform_Omni_Rendering_Radial_DrawTransform__"></a> TryCreate\(Transform, Transform, out DrawTransform\)

指定したRadial中心と対象から、カメラ相対表示変換を構築します。
対象と基準中心をLogical姿勢として解決し、減算後にmantissa/exponentへ分離します。

```csharp
public static bool TryCreate(Transform radialCenter, Transform target, out DrawTransform result)
```

#### 引数（Parameters）

`radialCenter` Transform

`target` Transform

`result` [DrawTransform](Omni.Rendering.Radial.DrawTransform.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Rendering_Radial_DrawTransform_TryCreate_Omni_Logical_Position3__Omni_Logical_RenderPose__Omni_Rendering_Radial_DrawTransform__"></a> TryCreate\(in Position3, in RenderPose, out DrawTransform\)

解決済みの論理描画姿勢から、指定論理中心に対するRadialTransformを構築します。
GPU本体、有限描画プロキシ、独自選択輪郭が同じ姿勢を再利用するための経路です。

```csharp
public static bool TryCreate(in Position3 logicalCenter, in RenderPose pose, out DrawTransform result)
```

#### 引数（Parameters）

`logicalCenter` [Position3](Omni.Logical.Position3.md)

`pose` [RenderPose](Omni.Logical.RenderPose.md)

`result` [DrawTransform](Omni.Rendering.Radial.DrawTransform.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
