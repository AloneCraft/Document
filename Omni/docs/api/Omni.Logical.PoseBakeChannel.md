# <a id="Omni_Logical_PoseBakeChannel"></a> Class PoseBakeChannel

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Omni.Sequencer.Runtime.dll  

1つの対象（カメラ、主光源など）についての時系列サンプル列です。

<p>
Logical値はサンプルごとの<xref href="Omni.Logical.ScalarField" data-throw-if-not-resolved="false"></xref>ではなく、チャンネル単位の
平坦な<code>ulong</code>配列（SoA）へ詰めます。<xref href="Omni.Logical.ScalarField" data-throw-if-not-resolved="false"></xref>は
<code>OnBeforeSerialize</code>のたびに<code>ulong[LimbCount]</code>を新規確保するため、
9000サンプル×11スカラーでは10万個規模の小配列が生まれます。平坦配列なら
チャンネルあたり数本で済み、読み出しも<xref href="System.ReadOnlySpan%601" data-throw-if-not-resolved="false"></xref>経由で
割り当てなしに行えます。加えてUnityは整数配列をYAMLへ16進ブロブ1行で書くため、
アセットの行数も桁違いに小さくなります。
</p>
<p>
空間値をfloatやdoubleへ落とした形では一切保存しません。保存されるのは
<xref href="Omni.Logical.IntRaw" data-throw-if-not-resolved="false"></xref>のraw limbそのものです。画角・クリップ・光の強さ・色は
空間量ではないのでfloatのまま持ちます。
</p>

