# <a id="Omni_OmniVirtualShadowPageCache_PageKey"></a> Struct OmniVirtualShadowPageCache.PageKey

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

ページの番号(段と Unity の座標に固定した格子の X・Y)。

```csharp
public readonly struct OmniVirtualShadowPageCache.PageKey : IEquatable<OmniVirtualShadowPageCache.PageKey>
```

#### 実装するインターフェース（Implements）

[IEquatable<OmniVirtualShadowPageCache.PageKey\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## コンストラクター（Constructors）

### <a id="Omni_OmniVirtualShadowPageCache_PageKey__ctor_System_Int32_System_Int64_System_Int64_"></a> PageKey\(int, long, long\)

```csharp
public PageKey(int level, long x, long y)
```

#### 引数（Parameters）

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`x` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`y` [long](https://learn.microsoft.com/dotnet/api/system.int64)

## フィールド（Fields）

### <a id="Omni_OmniVirtualShadowPageCache_PageKey_Level"></a> Level

```csharp
public readonly int Level
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowPageCache_PageKey_X"></a> X

```csharp
public readonly long X
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_OmniVirtualShadowPageCache_PageKey_Y"></a> Y

```csharp
public readonly long Y
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="Omni_OmniVirtualShadowPageCache_PageKey_Equals_Omni_OmniVirtualShadowPageCache_PageKey_"></a> Equals\(PageKey\)

```csharp
public bool Equals(OmniVirtualShadowPageCache.PageKey other)
```

#### 引数（Parameters）

`other` [OmniVirtualShadowPageCache](Omni.OmniVirtualShadowPageCache.md).[PageKey](Omni.OmniVirtualShadowPageCache.PageKey.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_OmniVirtualShadowPageCache_PageKey_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_OmniVirtualShadowPageCache_PageKey_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowPageCache_PageKey_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
