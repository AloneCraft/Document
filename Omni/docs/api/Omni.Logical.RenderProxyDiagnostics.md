# <a id="Omni_Logical_RenderProxyDiagnostics"></a> Struct RenderProxyDiagnostics

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

有限描画プロキシの現在状態です。プロキシは「隠す仕組み」ではなく「描く仕組み」なので、
対象が見えないときは<b>プロキシが実際に描かれているか</b>を確認する必要があります。

```csharp
public readonly struct RenderProxyDiagnostics
```

## フィールド（Fields）

### <a id="Omni_Logical_RenderProxyDiagnostics_BoundsOverridden"></a> BoundsOverridden

カリング用Boundsの上書きが有効な場合はtrueです。

```csharp
public readonly bool BoundsOverridden
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RenderProxyDiagnostics_CullingBoundsCenter"></a> CullingBoundsCenter

上書きしたカリング用Boundsのワールド中心です。描画カメラの至近にあるはずです。

```csharp
public readonly Vector3 CullingBoundsCenter
```

#### 値（Field Value）

 Vector3

### <a id="Omni_Logical_RenderProxyDiagnostics_LastSynchronizedFrame"></a> LastSynchronizedFrame

カリング用Boundsを同期した最後のフレームです。

```csharp
public readonly int LastSynchronizedFrame
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Logical_RenderProxyDiagnostics_SourceForceRenderingOff"></a> SourceForceRenderingOff

元Rendererを抑制している場合はtrueです。未対応隔離のときだけtrueになります。

```csharp
public readonly bool SourceForceRenderingOff
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_RenderProxyDiagnostics_Unsupported"></a> Unsupported

有限描画経路が未対応として隔離している場合はtrueです。

```csharp
public readonly bool Unsupported
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
