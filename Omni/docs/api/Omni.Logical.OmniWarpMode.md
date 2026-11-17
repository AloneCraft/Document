# <a id="Omni_Logical_OmniWarpMode"></a> Struct OmniWarpMode

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

そのフレームにカメラへ適用したワープ経路と、恒等（ワープなし）を選んだ判断材料です。

<p>
「互換性非表示」が跳ね上がるときの原因はほぼ恒等分岐ですが、恒等を選ぶ3条件
（ワープ全体の有効／ワープ元ドライバの解決／平行投影）はどれも描画後に読み直しても
当時の値を復元できません。<xref href="Omni.Logical.OmniCullingDebug.NoteCullingMatrix(UnityEngine.Camera%2cUnityEngine.Matrix4x4%40%2cSystem.String)" data-throw-if-not-resolved="false"></xref> と同じ理由で、
<b>決めた時点で</b>記録します。
</p>

```csharp
public readonly struct OmniWarpMode
```

## フィールド（Fields）

### <a id="Omni_Logical_OmniWarpMode_HasDriver"></a> HasDriver

このカメラのワープ元ドライバを解決できたかどうかです。

```csharp
public readonly bool HasDriver
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_OmniWarpMode_Identity"></a> Identity

恒等（ワープなし）で描いた場合はtrueです。

```csharp
public readonly bool Identity
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_OmniWarpMode_Orthographic"></a> Orthographic

描画カメラが平行投影だったかどうかです。

```csharp
public readonly bool Orthographic
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Logical_OmniWarpMode_WarpEnabled"></a> WarpEnabled

ワープ全体が有効だったかどうかです。

```csharp
public readonly bool WarpEnabled
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
