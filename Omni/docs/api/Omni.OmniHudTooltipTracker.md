# <a id="Omni_OmniHudTooltipTracker"></a> Class OmniHudTooltipTracker

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

説明を出す・消すタイミング。ホバーした説明の文字（空なら無し）と時刻を渡し、<xref href="Omni.OmniHudTooltipTracker.Tick(System.Single)" data-throw-if-not-resolved="false"></xref> で今出すべきかを得る。
説明の無い所から有る所へ入ると遅れ後に出る。出ている間に別の説明へ移ると、遅れなしですぐ切り替わる。押した後は、その要素を離れるまで出さない。

```csharp
public sealed class OmniHudTooltipTracker
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniHudTooltipTracker](Omni.OmniHudTooltipTracker.md)

## コンストラクター（Constructors）

### <a id="Omni_OmniHudTooltipTracker__ctor_System_Single_"></a> OmniHudTooltipTracker\(float\)

```csharp
public OmniHudTooltipTracker(float delaySeconds = 0.35)
```

#### 引数（Parameters）

`delaySeconds` [float](https://learn.microsoft.com/dotnet/api/system.single)

## プロパティ（Properties）

### <a id="Omni_OmniHudTooltipTracker_DelaySeconds"></a> DelaySeconds

```csharp
public float DelaySeconds { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_OmniHudTooltipTracker_Text"></a> Text

```csharp
public string Text { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_OmniHudTooltipTracker_Visible"></a> Visible

```csharp
public bool Visible { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_OmniHudTooltipTracker_Clear"></a> Clear\(\)

ポインタが説明の無い所へ移った、または UI の外へ出た。

```csharp
public void Clear()
```

### <a id="Omni_OmniHudTooltipTracker_Hover_System_String_System_Single_"></a> Hover\(string, float\)

ポインタの下の説明（無ければ null か空）を伝える。

```csharp
public void Hover(string text, float now)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

`now` [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_OmniHudTooltipTracker_Suppress"></a> Suppress\(\)

押された、スクロールされた、など。説明を消し、ポインタが別の所へ移るまで出さない。

```csharp
public void Suppress()
```

### <a id="Omni_OmniHudTooltipTracker_Tick_System_Single_"></a> Tick\(float\)

今出すべきなら true。

```csharp
public bool Tick(float now)
```

#### 引数（Parameters）

`now` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
