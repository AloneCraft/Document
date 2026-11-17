# <a id="Omni_Rendering_OmniMotionBlur"></a> Class OmniMotionBlur

Namespace: [Omni.Rendering](Omni.Rendering.md)  
Assembly: Radial.Runtime.dll  

奥行きを見るモーションブラーの Volume 設定(<xref href="Omni.Rendering.OmniMotionBlurFeature" data-throw-if-not-resolved="false"></xref> が読む)。
URP の <xref href="UnityEngine.Rendering.Universal.MotionBlur" data-throw-if-not-resolved="false"></xref> は手前と奥を区別せずに混ぜるため、速く流れる背景がほとんど動かない手前の物の色を拾い、縁の外へもやが出る。
これを使う Volume では、URP の Motion Blur を併用しない(二重にぼかさない)。強さ・上限・品質の意味は URP の Motion Blur と同じ。

```csharp
[Serializable]
[VolumeComponentMenu("Omni/Motion Blur (Depth Aware)")]
[SupportedOnRenderPipeline(typeof(UniversalRenderPipelineAsset))]
public sealed class OmniMotionBlur : VolumeComponent, IApplyRevertPropertyContextMenuItemProvider
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
VolumeComponent ← 
[OmniMotionBlur](Omni.Rendering.OmniMotionBlur.md)

#### 実装するインターフェース（Implements）

IApplyRevertPropertyContextMenuItemProvider

## フィールド（Fields）

### <a id="Omni_Rendering_OmniMotionBlur_clamp"></a> clamp

ぼかす全長の上限(画面に対する割合、UV)。

```csharp
public ClampedFloatParameter clamp
```

#### 値（Field Value）

 ClampedFloatParameter

### <a id="Omni_Rendering_OmniMotionBlur_intensity"></a> intensity

ぼかす長さ(フレーム間の動きに対する割合、シャッターの開き)。0 なら働かない。

```csharp
public ClampedFloatParameter intensity
```

#### 値（Field Value）

 ClampedFloatParameter

### <a id="Omni_Rendering_OmniMotionBlur_quality"></a> quality

標本の数(Low 8、Medium 12、High 16)。

```csharp
public MotionBlurQualityParameter quality
```

#### 値（Field Value）

 MotionBlurQualityParameter

## メソッド（Methods）

### <a id="Omni_Rendering_OmniMotionBlur_IsActive"></a> IsActive\(\)

```csharp
public bool IsActive()
```

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
