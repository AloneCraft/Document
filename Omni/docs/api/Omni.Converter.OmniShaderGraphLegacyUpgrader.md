# <a id="Omni_Converter_OmniShaderGraphLegacyUpgrader"></a> Class OmniShaderGraphLegacyUpgrader

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

Shader Graph 10 より前の形式（Master Node の形式。<code>m_SerializedProperties</code> と <code>JSONnodeData</code> を持ち、Target が無い）の Graph を、
Shader Graph の取り込みと同じ方法で今の形式（MultiJson、Target と SubTarget）へ上げます。

<p>
Unity は旧形式の Graph を取り込むたびに、メモリの上だけで今の形式へ上げています（<code>ShaderGraphImporter</code>:
<code>new GraphData { messageManager, assetGuid }</code> → <code>MultiJson.Deserialize</code> → <code>OnEnable</code> → <code>ValidateGraph</code>）。
Omni の注入器は今の形式だけを読むので、注入の前に同じ処理を通し、<code>MultiJson.Serialize</code> で書き出します。
例: URP 同梱の AutodeskInteractive（FBX の取り込みで自動的に割り当てられる）は旧形式です。
</p>
<p>
上げるたびに、Shader Graph は全ての Object へ新しい乱数の Id（<code>m_ObjectId</code>）を振り、書き出す順序もその乱数に引きずられます。
そのため、同じ入力から毎回別のバイト列ができ、生成物の指紋（変換保証）が決まらなくなります。
上げた結果は <xref href="Omni.Converter.OmniShaderGraphLegacyUpgrader.TryCanonicalizeObjectIds(System.String%2cSystem.String%40%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref> で、Id と書き出しの順序を内容だけから決まる形にそろえます。
</p>
<p>Shader Graph の内部の型は C# の反射で使います。見つからない版では理由を返して止めます（Fail Closed）。</p>

```csharp
public static class OmniShaderGraphLegacyUpgrader
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniShaderGraphLegacyUpgrader](Omni.Converter.OmniShaderGraphLegacyUpgrader.md)

## メソッド（Methods）

### <a id="Omni_Converter_OmniShaderGraphLegacyUpgrader_IsLegacyFormat_System_String_"></a> IsLegacyFormat\(string\)

旧形式（Master Node の形式）の Graph か。

```csharp
public static bool IsLegacyFormat(string text)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniShaderGraphLegacyUpgrader_TryUpgrade_System_String_System_String_System_String__System_String__"></a> TryUpgrade\(string, string, out string, out string\)

旧形式の Graph を今の形式の文字列へ上げます。Object の Id と書き出しの順序は、入力が同じなら毎回同じになるよう
そろえます（<xref href="Omni.Converter.OmniShaderGraphLegacyUpgrader.TryCanonicalizeObjectIds(System.String%2cSystem.String%40%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref>）。

```csharp
public static bool TryUpgrade(string text, string assetGuid, out string upgraded, out string reason)
```

#### 引数（Parameters）

`text` [string](https://learn.microsoft.com/dotnet/api/system.string)

`assetGuid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`upgraded` [string](https://learn.microsoft.com/dotnet/api/system.string)

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
