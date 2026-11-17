# <a id="VirtualizedGeometry_VirtualGeometryMaterials"></a> Class VirtualGeometryMaterials

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

地形の Cell とビルド済みメッシュ(<code>VirtualGeometryRenderer</code>)の Material が、VG 描画に使えるかを決める。
Materialのshaderが.vgshader由来でVG pass(<xref href="VirtualizedGeometry.VirtualGeometryMaterials.PassName" data-throw-if-not-resolved="false"></xref>)を持てばそのまま使う。
持たない通常のshaderは、メッシュ版に限り「VirtualGeometry/元shader名」のshader(同梱のURP標準分、または利用者が作った.vgshader)を探し、
内部Materialへpropertyとkeywordを写して使う(<xref href="VirtualizedGeometry.VirtualGeometryMaterials.TryResolve(UnityEngine.Material%2cUnityEngine.Material%40%2cSystem.Int32%40%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref>)。実行時生成の供給元(地形)は.vgshaderのMaterialだけを使う(<xref href="VirtualizedGeometry.VirtualGeometryMaterials.TryResolveSource(UnityEngine.Material%2cUnityEngine.Material%40%2cSystem.Int32%40%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref>)。

```csharp
public static class VirtualGeometryMaterials
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryMaterials](VirtualizedGeometry.VirtualGeometryMaterials.md)

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryMaterials_DepthNormalsPassName"></a> DepthNormalsPassName

```csharp
public const string DepthNormalsPassName = "VirtualGeometryDepthNormals"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryMaterials_DepthOnlyPassName"></a> DepthOnlyPassName

.vgshaderが元のDepthOnly・DepthNormals・ShadowCasterのpassから作るVG passのName/LightMode(prepassと影にVGの面を描く)。

```csharp
public const string DepthOnlyPassName = "VirtualGeometryDepthOnly"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryMaterials_PassName"></a> PassName

.vgshaderが追加するVG passのName/LightMode。URPはこのLightModeを通常Meshに描かない。

```csharp
public const string PassName = "VirtualGeometryForward"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryMaterials_ShaderPrefix"></a> ShaderPrefix

.vgshaderが生成するshader名の接頭辞。

```csharp
public const string ShaderPrefix = "VirtualGeometry/"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryMaterials_ShadowCasterPassName"></a> ShadowCasterPassName

```csharp
public const string ShadowCasterPassName = "VirtualGeometryShadowCaster"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryMaterials_FindDepthPass_UnityEngine_Material_System_Boolean_"></a> FindDepthPass\(Material, bool\)

VG の深度の pass(DepthNormals を求めるなら normals の pass、無ければ DepthOnly)。無ければ −1。

```csharp
public static int FindDepthPass(Material material, bool normals)
```

#### 引数（Parameters）

`material` Material

`normals` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryMaterials_FindShadowCasterPass_UnityEngine_Material_"></a> FindShadowCasterPass\(Material\)

VG の影の pass(元の ShadowCaster から作った pass)。無ければ −1。

```csharp
public static int FindShadowCasterPass(Material material)
```

#### 引数（Parameters）

`material` Material

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryMaterials_IsSupported_UnityEngine_Material_System_String__"></a> IsSupported\(Material, out string\)

描画可否の判定だけを行う。内部Materialは作らない。

```csharp
public static bool IsSupported(Material source, out string reason)
```

#### 引数（Parameters）

`source` Material

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryMaterials_NeedsVirtualShader_UnityEngine_Material_"></a> NeedsVirtualShader\(Material\)

不透明で、対応するVirtual Geometry Shaderがまだ無いMaterialか(.vgshaderを作れば描けるもの)。

```csharp
public static bool NeedsVirtualShader(Material source)
```

#### 引数（Parameters）

`source` Material

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryMaterials_Reset"></a> Reset\(\)

```csharp
[RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]
public static void Reset()
```

### <a id="VirtualizedGeometry_VirtualGeometryMaterials_TryResolve_UnityEngine_Material_UnityEngine_Material__System_Int32__System_String__"></a> TryResolve\(Material, out Material, out int, out string\)

メッシュ版用: VG描画に使うMaterialとpass index。.vgshader由来ならそのまま、持たなければ「VirtualGeometry/元shader名」のshaderで内部Materialを作って使う。
描けない場合は理由を返す。

```csharp
public static bool TryResolve(Material source, out Material material, out int pass, out string reason)
```

#### 引数（Parameters）

`source` Material

`material` Material

`pass` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryMaterials_TryResolveSource_UnityEngine_Material_UnityEngine_Material__System_Int32__System_String__"></a> TryResolveSource\(Material, out Material, out int, out string\)

実行時生成の供給元(地形など)用: .vgshader 由来で VG pass を持つ Material だけを描ける（通常の shader から内部 Material は作らない）。描けない場合は理由を返す。

```csharp
public static bool TryResolveSource(Material source, out Material material, out int pass, out string reason)
```

#### 引数（Parameters）

`source` Material

`material` Material

`pass` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
