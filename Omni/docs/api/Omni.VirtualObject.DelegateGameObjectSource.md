# <a id="Omni_VirtualObject_DelegateGameObjectSource"></a> Class DelegateGameObjectSource

Namespace: [Omni.VirtualObject](Omni.VirtualObject.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

delegate で同期に作る供給元（Begin で作り、すぐ TryTake できる）。EditMode のテストと、軽い生成に使う。

```csharp
public sealed class DelegateGameObjectSource : IGameObjectSource
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[DelegateGameObjectSource](Omni.VirtualObject.DelegateGameObjectSource.md)

#### 実装するインターフェース（Implements）

[IGameObjectSource](Omni.VirtualObject.IGameObjectSource.md)

## コンストラクター（Constructors）

### <a id="Omni_VirtualObject_DelegateGameObjectSource__ctor_System_Func_UnityEngine_GameObject__"></a> DelegateGameObjectSource\(Func<GameObject\>\)

```csharp
public DelegateGameObjectSource(Func<GameObject> factory)
```

#### 引数（Parameters）

`factory` [Func](https://learn.microsoft.com/dotnet/api/system.func\-1)<GameObject\>

## メソッド（Methods）

### <a id="Omni_VirtualObject_DelegateGameObjectSource_Begin"></a> Begin\(\)

生成を始める（冪等）。

```csharp
public void Begin()
```

### <a id="Omni_VirtualObject_DelegateGameObjectSource_Cancel"></a> Cancel\(\)

準備中の生成を捨てる（冪等）。

```csharp
public void Cancel()
```

### <a id="Omni_VirtualObject_DelegateGameObjectSource_TryTake_UnityEngine_GameObject__"></a> TryTake\(out GameObject\)

生成が終わっていれば instance を渡して true（所有は呼び出し側へ移る。次の Begin は新しく作る）。まだなら false。
instance は非アクティブにして受け取ること（表現が SetActive(false) を保証する）。

```csharp
public bool TryTake(out GameObject instance)
```

#### 引数（Parameters）

`instance` GameObject

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
