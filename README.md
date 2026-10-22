# Create Green Signals

Ein Resourcepack für **Minecraft 1.21.1** mit **Create 6.0.x** (NeoForge). Die Nixie Tubes an Create-Zugsignalen zeigen „Fahrt frei“ damit **grün** statt weiß an. So sieht das Signal eher wie ein echtes Ampel- oder Lichtsignal aus.

Steam 'n' Rails hatte diese Option früher. Im Community-Port für 1.21.1 fehlt sie. Dieses Pack holt sie zurück, und zwar ohne zusätzliche Mod und ohne Code.

## Features
- 🟢 **Grün** statt Weiß, wenn der Abschnitt frei ist
- 🔴 **Rot** (Halt) und 🟡 **Gelb** (Warten/Cross-Signal) bleiben wie in Create
- Auch der Leuchtschein um die Röhre ist grün, nicht nur die Röhre selbst
- Signale, die per ComputerCraft gesteuert werden, behalten ihre frei wählbaren Farben
- Reines Resourcepack: kein Java-Code, keine Mixins, funktioniert in Singleplayer und auf Servern (nur im Client nötig)

## Kompatibilität
| | Version |
|---|---|
| Minecraft | 1.21.1 |
| Mod-Loader | NeoForge |
| Create | 6.0.x |

Das Pack braucht Create, sonst hat es nichts zu verändern. Es sollte mit Shadern sowie mit Sodium/Embeddium funktionieren, weil es nur Modelle und Texturen austauscht.

## Installation
1. Die Zip-Datei herunterladen.
2. Nach `.minecraft/resourcepacks/` kopieren.
3. Im Spiel unter *Optionen → Ressourcenpakete* aktivieren. Das Pack muss **über** „Mod-Ressourcen“ stehen, was standardmäßig der Fall ist.

## Funktionsweise
Create rendert die Signallampe in `NixieTubeRenderer.renderAsSignal` aus Partial Models. Das Pack überschreibt nur zwei davon:

- `create:block/track_signal/white_tube`
- `create:block/track_signal/white_glow`

Die Ersatzmodelle und die Textur `create_green_signals:block/signal_green` sind komplett selbst erstellt. Das Pack enthält keine Dateien aus Create. Creates `signal_glow.png` bleibt unangetastet, weil sie auch von der roten Lampe und vom gemeinsamen Lampenkern (`white_cube`) genutzt wird.

## Selbst bauen
```sh
# Textur neu zeichnen (optional, z. B. mit anderer Farbe; braucht Pillow)
python3 tools/make_green_texture.py --tube 1F8534 --glow 33DA55
# Pack-Icon pack/pack.png neu zeichnen (optional)
python3 tools/make_pack_icon.py
# Zip bauen → dist/create-green-signals-<version>.zip
tools/build.sh 1.0.0
```

## Lizenz & Credits
- Dieses Pack steht unter der [MIT-Lizenz](LICENSE).
- [Create](https://github.com/Creators-of-Create/Create) gehört dem Create-Team (Code unter MIT, Assets „All Rights Reserved“). Das Pack enthält keine Create-Assets: Modelle und Textur sind eigenständig erstellt.
- Die Idee kommt aus [Create: Steam 'n' Rails](https://github.com/Layers-of-Railways/Railway).
- Inoffizielles Add-on, nicht mit dem Create-Team verbunden oder von ihm unterstützt.