```csharp
[Serializable]
[MovedFrom(true, "Omni.Sequencer", null, "LogicalPoseBakeChannel")]
public sealed class PoseBakeChannel : ISerializationCallbackReceiver
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PoseBakeChannel](Omni.Logical.PoseBakeChannel.md)

#### 実装するインターフェース（Implements）

ISerializationCallbackReceiver

## プロパティ（Properties）

### <a id="Omni_Logical_PoseBakeChannel_HasClipRange"></a> HasClipRange

クリップ範囲サンプルを持つ場合はtrueです。

```csharp
public bool HasClipRange { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeChannel_HasDistance"></a> HasDistance

カメラ距離サンプルを持つ場合はtrueです。

```csharp
public bool HasDistance { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeChannel_HasFieldOfView"></a> HasFieldOfView

画角サンプルを持つ場合はtrueです。

```csharp
public bool HasFieldOfView { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeChannel_HasLightShading"></a> HasLightShading

光の強さ・色サンプルを持つ場合はtrueです。

```csharp
public bool HasLightShading { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeChannel_HasLookOffset"></a> HasLookOffset

注視点Logicalオフセットのサンプルを持つ場合はtrueです。

```csharp
public bool HasLookOffset { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeChannel_HasPosition"></a> HasPosition

位置サンプルを持つ場合はtrueです。

```csharp
public bool HasPosition { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeChannel_HasRotation"></a> HasRotation

回転サンプルを持つ場合はtrueです。

```csharp
public bool HasRotation { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeChannel_HasTargetIndices"></a> HasTargetIndices

注視対象の索引サンプルを持つ場合はtrueです。

```csharp
public bool HasTargetIndices { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeChannel_Kind"></a> Kind

このチャンネルが駆動する対象の種類。

```csharp
public PoseBakeChannelKind Kind { get; }
```

#### 値（Property Value）

 [PoseBakeChannelKind](Omni.Logical.PoseBakeChannelKind.md)

### <a id="Omni_Logical_PoseBakeChannel_SampleCount"></a> SampleCount

サンプル数。

```csharp
public int SampleCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_PoseBakeChannel_TargetPath"></a> TargetPath

バインド対象を指す安定した識別子（"Camera" / "KeyLight" など）。

```csharp
public string TargetPath { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Logical_PoseBakeChannel_CreateForBake_System_String_Omni_Logical_PoseBakeChannelKind_System_Int32_"></a> CreateForBake\(string, PoseBakeChannelKind, int\)

ベイク実行時にサンプル配列を確保します。ベイカー以外から呼ぶ想定はありません。

```csharp
public static PoseBakeChannel CreateForBake(string targetPath, PoseBakeChannelKind kind, int sampleCount)
```

#### 引数（Parameters）

`targetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

バインド対象の安定識別子。

`kind` [PoseBakeChannelKind](Omni.Logical.PoseBakeChannelKind.md)

駆動する対象の種類。

`sampleCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

サンプル数。

#### 戻り値（Returns）

 [PoseBakeChannel](Omni.Logical.PoseBakeChannel.md)

### <a id="Omni_Logical_PoseBakeChannel_IsWellFormed"></a> IsWellFormed\(\)

宣言したサンプル数と実際の配列長が食い違っていないことを確認します。
壊れたシリアライズデータを部分的に読み進めて、途中から別サンプルの
limbを混ぜてしまう事故を防ぎます。

```csharp
public bool IsWellFormed()
```

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeChannel_OnAfterDeserialize"></a> OnAfterDeserialize\(\)

旧形式（Logicalが128ビット・小数32ビットだったころの、値ごとに2 limb）の位置・距離・注視点オフセットを、
同じ数値の現在の形式へ広げます（配布先の既存のベイク資産を読むための互換。回転は128ビットのままで変わりません）。

```csharp
public void OnAfterDeserialize()
```

### <a id="Omni_Logical_PoseBakeChannel_OnBeforeSerialize"></a> OnBeforeSerialize\(\)

<p>Implement this callback to transform data into serializable data types immediately before an object is serialized.</p>

```csharp
public void OnBeforeSerialize()
```

### <a id="Omni_Logical_PoseBakeChannel_TryReadClipRange_System_Int32_System_Single__System_Single__"></a> TryReadClipRange\(int, out float, out float\)

指定サンプルのクリップ範囲を返します。

```csharp
public bool TryReadClipRange(int index, out float nearClip, out float farClip)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`nearClip` [float](https://learn.microsoft.com/dotnet/api/system.single)

`farClip` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeChannel_TryReadDistance_System_Int32_Omni_Logical_Scalar__"></a> TryReadDistance\(int, out Scalar\)

指定サンプルのカメラ距離を復元します。

```csharp
public bool TryReadDistance(int index, out Scalar value)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`value` Scalar

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeChannel_TryReadFieldOfView_System_Int32_System_Single__"></a> TryReadFieldOfView\(int, out float\)

指定サンプルの画角を返します。

```csharp
public bool TryReadFieldOfView(int index, out float fieldOfView)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`fieldOfView` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeChannel_TryReadLightShading_System_Int32_System_Single__UnityEngine_Color__"></a> TryReadLightShading\(int, out float, out Color\)

指定サンプルの光の強さ・色を返します。

```csharp
public bool TryReadLightShading(int index, out float intensity, out Color color)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`intensity` [float](https://learn.microsoft.com/dotnet/api/system.single)

`color` Color

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeChannel_TryReadLookOffset_System_Int32_Omni_Logical_Vector3__"></a> TryReadLookOffset\(int, out Vector3\)

指定サンプルの注視点Logicalオフセットを復元します。

```csharp
public bool TryReadLookOffset(int index, out Vector3 value)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`value` Vector3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeChannel_TryReadPosition_System_Int32_Omni_Logical_Position3__"></a> TryReadPosition\(int, out Position3\)

指定サンプルの位置を復元します。

```csharp
public bool TryReadPosition(int index, out Position3 value)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`value` Position3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeChannel_TryReadRotation_System_Int32_Omni_Logical_Quaternion__"></a> TryReadRotation\(int, out Quaternion\)

指定サンプルの回転を復元します。正規化はしません（raw一致検証のため）。

```csharp
public bool TryReadRotation(int index, out Quaternion value)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`value` Quaternion

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeChannel_TryReadTargetIndex_System_Int32_System_Int32__"></a> TryReadTargetIndex\(int, out int\)

指定サンプルの注視対象索引を返します。

```csharp
public bool TryReadTargetIndex(int index, out int targetIndex)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`targetIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_PoseBakeChannel_WriteCameraSettings_System_Int32_System_Int32_System_Single_System_Single_System_Single_"></a> WriteCameraSettings\(int, int, float, float, float\)

ベイク実行時に1サンプル分のカメラ設定を書き込みます。

```csharp
public void WriteCameraSettings(int index, int targetIndex, float fieldOfView, float nearClip, float farClip)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`targetIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`fieldOfView` [float](https://learn.microsoft.com/dotnet/api/system.single)

`nearClip` [float](https://learn.microsoft.com/dotnet/api/system.single)

`farClip` [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Logical_PoseBakeChannel_WriteDistance_System_Int32_Omni_Logical_Scalar__"></a> WriteDistance\(int, in Scalar\)

ベイク実行時に1サンプル分のカメラ距離を書き込みます。

```csharp
public void WriteDistance(int index, in Scalar value)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`value` Scalar

### <a id="Omni_Logical_PoseBakeChannel_WriteLightShading_System_Int32_System_Single_UnityEngine_Color_"></a> WriteLightShading\(int, float, Color\)

ベイク実行時に1サンプル分の光の強さ・色を書き込みます。

```csharp
public void WriteLightShading(int index, float intensity, Color color)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`intensity` [float](https://learn.microsoft.com/dotnet/api/system.single)

`color` Color

### <a id="Omni_Logical_PoseBakeChannel_WriteLookOffset_System_Int32_Omni_Logical_Vector3__"></a> WriteLookOffset\(int, in Vector3\)

ベイク実行時に1サンプル分の注視点Logicalオフセットを書き込みます。

```csharp
public void WriteLookOffset(int index, in Vector3 value)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`value` Vector3

### <a id="Omni_Logical_PoseBakeChannel_WritePosition_System_Int32_Omni_Logical_Position3__"></a> WritePosition\(int, in Position3\)

ベイク実行時に1サンプル分の位置を書き込みます。

```csharp
public void WritePosition(int index, in Position3 value)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`value` Position3

### <a id="Omni_Logical_PoseBakeChannel_WriteRotation_System_Int32_Omni_Logical_Quaternion__"></a> WriteRotation\(int, in Quaternion\)

ベイク実行時に1サンプル分の回転を書き込みます。

```csharp
public void WriteRotation(int index, in Quaternion value)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`value` Quaternion
