# <a id="Omni_BatchRendering_RadialBatchInstanceHandle"></a> Struct RadialBatchInstanceHandle

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

ランタイム生成したMeshRendererをScene BRGへ登録した結果です。
Garden/OasisなどのScene Meshを、再利用されたslotの古い参照から保護するためgenerationを持ちます。

```csharp
public readonly struct RadialBatchInstanceHandle : IEquatable<RadialBatchInstanceHandle>
```

#### 実装するインターフェース（Implements）

[IEquatable<RadialBatchInstanceHandle\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## コンストラクター（Constructors）

### <a id="Omni_BatchRendering_RadialBatchInstanceHandle__ctor_System_Int32_System_UInt32_"></a> RadialBatchInstanceHandle\(int, uint\)

登録slotと世代番号からHandleを作成します。

```csharp
public RadialBatchInstanceHandle(int index, uint generation)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

Scene backend内の0始まりslotです。負数は無効です。

`generation` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

slot再利用ごとに増える世代です。0は無効です。

## プロパティ（Properties）

### <a id="Omni_BatchRendering_RadialBatchInstanceHandle_Generation"></a> Generation

slotの再利用を区別する世代番号です。

```csharp
public uint Generation { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_BatchRendering_RadialBatchInstanceHandle_Index"></a> Index

Scene backend内のslotです。

```csharp
public int Index { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialBatchInstanceHandle_IsValid"></a> IsValid

現在のbackendへ問い合わせ可能な形式かを返します。

```csharp
public bool IsValid { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_BatchRendering_RadialBatchInstanceHandle_Equals_Omni_BatchRendering_RadialBatchInstanceHandle_"></a> Equals\(RadialBatchInstanceHandle\)

```csharp
public bool Equals(RadialBatchInstanceHandle other)
```

#### 引数（Parameters）

`other` [RadialBatchInstanceHandle](Omni.BatchRendering.RadialBatchInstanceHandle.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialBatchInstanceHandle_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialBatchInstanceHandle_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## 演算子（Operators）

### <a id="Omni_BatchRendering_RadialBatchInstanceHandle_op_Equality_Omni_BatchRendering_RadialBatchInstanceHandle_Omni_BatchRendering_RadialBatchInstanceHandle_"></a> operator ==\(RadialBatchInstanceHandle, RadialBatchInstanceHandle\)

2つのHandleが同じslot世代を指すかを返します。

```csharp
public static bool operator ==(RadialBatchInstanceHandle left, RadialBatchInstanceHandle right)
```

#### 引数（Parameters）

`left` [RadialBatchInstanceHandle](Omni.BatchRendering.RadialBatchInstanceHandle.md)

`right` [RadialBatchInstanceHandle](Omni.BatchRendering.RadialBatchInstanceHandle.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_BatchRendering_RadialBatchInstanceHandle_op_Inequality_Omni_BatchRendering_RadialBatchInstanceHandle_Omni_BatchRendering_RadialBatchInstanceHandle_"></a> operator \!=\(RadialBatchInstanceHandle, RadialBatchInstanceHandle\)

2つのHandleが異なるslot世代を指すかを返します。

```csharp
public static bool operator !=(RadialBatchInstanceHandle left, RadialBatchInstanceHandle right)
```

#### 引数（Parameters）

`left` [RadialBatchInstanceHandle](Omni.BatchRendering.RadialBatchInstanceHandle.md)

`right` [RadialBatchInstanceHandle](Omni.BatchRendering.RadialBatchInstanceHandle.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
