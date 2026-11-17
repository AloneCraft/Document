# <a id="Omni_Editor_Manager_OmniShaderErrorChecker"></a> Class OmniShaderErrorChecker

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

<code>Assets/Radial/</code> 配下の生成シェーダーを走査し、コンパイルエラーを検出します。

<p>
生成物が壊れたときの最も分かりやすい症状は「マテリアルがマゼンタになる」ことですが、
変換対象が SRP パッケージ全体（URP だけで 20 シェーダー）に広がると、
4 シーンを目視で確認する運用では取りこぼします。ここでコード側から確実に検出します。
</p>
<p>
逆に「コンパイルは通るがレンダーステートが欠落して静かに見た目が壊れる」類の破綻は
原理的にここでは検出できません。それは <xref href="Omni.Editor.Manager.OmniShaderGenerator" data-throw-if-not-resolved="false"></xref> が
原文を複製する方式を採ることで、そもそも発生させない設計になっています。
</p>

```csharp
public static class OmniShaderErrorChecker
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniShaderErrorChecker](Omni.Editor.Manager.OmniShaderErrorChecker.md)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_OmniShaderErrorChecker_AppendIssues_System_Collections_Generic_List_Omni_Editor_Manager_OmniIssue__"></a> AppendIssues\(List<OmniIssue\>\)

検出結果を <xref href="Omni.Editor.Manager.OmniIssue" data-throw-if-not-resolved="false"></xref> へ変換して <code class="paramref">issues</code> へ足します。
<xref href="Omni.Editor.Manager.OmniValidator" data-throw-if-not-resolved="false"></xref> から呼ばれます。

```csharp
public static void AppendIssues(List<OmniIssue> issues)
```

#### 引数（Parameters）

`issues` [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniIssue](Omni.Editor.Manager.OmniIssue.md)\>

### <a id="Omni_Editor_Manager_OmniShaderErrorChecker_CollectErrors"></a> CollectErrors\(\)

生成済みシェーダーを全走査し、コンパイルエラーを持つものを返します。

```csharp
public static List<OmniShaderErrorChecker.ShaderError> CollectErrors()
```

#### 戻り値（Returns）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniShaderErrorChecker](Omni.Editor.Manager.OmniShaderErrorChecker.md).[ShaderError](Omni.Editor.Manager.OmniShaderErrorChecker.ShaderError.md)\>

### <a id="Omni_Editor_Manager_OmniShaderErrorChecker_RunAndLog"></a> RunAndLog\(\)

```csharp
public static void RunAndLog()
```
