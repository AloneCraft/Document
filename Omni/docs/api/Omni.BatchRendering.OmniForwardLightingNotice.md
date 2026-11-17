# <a id="Omni_BatchRendering_OmniForwardLightingNotice"></a> Class OmniForwardLightingNotice

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

URP の Forward の Renderer で描いているとき、Scene BRG（一括描画）を止めて通常の描画へ戻している理由を、利用者へ知らせる文言です。
デモの HUD と Omni Manager が使います。

```csharp
public static class OmniForwardLightingNotice
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniForwardLightingNotice](Omni.BatchRendering.OmniForwardLightingNotice.md)

## 補足（Remarks）

理由は Omni 固有ではなく、標準の URP の制限です（検証 Scene <code>Functions/Lighting/ForwardLightingPaths.unity</code> で、
Omni を通さない素の BatchRendererGroup でも同じ結果になることを確かめてあります）。
Forward は点光源・スポットライトとその影を物体ごとのライト一覧で渡しますが、BRG の物体にはその一覧が無いため、
Forward では BRG の物体にメインライトしか当たりません。Forward+ は一覧を使わないので影響を受けません。

## フィールド（Fields）

### <a id="Omni_BatchRendering_OmniForwardLightingNotice_English"></a> English

```csharp
public const string English = "Renderer note: this camera uses URP Forward. In Forward, Unity cannot give point/spot lights and their shadows to batched (BRG) objects, so Omni draws the normal way instead. Reflection and light probe picking can differ from standard. Use Forward+ for the batched path."
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_BatchRendering_OmniForwardLightingNotice_Japanese"></a> Japanese

```csharp
public const string Japanese = "描画の注記: このカメラは URP の Forward を使っています。Forward では、Unity が点光源・スポットライトとその影を一括描画（BRG）の物体へ渡せないため、Omni は通常の描画に切り替えています。反射や Light Probe の選び方は標準とずれることがあります。一括描画を使うには Forward+ にしてください。"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_BatchRendering_OmniForwardLightingNotice_IsActive"></a> IsActive

Scene BRG が URP Forward の Camera のために止まっている間 true です。

```csharp
public static bool IsActive { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_BatchRendering_OmniForwardLightingNotice_Text_System_Boolean_"></a> Text\(bool\)

指定した言語の説明文です。

```csharp
public static string Text(bool japanese)
```

#### 引数（Parameters）

`japanese` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_BatchRendering_OmniForwardLightingNotice_Text"></a> Text\(\)

Omni の表示言語（Editor は Editor の言語、Player は OS の言語、Web は英語）の説明文です。

```csharp
public static string Text()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
