# <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout"></a> Struct RadialSceneBatchGpuLayout

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

Scene BRGが共有するRaw GraphicsBufferのSoA配置です。
Instance 0は0行列sentinel、実Renderer submeshは1始まりで格納します。

```csharp
public readonly struct RadialSceneBatchGpuLayout
```

## フィールド（Fields）

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_CameraPacketByteCount"></a> CameraPacketByteCount

camera packet 1 slotのbyte数です。

```csharp
public const int CameraPacketByteCount = 224
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_CameraPacketCapacity"></a> CameraPacketCapacity

同時に保持できるBRG camera packet slot数です。

```csharp
public const int CameraPacketCapacity = 64
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_CameraPacketVectorCount"></a> CameraPacketVectorCount

cameraごとにBRGへ登録する固定packetのVector4数です。

```csharp
public const int CameraPacketVectorCount = 14
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_HeaderByteCount"></a> HeaderByteCount

Unity標準のdefault metadata参照を安全にする先頭ゼロ領域です。

```csharp
public const int HeaderByteCount = 64
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_MetadataCount"></a> MetadataCount

Scene residentとcamera packetを合わせたDOTS metadata数です。

```csharp
public const int MetadataCount = 34
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_PerInstanceDataBit"></a> PerInstanceDataBit

BRGのper-instance metadata bitです。

```csharp
public const uint PerInstanceDataBit = 2147483648
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_SceneMetadataCount"></a> SceneMetadataCount

Scene residentのper-instance DOTS metadata数です。

```csharp
public const int SceneMetadataCount = 20
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_CameraPacketOffset"></a> CameraPacketOffset

camera packet slot 0のbyte offsetです。

```csharp
public int CameraPacketOffset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_CameraRelativeTransformExponentsOffset"></a> CameraRelativeTransformExponentsOffset

cameraごとに分離したRadialTransformExponents配列のslot 0先頭byte offsetです。

```csharp
public int CameraRelativeTransformExponentsOffset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_CameraRelativeTransformRelativeOffset"></a> CameraRelativeTransformRelativeOffset

cameraごとに分離したRadialTransformRelative配列のslot 0先頭byte offsetです。
この領域は巨大な絶対値をGPUで減算せず、Logical中心との差分をCPUで符号化した値を持ちます。

```csharp
public int CameraRelativeTransformRelativeOffset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_FacePlaneEyeObjectHighOffset"></a> FacePlaneEyeObjectHighOffset

cameraごとに分離した「描画の中心を物体座標で表した値」の上位 float(xyz、w=使える印)配列の slot 0 先頭 byte offset です。
交点方式(面と視線の交点)が面までの距離を物体座標で測るために使います(<xref href="Omni.Rendering.Radial.FacePlaneEyeObject" data-throw-if-not-resolved="false"></xref>)。

```csharp
public int FacePlaneEyeObjectHighOffset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_FacePlaneEyeObjectLowOffset"></a> FacePlaneEyeObjectLowOffset

同じ値の下位 float(xyz)配列の slot 0 先頭 byte offset です。

```csharp
public int FacePlaneEyeObjectLowOffset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_InstanceCapacity"></a> InstanceCapacity

sentinelを含むinstance slot数です。

```csharp
public int InstanceCapacity { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_LightmapScaleOffsetOffset"></a> LightmapScaleOffsetOffset

unity_LightmapST配列のbyte offsetです。

```csharp
public int LightmapScaleOffsetOffset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_ObjectToWorldOffset"></a> ObjectToWorldOffset

現在ObjectToWorld配列のbyte offsetです。

```csharp
public int ObjectToWorldOffset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_PreviousObjectToWorldOffset"></a> PreviousObjectToWorldOffset

前フレームObjectToWorld配列のbyte offsetです。

```csharp
public int PreviousObjectToWorldOffset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_PreviousWorldToObjectOffset"></a> PreviousWorldToObjectOffset

前フレームWorldToObject配列のbyte offsetです。

