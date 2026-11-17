# <a id="Omni_Logical_OmniCullingRange"></a> Struct OmniCullingRange

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

第1層が実際に使ったカリング範囲です。描画空間のnear/farと、それを逆写像した実距離を
並べて持ちます。「実距離の下限が跳ね上がって手前を全部刈っている」ような状態を
数値で読めるようにするためのものです。

```csharp
public readonly struct OmniCullingRange
```

## フィールド（Fields）

### <a id="Omni_Logical_OmniCullingRange_CullFar"></a> CullFar

カリングに使った実距離の上限です。

```csharp
public readonly float CullFar
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Logical_OmniCullingRange_CullNear"></a> CullNear

カリングに使った実距離の下限です。

```csharp
public readonly float CullNear
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Logical_OmniCullingRange_RenderFar"></a> RenderFar

カメラの描画far clipです。

```csharp
public readonly float RenderFar
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Logical_OmniCullingRange_RenderNear"></a> RenderNear

カメラの描画near clipです。

```csharp
public readonly float RenderNear
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Logical_OmniCullingRange_UnmapFailed"></a> UnmapFailed

逆写像に失敗して実質カリング無しの範囲へ倒した場合はtrueです。

```csharp
public readonly bool UnmapFailed
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
