# <a id="Omni_RadialWarpSource"></a> Struct RadialWarpSource

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

あるカメラのワープ元（<xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref>）と、それを適用してよい範囲を
まとめて表します。

<p>
適用範囲を <code>ApplyCullingMatrixOverride</code> と <code>ApplyShellCulling</code> の
2 段に分けているのは、両者の安全性がまったく違うためです。
<code>camera.cullingMatrix</code> は Unity がカメラごとに保持するプロパティなので、
ワープ中心が描画中カメラ自身の位置と一致してさえいれば、誰が上書きしても
他のカメラには影響しません。一方 <code>Renderer.forceRenderingOff</code> は
カメラに紐付かないグローバルなフラグで、「1 フレーム内でカメラは順次描画され、
同時にアクティブなのは 1 台」という前提の上でしか安全に使えません
（<xref href="Omni.RadialCullingSystem" data-throw-if-not-resolved="false"></xref> 参照）。Play モード中は Game カメラと
Scene View が同一フレーム内で両方描画されるためこの前提が崩れるので、
シェルカリングだけは「権限を持つカメラ」に限定します。
</p>
<p>
<code>ApplyShellCulling</code> は <code>ApplyCullingMatrixOverride</code> の部分集合です
（シェルカリングを適用してよいなら cullingMatrix の上書きも必ず妥当）。
呼び出し側が矛盾した組み合わせを作れないよう、生成はファクトリメソッド経由に限定しています。
</p>

```csharp
public readonly struct RadialWarpSource
```

## フィールド（Fields）

### <a id="Omni_RadialWarpSource_ApplyConservativeObserverCulling"></a> ApplyConservativeObserverCulling

```csharp
public readonly bool ApplyConservativeObserverCulling
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialWarpSource_ApplyCullingMatrixOverride"></a> ApplyCullingMatrixOverride

```csharp
public readonly bool ApplyCullingMatrixOverride
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialWarpSource_ApplyShellCulling"></a> ApplyShellCulling

```csharp
public readonly bool ApplyShellCulling
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialWarpSource_Driver"></a> Driver

```csharp
public readonly RadialCamera Driver
```

#### 値（Field Value）

 [RadialCamera](Omni.RadialCamera.md)

### <a id="Omni_RadialWarpSource_IncludeUnwarpedCullingVolume"></a> IncludeUnwarpedCullingVolume

Observerカリングを使う場合に通常視錘台も含めるかどうかです。
外部Observerではfalseにして余分なRenderer候補を抑えます。Scene Viewの基準カメラ
比較ではObserverカリング自体を無効化するため、この値は描画に影響しません。

```csharp
public readonly bool IncludeUnwarpedCullingVolume
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialWarpSource_IsSelfCentered"></a> IsSelfCentered

```csharp
public readonly bool IsSelfCentered
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialWarpSource_None"></a> None

ワープ元が無い状態です。呼び出し側は恒等（ワープ無効）として扱います。

```csharp
public static readonly RadialWarpSource None
```

#### 値（Field Value）

 [RadialWarpSource](Omni.RadialWarpSource.md)

## プロパティ（Properties）

### <a id="Omni_RadialWarpSource_HasDriver"></a> HasDriver

ドライバが有効かどうかです。無効なドライバは恒等として扱われます。

```csharp
public bool HasDriver { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_RadialWarpSource_Observer_Omni_RadialCamera_System_Boolean_"></a> Observer\(RadialCamera, bool\)

基準カメラを切り替えて別カメラの <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> を借りる経路です。
外部観察カメラでは位置が一致する場合にOwnerと同じnear/far補正を使い、異なる場合は
保守的な逆写像ボリュームを使います。Scene Viewの基準カメラ比較では、描画欠落を
避けるためRenderSystem側がObserverカリングをfail-openへ切り替えます。
シェルカリングは複数カメラへの影響を避けるためObserverでは適用しません。

```csharp
public static RadialWarpSource Observer(RadialCamera driver, bool includeUnwarpedCullingVolume = false)
```

#### 引数（Parameters）

`driver` [RadialCamera](Omni.RadialCamera.md)

`includeUnwarpedCullingVolume` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

通常の非ワープ視錘台も保守的なカリング範囲へ含めるかどうかです。
Scene View比較用の通常視錘台を含める値としてtrue、外部Observerではfalseにします。

#### 戻り値（Returns）

 [RadialWarpSource](Omni.RadialWarpSource.md)

### <a id="Omni_RadialWarpSource_Owner_Omni_RadialCamera_"></a> Owner\(RadialCamera\)

描画中カメラ自身がワープ中心の実カメラです（Game カメラ本来の経路）。
ワープ中心＝自分の位置なので、cullingMatrix・シェルカリングの両方を適用してよい。

```csharp
public static RadialWarpSource Owner(RadialCamera driver)
```

#### 引数（Parameters）

`driver` [RadialCamera](Omni.RadialCamera.md)

#### 戻り値（Returns）

 [RadialWarpSource](Omni.RadialWarpSource.md)

### <a id="Omni_RadialWarpSource_SelfCentered_Omni_RadialCamera_System_Boolean_"></a> SelfCentered\(RadialCamera, bool\)

Scene View カメラ自身が中心のときの経路です。ワープ中心＝描画中カメラ自身の位置なので
cullingMatrix の上書きは妥当ですが、シェルカリングは Play モード中は Game カメラへ譲る
必要があるため、呼び出し側から権限の有無を渡してもらいます。

```csharp
public static RadialWarpSource SelfCentered(RadialCamera driver, bool applyShellCulling)
```

#### 引数（Parameters）

`driver` [RadialCamera](Omni.RadialCamera.md)

`applyShellCulling` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [RadialWarpSource](Omni.RadialWarpSource.md)
