# <a id="Omni_BatchRendering_RadialBatchViewKey"></a> Struct RadialBatchViewKey

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

BRG callbackのviewを識別する不変キーです。

<p>
Unity 6000のCamera cullingで実測したBRG viewIDは対象Camera componentの
<xref href="UnityEngine.EntityId" data-throw-if-not-resolved="false"></xref>と一致するため、その64bit表現を保持します。
SaturnシーンのGame View、Scene View、比較用CameraはこのキーごとにGPU bufferとBatchIDを分離します。
</p>

```csharp
public readonly struct RadialBatchViewKey : IEquatable<RadialBatchViewKey>
```

#### 実装するインターフェース（Implements）

[IEquatable<RadialBatchViewKey\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## コンストラクター（Constructors）

### <a id="Omni_BatchRendering_RadialBatchViewKey__ctor_UnityEngine_EntityId_"></a> RadialBatchViewKey\(EntityId\)

有効なEntityIdからキーを作成します。

```csharp
public RadialBatchViewKey(EntityId entityId)
```

#### 引数（Parameters）

`entityId` EntityId

Camera等のUnity Objectを表すEntityId。無効値なら無効キーになります。

### <a id="Omni_BatchRendering_RadialBatchViewKey__ctor_System_UInt64_"></a> RadialBatchViewKey\(ulong\)

テスト・IPC向けに既知の64bit値からキーを作成します。

```csharp
public RadialBatchViewKey(ulong value)
```

#### 引数（Parameters）

`value` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

EntityId.ToULongで取得した値。0は無効キーです。

## プロパティ（Properties）

### <a id="Omni_BatchRendering_RadialBatchViewKey_IsValid"></a> IsValid

キーが有効なUnity Entityを表すかを返します。

```csharp
public bool IsValid { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialBatchViewKey_Value"></a> Value

BRG viewを一意に表す生のEntityId値です。

```csharp
public ulong Value { get; }
```

#### 値（Property Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

## メソッド（Methods）

### <a id="Omni_BatchRendering_RadialBatchViewKey_Equals_Omni_BatchRendering_RadialBatchViewKey_"></a> Equals\(RadialBatchViewKey\)

```csharp
public bool Equals(RadialBatchViewKey other)
```

#### 引数（Parameters）

`other` [RadialBatchViewKey](Omni.BatchRendering.RadialBatchViewKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialBatchViewKey_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialBatchViewKey_FromCamera_UnityEngine_Camera_"></a> FromCamera\(Camera\)

Cameraコンポーネントから同じviewキーを作成します。

```csharp
public static RadialBatchViewKey FromCamera(Camera camera)
```

#### 引数（Parameters）

`camera` Camera

SaturnシーンでBRGを描画するCamera。nullなら無効キーを返します。

#### 戻り値（Returns）

 [RadialBatchViewKey](Omni.BatchRendering.RadialBatchViewKey.md)

### <a id="Omni_BatchRendering_RadialBatchViewKey_FromCullingContext_UnityEngine_Rendering_BatchCullingContext__"></a> FromCullingContext\(in BatchCullingContext\)

BRG callbackのviewIDからキーを作成します。

```csharp
public static RadialBatchViewKey FromCullingContext(in BatchCullingContext cullingContext)
```

#### 引数（Parameters）

`cullingContext` BatchCullingContext

Unityが現在のCamera culling用に渡す読み取り専用コンテキストです。

#### 戻り値（Returns）

 [RadialBatchViewKey](Omni.BatchRendering.RadialBatchViewKey.md)

### <a id="Omni_BatchRendering_RadialBatchViewKey_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## 演算子（Operators）

### <a id="Omni_BatchRendering_RadialBatchViewKey_op_Equality_Omni_BatchRendering_RadialBatchViewKey_Omni_BatchRendering_RadialBatchViewKey_"></a> operator ==\(RadialBatchViewKey, RadialBatchViewKey\)

2つのviewキーが同じCamera/Scene viewを表すかを比較します。

```csharp
public static bool operator ==(RadialBatchViewKey left, RadialBatchViewKey right)
```

#### 引数（Parameters）

`left` [RadialBatchViewKey](Omni.BatchRendering.RadialBatchViewKey.md)

`right` [RadialBatchViewKey](Omni.BatchRendering.RadialBatchViewKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialBatchViewKey_op_Inequality_Omni_BatchRendering_RadialBatchViewKey_Omni_BatchRendering_RadialBatchViewKey_"></a> operator \!=\(RadialBatchViewKey, RadialBatchViewKey\)

2つのviewキーが異なるCamera/Scene viewを表すかを比較します。

```csharp
public static bool operator !=(RadialBatchViewKey left, RadialBatchViewKey right)
```

#### 引数（Parameters）

`left` [RadialBatchViewKey](Omni.BatchRendering.RadialBatchViewKey.md)

`right` [RadialBatchViewKey](Omni.BatchRendering.RadialBatchViewKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
