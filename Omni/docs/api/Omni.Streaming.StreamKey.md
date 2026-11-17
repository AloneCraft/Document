# <a id="Omni_Streaming_StreamKey"></a> Struct StreamKey

Namespace: [Omni.Streaming](Omni.Streaming.md)  
Assembly: Omni.Streaming.Core.dll  

ストリーミングするデータの論理キー(どこ)。層(高さ・色などの種類)+ 空間キー(面・階層・格子番号)。
空間キーは四分木の1マス: 面 Face、階層 Level(0〜<xref href="Omni.Streaming.StreamKey.MaximumLevel" data-throw-if-not-resolved="false"></xref>)、格子番号 X・Y(0〜2^Level−1)。
面の番号の意味は利用者が決める(VG の地形は、球が cube-sphere の 0〜5、平面が 2 を使い、そのまま写す)。階層が 31 を超える Cell は表せない(<xref href="Omni.Streaming.StreamKey.TryChild(System.Int32%2cOmni.Streaming.StreamKey%40)" data-throw-if-not-resolved="false"></xref> が false を返す)。
中身(何)を指す <xref href="Omni.Streaming.ContentId" data-throw-if-not-resolved="false"></xref> とは別: 同じ中身を複数のキーが共有できる。

```csharp
public readonly struct StreamKey : IEquatable<StreamKey>, IComparable<StreamKey>
```

#### 実装するインターフェース（Implements）

[IEquatable<StreamKey\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1), 
[IComparable<StreamKey\>](https://learn.microsoft.com/dotnet/api/system.icomparable\-1)

## コンストラクター（Constructors）

### <a id="Omni_Streaming_StreamKey__ctor_System_UInt32_System_Int32_System_Int32_System_UInt32_System_UInt32_"></a> StreamKey\(uint, int, int, uint, uint\)

```csharp
public StreamKey(uint layer, int face, int level, uint x, uint y)
```

#### 引数（Parameters）

`layer` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`face` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`x` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`y` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## フィールド（Fields）

### <a id="Omni_Streaming_StreamKey_Face"></a> Face

```csharp
public readonly byte Face
```

#### 値（Field Value）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)

### <a id="Omni_Streaming_StreamKey_Layer"></a> Layer

```csharp
public readonly uint Layer
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_Streaming_StreamKey_Level"></a> Level

```csharp
public readonly byte Level
```

#### 値（Field Value）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)

### <a id="Omni_Streaming_StreamKey_MaximumLevel"></a> MaximumLevel

```csharp
public const int MaximumLevel = 31
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_StreamKey_X"></a> X

```csharp
public readonly uint X
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

### <a id="Omni_Streaming_StreamKey_Y"></a> Y

```csharp
public readonly uint Y
```

#### 値（Field Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

## プロパティ（Properties）

### <a id="Omni_Streaming_StreamKey_ChildIndex"></a> ChildIndex

この階層の親から見て何番目の子か(0〜3)。root は 0。

```csharp
public int ChildIndex { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Streaming_StreamKey_Child_System_Int32_"></a> Child\(int\)

```csharp
public StreamKey Child(int index)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [StreamKey](Omni.Streaming.StreamKey.md)

### <a id="Omni_Streaming_StreamKey_CompareTo_Omni_Streaming_StreamKey_"></a> CompareTo\(StreamKey\)

層・面・階層・Y・X の順(整列と再現性のため。コンテナの並びは <xref href="Omni.Streaming.SpatialOrder" data-throw-if-not-resolved="false"></xref> が決める)。

```csharp
public int CompareTo(StreamKey other)
```

#### 引数（Parameters）

`other` [StreamKey](Omni.Streaming.StreamKey.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_StreamKey_Equals_Omni_Streaming_StreamKey_"></a> Equals\(StreamKey\)

```csharp
public bool Equals(StreamKey other)
```

#### 引数（Parameters）

`other` [StreamKey](Omni.Streaming.StreamKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_StreamKey_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_StreamKey_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Streaming_StreamKey_IsWithin_Omni_Streaming_StreamKey__"></a> IsWithin\(in StreamKey\)

このキーが ancestor の子孫(または同じ)か。層と面が同じで、階層が深く、格子番号が祖先の範囲に入る。

```csharp
public bool IsWithin(in StreamKey ancestor)
```

#### 引数（Parameters）

`ancestor` [StreamKey](Omni.Streaming.StreamKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_StreamKey_Root_System_UInt32_System_Int32_"></a> Root\(uint, int\)

```csharp
public static StreamKey Root(uint layer, int face)
```

#### 引数（Parameters）

`layer` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`face` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [StreamKey](Omni.Streaming.StreamKey.md)

### <a id="Omni_Streaming_StreamKey_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Streaming_StreamKey_TryChild_System_Int32_Omni_Streaming_StreamKey__"></a> TryChild\(int, out StreamKey\)

子(index は 0〜3。bit0 が x、bit1 が y)。階層が上限なら false。

```csharp
public bool TryChild(int index, out StreamKey child)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`child` [StreamKey](Omni.Streaming.StreamKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_StreamKey_TryParent_Omni_Streaming_StreamKey__"></a> TryParent\(out StreamKey\)

```csharp
public bool TryParent(out StreamKey parent)
```

#### 引数（Parameters）

`parent` [StreamKey](Omni.Streaming.StreamKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_StreamKey_WithLayer_System_UInt32_"></a> WithLayer\(uint\)

同じ面・階層・格子で、層だけ違うキー。

```csharp
public StreamKey WithLayer(uint layer)
```

#### 引数（Parameters）

`layer` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

#### 戻り値（Returns）

 [StreamKey](Omni.Streaming.StreamKey.md)

## 演算子（Operators）

### <a id="Omni_Streaming_StreamKey_op_Equality_Omni_Streaming_StreamKey_Omni_Streaming_StreamKey_"></a> operator ==\(StreamKey, StreamKey\)

```csharp
public static bool operator ==(StreamKey a, StreamKey b)
```

#### 引数（Parameters）

`a` [StreamKey](Omni.Streaming.StreamKey.md)

`b` [StreamKey](Omni.Streaming.StreamKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Streaming_StreamKey_op_Inequality_Omni_Streaming_StreamKey_Omni_Streaming_StreamKey_"></a> operator \!=\(StreamKey, StreamKey\)

```csharp
public static bool operator !=(StreamKey a, StreamKey b)
```

#### 引数（Parameters）

`a` [StreamKey](Omni.Streaming.StreamKey.md)

`b` [StreamKey](Omni.Streaming.StreamKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
