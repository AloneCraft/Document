# <a id="Omni_Converter_RadialSceneState"></a> Struct RadialSceneState

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

シーンの「Radial マテリアル適用状態」を<b>シーンの実データから</b>数えた結果です。

<p>
以前は UI 側の非シリアライズ bool 1 個で適用状態を覚えていたため、
ドメインリロードのたびに「元に戻す」ボタンが押せなくなり、
同時に一覧も 0 件になって「放射マテリアル」も押せない、という詰みが起きていました。
状態は毎回シーンから数え直すこと。覚えないのが正解です。
</p>

```csharp
public struct RadialSceneState
```

## フィールド（Fields）

### <a id="Omni_Converter_RadialSceneState_ApplicableSlots"></a> ApplicableSlots

生成物を持つ元マテリアルを指しているスロット数（＝適用できる）。

```csharp
public int ApplicableSlots
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_RadialSceneState_AppliedSlots"></a> AppliedSlots

生成マテリアルを指しており、かつ実際に Radial ワープ注入済みのシェーダーを
    参照しているスロット数。

```csharp
public int AppliedSlots
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_RadialSceneState_DiagnosticMaterials"></a> DiagnosticMaterials

そのスロットが参照する管理診断Materialの数（重複なし）。変換できなかった元Materialの数と同じです
（元Material 1つにつき管理診断Materialは1つ）。1つのMaterialを複数のRendererが使うと
<xref href="Omni.Converter.RadialSceneState.DiagnosticSlots" data-throw-if-not-resolved="false"></xref> より少なくなります。

```csharp
public int DiagnosticMaterials
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_RadialSceneState_DiagnosticSlots"></a> DiagnosticSlots

変換不能を可視化する管理診断Materialを参照しているスロット数。

```csharp
public int DiagnosticSlots
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_RadialSceneState_ManagedVfxRuntimeSlots"></a> ManagedVfxRuntimeSlots

Omniが管理するVFX Graphの非AssetランタイムMaterialスロット数。

```csharp
public int ManagedVfxRuntimeSlots
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_RadialSceneState_NativeRadialSlots"></a> NativeRadialSlots

生成物ではなく、対数契約を直接実装したShader（RenderObjectsのoverrideに使う
<code>Custom/StencilOnly</code> 等）のスロット数。標準版を持たず、RadialCameraの有無に
かかわらず正しく描けるので、適用済み（標準へ戻す対象）には数えません。数えると、
これを使うSceneは標準レンダリングへ切り替えられなくなります（Terminal等で発生）。
Manager上は「Omni 対応済（ネイティブ）」として表示し、ヘッダーの対応済み数にだけ含め、
切替の有無の判定（<code>HasSwitchTargets</code>）にも使います（UB-009）。復元の対象にはなりません。

```csharp
public int NativeRadialSlots
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_RadialSceneState_RevertibleSlots"></a> RevertibleSlots

そのうち、元マテリアルを解決できたスロット数。

```csharp
public int RevertibleSlots
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_RadialSceneState_StandardSlots"></a> StandardSlots

Radial未適用の永続Materialで、現在は標準描画として残るスロット数。

```csharp
public int StandardSlots
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_RadialSceneState_UnknownRuntimeSlots"></a> UnknownRuntimeSlots

所有者を証明できない非AssetランタイムMaterialスロット数。

```csharp
public int UnknownRuntimeSlots
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_RadialSceneState_Unreliable"></a> Unreliable

描画中のランタイムインスタンスを掴んだ等、走査が信用できない場合。

```csharp
public bool Unreliable
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_RadialSceneState_Unresolved"></a> Unresolved

解決できなかったスロットの説明。

```csharp
public List<string> Unresolved
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_RadialSceneState_UnwarpedSlots"></a> UnwarpedSlots

生成マテリアルを指しているが、割り当てシェーダーが Radial 注入済みではない
    スロット数。<xref href="Omni.Converter.RadialSourceResolver.IsRadialInjected(UnityEngine.Material)" data-throw-if-not-resolved="false"></xref> のコメント参照。

```csharp
public int UnwarpedSlots
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_RadialSceneState_Vfx"></a> Vfx

現在のSceneで必要なVFX presentation backendの状態。

```csharp
public RadialVfxSceneState Vfx
```

#### 値（Field Value）

 [RadialVfxSceneState](Omni.Converter.RadialVfxSceneState.md)
