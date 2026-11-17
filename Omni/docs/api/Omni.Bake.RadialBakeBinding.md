# <a id="Omni_Bake_RadialBakeBinding"></a> Class RadialBakeBinding

Namespace: [Omni.Bake](Omni.Bake.md)  
Assembly: Radial.Runtime.dll  

シーン内 Renderer の配列を、対応する <xref href="Omni.Rendering.Radial.BakeData" data-throw-if-not-resolved="false"></xref> の
<xref href="Omni.Rendering.Radial.BakeData.Entries" data-throw-if-not-resolved="false"></xref> と同じ並びで保持する橋渡しです。

<p>
GlobalObjectId は Editor 専用でランタイムから引けず、ヒエラルキーパス文字列は
リネームで壊れるため、Unity のシーンローカル参照（コンポーネント経由のオブジェクト参照）で
対応を安定させます。シーンにつき1つ、<code>RadialBaker</code> が生成・更新します。
</p>

```csharp
public sealed class RadialBakeBinding : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[RadialBakeBinding](Omni.Bake.RadialBakeBinding.md)

## プロパティ（Properties）

### <a id="Omni_Bake_RadialBakeBinding_Data"></a> Data

紐づく <xref href="Omni.Rendering.Radial.BakeData" data-throw-if-not-resolved="false"></xref> です。

```csharp
public BakeData Data { get; }
```

#### 値（Property Value）

 [BakeData](Omni.Rendering.Radial.BakeData.md)

### <a id="Omni_Bake_RadialBakeBinding_RendererCount"></a> RendererCount

対応する Renderer の数（Data.Entries.Length と一致するはずです）。

```csharp
public int RendererCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Bake_RadialBakeBinding_GetRenderer_System_Int32_"></a> GetRenderer\(int\)

index番目の Renderer を返します（<xref href="Omni.Rendering.Radial.BakeData.Entries" data-throw-if-not-resolved="false"></xref>[index] に対応）。

```csharp
public Renderer GetRenderer(int index)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 Renderer

### <a id="Omni_Bake_RadialBakeBinding_SetData_Omni_Rendering_Radial_BakeData_UnityEngine_Renderer___"></a> SetData\(BakeData, Renderer\[\]\)

ベイク結果とRenderer対応表を設定します。RadialBaker からのみ呼ばれる想定です。

```csharp
public void SetData(BakeData data, Renderer[] renderers)
```

#### 引数（Parameters）

`data` [BakeData](Omni.Rendering.Radial.BakeData.md)

`renderers` Renderer\[\]
