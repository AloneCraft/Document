# <a id="Omni_VirtualObject_IGameObjectSource"></a> Interface IGameObjectSource

Namespace: [Omni.VirtualObject](Omni.VirtualObject.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

GameObject のインスタンスの供給元。準備（生成）を非同期にしたいときに、表現から切り離す。

```csharp
public interface IGameObjectSource
```

## メソッド（Methods）

### <a id="Omni_VirtualObject_IGameObjectSource_Begin"></a> Begin\(\)

生成を始める（冪等）。

```csharp
void Begin()
```

### <a id="Omni_VirtualObject_IGameObjectSource_Cancel"></a> Cancel\(\)

準備中の生成を捨てる（冪等）。

```csharp
void Cancel()
```

### <a id="Omni_VirtualObject_IGameObjectSource_TryTake_UnityEngine_GameObject__"></a> TryTake\(out GameObject\)

生成が終わっていれば instance を渡して true（所有は呼び出し側へ移る。次の Begin は新しく作る）。まだなら false。
instance は非アクティブにして受け取ること（表現が SetActive(false) を保証する）。

```csharp
bool TryTake(out GameObject instance)
```

#### 引数（Parameters）

`instance` GameObject

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
