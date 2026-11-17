# <a id="Omni_RadialLightProxy"></a> Class RadialLightProxy

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

安全域の外にある Spot／Point Light の Unity Transform を、描画する Camera ごとの camera 相対位置へ置きます。

<p>
URP の追加ライトの位置・範囲・影行列は、Light の Unity Transform から作られます。Logical 位置が巨大な光の
Unity Transform は代理値（原点）になるため、そのままでは範囲外として照明にも影にも寄与しません。
この Component は、描画の直前に「光の Logical 位置 - Camera の Logical 位置」を有限値にして、native Camera
の位置（安全域外では原点 proxy）へ足した位置を、所有権つきの表示用代理位置として設定します。
ユーザーの Transform を外から書き換えず、<xref href="Omni.Logical.Transform" data-throw-if-not-resolved="false"></xref> の単一書き手の制約を守ります。
</p>
<p>
安全域内の光には何もしません。複数 Camera では、描画する Camera ごとに値を書き直します。
</p>

```csharp
[ExecuteAlways]
[DisallowMultipleComponent]
[RequireComponent(typeof(Light))]
[AddComponentMenu("")]
public sealed class RadialLightProxy : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[RadialLightProxy](Omni.RadialLightProxy.md)
