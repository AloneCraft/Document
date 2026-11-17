# <a id="Omni_Editor_Diagnostics_OmniSceneViewCapture"></a> Class OmniSceneViewCapture

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

対象Scene Viewカメラの実GPUカラー出力をPNGへ保存する診断用キャプチャです。
OS画面座標は使用しないため、別ウィンドウが前面でも誤った画像を成功扱いしません。

```csharp
[InitializeOnLoad]
public static class OmniSceneViewCapture
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniSceneViewCapture](Omni.Editor.Diagnostics.OmniSceneViewCapture.md)

## メソッド（Methods）

### <a id="Omni_Editor_Diagnostics_OmniSceneViewCapture_Begin_System_String_System_Action_System_Boolean_System_String__"></a> Begin\(string, Action<bool, string\>\)

Scene Viewの再描画を待ち、対象カメラのGPU出力をPNGへ保存します。

```csharp
public static void Begin(string outputPath, Action<bool, string> completion)
```

#### 引数（Parameters）

`outputPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`completion` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_Diagnostics_OmniSceneViewCapture_Compare_System_String_System_String_"></a> Compare\(string, string\)

2枚のPNGをRGBAの各channel差分2/255超で比較し、差分率を返します。
Scene Viewの固定カメラ画像回帰で、閾値を超える画素を可視化するための診断用APIです。

```csharp
public static string Compare(string expectedPath, string actualPath)
```

#### 引数（Parameters）

`expectedPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`actualPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniSceneViewCapture_CompareWithTargetMask_System_String_System_String_System_String_"></a> CompareWithTargetMask\(string, string, string\)

<xref href="Omni.Editor.Diagnostics.OmniSceneViewCapture.Compare(System.String%2cSystem.String)" data-throw-if-not-resolved="false"></xref> に、比較の対象を示す mask を加えた比較型の観測です。mask は expected・actual と同じ
大きさの PNG で、RGB の最大が 128 以上の画素（白）を対象とします。差分率は mask の中の画素だけで数えます
（mask の中の画素数に対する、RGBA のいずれかが 2/255 を超えて違う画素の割合が 0.01% 以下なら合格）。
前提は比較の参照（expected）だけで判定します。mask が空（<xref href="Omni.Editor.Diagnostics.OmniObservationReason.ForegroundPixelsZero" data-throw-if-not-resolved="false"></xref>）
か、expected の mask の中がすべて背景色（<xref href="Omni.Editor.Diagnostics.OmniObservationReason.BackgroundOnly" data-throw-if-not-resolved="false"></xref>）なら、比較する
対象が無いので計測の合否によらず Unavailable です。背景色は expected の mask の外で最も多い色（mask の外が
無ければ画像全体で最も多い色）です。actual の mask の中が背景だけになったこと（対象が描画されない）は前提の
崩れではなく計測の結果なので、差分のとおり Failed になります（補足に actual の背景以外の画素数を載せます）。

```csharp
public static OmniObservationReport CompareWithTargetMask(string expectedPath, string actualPath, string targetMaskPath)
```

#### 引数（Parameters）

`expectedPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

期待画像の PNG の絶対パスです。

`actualPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

実際の画像の PNG の絶対パスです。

`targetMaskPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

比較の対象の mask の PNG の絶対パスです。

#### 戻り値（Returns）

 [OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)

本文（detail）に比較の結果を持つ観測の報告です。

#### 例外（Exceptions）

 [InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)

PNG を読めない、または mask の大きさが画像と違う場合。
