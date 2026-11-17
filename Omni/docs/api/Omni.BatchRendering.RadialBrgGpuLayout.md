# <a id="Omni_BatchRendering_RadialBrgGpuLayout"></a> Class RadialBrgGpuLayout

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

Saturn Meso粒子の32 byte recordとBRG RawBufferの固定レイアウトです。

<p>
record自体の生成責務はSaturn Coreにあり、この型はDOTS metadataとbyte offsetだけを唯一の
真実源として管理します。Shaderは同じoffsetをRadialBrgParticle.hlslから読むため、
C#とHLSLのlayoutずれを検出できます。
</p>

```csharp
public static class RadialBrgGpuLayout
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialBrgGpuLayout](Omni.BatchRendering.RadialBrgGpuLayout.md)

## フィールド（Fields）

### <a id="Omni_BatchRendering_RadialBrgGpuLayout_HeaderByteSize"></a> HeaderByteSize

Camera固有ヘッダー本体の固定byte数です。

```csharp
public const int HeaderByteSize = 208
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialBrgGpuLayout_HeaderDataOffsetBytes"></a> HeaderDataOffsetBytes

Unity推奨の先頭予約領域と共有identity transformの後に置く実ヘッダーoffsetです。

```csharp
public const int HeaderDataOffsetBytes = 128
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialBrgGpuLayout_MetadataCount"></a> MetadataCount

BRG batchへ渡すmetadata数です。

```csharp
public const int MetadataCount = 2
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialBrgGpuLayout_OrbitLocalToWorldOffset"></a> OrbitLocalToWorldOffset

orbit local→world行列のRawBuffer byte offsetです。

```csharp
public const uint OrbitLocalToWorldOffset = 272
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_BatchRendering_RadialBrgGpuLayout_ParticleDataOffsetBytes"></a> ParticleDataOffsetBytes

Cameraヘッダーと先頭予約領域を含む粒子record開始byte offsetです。

```csharp
public const int ParticleDataOffsetBytes = 336
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialBrgGpuLayout_ParticleDataOffsetWords"></a> ParticleDataOffsetWords

粒子recordを <code>GraphicsBuffer.SetData&lt;uint&gt;</code> で書き込む先頭word indexです。

```csharp
public const int ParticleDataOffsetWords = 84
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialBrgGpuLayout_ParticleRecordByteSize"></a> ParticleRecordByteSize

1粒子recordの固定byte数です。

```csharp
public const int ParticleRecordByteSize = 32
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialBrgGpuLayout_PerInstanceDataBit"></a> PerInstanceDataBit

DOTS metadataでper-instance offsetを有効化するbitです。

```csharp
public const uint PerInstanceDataBit = 2147483648
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_BatchRendering_RadialBrgGpuLayout_TransformDataOffsetBytes"></a> TransformDataOffsetBytes

unity_ObjectToWorld／unity_WorldToObjectが共有するidentity float3x4のoffsetです。

```csharp
public const uint TransformDataOffsetBytes = 64
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## メソッド（Methods）

### <a id="Omni_BatchRendering_RadialBrgGpuLayout_IsHeaderLayoutValid"></a> IsHeaderLayoutValid\(\)

このlayoutがC#側で想定したbyte数と一致するかを返します。
Sceneの初期化時にfalseならBRGを使わずMacroOnlyへ縮退します。

```csharp
public static bool IsHeaderLayoutValid()
```

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialBrgGpuLayout_WriteMetadata_Unity_Collections_NativeArray_UnityEngine_Rendering_MetadataValue__"></a> WriteMetadata\(NativeArray<MetadataValue\>\)

BRGが要求する共有identity transform metadataを書き込みます。
Camera headerとrecordは固定RawBuffer offsetから直接読みます。
<param name="metadata">長さ2以上のadapter確保済み配列です。</param>

```csharp
public static void WriteMetadata(NativeArray<MetadataValue> metadata)
```

#### 引数（Parameters）

`metadata` NativeArray<MetadataValue\>