```csharp
public int PreviousWorldToObjectOffset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_PropertyOffsets"></a> PropertyOffsets

全DOTS property先頭offsetを列挙します。Editor検証とテスト専用です。

```csharp
public IReadOnlyList<int> PropertyOffsets { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_RadialBasisRow0Offset"></a> RadialBasisRow0Offset

Radial basis row 0配列のbyte offsetです。

```csharp
public int RadialBasisRow0Offset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_RadialBasisRow1Offset"></a> RadialBasisRow1Offset

Radial basis row 1配列のbyte offsetです。

```csharp
public int RadialBasisRow1Offset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_RadialBasisRow2Offset"></a> RadialBasisRow2Offset

Radial basis row 2配列のbyte offsetです。

```csharp
public int RadialBasisRow2Offset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_RadialLabelVisibleOffset"></a> RadialLabelVisibleOffset

LabelVisible配列のbyte offsetです。

```csharp
public int RadialLabelVisibleOffset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_RadialNormalRow0Offset"></a> RadialNormalRow0Offset

Radial normal row 0配列のbyte offsetです。

```csharp
public int RadialNormalRow0Offset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_RadialNormalRow1Offset"></a> RadialNormalRow1Offset

Radial normal row 1配列のbyte offsetです。

```csharp
public int RadialNormalRow1Offset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_RadialNormalRow2Offset"></a> RadialNormalRow2Offset

Radial normal row 2配列のbyte offsetです。

```csharp
public int RadialNormalRow2Offset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_RadialTransformExponentsOffset"></a> RadialTransformExponentsOffset

RadialTransformExponents配列のbyte offsetです。

```csharp
public int RadialTransformExponentsOffset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_RadialTransformRelativeOffset"></a> RadialTransformRelativeOffset

RadialTransformRelative配列のbyte offsetです。

```csharp
public int RadialTransformRelativeOffset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_RadialUseRigidAnchorOffset"></a> RadialUseRigidAnchorOffset

UseRigidAnchor配列のbyte offsetです。

```csharp
public int RadialUseRigidAnchorOffset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_RadialUseTransformOffset"></a> RadialUseTransformOffset

UseRadialTransform配列のbyte offsetです。

```csharp
public int RadialUseTransformOffset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_SphericalHarmonicsOffset"></a> SphericalHarmonicsOffset

unity_SHCoefficients配列のbyte offsetです。

```csharp
public int SphericalHarmonicsOffset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_TotalByteCount"></a> TotalByteCount

Raw GraphicsBuffer全体のbyte数です。

```csharp
public int TotalByteCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_WorldToObjectOffset"></a> WorldToObjectOffset

現在WorldToObject配列のbyte offsetです。

```csharp
public int WorldToObjectOffset { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_Create_System_Int32_"></a> Create\(int\)

instance容量から重複しないSoA配置を構築します。

```csharp
public static RadialSceneBatchGpuLayout Create(int instanceCapacity)
```

#### 引数（Parameters）

`instanceCapacity` [int](https://learn.microsoft.com/dotnet/api/system.int32)

sentinelを含む1以上のslot数です。

#### 戻り値（Returns）

 [RadialSceneBatchGpuLayout](Omni.BatchRendering.RadialSceneBatchGpuLayout.md)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_GetCameraPacketOffset_System_Int32_"></a> GetCameraPacketOffset\(int\)

camera packet slotの先頭byte offsetを返します。

```csharp
public int GetCameraPacketOffset(int cameraPacketSlot)
```

#### 引数（Parameters）

`cameraPacketSlot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_GetCameraRelativeTransformExponentsOffset_System_Int32_"></a> GetCameraRelativeTransformExponentsOffset\(int\)

指定camera slotの相対位置指数配列先頭byte offsetを返します。

```csharp
public int GetCameraRelativeTransformExponentsOffset(int cameraPacketSlot)
```

#### 引数（Parameters）

`cameraPacketSlot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_GetCameraRelativeTransformRelativeOffset_System_Int32_"></a> GetCameraRelativeTransformRelativeOffset\(int\)

指定camera slotの相対位置配列先頭byte offsetを返します。

```csharp
public int GetCameraRelativeTransformRelativeOffset(int cameraPacketSlot)
```

#### 引数（Parameters）

`cameraPacketSlot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_GetFacePlaneEyeObjectHighOffset_System_Int32_"></a> GetFacePlaneEyeObjectHighOffset\(int\)

指定camera slotの「描画の中心を物体座標で表した値」(上位)配列先頭byte offsetを返します。

```csharp
public int GetFacePlaneEyeObjectHighOffset(int cameraPacketSlot)
```

#### 引数（Parameters）

`cameraPacketSlot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_GetFacePlaneEyeObjectLowOffset_System_Int32_"></a> GetFacePlaneEyeObjectLowOffset\(int\)

指定camera slotの「描画の中心を物体座標で表した値」(下位)配列先頭byte offsetを返します。

```csharp
public int GetFacePlaneEyeObjectLowOffset(int cameraPacketSlot)
```

#### 引数（Parameters）

`cameraPacketSlot` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_Validate_System_String__"></a> Validate\(out string\)

配置が有限範囲かつ昇順・16 byte整列かを検証します。

```csharp
public bool Validate(out string reason)
```

#### 引数（Parameters）

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_WriteMetadata_Unity_Collections_NativeArray_UnityEngine_Rendering_MetadataValue__"></a> WriteMetadata\(NativeArray<MetadataValue\>\)

slot 0のcamera packetを参照するDOTS metadataを構築します。

```csharp
public void WriteMetadata(NativeArray<MetadataValue> metadata)
```

#### 引数（Parameters）

`metadata` NativeArray<MetadataValue\>

### <a id="Omni_BatchRendering_RadialSceneBatchGpuLayout_WriteMetadata_Unity_Collections_NativeArray_UnityEngine_Rendering_MetadataValue__System_Int32_"></a> WriteMetadata\(NativeArray<MetadataValue\>, int\)

指定camera packet slotの固定値を参照するDOTS metadataを構築します。
Scene resident値は従来どおりper-instance、camera値は固定アドレスです。

```csharp
public void WriteMetadata(NativeArray<MetadataValue> metadata, int cameraPacketSlot)
```

#### 引数（Parameters）

`metadata` NativeArray<MetadataValue\>

`cameraPacketSlot` [int](https://learn.microsoft.com/dotnet/api/system.int32)
