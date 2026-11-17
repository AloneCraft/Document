# <a id="Omni_OmniVirtualShadowStatistics"></a> Struct OmniVirtualShadowStatistics

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

仮想シャドウマップの 1 フレームの状態(診断用)。

```csharp
public readonly struct OmniVirtualShadowStatistics
```

## コンストラクター（Constructors）

### <a id="Omni_OmniVirtualShadowStatistics__ctor_System_Int32_System_Int32_System_Int32_System_Int32_System_Boolean_UnityEngine_Vector3_UnityEngine_Vector3_System_Int32_System_String_System_Int32_System_Int32_"></a> OmniVirtualShadowStatistics\(int, int, int, int, bool, Vector3, Vector3, int, string, int, int\)

```csharp
public OmniVirtualShadowStatistics(int used, int requested, int rendered, int pending, bool hasCull, Vector3 anchor = default, Vector3 cameraPosition = default, int levelBias = 0, string requestedByLevel = null, int tiles = 0, int dynamicStale = 0)
```

#### 引数（Parameters）

`used` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`requested` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`rendered` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`pending` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`hasCull` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`anchor` Vector3

`cameraPosition` Vector3

`levelBias` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`requestedByLevel` [string](https://learn.microsoft.com/dotnet/api/system.string)

`tiles` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`dynamicStale` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## フィールド（Fields）

### <a id="Omni_OmniVirtualShadowStatistics_Anchor"></a> Anchor

段の基準点(カメラの Unity の座標)と、URP のカメラの位置。

```csharp
public readonly Vector3 Anchor
```

#### 値（Field Value）

 Vector3

### <a id="Omni_OmniVirtualShadowStatistics_CameraPosition"></a> CameraPosition

段の基準点(カメラの Unity の座標)と、URP のカメラの位置。

```csharp
public readonly Vector3 CameraPosition
```

#### 値（Field Value）

 Vector3

### <a id="Omni_OmniVirtualShadowStatistics_DynamicStalePages"></a> DynamicStalePages

動く物のために「古い」にしたページの累計。

```csharp
public readonly int DynamicStalePages
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowStatistics_FrameMs"></a> FrameMs

前のフレームからの経過時間(ms)。

```csharp
public readonly float FrameMs
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_OmniVirtualShadowStatistics_HasCasterCulling"></a> HasCasterCulling

```csharp
public readonly bool HasCasterCulling
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_OmniVirtualShadowStatistics_LevelBias"></a> LevelBias

置き場が足りないために粗くしている段の数。

```csharp
public readonly int LevelBias
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowStatistics_PendingPages"></a> PendingPages

```csharp
public readonly int PendingPages
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowStatistics_RenderedPages"></a> RenderedPages

```csharp
public readonly int RenderedPages
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowStatistics_RequestedByLevel"></a> RequestedByLevel

要求されたページの段ごとの数(診断用)。

```csharp
public readonly string RequestedByLevel
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_OmniVirtualShadowStatistics_RequestedPages"></a> RequestedPages

```csharp
public readonly int RequestedPages
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowStatistics_Tiles"></a> Tiles

このフレームに描いたタイル(影を落とす物を描いた回数)。

```csharp
public readonly int Tiles
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_OmniVirtualShadowStatistics_UsedPages"></a> UsedPages

```csharp
public readonly int UsedPages
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_OmniVirtualShadowStatistics_ToString"></a> ToString\(\)

```csharp
public override string ToString()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
