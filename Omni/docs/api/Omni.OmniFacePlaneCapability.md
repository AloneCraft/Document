# <a id="Omni_OmniFacePlaneCapability"></a> Class OmniFacePlaneCapability

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

交点方式(面と視線の交点。三角形の 3 頂点の値を画素で読む)を、この環境で使えるかと、使えない理由を返します。

<p>
生成シェーダーは交点方式の SubShader を先に置き、使えない環境では Unity が自動で次の SubShader(奥行き対数補間)を選びます。
奥行き対数補間では、とても長い三角形を視点の近くで見ると、奥行きが崩れることがあります(D05)。
自動で切り替わるので目では分かりにくく、理由を Console(1 回だけ)と検証 Scene の画面に出します。
視点の近くの被覆の欠け(D06)は、どの環境でも <xref href="Omni.OmniNearPatch" data-throw-if-not-resolved="false"></xref>(CPU)が補います。
2026-11-14 までは Geometry Shader も使っていたが、OmniNearPatch に置き換えて外した
(Docs/refactoring-designs/20261114-0400-cpu-near-patch-long-triangles.md)。
</p>

```csharp
public static class OmniFacePlaneCapability
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniFacePlaneCapability](Omni.OmniFacePlaneCapability.md)

## フィールド（Fields）

### <a id="Omni_OmniFacePlaneCapability_FacePlaneTagName"></a> FacePlaneTagName

交点方式の SubShader に付けた目印のタグ(変換器 <code>HlslRadialFacePlaneRewrite</code> が付ける)。

```csharp
public const string FacePlaneTagName = "OmniRadialDepth"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_OmniFacePlaneCapability_FacePlaneTagValue"></a> FacePlaneTagValue

```csharp
public const string FacePlaneTagValue = "FacePlane"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_OmniFacePlaneCapability_Supported"></a> Supported

この環境で交点方式を使えるなら true。

```csharp
public static bool Supported { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_OmniFacePlaneCapability_CurrentReason_System_Boolean_"></a> CurrentReason\(bool\)

今の環境で使えない理由(使えるなら空)。

```csharp
public static string CurrentReason(bool japanese)
```

#### 引数（Parameters）

`japanese` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_OmniFacePlaneCapability_IsSupported_UnityEngine_Rendering_GraphicsDeviceType_System_Boolean_"></a> IsSupported\(GraphicsDeviceType, bool\)

交点方式は DXC の barycentrics(Direct3D 12・Vulkan)を使います。WebGPU・Metal・OpenGL ES などでは使えません。
<code class="paramref">geometryShaders</code> は以前の版との互換のために残しています(今は見ません)。

```csharp
public static bool IsSupported(GraphicsDeviceType api, bool geometryShaders)
```

#### 引数（Parameters）

`api` GraphicsDeviceType

`geometryShaders` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_OmniFacePlaneCapability_Reason_UnityEngine_Rendering_GraphicsDeviceType_System_Boolean_System_Boolean_"></a> Reason\(GraphicsDeviceType, bool, bool\)

使えない理由(使えるなら空)。<code class="paramref">geometryShaders</code> は互換のために残しています(今は見ません)。

```csharp
public static string Reason(GraphicsDeviceType api, bool geometryShaders, bool japanese)
```

#### 引数（Parameters）

`api` GraphicsDeviceType

`geometryShaders` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`japanese` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_OmniFacePlaneCapability_UsesFacePlaneSubShader_UnityEngine_Material_"></a> UsesFacePlaneSubShader\(Material\)

材質で実際に選ばれている SubShader が交点方式なら true。Unity の <xref href="UnityEngine.Material.GetTag(System.String%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref> は、
この環境で動く SubShader のタグを返すので、どちらが選ばれたかを直接確かめられます。

```csharp
public static bool UsesFacePlaneSubShader(Material material)
```

#### 引数（Parameters）

`material` Material

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
