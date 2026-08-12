# Surface-electrotlyte-interface
packmol < add_zn.inp  
gmx editconf -f m-new.pdb -o m-1.gro -box 7.9241 7.96933 20 -resnr 1 -noc  
python3 rename.py  
