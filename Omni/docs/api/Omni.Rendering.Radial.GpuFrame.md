# <a id="Omni_Rendering_Radial_GpuFrame"></a> Struct GpuFrame

Namespace: [Omni.Rendering.Radial](Omni.Rendering.Radial.md)  
Assembly: Radial.Runtime.dll  

BRG専用シェーダーとCPUカリングが共有する、カメラ相対Radial GPU frameです。
この値は<xref href="UnityEngine.Shader.SetGlobalFloat(System.Int32%2cSystem.Single)" data-throw-if-not-resolved="false"></xref>から再取得せず、
<xref href="Omni.Rendering.Radial.ViewSnapshot" data-throw-if-not-resolved="false"></xref>を経由してカメラ別に受け渡します。
SaturnシーンのMesoリングBRG描画で使用します。

```csharp
public readonly struct GpuFrame
```

## コンストラクター（Constructors）

### <a id="Omni_Rendering_Radial_GpuFrame__ctor_System_Single_System_Single_System_Single_System_Single_UnityEngine_Vector4_System_Single_UnityEngine_Vector4_UnityEngine_Vector4_UnityEngine_Vector4_"></a> GpuFrame\(float, float, float, float, Vector4, float, Vector4, Vector4, Vector4\)

GPU frameを構築します。

```csharp
public GpuFrame(float radialScale, float mode, float linearRadius, float log2ViewScale, Vector4 eyeRelative, float eyeRelativeExponent, Vector4 viewRow0, Vector4 viewRow1, Vector4 viewRow2)
```

#### 引数（Parameters）

`radialScale` [float](https://learn.microsoft.com/dotnet/api/system.single)

放射スケールS。有限な描画単位を渡します。

`mode` [float](https://learn.microsoft.com/dotnet/api/system.single)

写像の有無（0 = Smooth Log、−1 = 写像しない）。

`linearRadius` [float](https://learn.microsoft.com/dotnet/api/system.single)

予約（常に 0）。

`log2ViewScale` [float](https://learn.microsoft.com/dotnet/api/system.single)

View Scaleの2進対数。有限値を渡します。

`eyeRelative` Vector4

ワープ中心からの目の相対仮数。非有限成分は後段でfail-openになります。

`eyeRelativeExponent` [float](https://learn.microsoft.com/dotnet/api/system.single)

目の相対仮数の2進指数。非有限値は後段でfail-openになります。

`viewRow0` Vector4

位置を持たないview回転の第0行です。

`viewRow1` Vector4

位置を持たないview回転の第1行です。

`viewRow2` Vector4

位置を持たないview回転の第2行です。

## フィールド（Fields）

### <a id="Omni_Rendering_Radial_GpuFrame_EyeRelative"></a> EyeRelative

ワープ中心から見た目の相対仮数。w=1は自己中心Orbitの写像前表示残差、w=0は通常のObserver Eyeです。

```csharp
public readonly Vector4 EyeRelative
```

#### 値（Field Value）

 Vector4

### <a id="Omni_Rendering_Radial_GpuFrame_EyeRelativeExponent"></a> EyeRelativeExponent

<xref href="Omni.Rendering.Radial.GpuFrame.EyeRelative" data-throw-if-not-resolved="false"></xref>の2進指数です。

```csharp
public readonly float EyeRelativeExponent
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Rendering_Radial_GpuFrame_LinearRadius"></a> LinearRadius

予約（常に 0。旧線形半径の位置で、写像には使いません）。

```csharp
public readonly float LinearRadius
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Rendering_Radial_GpuFrame_Log2ViewScale"></a> Log2ViewScale

View Scaleの2進対数です。

```csharp
public readonly float Log2ViewScale
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Rendering_Radial_GpuFrame_Mode"></a> Mode

写像の有無です（0 = Smooth Log、−1 = 写像しない）。

```csharp
public readonly float Mode
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Rendering_Radial_GpuFrame_RadialScale"></a> RadialScale

放射スケールSです（写像は Smooth Log だけで、常に <xref href="Omni.RadialSettings.RadialScale" data-throw-if-not-resolved="false"></xref> = 1）。

```csharp
public readonly float RadialScale
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Rendering_Radial_GpuFrame_ViewRow0"></a> ViewRow0

位置を含まないview行列の第0行です。

```csharp
public readonly Vector4 ViewRow0
```

#### 値（Field Value）

 Vector4

### <a id="Omni_Rendering_Radial_GpuFrame_ViewRow1"></a> ViewRow1

位置を含まないview行列の第1行です。

```csharp
public readonly Vector4 ViewRow1
```

#### 値（Field Value）

 Vector4

### <a id="Omni_Rendering_Radial_GpuFrame_ViewRow2"></a> ViewRow2

位置を含まないview行列の第2行です。

```csharp
public readonly Vector4 ViewRow2
```

#### 値（Field Value）

 Vector4

## プロパティ（Properties）

### <a id="Omni_Rendering_Radial_GpuFrame_IsFinite"></a> IsFinite

すべてのGPU入力が有限かを返します。falseならBRGは可視側へ倒します。

```csharp
public bool IsFinite { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Rendering_Radial_GpuFrame_IsUsable"></a> IsUsable

GPU frameをシェル判定へ使えるかを返します。ゼロ以下の尺度は退化としてfail-openにします。
予約の位置（<xref href="Omni.Rendering.Radial.GpuFrame.LinearRadius" data-throw-if-not-resolved="false"></xref>、常に 0）は判定に使いません。

```csharp
public bool IsUsable { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
