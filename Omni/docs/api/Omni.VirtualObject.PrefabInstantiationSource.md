# <a id="Omni_VirtualObject_PrefabInstantiationSource"></a> Class PrefabInstantiationSource

Namespace: [Omni.VirtualObject](Omni.VirtualObject.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Prefab を <code>Object.InstantiateAsync</code> で非同期に生成する供給元。Play 中の準備向け（Edit Mode ではフレームが進まず終わらないことがある）。
Prefab のルートを非アクティブにしておくと、Show まで Awake / OnEnable が走らない。そうでなければ、完了を見つけた時点で非アクティブにする
（それまでの 1 フレームは Awake が走りうる）。

```csharp
public sealed class PrefabInstantiationSource : IGameObjectSource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PrefabInstantiationSource](Omni.VirtualObject.PrefabInstantiationSource.md)

#### 実装するインターフェース（Implements）

[IGameObjectSource](Omni.VirtualObject.IGameObjectSource.md)

## コンストラクター（Constructors）

### <a id="Omni_VirtualObject_PrefabInstantiationSource__ctor_UnityEngine_GameObject_UnityEngine_Transform_"></a> PrefabInstantiationSource\(GameObject, Transform\)

```csharp
public PrefabInstantiationSource(GameObject prefab, Transform parent = null)
```

#### 引数（Parameters）

`prefab` GameObject

`parent` Transform

## メソッド（Methods）

### <a id="Omni_VirtualObject_PrefabInstantiationSource_Begin"></a> Begin\(\)

生成を始める（冪等）。

```csharp
public void Begin()
```

### <a id="Omni_VirtualObject_PrefabInstantiationSource_Cancel"></a> Cancel\(\)

準備中の生成を捨てる（冪等）。

```csharp
public void Cancel()
```

### <a id="Omni_VirtualObject_PrefabInstantiationSource_TryTake_UnityEngine_GameObject__"></a> TryTake\(out GameObject\)

生成が終わっていれば instance を渡して true（所有は呼び出し側へ移る。次の Begin は新しく作る）。まだなら false。
instance は非アクティブにして受け取ること（表現が SetActive(false) を保証する）。

```csharp
public bool TryTake(out GameObject instance)
```

#### 引数（Parameters）

`instance` GameObject

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
