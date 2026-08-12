def modify_residue_names_by_atom(input_file, output_file):
    with open(input_file, 'r') as f:
        gro_lines = f.readlines()

    title = gro_lines[0]
    natoms = int(gro_lines[1])
    atom_lines = gro_lines[2:-1]
    box_line = gro_lines[-1]

    modified_atom_lines = []
    for line in atom_lines:
        atom_name = line[10:15].strip()
        residue_name = line[5:10].strip()

        if atom_name == "Cu1" and residue_name == "MOL0":
            line = line[:5] + "MOL01" + line[10:]
        elif atom_name == "Pt1" and residue_name == "MOL0":
            line = line[:5] + "MOL02" + line[10:]
        
        modified_atom_lines.append(line)

    with open(output_file, 'w') as f:
        f.writelines([title, f"{len(modified_atom_lines)}\n"] + modified_atom_lines + [box_line])

# 使用範例
modify_residue_names_by_atom("m-1.gro", "m.gro")

