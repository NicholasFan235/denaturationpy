
```console
gmx pdb2gmx -f 2fgf_complete.pdb -o 2fgf_processed.gro -water spce
```

Solvate
```console
gmx editconf -f 2fgf_processed.gro -o 2fgf_newbox.gro -c -d 1.0 -bt cubic
gmx solvate -cp 2fgf_newbox.gro -cs spc216.gro -o 2fgf_solv.gro -p topol.top
```

Neutralize charge
```console
gmx grompp -f ions.mdp -c 2fgf_solv.gro -p topol.top -o ions.tpr
gmx genion -s ions.tpr -o 2fgf_solv_ions.gro -p topol.top -pname NA -nname CL -neutral
```

Energy minimization
```console
gmx grompp -f em.mdp -c 2fgf_solv_ions.gro -p topol.top -o em.tpr
gmx mdrun -v -deffnm em
```

Analyze energy
```console
gmx energy -f em.edr -o potential.xvg
```

Equilibration NVT
```console
gmx grompp -f nvt.mdp -c em.gro -r em.gro -p topol.top -o nvt.tpr
gmx mdrun -deffnm nvt
```

Equilibration analysis NVT
```console
gmx energy -f nvt.edr -o temperature.xvg
```

Equilibration NPT
```console
gmx grompp -f npt.mdp -c nvt.gro -r nvt.gro -t nvt.cpt -p topol.top -o npt.tpr
gmx mdrun -deffnm npt
```

Equilibration Analysis NPT
```console
gmx energy -f npt.edr -o pressure.xvg
gmx energy -f npt.edr -o density.xvg
```
