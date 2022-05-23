# FabAPP

Application written with PyQt5 to perform the following operations:
- Preparing Gerber X2 files for further process in CircuitPro PM 2.5
- Generating a custom Pick-and-Place file for the Neoden4 pick and place machine.

## Gerber X2 files formatting:
Because Circuit Pro PM 2.5 has an internal mapping for each gerber file to a specific layer, 
we need to rename the extensions from *.gbr (typical extension for X2 Gerbes) to one of the following extensions:

<table>
    <thead>
        <tr>
            <th>Layer</th>
            <th>Gerber file name</th>
            <th>Circuit Pro filename</th>
        </tr>
    </thead>
    <tbody>
    <tr>
    <td>Top</td>
    <td>*.gbr</td>
    <td>*.TOP</td>
    </tr>
    <td>Bot</td>
    <td>*.gbr</td>
    <td>*.BOT</td>
    </tr>
    </tr>
    <td>Board outline</td>
    <td>*.gbr</td>
    <td>*.BOA</td>
    </tr>
    </tr>
    <td>Drills</td>
    <td>*.drl</td>
    <td>*.DRD</td>
    </tr>
    </tr>
    <td>Solder mask Top</td>
    <td>*.gbr</td>
    <td>*.SMT</td>
    </tr>
    </tr>
    </tr>
    <td>Solder mask Bottom</td>
    <td>*.gbr</td>
    <td>*.SMB</td>
    </tr>
    <td>Solder paste Top</td>
    <td>*.gbr</td>
    <td>*.SPT</td>
    </tr>
    </tr>
    <td>Solder paste Bottom</td>
    <td>*.gbr</td>
    <td>*.SPB</td>
    </tr>
    </tr>
    <td>Silkscreen Top</td>
    <td>*.gbr</td>
    <td>*.SST</td>
    </tr>
    </tr>
    <td>Silkscreen Bottom</td>
    <td>*.gbr</td>
    <td>*.SSB</td>
    </tr>
    </tbody>
</table>

To avoid manual renaming of all of these files, I've created a simple desktop application so that you can drag & drop your
files to the, select an output folder and rename all of these files with the correct extension.


## Neoden4 Pick-and-Place File:
To shorten the tedious and manual process of creating a new pick&place job and manually adding components to this file,
I've also created a simple desktop program which let's you convert your "Component Placement" file to a Pick-and-place file
that Neoden4 recognizes and can be used for further process on the machine.

## Compile this app on your machine:
Follow the instructions on following the Wiki-page:<br>
<a href="https://github.com/fernandeclercq/FabAPP/wiki">Wiki pages</a>
