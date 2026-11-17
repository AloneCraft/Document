# <a id="Omni_Bake_RadialBakeRegistry"></a> Class RadialBakeRegistry

Namespace: [Omni.Bake](Omni.Bake.md)  
Assembly: Radial.Runtime.dll  

シーンGUID → <xref href="Omni.Rendering.Radial.BakeData" data-throw-if-not-resolved="false"></xref> の対応表です。プロジェクトに1つ。

<p>
<code>Assets/Radial/Resources/</code> 配下に置き、ランタイムから <xref href="UnityEngine.Resources.Load(System.String)" data-throw-if-not-resolved="false"></xref> で
引けるようにします（<code>[CreateAssetMenu]</code> は使わず、固定パスでロード/生成する
既存の慣習に合わせます）。
</p>
<p>
シーンを開かずにベイク状態を検証したい（<code>OmniValidator</code> の要件）ため、
シーンを開いて <xref href="Omni.Bake.RadialBakeBinding" data-throw-if-not-resolved="false"></xref> を辿る方式ではなく、こちらを正本にします。
</p>

```csharp
public sealed class RadialBakeRegistry : ScriptableObject
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
[RadialBakeRegistry](Omni.Bake.RadialBakeRegistry.md)

## フィールド（Fields）

### <a id="Omni_Bake_RadialBakeRegistry_ResourcesPath"></a> ResourcesPath

<xref href="UnityEngine.Resources.Load%60%601(System.String)" data-throw-if-not-resolved="false"></xref> に渡すパス（拡張子・Resourcesプレフィックス無し）。

```csharp
public const string ResourcesPath = "RadialBakeRegistry"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Bake_RadialBakeRegistry_AllSceneGuids"></a> AllSceneGuids

登録済みの全シーンGUIDです（Validatorが全シーンを検証する際に使用）。

```csharp
public IEnumerable<string> AllSceneGuids { get; }
```

#### 値（Property Value）

 [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Bake_RadialBakeRegistry_Instance"></a> Instance

ロード済みインスタンスを返します。無ければ Resources から読み込みます。
プロジェクトでまだ一度もベイクしていない場合は null（Editorでのベイク実行が生成のきっかけ）。

```csharp
public static RadialBakeRegistry Instance { get; }
```

#### 値（Property Value）

 [RadialBakeRegistry](Omni.Bake.RadialBakeRegistry.md)

## メソッド（Methods）

### <a id="Omni_Bake_RadialBakeRegistry_GetOrCreateForEditor"></a> GetOrCreateForEditor\(\)

Editor専用: アセットが無ければ生成し、あればロードして返します。

```csharp
public static RadialBakeRegistry GetOrCreateForEditor()
```

#### 戻り値（Returns）

 [RadialBakeRegistry](Omni.Bake.RadialBakeRegistry.md)

### <a id="Omni_Bake_RadialBakeRegistry_SetData_System_String_Omni_Rendering_Radial_BakeData_"></a> SetData\(string, BakeData\)

指定シーンGUIDのベイクデータを登録・更新します。

```csharp
public void SetData(string sceneGuid, BakeData data)
```

#### 引数（Parameters）

`sceneGuid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`data` [BakeData](Omni.Rendering.Radial.BakeData.md)

### <a id="Omni_Bake_RadialBakeRegistry_TryGetData_System_String_Omni_Rendering_Radial_BakeData__"></a> TryGetData\(string, out BakeData\)

指定シーンGUIDのベイクデータを取得します。

```csharp
public bool TryGetData(string sceneGuid, out BakeData data)
```

#### 引数（Parameters）

`sceneGuid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`data` [BakeData](Omni.Rendering.Radial.BakeData.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
