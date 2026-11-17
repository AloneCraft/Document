# <a id="Omni_Sequencer_Path_ILogicalTimelinePreview"></a> Interface ILogicalTimelinePreview

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

Timeline ウィンドウのプレビュー(スクラブ)で受け手が書き換える値を、Timeline へ知らせる受け手。

<p>
標準の Animation トラックと同じく、ここで登録した値は、プレビューの間だけ変わり、プレビューを終えると元の値へ戻る。
Scene も「変更あり」にならない。登録しないと、スクラブで動いた値がそのまま残り、Scene を保存すると保存される。
</p>

```csharp
public interface ILogicalTimelinePreview
```

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_ILogicalTimelinePreview_EndPreview"></a> EndPreview\(\)

Edit Mode で Timeline のグラフが壊されたとき(プレビューを終えた・グラフを作り直した)に呼ぶ。登録した値は Timeline が戻すので、
受け手は自分の中の状態(再生位置など、Scene に無い値)を、プレビューの前へ戻す。Play 中は呼ばない。

```csharp
void EndPreview()
```

### <a id="Omni_Sequencer_Path_ILogicalTimelinePreview_GatherPreviewProperties_UnityEngine_Playables_PlayableDirector_UnityEngine_Timeline_IPropertyCollector_"></a> GatherPreviewProperties\(PlayableDirector, IPropertyCollector\)

プレビューで書き換える部品を <code class="paramref">driver</code> へ登録する(例: <code>driver.AddFromComponent(gameObject, component)</code>)。

```csharp
void GatherPreviewProperties(PlayableDirector director, IPropertyCollector driver)
```

#### 引数（Parameters）

`director` PlayableDirector

`driver` IPropertyCollector
