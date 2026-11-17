# <a id="Omni_Converter_VfxGraphAuthoring"></a> Class VfxGraphAuthoring

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

VFX Graph の資産（<code>.vfx</code>）を、コードから空の状態で組み立て直します（Editor 専用）。

<p>
流れ: 空のグラフの YAML を書く → 取り込む → グラフを空にする → <xref href="Omni.Converter.VfxGraphBuilder" data-throw-if-not-resolved="false"></xref> で組む → 書き出す → 取り込み直す。
既存の <code>.vfx</code> は <code>.meta</code>（GUID）を保ったまま上書きするので、Scene や Profile の参照は変わりません。
取り込みのたびに <xref href="Omni.Converter.RadialVfxImportHook" data-throw-if-not-resolved="false"></xref> が表示用シェーダーへ Radial のパッチを当てます。
</p>
<p>
VFX Graph の編集 API は internal なので反射で使います。型やメンバーが見つからない版では、組み立てを始める前に
<xref href="Omni.Converter.VfxGraphAuthoring.CheckEnvironment(System.String%40)" data-throw-if-not-resolved="false"></xref> が理由を返し、<xref href="Omni.Converter.VfxGraphAuthoring.Author(System.String%2cSystem.Action%7bOmni.Converter.VfxGraphBuilder%7d%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref> は例外で止めます（途中まで作った資産を残しません）。
組み立ての途中で設定名や slot が見つからないときも、名前と候補を含む例外で止めます。
</p>

```csharp
public static class VfxGraphAuthoring
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VfxGraphAuthoring](Omni.Converter.VfxGraphAuthoring.md)

## メソッド（Methods）

### <a id="Omni_Converter_VfxGraphAuthoring_Author_System_String_System_Action_Omni_Converter_VfxGraphBuilder__System_Boolean_"></a> Author\(string, Action<VfxGraphBuilder\>, bool\)

<code class="paramref">path</code> の <code>.vfx</code> を空から組み立て直し、取り込んだ資産を返します。
<code class="paramref">requireExistingGuid</code> が true なら、<code>.meta</code> が無いときは作らずに止めます
（Scene や Profile が参照している資産の GUID を新しくしないため）。

```csharp
public static VisualEffectAsset Author(string path, Action<VfxGraphBuilder> build, bool requireExistingGuid = false)
```

#### 引数（Parameters）

`path` [string](https://learn.microsoft.com/dotnet/api/system.string)

`build` [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<[VfxGraphBuilder](Omni.Converter.VfxGraphBuilder.md)\>

`requireExistingGuid` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 VisualEffectAsset

### <a id="Omni_Converter_VfxGraphAuthoring_CheckEnvironment_System_String__"></a> CheckEnvironment\(out string\)

この Editor の VFX Graph で、組み立てに必要な internal の型とメソッドが揃っているか。

```csharp
public static bool CheckEnvironment(out string reason)
```

#### 引数（Parameters）

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_VfxGraphAuthoring_RequireExposedProperties_UnityEngine_VFX_VisualEffectAsset_System_ValueTuple_System_String_System_Type____"></a> RequireExposedProperties\(VisualEffectAsset, params \(string Name, Type Type\)\[\]\)

資産が公開プロパティを持つことを確かめます（無ければ例外）。型が null の項目は名前だけを確かめます。
型は互換なら一致とみなします（VFX Graph はテクスチャを基底の <xref href="UnityEngine.Texture" data-throw-if-not-resolved="false"></xref> で報告します）。

```csharp
public static void RequireExposedProperties(VisualEffectAsset asset, params (string Name, Type Type)[] properties)
```

#### 引数（Parameters）

`asset` VisualEffectAsset

`properties` \([string](https://learn.microsoft.com/dotnet/api/system.string) [Name](https://learn.microsoft.com/dotnet/api/system.valuetuple\-system.string,system.type\-.name), [Type](https://learn.microsoft.com/dotnet/api/system.type) [Type](https://learn.microsoft.com/dotnet/api/system.valuetuple\-system.string,system.type\-.type)\)\[\]
