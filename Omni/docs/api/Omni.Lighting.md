# <a id="Omni_Lighting"></a> Namespace Omni.Lighting

### クラス（Classes）

 [OmniAdaptiveProbeVolumeSpace](Omni.Lighting.OmniAdaptiveProbeVolumeSpace.md)

表示Rootの平行移動をURP APVの公式worldOffsetへ反映します。
Volume.profileの実行時cloneだけを変更し、共有Profile assetを変更しません。

 [OmniAdaptiveProbeVolumeSpaceRequirement](Omni.Lighting.OmniAdaptiveProbeVolumeSpaceRequirement.md)

表示RootにAPV焼成空間との明示的な対応が必要なことをSceneへ保存します。

 [OmniLightProbeSpace](Omni.Lighting.OmniLightProbeSpace.md)

対数表示のために移動した表示Rootと、原点付近に焼かれたLight Probe空間を対応付けます。

 [OmniLightProbeSpaceRequirement](Omni.Lighting.OmniLightProbeSpaceRequirement.md)

移動した表示RootにLight Probeベイク空間との明示的な対応が必要であることを保存します。
TerminalSceneなど、表示座標と物理Lighting Dataの座標が異なるScene Rootで使用します。

 [OmniLightingSpace](Omni.Lighting.OmniLightingSpace.md)

巨大Logical座標と、Reflection Probe・APV・Lightmapが扱う有限ベイク空間を対応付けます。
