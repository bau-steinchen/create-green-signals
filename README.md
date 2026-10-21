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

Beide verweisen danach auf eine eigene Textur, `create_green_signals:block/signal_glow_green`. Creates `signal_glow.png` bleibt unangetastet, weil sie auch von der roten Lampe und vom gemeinsamen Lampenkern (`white_cube`) genutzt wird.

## Selbst bauen
```sh
# Textur neu erzeugen (optional, z. B. mit anderer Farbe; braucht Pillow)
python3 tools/make_green_texture.py --color 3CFF64 --gain 1.8
# Zip bauen → dist/create-green-signals-<version>.zip
tools/build.sh 1.0.0
```

## Credits
- Die Modelle und die Ausgangstextur stammen aus [Create](https://github.com/Creators-of-Create/Create) von simibubi & Team.
- Die Idee kommt aus [Create: Steam 'n' Rails](https://github.com/Layers-of-Railways/Railway).
